// Check if g83RawData already exists
if (typeof window.g83RawData === 'undefined') {
    window.g83RawData = [];
}

// G83 Utils for data processing - EXACT MATCH WITH BACKEND
if (typeof window.G83Utils === 'undefined') {
    window.G83Utils = {
        // Helper method to safely parse values
        safeParseInt(str) {
            if (str === null || str === undefined) return 0;
            const num = parseInt(str.toString().replace(/[^0-9.-]/g, ''));
            return isNaN(num) ? 0 : num;
        },
        
        safeParseFloat(str) {
            if (str === null || str === undefined) return 0;
            const num = parseFloat(str.toString().replace(/[^0-9.-]/g, ''));
            return isNaN(num) ? 0 : num;
        },
        
        // Parse date string - matches CUSTOM_DATE_PARSER behavior
        parseDate(dateStr) {
            if (!dateStr || dateStr === 'None' || dateStr === '' || dateStr === 'Undefined' || dateStr === '-') return null;
            try {
                // Try parsing various date formats
                const date = new Date(dateStr);
                return isNaN(date.getTime()) ? null : date;
            } catch (e) {
                return null;
            }
        },
        
        // ============ DATA EXTRACTION METHODS ============
        getAppId(item) {
            if (!item) return 'Unknown';
            return item["Bus App ID"] || 
                   item["Business Application ID"] || 
                   item["BUSINESS_APP_ID"] || 
                   item.appId || 
                   item.app_id || 
                   item.id || 
                   'Unknown';
        },
        
        getAppName(item) {
            if (!item) return 'Unknown';
            return item["Bus App Name"] || 
                   item["Business Application Name"] || 
                   item["BUSINESS_APP_NAME"] || 
                   item.baName || 
                   item.appName || 
                   'Unknown';
        },

        getVS(item) {
            if (!item) return 'Unknown';
            return item["Tech Level 7"] || 
                   item["SERVICE_IT_ORG7"] || 
                   item.it_org7 || 
                   item["VS"] || 
                   item.vs || 
                   'Unknown';
        },
        
        getSVS(item) {
            if (!item) return 'Unknown';
            return item["Tech Level 8"] || 
                   item["L5AssetDept"] || 
                   item.it_org8 || 
                   item["SVS"] || 
                   item.svs || 
                   'Unknown';
        },

        getITSO(item) {
            if (!item) return 'Unknown';
            return item["ITSO"] || 
                   item["IT_SERVICE_OWNER"] || 
                   item.itso || 
                   'Unknown';
        },
    
        getVersion(item) {
            if (!item) return 'Unknown';
            return item["Technology Version"] || 
                   item.version || 
                   'Unknown';
        },
        
        getObsoleteDate(item) {
            if (!item) return 'None';
            return item["Obsolete Date"] || 
                   item.obsoleteDate || 
                   'None';
        },
        
        getIRD(item) {
            if (!item) return 'None';
            return item["Issue Remediation Date"] || 
                   item["IRD"] || 
                   item.ird || 
                   'None';
        },
        
        getRecordId(item) {
            if (!item) return '';
            const recordId = item["Record ID"] || 
                            item.recordId || 
                            item.record_id || 
                            '';
            return recordId ? recordId.toString().trim() : '';
        },
        
        isTechnologyObsolete(item) {
            if (!item) return false;
            const obsolete = item["Technology Obsolete"];
            return obsolete && obsolete.toString().toUpperCase() === 'YES';
        },
        
        // ============ BACKEND-ALIGNED COMPLIANCE LOGIC ============
        
        /**
         * EXACT MATCH with backend calculate_g83_compliance():
         * ✅ Compliant: NOT obsolete OR (obsolete AND has valid IRD)
         * ⚠️ Warning: obsolete AND has IRD in future (IRD >= today)
         * ❌ Non-compliant: obsolete AND (no IRD OR invalid IRD OR IRD < today)
         */
        
        determineAppStatus(techObsolete, irdStr) {
            if (!techObsolete) {
                return 'compliant'; // NOT obsolete
            }
            
            // Check IRD - match backend: if not ird_str or str(ird_str).strip() in ['', 'None', 'Undefined', '-']
            if (!irdStr || irdStr === '' || irdStr === 'None' || irdStr === 'Undefined' || irdStr === '-') {
                return 'non_compliant'; // No IRD defined
            }
            
            // Parse IRD
            const irdDate = this.parseDate(irdStr);
            if (!irdDate) {
                return 'non_compliant'; // Invalid IRD
            }
            
            // Compare dates (set to midnight for fair comparison)
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            irdDate.setHours(0, 0, 0, 0);
            
            if (irdDate < today) {
                return 'non_compliant'; // IRD in the past
            } else {
                return 'warning'; // IRD in the future
            }
        },
        
        /**
         * EXACT MATCH with backend: Group by distinct Bus App ID
         * This mirrors the backend's distinct_apps dictionary
         */
        groupByDistinctAppId(data) {
            if (!data || !Array.isArray(data)) return {};
            
            const distinctApps = {}; // matches backend's distinct_apps
            
            data.forEach(item => {
                const appId = this.getAppId(item);
                
                // Skip invalid app IDs - matches backend
                if (!appId || appId === 'Unknown' || appId === '') {
                    return;
                }
                
                const techObsolete = this.isTechnologyObsolete(item);
                const ird = this.getIRD(item);
                const vs = this.getVS(item);
                const svs = this.getSVS(item);
                const baName = this.getAppName(item);
                const itso = this.getITSO(item);
                
                if (!distinctApps[appId]) {
                    // First time seeing this app - matches backend initialization
                    distinctApps[appId] = {
                        app_id: appId,
                        vs: vs,
                        svs: svs,
                        ba_name: baName,
                        itso: itso,
                        tech_obsolete: techObsolete,
                        ird: ird,
                        items: [item],
                        compliance_status: null // Will calculate later
                    };
                } else {
                    // Update existing app - matches backend update logic
                    if (techObsolete) {
                        distinctApps[appId].tech_obsolete = true;
                        distinctApps[appId].ird = ird; // Use most recent IRD
                    }
                    distinctApps[appId].items.push(item);
                }
            });
            
            // Calculate compliance status for each app - matches backend Step 2
            Object.values(distinctApps).forEach(app => {
                app.compliance_status = this.determineAppStatus(
                    app.tech_obsolete,
                    app.ird
                );
            });
            
            return distinctApps;
        },
        
        /**
         * EXACT MATCH with backend: Calculate overall compliance metrics
         * Returns same structure as backend calculate_g83_compliance()
         */
        calculateComplianceDistinct(data) {
            const distinctApps = this.groupByDistinctAppId(data);
            const appIds = Object.keys(distinctApps);
            
            let nonCompliantApps = 0;
            let warningApps = 0;
            let compliantApps = 0;
            
            // Count by compliance status - matches backend Step 2
            Object.values(distinctApps).forEach(app => {
                if (app.compliance_status === 'non_compliant') {
                    nonCompliantApps++;
                } else if (app.compliance_status === 'warning') {
                    warningApps++;
                } else {
                    compliantApps++;
                }
            });
            
            const totalDistinctApps = appIds.length;
            const nonCompliantPct = totalDistinctApps > 0 
                ? (nonCompliantApps / totalDistinctApps) * 100 
                : 0;
            const complianceScore = 100 - nonCompliantPct;
            
            // G83 thresholds (fixed) - matches backend
            const redThreshold = 2;
            const amberThreshold = 0.5;
            
            let ragStatus = 'Green';
            if (nonCompliantPct > redThreshold) {
                ragStatus = 'Red';
            } else if (nonCompliantPct > amberThreshold) {
                ragStatus = 'Amber';
            }
            
            return {
                success: true,
                metric: 'G83',
                compliance_score: parseFloat(complianceScore.toFixed(2)),
                non_compliant_percentage: parseFloat(nonCompliantPct.toFixed(2)),
                rag_status: ragStatus,
                total_distinct_apps: totalDistinctApps,
                non_compliant_apps: nonCompliantApps,
                warning_apps: warningApps,
                compliant_apps: compliantApps,
                total_records: data.length,
                threshold_info: {
                    red_threshold: redThreshold,
                    amber_threshold: amberThreshold,
                    threshold_description: `Green≤${amberThreshold}%, Amber>${amberThreshold}-${redThreshold}%, Red>${redThreshold}%`
                },
                calculation_details: {
                    basis: 'distinct_bus_app_id',
                    non_compliance_criteria: 'Technology Obsolete = "YES" AND (no IRD OR IRD < today)',
                    warning_criteria: 'Technology Obsolete = "YES" AND IRD >= today',
                    compliant_criteria: 'NOT obsolete OR (obsolete AND IRD is valid)',
                    distinct_app_count: totalDistinctApps,
                    non_compliant_count: nonCompliantApps,
                    warning_count: warningApps,
                    compliant_count: compliantApps,
                    total_record_count: data.length
                }
            };
        },
        
        /**
         * EXACT MATCH with backend: VS breakdown with SVS
         * Matches backend's vs_groups and vs_breakdown
         */
        getNonCompliantByVSDistinct(data) {
            const distinctApps = this.groupByDistinctAppId(data);
            const vsGroups = {}; // matches backend's vs_groups
            
            // Group by VS+SVS - matches backend Step 4
            Object.values(distinctApps).forEach(app => {
                const vs = app.vs;
                const svs = app.svs;
                const key = `${vs}|${svs}`;
                
                if (!vsGroups[key]) {
                    vsGroups[key] = {
                        vs: vs,
                        svs: svs,
                        total_distinct_apps: 0,
                        non_compliant_distinct_apps: 0,
                        warning_distinct_apps: 0,
                        compliant_distinct_apps: 0,
                        apps: []
                    };
                }
                
                vsGroups[key].total_distinct_apps += 1;
                
                if (app.compliance_status === 'non_compliant') {
                    vsGroups[key].non_compliant_distinct_apps += 1;
                } else if (app.compliance_status === 'warning') {
                    vsGroups[key].warning_distinct_apps += 1;
                } else {
                    vsGroups[key].compliant_distinct_apps += 1;
                }
                
                vsGroups[key].apps.push(app);
            });
            
            // Build VS breakdown - matches backend Step 5
            const redThreshold = 2;
            const amberThreshold = 0.5;
            
            const vsBreakdown = [];
            
            Object.values(vsGroups).forEach(data => {
                const vsPercentage = data.total_distinct_apps > 0 
                    ? (data.non_compliant_distinct_apps / data.total_distinct_apps) * 100 
                    : 0;
                const warningPct = data.total_distinct_apps > 0 
                    ? (data.warning_distinct_apps / data.total_distinct_apps) * 100 
                    : 0;
                
                // Determine severity - matches backend
                let severity = 'good';
                let severityLabel = 'Green';
                
                if (vsPercentage > redThreshold) {
                    severity = 'critical';
                    severityLabel = 'Red';
                } else if (vsPercentage > amberThreshold) {
                    severity = 'warning';
                    severityLabel = 'Amber';
                }
                
                vsBreakdown.push({
                    vs: data.vs,
                    svs: data.svs,
                    percentage: parseFloat(vsPercentage.toFixed(2)),
                    warning_percentage: parseFloat(warningPct.toFixed(2)),
                    nonCompliantApps: data.non_compliant_distinct_apps,
                    warningApps: data.warning_distinct_apps,
                    compliantApps: data.compliant_distinct_apps,
                    totalApps: data.total_distinct_apps,
                    severity: severity,
                    severity_label: severityLabel,
                    apps: data.apps.flatMap(app => app.items)
                });
            });
            
            return vsBreakdown;
        },
        
        /**
         * EXACT MATCH with backend: SVS-only breakdown
         * Matches backend's svs_groups and svs_breakdown
         */
        getNonCompliantBySVS(data) {
            const distinctApps = this.groupByDistinctAppId(data);
            const svsGroups = {}; // matches backend's svs_groups
            
            // Group by SVS only - matches backend Step 6
            Object.values(distinctApps).forEach(app => {
                const svs = app.svs;
                
                if (!svsGroups[svs]) {
                    svsGroups[svs] = {
                        svs: svs,
                        total_distinct_apps: 0,
                        non_compliant_distinct_apps: 0,
                        warning_distinct_apps: 0,
                        compliant_distinct_apps: 0,
                        apps: []
                    };
                }
                
                svsGroups[svs].total_distinct_apps += 1;
                
                if (app.compliance_status === 'non_compliant') {
                    svsGroups[svs].non_compliant_distinct_apps += 1;
                } else if (app.compliance_status === 'warning') {
                    svsGroups[svs].warning_distinct_apps += 1;
                } else {
                    svsGroups[svs].compliant_distinct_apps += 1;
                }
                
                svsGroups[svs].apps.push(app);
            });
            
            // Build SVS breakdown - matches backend Step 6
            const redThreshold = 2;
            const amberThreshold = 0.5;
            
            const svsBreakdown = [];
            
            Object.entries(svsGroups).forEach(([svs, data]) => {
                const svsPercentage = data.total_distinct_apps > 0 
                    ? (data.non_compliant_distinct_apps / data.total_distinct_apps) * 100 
                    : 0;
                const warningPct = data.total_distinct_apps > 0 
                    ? (data.warning_distinct_apps / data.total_distinct_apps) * 100 
                    : 0;
                
                // Determine severity - matches backend
                let severity = 'good';
                let severityLabel = 'Green';
                
                if (svsPercentage > redThreshold) {
                    severity = 'critical';
                    severityLabel = 'Red';
                } else if (svsPercentage > amberThreshold) {
                    severity = 'warning';
                    severityLabel = 'Amber';
                }
                
                svsBreakdown.push({
                    svs: svs,
                    percentage: parseFloat(svsPercentage.toFixed(2)),
                    warning_percentage: parseFloat(warningPct.toFixed(2)),
                    nonCompliantApps: data.non_compliant_distinct_apps,
                    warningApps: data.warning_distinct_apps,
                    compliantApps: data.compliant_distinct_apps,
                    totalApps: data.total_distinct_apps,
                    severity: severity,
                    severity_label: severityLabel,
                    apps: data.apps.flatMap(app => app.items)
                });
            });
            
            return svsBreakdown;
        },
        
        // ============ ADDITIONAL METHODS NEEDED BY FRONTEND ============
        
        /**
         * Get top non-compliant applications (VS level)
         * This is used by the "Top Non-Compliant Technologies" card
         */
        getTopNonCompliantApps(data, limit = 5, by = 'percentage') {
            const vsData = this.getNonCompliantByVSDistinct(data);
            
            // Sort based on parameter
            if (by === 'count') {
                return vsData.sort((a, b) => b.nonCompliantApps - a.nonCompliantApps).slice(0, limit);
            } else {
                return vsData.sort((a, b) => b.percentage - a.percentage).slice(0, limit).map(item => ({
                    vs: item.vs,
                    appName: item.vs, // Use VS as appName for the top list
                    percentage: item.percentage,
                    nonCompliantApps: item.nonCompliantApps,
                    totalApps: item.totalApps
                }));
            }
        },
        
        // Get total non-compliant apps count (distinct)
        getTotalNonCompliantCount(data) {
            const distinct = this.calculateComplianceDistinct(data);
            return distinct.non_compliant_apps;
        },
        
        // Get total apps count (distinct)
        getTotalAppsCount(data) {
            const distinct = this.calculateComplianceDistinct(data);
            return distinct.total_distinct_apps;
        },
        
        // Get status thresholds for G83
        getStatusThresholds() {
            return {
                green: 0.5,
                amber: { min: 0.5, max: 2 },
                red: 2
            };
        },
        
        // Calculate status based on percentage
        getStatusTextForPercentage(percentage) {
            const thresholds = this.getStatusThresholds();
            if (percentage > thresholds.red) return 'Red';
            if (percentage >= thresholds.amber.min && percentage <= thresholds.amber.max) return 'Amber';
            return 'Green';
        },
        
        // Get status color based on percentage
        getStatusColorForPercentage(percentage) {
            const status = this.getStatusTextForPercentage(percentage);
            switch(status) {
                case 'Red': return 'red';
                case 'Amber': return 'yellow';
                default: return 'green';
            }
        },
        
        // ============ LEGACY METHODS (for backward compatibility) ============
        
        // Legacy method - now uses distinct calculation
        calculateTotalNonCompliantPercentage(data) {
            const result = this.calculateComplianceDistinct(data);
            return result.non_compliant_percentage;
        },
        
        // Legacy method - now uses distinct calculation
        getComplianceSummary(data) {
            const result = this.calculateComplianceDistinct(data);
            return {
                totalApps: result.total_distinct_apps,
                nonCompliantApps: result.non_compliant_apps,
                warningApps: result.warning_apps,
                compliantApps: result.compliant_apps
            };
        },
        
        // Legacy item-level methods - keep for backward compatibility
        isNonCompliant(item) {
            const techObsolete = this.isTechnologyObsolete(item);
            const ird = this.getIRD(item);
            const status = this.determineAppStatus(techObsolete, ird);
            return status === 'non_compliant';
        },
        
        isWarning(item) {
            const techObsolete = this.isTechnologyObsolete(item);
            const ird = this.getIRD(item);
            const status = this.determineAppStatus(techObsolete, ird);
            return status === 'warning';
        },
        
        getStatusText(item) {
            const techObsolete = this.isTechnologyObsolete(item);
            const ird = this.getIRD(item);
            const status = this.determineAppStatus(techObsolete, ird);
            
            switch(status) {
                case 'non_compliant': return 'Non-Compliant';
                case 'warning': return 'Warning';
                default: return 'Compliant';
            }
        },
        
        getStatusColor(item) {
            const status = this.getStatusText(item);
            switch(status.toLowerCase()) {
                case 'non-compliant': return 'red';
                case 'warning': return 'yellow';
                case 'compliant': return 'green';
                default: return 'gray';
            }
        }
    };
}