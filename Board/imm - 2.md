def get_effective_due_date(record):
    """Return the appropriate due date for a record, depending on its metric.
    Falls back to the record's due_date column, then raw data, and finally
    returns None if no date is found (which will be treated as overdue/today).
    """
    # 1. Use the record's due_date column if set
    if record.due_date:
        return record.due_date

    raw = record.raw_data or {}
    metric = record.metric_code

    # 2. Metric‑specific fields
    if metric == 'G5':
        val = raw.get('2x SLA due date') or raw.get('x2_sla_date')
        if val:
            parsed = CUSTOM_DATE_PARSER.parse_date(str(val))
            if parsed:
                return parsed
    elif metric == 'G51':
        val = raw.get('Obsolete Date')
        if val:
            parsed = CUSTOM_DATE_PARSER.parse_date(str(val))
            if parsed:
                return parsed
    elif metric == 'G83':
        val = raw.get('Issue Remediation Date')
        if val:
            parsed = CUSTOM_DATE_PARSER.parse_date(str(val))
            if parsed:
                return parsed

    # 3. Generic "Due Date" from raw data
    val = raw.get('Due Date')
    if val:
        parsed = CUSTOM_DATE_PARSER.parse_date(str(val))
        if parsed:
            return parsed

    return None



@app.route('/api/db/user/<username>/calendar', methods=['GET', 'OPTIONS'])
@app.route(f'{app_route}/api/db/user/<username>/calendar', methods=['GET', 'OPTIONS'])
def get_user_calendar(username):
    """
    Returns per‑date calendar data for an ITSO.
    Red = overdue (or no due date and status indicates red).
    Amber = due within the next 3 months (or no due date and status indicates amber).
    Each cell shows the number of distinct applications with red/amber items.
    Today's cell also includes all overdue items from any past date.
    """
    if request.method == 'OPTIONS':
        return '', 200

    try:
        ensure_database_initialized()

        # 1. Active uploads
        active_uploads_subq = db.session.query(Upload.id).filter(
            Upload.is_active == True,
            Upload.processing_status == 'completed'
        ).subquery()

        # 2. ITSO conditions
        username_lower = username.lower()
        user_conditions = db.or_(
            func.lower(DataRecord.itso) == username_lower,
            func.lower(DataRecord.raw_data['ITSO and / or Owning Individual'].astext) == username_lower,
            func.lower(DataRecord.raw_data['ITSO'].astext) == username_lower,
            func.lower(DataRecord.raw_data['Owner'].astext) == username_lower
        )

        today = datetime.now().date()
        three_months = today + timedelta(days=90)

        # 3. Use the comprehensive status patterns
        patterns = build_status_patterns(DataRecord)
        red_condition = patterns['critical']
        amber_condition = patterns['warning']

        # 4. Fetch all red/amber records for this user
        records = DataRecord.query.filter(
            DataRecord.upload_id.in_(active_uploads_subq),
            user_conditions,
            db.or_(red_condition, amber_condition)
        ).all()

        if not records:
            return safe_jsonify({
                'success': True,
                'username': username,
                'dates': []
            })

        # 5. Group by application and determine earliest effective date + worst status
        app_map = {}  # key: (app_name, vs, svs) -> { earliest_date, status }
        for rec in records:
            due_date = get_effective_due_date(rec)

            if due_date is None:
                # No date → place on today, determine colour from field‑level status
                due_date = today
                if is_record_red(rec):
                    status = 'red'
                elif is_record_amber(rec):
                    status = 'amber'
                else:
                    # Should not happen because of the earlier filter, but fallback
                    status = 'red'
            else:
                if due_date <= today:
                    status = 'red'
                elif due_date <= three_months:
                    status = 'amber'
                else:
                    continue  # future > 3 months — skip

            app_name = rec.application_name or (
                (rec.metric_data or {}).get('Application Name') or
                (rec.raw_data or {}).get('Application Name') or
                'Unknown'
            )
            vs = rec.it_org7 or 'Unknown'
            svs = rec.it_org8 or 'Unknown'
            key = f"{app_name}|{vs}|{svs}"

            if key not in app_map:
                app_map[key] = {'earliest_date': due_date, 'status': status}
            else:
                existing = app_map[key]
                # Keep the earliest date
                if due_date < existing['earliest_date']:
                    existing['earliest_date'] = due_date
                # Keep the worst status (red over amber)
                if status == 'red' or (status == 'amber' and existing['status'] != 'red'):
                    existing['status'] = status

        # 6. Aggregate counts per date
        date_counts = defaultdict(lambda: {'total': 0, 'critical': 0, 'warning': 0})
        for info in app_map.values():
            d = info['earliest_date']
            st = info['status']
            date_counts[d]['total'] += 1
            if st == 'red':
                date_counts[d]['critical'] += 1
            else:
                date_counts[d]['warning'] += 1

        # 7. Build response list
        dates_list = []
        for d, counts in sorted(date_counts.items()):
            dates_list.append({
                'date': d.isoformat(),
                'total': counts['total'],
                'critical': counts['critical'],
                'warning': counts['warning']
            })

        # 8. Today's cell: sum all apps with earliest_date <= today
        today_total = sum(1 for info in app_map.values() if info['earliest_date'] <= today)
        today_crit = sum(1 for info in app_map.values() if info['earliest_date'] <= today and info['status'] == 'red')
        today_amber = today_total - today_crit

        today_str = today.isoformat()
        today_found = False
        for entry in dates_list:
            if entry['date'] == today_str:
                entry['total'] = today_total
                entry['critical'] = today_crit
                entry['warning'] = today_amber
                today_found = True
                break
        if not today_found and today_total > 0:
            dates_list.append({
                'date': today_str,
                'total': today_total,
                'critical': today_crit,
                'warning': today_amber
            })
            dates_list.sort(key=lambda x: x['date'])

        return safe_jsonify({
            'success': True,
            'username': username,
            'dates': dates_list
        })

    except Exception as e:
        logger.error(f"Error in calendar endpoint: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/db/user/<username>/calendar/details', methods=['GET', 'OPTIONS'])
@app.route(f'{app_route}/api/db/user/<username>/calendar/details', methods=['GET', 'OPTIONS'])
def get_user_calendar_details(username):
    """
    Returns all applications (with per‑metric breakdown) that have red/amber
    items due on or before the given date.
    """
    if request.method == 'OPTIONS':
        return '', 200

    try:
        ensure_database_initialized()

        date_str = request.args.get('date')
        include_metrics = request.args.get('include_metrics', 'false').lower() == 'true'

        if not date_str:
            return jsonify({'success': False, 'error': 'date parameter required'}), 400

        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid date format (YYYY-MM-DD)'}), 400

        today = datetime.now().date()
        three_months = today + timedelta(days=90)
        is_today = target_date == today

        # ITSO conditions
        username_lower = username.lower()
        user_conditions = db.or_(
            func.lower(DataRecord.itso) == username_lower,
            func.lower(DataRecord.raw_data['ITSO and / or Owning Individual'].astext) == username_lower,
            func.lower(DataRecord.raw_data['ITSO'].astext) == username_lower,
            func.lower(DataRecord.raw_data['Owner'].astext) == username_lower
        )

        # Active uploads
        active_uploads_subq = db.session.query(Upload.id).filter(
            Upload.is_active == True,
            Upload.processing_status == 'completed'
        ).subquery()

        # Use the comprehensive status patterns
        patterns = build_status_patterns(DataRecord)
        red_condition = patterns['critical']
        amber_condition = patterns['warning']

        # Fetch all red/amber records for this user
        records = DataRecord.query.filter(
            DataRecord.upload_id.in_(active_uploads_subq),
            user_conditions,
            db.or_(red_condition, amber_condition)
        ).all()

        if not records:
            return safe_jsonify({
                'success': True,
                'date': date_str,
                'is_today': is_today,
                'applications': []
            })

        # Filter and classify
        filtered = []
        for rec in records:
            due_date = get_effective_due_date(rec)

            if due_date is None:
                due_date = today
                # Fallback to field‑based classification when no date exists
                if is_record_red(rec):
                    status = 'red'
                elif is_record_amber(rec):
                    status = 'amber'
                else:
                    status = 'red'   # should not happen
            else:
                if due_date <= today:
                    status = 'red'
                elif due_date <= three_months:
                    status = 'amber'
                else:
                    continue

            if is_today:
                if due_date <= target_date:
                    filtered.append((rec, status))
            else:
                if due_date == target_date:
                    filtered.append((rec, status))

        if not filtered:
            return safe_jsonify({
                'success': True,
                'date': date_str,
                'is_today': is_today,
                'applications': []
            })

        # Group by application
        app_groups = defaultdict(lambda: {'records': [], 'has_red': False, 'has_amber': False})
        for rec, status in filtered:
            app_name = rec.application_name or (
                (rec.metric_data or {}).get('Application Name') or
                (rec.raw_data or {}).get('Application Name') or
                'Unknown'
            )
            vs = rec.it_org7 or 'Unknown'
            svs = rec.it_org8 or 'Unknown'
            key = f"{app_name}|{vs}|{svs}"
            app_groups[key]['records'].append(rec)
            if status == 'red':
                app_groups[key]['has_red'] = True
            else:
                app_groups[key]['has_amber'] = True

        applications = []
        for key, group in app_groups.items():
            app_name, vs, svs = key.split('|', 2)
            status = 'critical' if group['has_red'] else 'warning'
            total_controls = len(group['records'])

            metrics_breakdown = []
            if include_metrics:
                metric_map = defaultdict(lambda: {'critical': 0, 'warning': 0, 'compliant': 0})
                for rec in group['records']:
                    mc = rec.metric_code or 'Unknown'
                    due = get_effective_due_date(rec)
                    if due is None or due <= today:
                        # Classify based on field-level status
                        if is_record_red(rec):
                            metric_map[mc]['critical'] += 1
                        elif is_record_amber(rec):
                            metric_map[mc]['warning'] += 1
                        else:
                            metric_map[mc]['compliant'] += 1
                    else:
                        metric_map[mc]['warning'] += 1
                metrics_breakdown = [
                    {'metric_code': mc, **counts}
                    for mc, counts in metric_map.items()
                ]

            applications.append({
                'app_name': app_name,
                'vs': vs,
                'svs': svs,
                'status': status,
                'controls': total_controls,
                'metrics': metrics_breakdown if include_metrics else []
            })

        return safe_jsonify({
            'success': True,
            'date': date_str,
            'is_today': is_today,
            'applications': applications
        })

    except Exception as e:
        logger.error(f"Calendar details error: {e}", exc_info=True)
        return jsonify({'success': False, 'error': str(e)}), 500


