# Project Code Snippets

## File: `index.html`

```plaintext
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT Control & Governance Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles/main.css">
</head>

<body class="min-h-screen antialiased">
    <!-- Overlay -->
    <div id="overlay" class="overlay"></div>

    <!-- Menu -->
    <aside id="menu" class="menu p-4">
        <div class="flex justify-between items-center mb-8">
            <h1 class="text-2xl font-extrabold text-gray-900">IT Control</h1>
            <button id="menu-close" class="p-2 rounded-full text-gray-500 hover:bg-gray-100">
                <i class="fas fa-times text-xl"></i>
            </button>
        </div>

        <nav id="main-nav">
            <div class="nav-item active" data-path="Overview">
                <span>Overview</span>
            </div>

            <h3 class="text-xs font-bold text-gray-500 uppercase mt-6 mb-3 ml-2">GRAS Metrics</h3>
            <div class="nav-item ml-4" data-path="GRAS.Overview">
                <span>GRAS Overview</span>
            </div>
            <div class="nav-item ml-4" data-path="GRAS.G3">
                <span>G3: Control Status</span>
            </div>
            <div class="nav-item ml-4" data-path="GRAS.G5">
                <span>G5: Critical & High Vulnerabilities</span>
            </div>
            <div class="nav-item ml-4" data-path="GRAS.G43">
                <span>G43: Patching Coverage</span>
            </div>
            <div class="nav-item ml-4" data-path="GRAS.G51">
                <span>G51: IAM Compliance</span>
            </div>

            <h3 class="text-xs font-bold text-gray-500 uppercase mt-6 mb-3 ml-2">Cyber OKR</h3>
            <div class="nav-item ml-4" data-path="OKR.Overview">
                <span>OKR Overview</span>
            </div>
            <div class="nav-item ml-4" data-path="OKR.SECA">
                <span>SECA: Security Adoption</span>
            </div>

            <h3 class="text-xs font-bold text-gray-500 uppercase mt-6 mb-3 ml-2">Control Governance</h3>
            <div class="nav-item ml-4" data-path="GOV.ITOP1">
                <span>ITOP.1: Change Management</span>
            </div>
            <div class="nav-item ml-4" data-path="GOV.ITOP2">
                <span>ITOP.2: Critical Config Compliance</span>
            </div>
            <div class="nav-item ml-4" data-path="GOV.ITAM3">
                <span>ITAM.3: Asset Inventory</span>
            </div>
        </nav>
    </aside>

    <!-- Chart Modal -->
    <div id="chart-modal" class="modal">
        <div class="modal-content">
            <div class="flex justify-between items-center mb-6 border-b pb-4">
                <h2 class="text-2xl lg:text-3xl font-bold text-gray-900" id="modal-title">VS Non-Compliance Details</h2>
                <button id="modal-close" class="p-2 rounded-full text-gray-500 hover:bg-gray-100">
                    <i class="fas fa-times text-xl"></i>
                </button>
            </div>

            <div id="modal-content" class="space-y-6">
                <!-- Modal content will be populated dynamically -->
            </div>
        </div>
    </div>

    <!-- Main Content Wrapper -->
    <div class="flex flex-col flex-grow w-full">
        <!-- Top Application Header Bar -->
        <header class="w-full h-16 flex items-center justify-between px-4 lg:px-8 sticky top-0 bg-white shadow-sm z-10">
            <div class="flex items-center">
                <button id="menu-toggle" class="p-2 mr-4 rounded-md text-gray-500 hover:bg-gray-100">
                    <i class="fas fa-bars text-xl"></i>
                </button>
                <h1 class="text-xl font-semibold text-gray-800">IT Governance Console</h1>
            </div>
            <div class="flex items-center space-x-4">
                <div class="relative hidden md:block">
                    <input type="text" placeholder="Search Metrics, TDOs, or Assets..." class="w-64 p-2 pl-10 rounded-lg bg-gray-100 border border-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-150 text-sm">
                    <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                </div>
                <button class="text-gray-500 hover:text-blue-600 p-2 rounded-full hover:bg-gray-100 transition">
                    <i class="fas fa-bell text-xl"></i>
                </button>
                <span class="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold text-sm">JS</span>
            </div>
        </header>

        <!-- Main Content Area -->
        <main class="main-content flex-grow p-4 lg:p-8">
            <header class="mb-6 lg:mb-8">
                <h2 id="page-title" class="text-2xl lg:text-4xl font-extrabold text-gray-900">Dashboard Overview</h2>
                <p id="page-subtitle" class="text-base lg:text-lg text-gray-500 mt-1">A high-level summary of all IT Control domains.</p>
            </header>

            <!-- Content rendering container -->
            <div id="content-container" class="grid grid-cols-1 gap-6 lg:gap-8">
                <!-- Content will be rendered here by JavaScript -->
            </div>
        </main>
    </div>

    <!-- Core JavaScript -->
    <script src="js/core/utils.js"></script>
    <script src="js/core/modal.js"></script>
    <script src="js/core/navigation.js"></script>

    <!-- Data Management -->
    <script src="js/core/data-manager.js"></script>

    <!-- Data Files -->
    <script src="data/g3-data.js"></script>
    <script src="data/g5-data.js"></script>
    <script src="data/itop2-data.js"></script>
    <!-- Add this line -->

    <!-- Component Templates -->
    <script src="js/pages/component-templates.js"></script>

    <!-- Page Components -->
    <script src="js/pages/overview.js"></script>
    <script src="js/pages/gras-overview.js"></script>
    <script src="js/pages/gras-g3.js"></script>
    <script src="js/pages/gras-g5.js"></script>
    <script src="js/pages/gov-itop2.js"></script>
    <!-- Add this line -->

    <!-- Router (must be loaded after all components) -->
    <script src="js/core/router.js"></script>

    <!-- Main App -->
    <script src="js/main.js"></script>
</body>

</html>
```

## File: `data\g3-data.js`

```plaintext
// Check if g3RawData already exists
if (typeof window.g3RawData === 'undefined') {
    window.g3RawData = [
        { appName: 'App Name1 example', vs: 'VS-001 Complete value', svs: 'svs 1', itso: 'itso name 1', totalAccount: 43, compliant: 23, nonCompliant: 20, nonCompliantAccounts: 8, other1: 0, other2: 8, other3: 4 },
        { appName: 'App Name2', vs: 'VS-001', svs: 'svs 2', itso: 'itso name 2', totalAccount: 72, compliant: 42, nonCompliant: 30, nonCompliantAccounts: 14, other1: 0, other2: 14, other3: 2 },
        { appName: 'App Name3', vs: 'VS-002', svs: 'svs 3', itso: 'itso name 3', totalAccount: 56, compliant: 35, nonCompliant: 21, nonCompliantAccounts: 9, other1: 0, other2: 9, other3: 3 },
        { appName: 'App Name4 example 4', vs: 'VS-002', svs: 'svs 4', itso: 'itso name 4', totalAccount: 38, compliant: 18, nonCompliant: 20, nonCompliantAccounts: 6, other1: 0, other2: 6, other3: 8 },
        { appName: 'App Name5', vs: 'VS-003', svs: 'svs 5', itso: 'itso name 5', totalAccount: 91, compliant: 65, nonCompliant: 26, nonCompliantAccounts: 12, other1: 0, other2: 12, other3: 2 },
        { appName: 'App Name6', vs: 'VS-004', svs: 'svs 6', itso: 'itso name 6', totalAccount: 25, compliant: 5, nonCompliant: 20, nonCompliantAccounts: 8, other1: 0, other2: 8, other3: 4 },
        { appName: 'App Name7', vs: 'VS-005', svs: 'svs 7', itso: 'itso name 7', totalAccount: 60, compliant: 45, nonCompliant: 15, nonCompliantAccounts: 7, other1: 0, other2: 7, other3: 1 },
        { appName: 'App Name8', vs: 'VS-006', svs: 'svs 8', itso: 'itso name 8', totalAccount: 80, compliant: 30, nonCompliant: 50, nonCompliantAccounts: 20, other1: 0, other2: 20, other3: 10 },
        { appName: 'App Name9', vs: 'VS-007', svs: 'svs 9', itso: 'itso name 9', totalAccount: 45, compliant: 40, nonCompliant: 5, nonCompliantAccounts: 2, other1: 0, other2: 2, other3: 1 },
        { appName: 'App Name10', vs: 'VS-008', svs: 'svs 10', itso: 'itso name 10', totalAccount: 70, compliant: 25, nonCompliant: 45, nonCompliantAccounts: 18, other1: 0, other2: 18, other3: 9 }
    ];
}

// Check if G3Utils already exists
if (typeof window.G3Utils === 'undefined') {
    window.G3Utils = {
            calculateTotalNonCompliantPercentage(data) {
                const totalAccounts = data.reduce((sum, item) => sum + item.totalAccount, 0);
                const totalNonCompliant = data.reduce((sum, item) => sum + item.nonCompliant, 0);
                return totalAccounts > 0 ? (totalNonCompliant / totalAccounts * 100).toFixed(2) : 0;
            },

            calculatePoR(nonCompliant, totalAccount) {
                return totalAccount > 0 ? ((nonCompliant / totalAccount) * 100).toFixed(2) : 0;
            },

            getSeverity(percentage) {
                if (percentage > 30) return 'critical';
                if (percentage > 15) return 'warning';
                return 'good';
            },

            getNonComplianceByVS(data) {
                const vsGroups = {};
                data.forEach(item => {
                    if (!vsGroups[item.vs]) {
                        vsGroups[item.vs] = {
                            totalAccounts: 0,
                            nonCompliant: 0,
                            apps: []
                        };
                    }
                    vsGroups[item.vs].totalAccounts += item.totalAccount;
                    vsGroups[item.vs].nonCompliant += item.nonCompliant;
                    vsGroups[item.vs].apps.push(item);
                });

                return Object.entries(vsGroups).map(([vs, data]) => ({
                    vs,
                    percentage: this.calculatePoR(data.nonCompliant, data.totalAccounts),
                    nonCompliant: data.nonCompliant,
                    totalAccounts: data.totalAccounts,
                    severity: this.getSeverity(this.calculatePoR(data.nonCompliant, data.totalAccounts)),
                    apps: data.apps
                }));
            },

            filterData(data, filter) {
                if (filter === 'all') return data;

                return data.filter(item => {
                    const porPercentage = this.calculatePoR(item.nonCompliant, item.totalAccount);
                    const severity = this.getSeverity(porPercentage);
                    return severity === 'critical' || severity === 'warning';
                });
            },

            renderBarChart(vsData) {
                if (!vsData.length) return '<p class="text-gray-500 text-center py-8">No data to display</p>';

                const maxPercentage = Math.max(...vsData.map(item => parseFloat(item.percentage)));
                const chartHeight = 240; // Increased from 200 to 240

                return `
                <div class="chart-container bg-white p-4 rounded-lg border border-gray-200" style="min-height: ${chartHeight + 76}px">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-semibold text-gray-900">Non-Compliance by VS</h3>
                        <span class="text-sm text-gray-500">Click bars for details</span>
                    </div>
                    <div class="flex items-end justify-between h-${chartHeight/4} space-x-2" style="height: ${chartHeight}px">
                        ${vsData.map(item => {
                            const barHeight = (parseFloat(item.percentage) / maxPercentage) * (chartHeight - 60); // Reduced from 40 to 60
                            const color = item.severity === 'critical' ? 'red' : item.severity === 'warning' ? 'yellow' : 'green';
                            
                            return `
                                <div class="flex flex-col items-center flex-1" data-vs="${item.vs}">
                                    <div class="chart-bar bg-${color}-500 rounded-t-lg w-full max-w-16 mx-auto cursor-pointer hover:bg-${color}-600 transition-all duration-300"
                                            style="height: ${barHeight}px; min-height: 10px;"
                                            title="${item.vs}: ${item.percentage}% non-compliant">
                                    </div>
                                    <div class="text-xs text-gray-600 mt-2 text-center truncate w-full max-w-20" title="${item.vs}">
                                        ${this.truncateVSName(item.vs)}
                                    </div>
                                    <div class="text-xs font-semibold text-gray-800 mt-1">
                                        ${item.percentage}%
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                </div>
            `;
        },
        
        // Add this helper method for VS name truncation
        truncateVSName(vsName) {
            return vsName.length > 8 ? vsName.substring(0, 8) + '...' : vsName;
        },

        // Additional utility methods
        getTopNonCompliantApps(data, limit = 5) {
            return data
                .map(item => ({
                    ...item,
                    porPercentage: this.calculatePoR(item.nonCompliant, item.totalAccount)
                }))
                .sort((a, b) => parseFloat(b.porPercentage) - parseFloat(a.porPercentage))
                .slice(0, limit);
        },

        getComplianceSummary(data) {
            const totalApps = data.length;
            const criticalApps = data.filter(item => {
                const porPercentage = this.calculatePoR(item.nonCompliant, item.totalAccount);
                return this.getSeverity(porPercentage) === 'critical';
            }).length;
            
            const warningApps = data.filter(item => {
                const porPercentage = this.calculatePoR(item.nonCompliant, item.totalAccount);
                return this.getSeverity(porPercentage) === 'warning';
            }).length;

            return {
                totalApps,
                criticalApps,
                warningApps,
                goodApps: totalApps - criticalApps - warningApps
            };
        }
    };
}
```

## File: `data\g5-data.js`

```plaintext
// G5 Vulnerability Data
if (typeof window.g5RawData === 'undefined') {
    window.g5RawData = [{
            vs: 'VS-001',
            svs: 'SVS-001',
            itso: 'John Smith',
            appName: 'Customer Portal',
            severity: 'Critical',
            vulnerabilityId: 'VULN-2024-001',
            description: 'SQL Injection vulnerability in login endpoint',
            dueDate: '2024-12-31',
            status: 'Open',
            comment: 'Pending remediation from dev team'
        },
        {
            vs: 'VS-001',
            svs: 'SVS-001',
            itso: 'John Smith',
            appName: 'Customer Portal',
            severity: 'High',
            vulnerabilityId: 'VULN-2024-002',
            description: 'Cross-site scripting in user profile',
            dueDate: '2024-11-15',
            status: 'In Progress',
            comment: 'Fix scheduled for next sprint'
        },
        {
            vs: 'VS-002',
            svs: 'SVS-003',
            itso: 'Maria Garcia',
            appName: 'Payment Gateway',
            severity: 'Critical',
            vulnerabilityId: 'VULN-2024-003',
            description: 'Authentication bypass in API',
            dueDate: '2024-10-30',
            status: 'Open',
            comment: ''
        },
        {
            vs: 'VS-002',
            svs: 'SVS-004',
            itso: 'Maria Garcia',
            appName: 'Payment Gateway',
            severity: 'High',
            vulnerabilityId: 'VULN-2024-004',
            description: 'Insecure direct object reference',
            dueDate: '2024-11-20',
            status: 'Open',
            comment: 'Security review pending'
        },
        {
            vs: 'VS-003',
            svs: 'SVS-005',
            itso: 'David Chen',
            appName: 'Inventory Management',
            severity: 'High',
            vulnerabilityId: 'VULN-2024-005',
            description: 'Information disclosure in error messages',
            dueDate: '2024-12-10',
            status: 'Closed',
            comment: 'Resolved in v2.1.5'
        },
        {
            vs: 'VS-004',
            svs: 'SVS-006',
            itso: 'Sarah Wilson',
            appName: 'HR System',
            severity: 'Critical',
            vulnerabilityId: 'VULN-2024-006',
            description: 'Privilege escalation vulnerability',
            dueDate: '2024-10-25',
            status: 'Open',
            comment: 'Critical fix required'
        }
    ];
}

// G5 Utilities
if (typeof window.G5Utils === 'undefined') {
    window.G5Utils = {
            // Calculate severity status based on vulnerability counts
            calculateSeverityStatus(criticalCount, highCount) {
                if (criticalCount > 0) return 'critical';
                if (highCount > 100) return 'critical';
                if (highCount > 0) return 'warning';
                return 'good';
            },

            // Get vulnerabilities by VS
            getVulnerabilitiesByVS(data) {
                const vsGroups = {};

                data.forEach(item => {
                    if (!vsGroups[item.vs]) {
                        vsGroups[item.vs] = {
                            critical: 0,
                            high: 0,
                            vulnerabilities: []
                        };
                    }

                    if (item.severity === 'Critical') {
                        vsGroups[item.vs].critical++;
                    } else if (item.severity === 'High') {
                        vsGroups[item.vs].high++;
                    }

                    vsGroups[item.vs].vulnerabilities.push(item);
                });

                return Object.entries(vsGroups).map(([vs, data]) => ({
                    vs,
                    critical: data.critical,
                    high: data.high,
                    total: data.critical + data.high,
                    severity: this.calculateSeverityStatus(data.critical, data.high),
                    vulnerabilities: data.vulnerabilities
                }));
            },

            // Filter data by severity
            filterData(data, filter) {
                if (filter === 'all') return data;

                return data.filter(item => {
                    if (filter === 'critical') {
                        return item.severity === 'Critical';
                    } else if (filter === 'high') {
                        return item.severity === 'High';
                    }
                    return true;
                });
            },

            // In data\g5-data.js - Update the renderBarChart method
            renderBarChart(vsData) {
                if (!vsData.length) return '<p class="text-gray-500 text-center py-8">No vulnerabilities to display</p>';

                const maxTotal = Math.max(...vsData.map(item => item.total));
                const chartHeight = 240; // Increased from 200 to 240

                return `
                <div class="chart-container bg-white p-4 rounded-lg border border-gray-200" style="min-height: ${chartHeight + 118}px">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-semibold text-gray-900">Vulnerabilities by VS</h3>
                        <span class="text-sm text-gray-500">Click bars for details</span>
                    </div>
                    <div class="flex items-end justify-between space-x-2" style="height: ${chartHeight}px">
                        ${vsData.map(item => {
                            const criticalHeight = item.critical > 0 ? (item.critical / maxTotal) * (chartHeight - 80) : 0;
                            const highHeight = item.high > 0 ? (item.high / maxTotal) * (chartHeight - 80) : 0;
                            const totalHeight = criticalHeight + highHeight;
                            
                            return `
                                <div class="flex flex-col items-center flex-1" data-vs="${item.vs}">
                                    <div class="relative w-full max-w-16 mx-auto" style="height: ${chartHeight - 60}px">
                                        <!-- Critical vulnerabilities -->
                                        ${item.critical > 0 ? `
                                            <div class="chart-bar bg-red-500 hover:bg-red-600 rounded-t-lg w-full cursor-pointer transition-all duration-300 absolute bottom-0"
                                                    style="height: ${criticalHeight}px; min-height: 5px; z-index: 20;"
                                                    title="${item.vs}: ${item.critical} Critical vulnerabilities">
                                            </div>
                                        ` : ''}
                                        <!-- High vulnerabilities -->
                                        ${item.high > 0 ? `
                                            <div class="chart-bar bg-yellow-500 hover:bg-yellow-600 rounded-t-lg w-full cursor-pointer transition-all duration-300 absolute bottom-0"
                                                    style="height: ${highHeight}px; min-height: 5px; bottom: ${criticalHeight}px; z-index: 10;"
                                                    title="${item.vs}: ${item.high} High vulnerabilities">
                                            </div>
                                        ` : ''}
                                    </div>
                                    <div class="text-xs text-gray-600 mt-2 text-center truncate w-full max-w-20" title="${item.vs}">
                                        ${this.truncateVSName(item.vs)}
                                    </div>
                                    <div class="text-xs font-semibold text-gray-800 mt-1">
                                        C:${item.critical} H:${item.high}
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                    <div class="flex justify-center space-x-4 mt-6 text-xs">
                        <div class="flex items-center">
                            <div class="w-3 h-3 bg-red-500 rounded mr-1"></div>
                            <span>Critical</span>
                        </div>
                        <div class="flex items-center">
                            <div class="w-3 h-3 bg-yellow-500 rounded mr-1"></div>
                            <span>High</span>
                        </div>
                    </div>
                </div>
            `;
            },
            
            // Add this helper method for VS name truncation
            truncateVSName(vsName) {
                return vsName.length > 8 ? vsName.substring(0, 8) + '...' : vsName;
            },

        // Get summary statistics
        getSummary(data) {
            const critical = data.filter(item => item.severity === 'Critical').length;
            const high = data.filter(item => item.severity === 'High').length;
            const total = critical + high;
            
            return {
                total,
                critical,
                high,
                status: this.calculateSeverityStatus(critical, high)
            };
        },

        // Format date for display
        formatDate(dateString) {
            if (!dateString) return 'N/A';
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'short', 
                day: 'numeric' 
            });
        }
    };
}
```

## File: `data\itop2-data.js`

```plaintext
// ITOP.2 Critical Configuration Compliance Data
if (typeof window.itop2RawData === 'undefined') {
    window.itop2RawData = [{
            kci: 'ITOP.2.1A',
            vs: 'VS-001',
            svs: 'SVS-001',
            itso: 'John Smith',
            itService: 'Customer Portal',
            configItem: 'Firewall Rule Compliance',
            description: 'Violation of high critical config 1a - Unauthorized firewall rule detected',
            dueDate: '2024-10-15',
            status: 'Overdue',
            severity: 'High',
            por: 3
        },
        {
            kci: 'ITOP.2.1A',
            vs: 'VS-001',
            svs: 'SVS-002',
            itso: 'John Smith',
            itService: 'Customer Portal API',
            configItem: 'Access Control Compliance',
            description: 'Violation of high critical config 1a - Excessive permissions detected',
            dueDate: '2024-10-20',
            status: 'Overdue',
            severity: 'High',
            por: 2
        },
        {
            kci: 'ITOP.2.1B',
            vs: 'VS-002',
            svs: 'SVS-003',
            itso: 'Maria Garcia',
            itService: 'Payment Gateway',
            configItem: 'Encryption Configuration',
            description: 'Violation of high critical config 1b - Weak encryption algorithm in use',
            dueDate: '2024-10-18',
            status: 'Overdue',
            severity: 'Critical',
            por: 5
        },
        {
            kci: 'ITOP.2.1B',
            vs: 'VS-002',
            svs: 'SVS-004',
            itso: 'Maria Garcia',
            itService: 'Payment Gateway API',
            configItem: 'TLS Configuration',
            description: 'Violation of high critical config 1b - TLS 1.0 still enabled',
            dueDate: '2024-10-25',
            status: 'Overdue',
            severity: 'Critical',
            por: 4
        },
        {
            kci: 'ITOP.2.1A',
            vs: 'VS-003',
            svs: 'SVS-005',
            itso: 'David Chen',
            itService: 'Inventory Management',
            configItem: 'Logging Configuration',
            description: 'Violation of high critical config 1a - Insufficient logging configured',
            dueDate: '2024-11-01',
            status: 'Overdue',
            severity: 'Medium',
            por: 1
        },
        {
            kci: 'ITOP.2.1B',
            vs: 'VS-004',
            svs: 'SVS-006',
            itso: 'Sarah Wilson',
            itService: 'HR System',
            configItem: 'Authentication Configuration',
            description: 'Violation of high critical config 1b - MFA not enforced for admin accounts',
            dueDate: '2024-10-30',
            status: 'Overdue',
            severity: 'High',
            por: 3
        }
    ];
}

// ITOP.2 Utilities
if (typeof window.ITOP2Utils === 'undefined') {
    window.ITOP2Utils = {
            // Filter data by KCI selection
            filterData(data, kciFilter) {
                if (kciFilter === 'all') return data;
                return data.filter(item => item.kci === kciFilter);
            },

            // Get overdue items by VS
            getOverdueByVS(data) {
                const vsGroups = {};

                data.forEach(item => {
                    if (!vsGroups[item.vs]) {
                        vsGroups[item.vs] = {
                            kci1a: 0,
                            kci1b: 0,
                            total: 0,
                            items: []
                        };
                    }

                    if (item.kci === 'ITOP.2.1A') {
                        vsGroups[item.vs].kci1a += item.por;
                    } else if (item.kci === 'ITOP.2.1B') {
                        vsGroups[item.vs].kci1b += item.por;
                    }

                    vsGroups[item.vs].total += item.por;
                    vsGroups[item.vs].items.push(item);
                });

                return Object.entries(vsGroups).map(([vs, data]) => ({
                    vs,
                    kci1a: data.kci1a,
                    kci1b: data.kci1b,
                    total: data.total,
                    items: data.items
                }));
            },

            // Calculate severity status
            calculateSeverityStatus(total) {
                if (total > 10) return 'critical';
                if (total > 5) return 'warning';
                return 'good';
            },

            // Render bar chart for overdue items
            renderBarChart(vsData, kciFilter) {
                if (!vsData.length) return '<p class="text-gray-500 text-center py-8">No overdue items to display</p>';

                const maxTotal = Math.max(...vsData.map(item => item.total));
                const chartHeight = 240;

                return `
                <div class="chart-container bg-white p-4 rounded-lg border border-gray-200" style="min-height: ${chartHeight + 118}px">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-semibold text-gray-900">Overdue Items by VS</h3>
                        <span class="text-sm text-gray-500">Click bars for details</span>
                    </div>
                    <div class="flex items-end justify-between space-x-2" style="height: ${chartHeight}px">
                        ${vsData.map(item => {
                            const kci1aHeight = item.kci1a > 0 ? (item.kci1a / maxTotal) * (chartHeight - 80) : 0;
                            const kci1bHeight = item.kci1b > 0 ? (item.kci1b / maxTotal) * (chartHeight - 80) : 0;
                            const totalHeight = kci1aHeight + kci1bHeight;
                            
                            return `
                                <div class="flex flex-col items-center flex-1" data-vs="${item.vs}">
                                    <div class="relative w-full max-w-16 mx-auto" style="height: ${chartHeight - 60}px">
                                        <!-- KCI 1A items -->
                                        ${item.kci1a > 0 ? `
                                            <div class="chart-bar bg-blue-500 hover:bg-blue-600 rounded-t-lg w-full cursor-pointer transition-all duration-300 absolute bottom-0"
                                                    style="height: ${kci1aHeight}px; min-height: 5px; z-index: 20;"
                                                    title="${item.vs}: ${item.kci1a} KCI 1A overdue items">
                                            </div>
                                        ` : ''}
                                        <!-- KCI 1B items -->
                                        ${item.kci1b > 0 ? `
                                            <div class="chart-bar bg-purple-500 hover:bg-purple-600 rounded-t-lg w-full cursor-pointer transition-all duration-300 absolute bottom-0"
                                                    style="height: ${kci1bHeight}px; min-height: 5px; bottom: ${kci1aHeight}px; z-index: 10;"
                                                    title="${item.vs}: ${item.kci1b} KCI 1B overdue items">
                                            </div>
                                        ` : ''}
                                    </div>
                                    <div class="text-xs text-gray-600 mt-2 text-center truncate w-full max-w-20" title="${item.vs}">
                                        ${this.truncateVSName(item.vs)}
                                    </div>
                                    <div class="text-xs font-semibold text-gray-800 mt-1">
                                        A:${item.kci1a} B:${item.kci1b}
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                    <div class="flex justify-center space-x-4 mt-6 text-xs">
                        <div class="flex items-center">
                            <div class="w-3 h-3 bg-blue-500 rounded mr-1"></div>
                            <span>KCI 1A</span>
                        </div>
                        <div class="flex items-center">
                            <div class="w-3 h-3 bg-purple-500 rounded mr-1"></div>
                            <span>KCI 1B</span>
                        </div>
                    </div>
                </div>
            `;
        },

        // Helper method for VS name truncation
        truncateVSName(vsName) {
            return vsName.length > 8 ? vsName.substring(0, 8) + '...' : vsName;
        },

        // Get summary statistics
        getSummary(data) {
            const kci1a = data.filter(item => item.kci === 'ITOP.2.1A').length;
            const kci1b = data.filter(item => item.kci === 'ITOP.2.1B').length;
            const total = kci1a + kci1b;
            const totalPor = data.reduce((sum, item) => sum + item.por, 0);
            
            return {
                total,
                kci1a,
                kci1b,
                totalPor,
                status: this.calculateSeverityStatus(totalPor)
            };
        },

        // Format date for display
        formatDate(dateString) {
            if (!dateString) return 'N/A';
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'short', 
                day: 'numeric' 
            });
        }
    };
}
```

## File: `js\main.js`

```plaintext
// Main application entry point
document.addEventListener('DOMContentLoaded', () => {
    console.log('IT Governance Dashboard initialized');
    
    // Application version and info
    const appInfo = {
        name: 'IT Control & Governance Dashboard',
        version: '1.0.0',
        description: 'Compliance monitoring and risk management dashboard'
    };
    
    console.log(`🚀 ${appInfo.name} v${appInfo.version}`);
    console.log('📊 All modules loaded successfully');
    
    // Global error handler
    window.addEventListener('error', (event) => {
        console.error('Global error:', event.error);
    });
    
    // Performance monitoring
    const perfMark = 'app_fully_loaded';
    performance.mark(perfMark);
    
    // Additional global event listeners can be added here
    document.addEventListener('keydown', (e) => {
        // Global keyboard shortcuts
        if (e.ctrlKey || e.metaKey) {
            switch(e.key) {
                case '1':
                    e.preventDefault();
                    window.Router.renderPage('Overview');
                    break;
                case '2':
                    e.preventDefault();
                    window.Router.renderPage('GRAS.Overview');
                    break;
                case '3':
                    e.preventDefault();
                    window.Router.renderPage('GRAS.G3');
                    break;
            }
        }
    });
    
    // Export global app info for debugging
    window.AppInfo = appInfo;
});
```

## File: `js\core\data-manager.js`

```plaintext
// Check if DataManager already exists
if (typeof window.DataManager === 'undefined') {
    window.DataManager = {
        cache: new Map(),
        cacheDuration: 5 * 60 * 1000, // 5 minutes cache

        async getPageData(pageId, forceRefresh = false) {
            const cached = this.getFromCache(pageId);

            if (cached && !forceRefresh) {
                console.log(`Using cached data for ${pageId}`);
                return cached;
            }

            try {
                console.log(`Fetching fresh data for ${pageId}`);
                const data = await this.fetchPageData(pageId);
                this.setToCache(pageId, data);
                return data;
            } catch (error) {
                console.warn(`Failed to load data for ${pageId}, using fallback:`, error);
                return this.getFallbackData(pageId);
            }
        },

        async fetchPageData(pageId) {
            // In production, this would call real APIs
            // For now, simulate API delay and return mock data
            return new Promise((resolve) => {
                setTimeout(() => {
                    const mockData = this.getMockData(pageId);
                    resolve(mockData);
                }, 300); // Simulate network delay
            });
        },

        // Add to the getMockData method in DataManager
        getMockData(pageId) {
            const mockData = {
                'Overview': {
                    metrics: {
                        gras: window.getMetricData('GRAS.Overall', 90),
                        okr: window.getMetricData('OKR.Overall', 80),
                        gov: window.getMetricData('GOV.Overall', 95)
                    },
                    statusBoxes: [{
                            type: 'focus',
                            title: 'Key Focus',
                            content: 'Immediate action required on critical vulnerabilities (G46) older than 60 days.'
                        },
                        {
                            type: 'success',
                            title: 'Success Story',
                            content: 'Patching coverage (G43) hit a record 99.2% last month due to automation rollout.'
                        },
                        {
                            type: 'upcoming',
                            title: 'Upcoming Audit',
                            content: 'External audit for ITAM.3 and ITOP.1 scheduled for next week.'
                        }
                    ]
                },
                'GRAS.Overview': {
                    kpis: [
                        { metric: 'G3', title: 'Critical Control Status', description: '% of controls passing audits', target: 98, realValue: this.calculateG3Compliance() },
                        { metric: 'G5', title: 'High-Risk Reduction', description: '% of critical risks closed on time', target: 90, realValue: this.calculateG5Compliance() },
                        { metric: 'G43', title: 'Patching Coverage', description: '% of in-scope assets patched', target: 98, realValue: 96 },
                        { metric: 'G46', title: 'Vulnerability Age', description: 'Avg. days open for critical vulns', target: 70, realValue: 65 },
                        { metric: 'G51', title: 'IAM Compliance', description: '% of privileged accounts reviewed', target: 95, realValue: 92 },
                        { metric: 'G52', title: 'Access Reviews', description: '% of access reviews completed', target: 85, realValue: 88 },
                        { metric: 'G60', title: 'Incident Volume', description: '% reduction in repeat incidents', target: 50, realValue: 45 },
                        { metric: 'GXX', title: 'Future Metric', description: 'Placeholder for a new control metric', target: 99, realValue: 95 }
                    ]
                },

                'GOV.ITOP2': {
                    items: window.itop2RawData || []
                },
                // ... rest of your existing mockData
            };

            return mockData[pageId] || {};
        },

        // Add these calculation methods to DataManager
        calculateG3Compliance() {
            const items = window.g3RawData || [];
            if (items.length === 0) return 85;

            const totalNonCompliantPercentage = window.G3Utils.calculateTotalNonCompliantPercentage(items);
            return Math.max(0, 100 - parseFloat(totalNonCompliantPercentage));
        },

        calculateG5Compliance() {
            const items = window.g5RawData || [];
            if (items.length === 0) return 75;

            const summary = window.G5Utils.getSummary(items);
            let score = 100;
            if (summary.critical > 0) score -= 30;
            if (summary.high > 0) score -= Math.min(25, summary.high * 2);

            return Math.max(0, score);
        },

        // Add this method to your existing DataManager in js/core/data-manager.js
        getPageDataSync(pageId) {
            // For now, return mock data synchronously
            // In production, you'd want proper async handling
            return this.getMockData(pageId);
        },

        getFromCache(key) {
            const item = this.cache.get(key);
            if (item && Date.now() - item.timestamp < this.cacheDuration) {
                return item.data;
            }
            this.cache.delete(key);
            return null;
        },

        setToCache(key, data) {
            this.cache.set(key, {
                data,
                timestamp: Date.now()
            });
        },

        getFallbackData(pageId) {
            // Return basic fallback data when everything fails
            const fallbackData = {
                'Overview': { metrics: {}, statusBoxes: [] },
                'GRAS.Overview': { kpis: [] },
                'GRAS.G3': { items: [], summary: {} }
            };

            return fallbackData[pageId] || {};
        },

        clearCache() {
            this.cache.clear();
            console.log('Data cache cleared');
        },

        // Utility to check if we have cached data
        hasCachedData(pageId) {
            return this.getFromCache(pageId) !== null;
        }
    };
}
```

## File: `js\core\modal.js`

```plaintext
// Check if ModalManager already exists
if (typeof window.ModalManager === 'undefined') {
    window.ModalManager = {
        init() {
            const { modal, modalClose } = window.getDOMElements();
            
            if (modalClose) {
                modalClose.addEventListener('click', this.closeModal);
            }
            
            // Close modal on escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    this.closeModal();
                }
            });
            
            // Close modal when clicking outside content
            if (modal) {
                modal.addEventListener('click', (e) => {
                    if (e.target === modal) {
                        this.closeModal();
                    }
                });
            }
        },
        
        openModal(content, title = 'Details') {
            const { modal, modalTitle, modalContent } = window.getDOMElements();
            modalTitle.textContent = title;
            modalContent.innerHTML = content;
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        },
        
        closeModal() {
            const { modal } = window.getDOMElements();
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        },
        
        // Utility method to create modal content for charts
        createChartModal(title, chartData) {
            return `
                <div class="bg-white rounded-lg p-6">
                    <h3 class="text-xl font-bold mb-4">${title}</h3>
                    <div class="chart-placeholder h-64 bg-gray-100 rounded-lg flex items-center justify-center">
                        <p class="text-gray-500">Chart visualization for ${title}</p>
                    </div>
                    <div class="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-blue-50 p-4 rounded-lg">
                            <p class="text-sm font-semibold text-blue-800">Summary</p>
                            <p class="text-gray-600 mt-2">Detailed analysis and insights would be displayed here.</p>
                        </div>
                        <div class="bg-green-50 p-4 rounded-lg">
                            <p class="text-sm font-semibold text-green-800">Recommendations</p>
                            <p class="text-gray-600 mt-2">Action items and recommendations based on the data.</p>
                        </div>
                    </div>
                </div>
            `;
        }
    };

    // Initialize modal when script loads
    document.addEventListener('DOMContentLoaded', () => {
        window.ModalManager.init();
    });
}
```

## File: `js\core\navigation.js`

```plaintext
// Check if NavigationManager already exists
if (typeof window.NavigationManager === 'undefined') {
    window.NavigationManager = {
        init() {
            const { menu, menuToggle, menuClose, overlay, navItems } = window.getDOMElements();

            if (menuToggle) menuToggle.addEventListener('click', this.openMenu);
            if (menuClose) menuClose.addEventListener('click', this.closeMenu);
            if (overlay) overlay.addEventListener('click', this.closeMenu);

            // Initialize nav items
            navItems.forEach(item => {
                item.addEventListener('click', (e) => {
                    const path = e.currentTarget.dataset.path;
                    if (path) {
                        this.navigateTo(path);
                    }
                });
            });

            // Handle browser navigation
            window.addEventListener('hashchange', this.handleHashChange);

            // Close menu on resize (for mobile)
            window.addEventListener('resize', () => {
                if (window.innerWidth > 768) {
                    this.closeMenu();
                }
            });
        },

        openMenu() {
            const { menu, overlay } = window.getDOMElements();
            menu.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        },

        closeMenu() {
            const { menu, overlay } = window.getDOMElements();
            menu.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = 'auto';
        },

        navigateTo(path) {
            window.location.hash = path;
            this.closeMenu();
        },

        handleHashChange() {
            const path = window.location.hash.slice(1) || 'Overview';
            if (window.Router) {
                window.Router.renderPage(path);
            }
        },

        setActiveNavItem(path) {
            const { navItems } = window.getDOMElements();
            navItems.forEach(item => {
                item.classList.remove('active', 'bg-blue-700', 'text-white');
            });

            const activeItem = document.querySelector(`.nav-item[data-path="${path}"]`);
            if (activeItem) {
                activeItem.classList.add('active', 'bg-blue-700', 'text-white');
            }
        },

        // Utility to update page breadcrumbs
        updateBreadcrumbs(path) {
            // This could be extended to show breadcrumb navigation
            console.log('Navigation to:', path);
        }
    };

    // Initialize navigation when script loads
    document.addEventListener('DOMContentLoaded', () => {
        window.NavigationManager.init();
    });
}
```

## File: `js\core\router.js`

```plaintext
// Check if Router already exists
if (typeof window.Router === 'undefined') {
    window.Router = {
        componentRegistry: {},

        init() {
            this.registerCoreComponents();
            this.loadInitialPage();
        },

        registerCoreComponents() {
            // Core components that are always available
            this.componentRegistry = {
                'Overview': () => {
                    if (typeof window.OverviewComponent !== 'undefined') {
                        return window.OverviewComponent();
                    }
                    return this.showPlaceholder('Dashboard Overview');
                },
                'GRAS.Overview': () => {
                    if (typeof window.GRASOverviewComponent !== 'undefined') {
                        return window.GRASOverviewComponent();
                    }
                    return this.showPlaceholder('GRAS Overview');
                },
                'GRAS.G3': () => {
                    if (typeof window.GRASG3Component !== 'undefined') {
                        return window.GRASG3Component();
                    }
                    return this.showPlaceholder('G3: Control Status');
                },
                'GRAS.G5': () => {
                    console.log('G5 Component check - GRASG5Component exists:', typeof window.GRASG5Component !== 'undefined');
                    console.log('G5 Utils check - G5Utils exists:', typeof window.G5Utils !== 'undefined');
                    console.log('G5 Data check - g5RawData exists:', typeof window.g5RawData !== 'undefined');

                    if (typeof window.GRASG5Component !== 'undefined') {
                        console.log('Calling GRASG5Component...');
                        return window.GRASG5Component();
                    }
                    console.log('Falling back to placeholder');
                    return this.showPlaceholder('G5: Critical & High Vulnerabilities');
                },
                'GRAS.G43': () => this.showPlaceholder('G43: Patching Coverage'),
                'GRAS.G51': () => this.showPlaceholder('G51: IAM Compliance'),
                'OKR.Overview': () => this.showPlaceholder('Cyber OKR Overview'),
                'OKR.SECA': () => this.showPlaceholder('SECA: Security Adoption'),
                'GOV.ITOP1': () => this.showPlaceholder('ITOP.1: Change Management'),
                // Add to the componentRegistry in router.js
                'GOV.ITOP2': () => {
                    if (typeof window.GOVITOP2Component !== 'undefined') {
                        return window.GOVITOP2Component();
                    }
                    return this.showPlaceholder('ITOP.2: Critical Config Compliance');
                },

                'GOV.ITAM3': () => this.showPlaceholder('ITAM.3: Asset Inventory')
            };
        },

        async renderPage(path) {
            const { contentContainer, pageTitle, pageSubtitle } = window.getDOMElements();

            window.AppState.currentPage = path;
            window.NavigationManager.setActiveNavItem(path);

            // Set default page titles first
            const pageTitles = {
                'Overview': { title: 'Dashboard Overview', subtitle: 'A high-level summary of all IT Control domains.' },
                'GRAS.Overview': { title: 'GRAS Metrics Overview', subtitle: 'Key Performance Indicators across all risk categories.' },
                'GRAS.G3': { title: 'GRAS Metric: G3 (Control Status)', subtitle: 'Real-time compliance status of critical IT controls.' },
                'GRAS.G5': { title: 'GRAS Metric: G5 (Critical & High Vulnerabilities)', subtitle: 'Management of Critical and High severity vulnerabilities across all systems.' },
                'GRAS.G43': { title: 'G43: Patching Coverage', subtitle: 'Asset patching compliance details.' },
                'GRAS.G51': { title: 'G51: IAM Compliance', subtitle: 'User access management compliance tracking.' },
                'OKR.Overview': { title: 'Cyber OKR Overview', subtitle: 'Quarter-by-quarter objective progress.' },
                'OKR.SECA': { title: 'SECA: Security Adoption', subtitle: 'Adoption rate of new security tools.' },
                'GOV.ITOP1': { title: 'ITOP.1: Change Management', subtitle: 'Change management compliance tracking.' },
                'GOV.ITOP2': { title: 'ITOP.2: Critical Config Compliance', subtitle: 'Monitoring of overdue critical configuration compliance items.' },
                'GOV.ITAM3': { title: 'ITAM.3: Asset Inventory', subtitle: 'Asset database accuracy tracking.' }
            };

            const defaultTitle = pageTitles[path] || { title: path, subtitle: 'Page details' };
            pageTitle.textContent = defaultTitle.title;
            pageSubtitle.textContent = defaultTitle.subtitle;

            // Show loading state
            contentContainer.innerHTML = `
                <div class="col-span-3 flex justify-center items-center h-64">
                    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700"></div>
                    <span class="ml-3 text-gray-600">Loading ${path}...</span>
                </div>
            `;

            try {
                const component = this.componentRegistry[path];
                if (component) {
                    // Handle both async and sync components
                    const html = await Promise.resolve(component());
                    contentContainer.innerHTML = html;

                    // Initialize page-specific event handlers
                    this.initializePageHandlers(path);
                } else {
                    contentContainer.innerHTML = this.show404(path);
                }
            } catch (error) {
                console.error(`Error rendering page ${path}:`, error);
                contentContainer.innerHTML = this.showError(`Error loading ${path}: ${error.message}`);
            }
        },

        initializePageHandlers(path) {
            // Page-specific initialization
            switch (path) {
                case 'GRAS.G3':
                    this.initializeG3Handlers();
                    break;
                case 'GRAS.G5':
                    this.initializeG5Handlers();
                    break;
                    // Add other page handlers as needed
            }
        },

        initializeG3Handlers() {
            // G3 specific event handlers - FIXED: No page refresh
            const criticalBtn = document.getElementById('show-critical-btn');
            const clearFilterBtn = document.getElementById('clear-filter-btn');

            if (criticalBtn) {
                criticalBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.AppState.currentFilter = 'critical';
                    this.updateG3Content();
                });
            }

            if (clearFilterBtn) {
                clearFilterBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.AppState.currentFilter = 'all';
                    this.updateG3Content();
                });
            }

            // Chart bar handlers
            const chartBars = document.querySelectorAll('.chart-bar');
            chartBars.forEach(bar => {
                bar.addEventListener('click', (e) => {
                    e.preventDefault();
                    const vsContainer = e.target.closest('[data-vs]');
                    if (vsContainer) {
                        const vs = vsContainer.getAttribute('data-vs');
                        this.openVSModal(vs);
                    }
                });
            });
        },

        // NEW METHOD: Update G3 content without full page refresh
        updateG3Content() {
            const { contentContainer } = window.getDOMElements();

            // Show loading state for smooth transition
            contentContainer.innerHTML = `
                <div class="col-span-3 flex justify-center items-center h-64">
                    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700"></div>
                    <span class="ml-3 text-gray-600">Updating data...</span>
                </div>
            `;

            // Small delay to show loading, then update content
            setTimeout(() => {
                if (typeof window.GRASG3Component !== 'undefined') {
                    const html = window.GRASG3Component();
                    contentContainer.innerHTML = html;

                    // Re-initialize handlers for the updated content
                    this.initializeG3Handlers();
                }
            }, 150);
        },

        openVSModal(vs) {
            // This would be implemented in the G3 component
            console.log('Opening modal for VS:', vs);
            // For now, show a simple modal
            window.ModalManager.openModal(`
                <div class="bg-white p-6 rounded-lg">
                    <h3 class="text-xl font-bold mb-4">${vs} - Details</h3>
                    <p class="text-gray-600">Detailed view for ${vs} would go here.</p>
                    <p class="text-gray-600 mt-2">This modal can show charts, tables, or any other detailed information.</p>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-sm text-blue-800">VS-specific data and analysis would be displayed in this modal.</p>
                    </div>
                </div>
            `, `${vs} Details`);
        },

        initializeG5Handlers() {
            // G5 specific event handlers
            const criticalBtn = document.getElementById('show-critical-btn');
            const highBtn = document.getElementById('show-high-btn');
            const clearFilterBtn = document.getElementById('clear-filter-btn');

            if (criticalBtn) {
                criticalBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.AppState.currentFilter = 'critical';
                    this.updateG5Content();
                });
            }

            if (highBtn) {
                highBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.AppState.currentFilter = 'high';
                    this.updateG5Content();
                });
            }

            if (clearFilterBtn) {
                clearFilterBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    window.AppState.currentFilter = 'all';
                    this.updateG5Content();
                });
            }

            // Chart bar handlers for VS details
            const chartBars = document.querySelectorAll('.chart-bar');
            chartBars.forEach(bar => {
                bar.addEventListener('click', (e) => {
                    e.preventDefault();
                    const vsContainer = e.target.closest('[data-vs]');
                    if (vsContainer) {
                        const vs = vsContainer.getAttribute('data-vs');
                        this.openVSVulnerabilitiesModal(vs);
                    }
                });
            });
        },

        updateG5Content() {
            const { contentContainer } = window.getDOMElements();

            // Show loading state
            contentContainer.innerHTML = `
                <div class="col-span-3 flex justify-center items-center h-64">
                    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700"></div>
                    <span class="ml-3 text-gray-600">Updating vulnerability data...</span>
                </div>
            `;

            // Update content
            setTimeout(() => {
                if (typeof window.GRASG5Component !== 'undefined') {
                    const html = window.GRASG5Component();
                    contentContainer.innerHTML = html;
                    this.initializeG5Handlers();
                }
            }, 150);
        },

        openVSVulnerabilitiesModal(vs) {
            const vsData = window.AppState.currentVSData.find(item => item.vs === vs);
            if (!vsData) return;

            const vulnerabilities = vsData.vulnerabilities.map(vuln => `
                <tr class="border-t border-gray-100">
                    <td class="p-3 text-sm text-gray-800">${vuln.appName}</td>
                    <td class="p-3 text-sm text-gray-600">${vuln.vulnerabilityId}</td>
                    <td class="p-3 text-sm">${window.ComponentTemplates.renderStatusBadge(vuln.severity.toLowerCase(), 'sm')}</td>
                    <td class="p-3 text-sm text-gray-600">${window.G5Utils.formatDate(vuln.dueDate)}</td>
                    <td class="p-3 text-sm text-gray-600">${vuln.status}</td>
                </tr>
            `).join('');

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-6xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">${vs} - Vulnerability Details</h3>
                    <div class="mb-4 grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-red-50 p-3 rounded-lg text-center">
                            <p class="text-2xl font-bold text-red-600">${vsData.critical}</p>
                            <p class="text-sm text-red-800">Critical</p>
                        </div>
                        <div class="bg-orange-50 p-3 rounded-lg text-center">
                            <p class="text-2xl font-bold text-orange-600">${vsData.high}</p>
                            <p class="text-sm text-orange-800">High</p>
                        </div>
                        <div class="bg-blue-50 p-3 rounded-lg text-center">
                            <p class="text-2xl font-bold text-blue-600">${vsData.total}</p>
                            <p class="text-sm text-blue-800">Total</p>
                        </div>
                        <div class="bg-gray-50 p-3 rounded-lg text-center">
                            <p class="text-sm font-semibold text-${vsData.severity}-600 capitalize">${vsData.severity}</p>
                            <p class="text-sm text-gray-800">Status</p>
                        </div>
                    </div>
                    
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">App Name</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Vulnerability ID</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Severity</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Due Date</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Status</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                ${vulnerabilities}
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="mt-4 flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, `${vs} Vulnerabilities`);
        },

        showPlaceholder(title) {
            return `
                <div class="col-span-3 bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl font-bold text-gray-900 mb-4">${title}</h3>
                    <p class="text-gray-600">This page is under development.</p>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-sm text-blue-800">To implement this page, create a JavaScript file in the pages folder and register it in the router.</p>
                    </div>
                </div>
            `;
        },

        show404(path) {
            return `
                <div class="col-span-3 bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl text-red-600 font-bold mb-4">404: Page Not Found</h3>
                    <p class="text-gray-600">The page "${path}" was not found.</p>
                    <button onclick="window.Router.renderPage('Overview')" class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition duration-200">
                        Return to Dashboard
                    </button>
                </div>
            `;
        },

        showError(message) {
            return `
                <div class="col-span-3 bg-white p-8 rounded-xl shadow-lg">
                    <h3 class="text-2xl text-red-600 font-bold mb-4">Error</h3>
                    <p class="text-gray-600">${message}</p>
                    <button onclick="window.location.reload()" class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition duration-200">
                        Reload Page
                    </button>
                </div>
            `;
        },

        loadInitialPage() {
            const initialPath = window.location.hash.slice(1) || 'Overview';
            this.renderPage(initialPath);
        }
    };

    // Initialize router when script loads
    document.addEventListener('DOMContentLoaded', () => {
        window.Router.init();
    });
}
```

## File: `js\core\utils.js`

```plaintext
// Global state management - only define once
if (typeof window.AppState === 'undefined') {
    window.AppState = {
        currentFilter: 'all',
        currentKCI: 'all',
        currentData: [],
        currentVSData: [],
        currentPage: 'Overview'
    };
}

// Core utility functions - only define once
if (typeof window.getMetricData === 'undefined') {
    window.getMetricData = (name, target = 95) => {
        const value = Math.floor(Math.random() * 90) + 10;
        const trend = (Math.random() > 0.5) ? 'up' : 'down';
        return {
            value: value,
            target: target,
            status: value >= target ? 'High' : (value >= (target - 10) ? 'Medium' : 'Low'),
            color: value >= target ? 'green' : (value >= (target - 10) ? 'yellow' : 'red'),
            trend: trend,
            trendIcon: trend === 'up' ? '▲' : '▼'
        };
    };
}

// DOM element getters - only define once
if (typeof window.getDOMElements === 'undefined') {
    window.getDOMElements = () => ({
        menu: document.getElementById('menu'),
        menuToggle: document.getElementById('menu-toggle'),
        menuClose: document.getElementById('menu-close'),
        overlay: document.getElementById('overlay'),
        modal: document.getElementById('chart-modal'),
        modalClose: document.getElementById('modal-close'),
        modalTitle: document.getElementById('modal-title'),
        modalContent: document.getElementById('modal-content'),
        navItems: document.querySelectorAll('.nav-item'),
        contentContainer: document.getElementById('content-container'),
        pageTitle: document.getElementById('page-title'),
        pageSubtitle: document.getElementById('page-subtitle')
    });
}

// Additional utility functions
if (typeof window.formatPercentage === 'undefined') {
    window.formatPercentage = (value) => {
        return `${parseFloat(value).toFixed(2)}%`;
    };
}

if (typeof window.getColorClass === 'undefined') {
    window.getColorClass = (value, target) => {
        if (value >= target) return 'green';
        if (value >= target - 10) return 'yellow';
        return 'red';
    };
}

// Comment Manager - only define once

// Replace the CommentManager in utils.js with this complete version
if (typeof window.CommentManager === 'undefined') {
    window.CommentManager = {
            // Action types with standardized statuses
            actionTypes: {
                REMEDIATED: 'remediated',
                FIXED: 'fixed',
                CLOSED: 'closed',
                PENDING: 'pending',
                ESCALATION: 'escalation',
                CALL_OUT: 'call_out',
                RISK_ACCEPTANCE: 'risk_acceptance',
                EXCEPTION: 'exception',
                FALSE_POSITIVE: 'false_positive',
                DEMISED: 'demised'
            },

            // Action type configurations with static classes
            actionConfig: {
                remediated: {
                    label: 'Remediated',
                    colorClass: 'action-green',
                    icon: 'fa-check-circle',
                    description: 'Issue has been fully remediated'
                },
                fixed: {
                    label: 'Fixed',
                    colorClass: 'action-green',
                    icon: 'fa-wrench',
                    description: 'Technical fix applied'
                },
                closed: {
                    label: 'Closed',
                    colorClass: 'action-gray',
                    icon: 'fa-times-circle',
                    description: 'Issue closed without action'
                },
                pending: {
                    label: 'Pending',
                    colorClass: 'action-yellow',
                    icon: 'fa-clock',
                    description: 'Action in progress'
                },
                escalation: {
                    label: 'Escalation',
                    colorClass: 'action-orange',
                    icon: 'fa-exclamation-triangle',
                    description: 'Escalated to leadership'
                },
                call_out: {
                    label: 'Call Out',
                    colorClass: 'action-red',
                    icon: 'fa-bullhorn',
                    description: 'Critical issue requiring attention'
                },
                risk_acceptance: {
                    label: 'Risk Acceptance',
                    colorClass: 'action-blue',
                    icon: 'fa-file-signature',
                    description: 'Risk formally accepted'
                },
                exception: {
                    label: 'Exception',
                    colorClass: 'action-purple',
                    icon: 'fa-flag',
                    description: 'Temporary exception granted'
                },
                false_positive: {
                    label: 'False Positive',
                    colorClass: 'action-gray',
                    icon: 'fa-search',
                    description: 'Identified as false positive'
                },
                demised: {
                    label: 'Demised',
                    colorClass: 'action-gray',
                    icon: 'fa-trash',
                    description: 'Asset/control no longer exists'
                }
            },

            // Generate simplified comment form with action buttons
            generateCommentForm(itemId, itemType, currentData) {
                return `
                <div class="bg-white p-6 rounded-lg max-w-4xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Control Commentary</h3>
                    
                    <!-- Item Information -->
                    <div class="bg-gray-50 p-4 rounded-lg mb-6">
                        <h4 class="font-semibold text-gray-800 mb-2">Item Details</h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
                            ${this.renderItemDetails(currentData)}
                        </div>
                    </div>

                    <!-- Action Type Selection -->
                    <div class="mb-6">
                        <label class="block text-sm font-medium text-gray-700 mb-3">Select Action Type</label>
                        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3" id="action-buttons-container-${itemId}">
                            ${Object.entries(this.actionTypes).map(([key, value]) => {
                                const config = this.actionConfig[value];
                                return `
                                    <button type="button" 
                                            data-action-type="${value}"
                                            class="action-type-btn p-3 border-2 border-gray-300 rounded-lg text-left transition-all duration-200 hover:scale-105 hover:shadow-md">
                                        <div class="flex items-center">
                                            <i class="fas ${config.icon} ${config.colorClass}-icon mr-2"></i>
                                            <span class="font-medium text-gray-900">${config.label}</span>
                                        </div>
                                        <div class="text-xs text-gray-500 mt-1">${config.description}</div>
                                    </button>
                                `;
                            }).join('')}
                        </div>
                    </div>

                    <!-- Selected Action Display -->
                    <div id="selected-action-${itemId}" class="hidden mb-4 p-3 rounded-lg border action-blue-bg">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center">
                                <i class="fas fa-check-circle text-blue-600 mr-2"></i>
                                <span class="font-medium text-blue-800">Action Selected: <span id="selected-action-label-${itemId}"></span></span>
                            </div>
                            <button onclick="CommentManager.clearActionType('${itemId}')" 
                                    class="text-blue-600 hover:text-blue-800 text-sm">
                                Change
                            </button>
                        </div>
                    </div>

                    <!-- Comment Field -->
                    <div class="mb-6">
                        <label class="block text-sm font-medium text-gray-700 mb-2">
                            Explanation & Details
                        </label>
                        <textarea 
                            id="comment-explanation-${itemId}"
                            class="w-full p-3 rounded-lg bg-gray-50 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"
                            rows="4"
                            placeholder="Provide detailed explanation of the issue, actions taken, timeline, and any relevant context..."></textarea>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex justify-end space-x-3 mt-6 pt-4 border-t">
                        <button onclick="window.ModalManager.closeModal()" 
                                class="px-4 py-2 text-gray-600 hover:text-gray-800 font-medium">
                            Cancel
                        </button>
                        <button onclick="CommentManager.saveComment('${itemId}', '${itemType}')" 
                                class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                                id="save-comment-btn-${itemId}"
                                disabled>
                            Save Commentary
                        </button>
                    </div>
                </div>
            `;
        },

        // Get item data from global state
        getItemData(itemId, itemType) {
            let itemData = {
                vs: 'Unknown',
                appName: 'Unknown',
                itso: 'Unknown',
                severity: 'Unknown'
            };

            try {
                if (itemType === 'G3') {
                    // Extract VS and AppName from itemId format: "G3_VS-001_AppName"
                    const parts = itemId.split('_');
                    if (parts.length >= 3) {
                        const vs = parts[1];
                        const appName = parts.slice(2).join('_');
                        
                        // Find the item in G3 data
                        const g3Data = window.g3RawData || [];
                        const item = g3Data.find(d => d.vs === vs && d.appName === appName.replace(/_/g, ' '));
                        
                        if (item) {
                            const porPercentage = window.G3Utils ? window.G3Utils.calculatePoR(item.nonCompliant, item.totalAccount) : 0;
                            const severity = window.G3Utils ? window.G3Utils.getSeverity(porPercentage) : 'Unknown';
                            itemData = {
                                ...item,
                                severity: severity,
                                porPercentage: porPercentage
                            };
                        } else {
                            itemData.vs = vs;
                            itemData.appName = appName.replace(/_/g, ' ');
                        }
                    }
                } else if (itemType === 'G5') {
                    // Extract vulnerability ID from itemId format: "G5_VULN-2024-001"
                    const vulnId = itemId.replace('G5_', '');
                    
                    // Find the item in G5 data
                    const g5Data = window.g5RawData || [];
                    const item = g5Data.find(d => d.vulnerabilityId === vulnId);
                    
                    if (item) {
                        itemData = item;
                    } else {
                        itemData.vulnerabilityId = vulnId;
                    }
                }
            } catch (error) {
                console.error('Error getting item data:', error);
            }
            
            return itemData;
        },

        renderItemDetails(data) {
            if (!data) {
                return '<div>Item details not available</div>';
            }

            const details = [];

            if (data.vs) details.push(`<div><strong>VS:</strong> ${data.vs}</div>`);
            if (data.appName) details.push(`<div><strong>Application:</strong> ${data.appName}</div>`);
            if (data.itso && data.itso !== 'Unknown') details.push(`<div><strong>ITSO:</strong> ${data.itso}</div>`);
            if (data.severity && data.severity !== 'Unknown') details.push(`<div><strong>Severity:</strong> ${data.severity}</div>`);

            // G3 specific details
            if (data.porPercentage) details.push(`<div><strong>Non-Compliance:</strong> ${data.porPercentage}%</div>`);
            if (data.nonCompliant !== undefined && data.totalAccount !== undefined) {
                details.push(`<div><strong>Accounts:</strong> ${data.nonCompliant}/${data.totalAccount} non-compliant</div>`);
            }

            // G5 specific details
            if (data.vulnerabilityId) details.push(`<div><strong>Vulnerability ID:</strong> ${data.vulnerabilityId}</div>`);
            if (data.description) details.push(`<div><strong>Description:</strong> ${data.description}</div>`);
            if (data.dueDate) {
                const formattedDate = window.G5Utils ? window.G5Utils.formatDate(data.dueDate) : data.dueDate;
                details.push(`<div><strong>Due Date:</strong> ${formattedDate}</div>`);
            }

            if (details.length === 0) {
                return '<div>Item details not available</div>';
            }

            return details.join('');
        },

        selectActionType(actionType, itemId) {
            const config = this.actionConfig[actionType];
            
            // Remove selection from all buttons
            document.querySelectorAll('.action-type-btn').forEach(btn => {
                btn.classList.remove('action-selected');
                btn.style.borderColor = '#d1d5db'; // gray-300
                btn.style.backgroundColor = '#ffffff'; // white
            });
            
            // Highlight selected button
            const selectedBtn = event.target.closest('.action-type-btn');
            selectedBtn.classList.add('action-selected');
            selectedBtn.style.borderColor = this.getBorderColor(config.colorClass);
            selectedBtn.style.backgroundColor = this.getBackgroundColor(config.colorClass);
            
            // Show selected action display
            const selectedActionDiv = document.getElementById(`selected-action-${itemId}`);
            const selectedActionLabel = document.getElementById(`selected-action-label-${itemId}`);
            
            selectedActionLabel.textContent = config.label;
            selectedActionDiv.className = `mb-4 p-3 rounded-lg border ${config.colorClass}-bg`;
            selectedActionDiv.classList.remove('hidden');
            
            // Enable save button
            document.getElementById(`save-comment-btn-${itemId}`).disabled = false;
        },

        getBorderColor(colorClass) {
            const colors = {
                'action-green': '#10b981',
                'action-red': '#ef4444', 
                'action-yellow': '#f59e0b',
                'action-orange': '#f97316',
                'action-blue': '#3b82f6',
                'action-purple': '#8b5cf6',
                'action-gray': '#6b7280'
            };
            return colors[colorClass] || '#3b82f6';
        },

        getBackgroundColor(colorClass) {
            const colors = {
                'action-green': '#ecfdf5',
                'action-red': '#fef2f2',
                'action-yellow': '#fffbeb', 
                'action-orange': '#fff7ed',
                'action-blue': '#eff6ff',
                'action-purple': '#faf5ff',
                'action-gray': '#f9fafb'
            };
            return colors[colorClass] || '#eff6ff';
        },

        clearActionType(itemId) {
            // Reset all buttons
            document.querySelectorAll('.action-type-btn').forEach(btn => {
                btn.classList.remove('action-selected');
                btn.style.borderColor = '#d1d5db';
                btn.style.backgroundColor = '#ffffff';
            });
            
            // Hide selected action display
            document.getElementById(`selected-action-${itemId}`).classList.add('hidden');
            
            // Disable save button
            document.getElementById(`save-comment-btn-${itemId}`).disabled = true;
        },

        // Initialize action buttons after modal opens
        initActionButtons(itemId) {
            const container = document.getElementById(`action-buttons-container-${itemId}`);
            if (container) {
                container.addEventListener('click', (e) => {
                    const button = e.target.closest('.action-type-btn');
                    if (button) {
                        const actionType = button.getAttribute('data-action-type');
                        this.selectActionType(actionType, itemId);
                    }
                });
            }
        },

        // Updated openCommentModal to initialize buttons
        openCommentModal(itemId, itemType) {
            try {
                this.ensureCommentManagerInitialized();
                const itemData = this.getItemData(itemId, itemType);
                const modalContent = this.generateCommentForm(itemId, itemType, itemData);
                window.ModalManager.openModal(modalContent, 'Standardized Commentary');
                
                // Initialize buttons after a short delay to ensure DOM is ready
                setTimeout(() => {
                    this.initActionButtons(itemId);
                }, 100);
            } catch (error) {
                console.error('Error opening comment modal:', error);
                const fallbackContent = `
                    <div class="bg-white p-6 rounded-lg">
                        <h3 class="text-xl font-bold text-red-600 mb-4">Error</h3>
                        <p class="text-gray-600">Unable to load comment form. Please try again.</p>
                        <div class="mt-4 flex justify-end">
                            <button onclick="window.ModalManager.closeModal()" 
                                    class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">
                                Close
                            </button>
                        </div>
                    </div>
                `;
                window.ModalManager.openModal(fallbackContent, 'Error');
            }
        },

        async saveComment(itemId, itemType) {
            try {
                const selectedBtn = document.querySelector('.action-type-btn.action-selected');
                
                if (!selectedBtn) {
                    this.showErrorMessage('Please select an action type');
                    return;
                }

                const actionType = selectedBtn.getAttribute('data-action-type');
                const config = this.actionConfig[actionType];

                const commentData = {
                    id: this.generateCommentId(),
                    itemId: itemId,
                    itemType: itemType,
                    actionType: actionType,
                    actionLabel: config.label,
                    timestamp: new Date().toISOString(),
                    user: 'Current User',
                    status: config.colorClass.replace('action-', '').toUpperCase(),
                    explanation: document.getElementById(`comment-explanation-${itemId}`)?.value || ''
                };

                // Save to localStorage
                this.saveToStorage(commentData);

                // Update UI to show comment exists
                this.updateItemCommentIndicator(itemId, commentData);

                window.ModalManager.closeModal();
                this.showSuccessMessage(`${config.label} commentary saved successfully!`);
            } catch (error) {
                console.error('Error saving comment:', error);
                this.showErrorMessage('Failed to save commentary. Please try again.');
            }
        },

        // Updated viewComments to show action-based comments
        viewComments(itemId) {
            const comments = this.getCommentsForItem(itemId);
            const modalContent = this.renderCommentsList(itemId, comments);
            window.ModalManager.openModal(modalContent, 'Action History');
        },

        renderCommentsList(itemId, comments) {
            if (!comments.length) {
                return '<div class="p-6 text-center text-gray-500">No comments found</div>';
            }

            return `
                <div class="bg-white p-6 rounded-lg max-w-4xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Action History</h3>
                    <div class="space-y-4">
                        ${comments.map(comment => {
                            const config = this.actionConfig[comment.actionType];
                            return `
                                <div class="border border-gray-200 rounded-lg p-4">
                                    <div class="flex justify-between items-start mb-3">
                                        <div class="flex items-center">
                                            <span class="px-3 py-1 rounded-full text-sm font-semibold mr-3 flex items-center ${config.colorClass}-badge">
                                                <i class="fas ${config.icon} mr-1"></i>
                                                ${comment.actionLabel}
                                            </span>
                                            <span class="text-sm text-gray-500">by ${comment.user}</span>
                                        </div>
                                        <span class="text-xs text-gray-500">${new Date(comment.timestamp).toLocaleString()}</span>
                                    </div>
                                    
                                    ${comment.explanation ? `
                                        <div class="mb-3">
                                            <h4 class="font-semibold text-gray-700 text-sm mb-1">Explanation</h4>
                                            <p class="text-sm text-gray-700">${comment.explanation}</p>
                                        </div>
                                    ` : ''}
                                </div>
                            `;
                        }).join('')}
                    </div>
                    <div class="flex justify-end mt-4">
                        <button onclick="window.ModalManager.closeModal()" 
                                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg">
                            Close
                        </button>
                    </div>
                </div>
            `;
        },

        generateCommentId() {
            return 'COMM_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        },

        saveToStorage(commentData) {
            let comments = JSON.parse(localStorage.getItem('control_comments') || '{}');
            if (!comments[commentData.itemId]) {
                comments[commentData.itemId] = [];
            }
            comments[commentData.itemId].push(commentData);
            localStorage.setItem('control_comments', JSON.stringify(comments));
        },

        getCommentsForItem(itemId) {
            const comments = JSON.parse(localStorage.getItem('control_comments') || '{}');
            return comments[itemId] || [];
        },

        updateItemCommentIndicator(itemId, commentData) {
            const commentBtn = document.querySelector(`[data-item-id="${itemId}"]`);
            if (commentBtn) {
                commentBtn.innerHTML = `
                    <i class="fas fa-comment-check text-green-600 mr-1"></i>
                    <span class="text-green-600 text-xs">Commented</span>
                `;
                commentBtn.title = `Last action: ${commentData.actionLabel} - ${new Date(commentData.timestamp).toLocaleDateString()}`;
            }
        },

        ensureCommentManagerInitialized() {
            if (!localStorage.getItem('control_comments')) {
                localStorage.setItem('control_comments', JSON.stringify({}));
            }
        },

        showSuccessMessage(message) {
            const toast = document.createElement('div');
            toast.className = 'fixed top-4 right-4 bg-green-600 text-white p-4 rounded-lg shadow-lg z-50';
            toast.innerHTML = `
                <div class="flex items-center">
                    <i class="fas fa-check-circle mr-2"></i>
                    <span>${message}</span>
                </div>
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        },

        showErrorMessage(message) {
            const toast = document.createElement('div');
            toast.className = 'fixed top-4 right-4 bg-red-600 text-white p-4 rounded-lg shadow-lg z-50';
            toast.innerHTML = `
                <div class="flex items-center">
                    <i class="fas fa-exclamation-circle mr-2"></i>
                    <span>${message}</span>
                </div>
            `;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        },

        // Export functionality methods
        exportCommentsByMetric(metricType) {
            const allComments = JSON.parse(localStorage.getItem('control_comments') || '{}');
            const metricComments = this.filterCommentsByMetric(allComments, metricType);
            
            if (Object.keys(metricComments).length === 0) {
                this.showErrorMessage(`No comments found for ${metricType}`);
                return;
            }
            
            const csvContent = this.convertMetricCommentsToCSV(metricComments, metricType);
            const filename = `${metricType}_comments_${new Date().toISOString().split('T')[0]}.csv`;
            this.downloadCSV(csvContent, filename);
        },

        filterCommentsByMetric(allComments, metricType) {
            const filtered = {};
            
            Object.entries(allComments).forEach(([itemId, commentList]) => {
                const metricComments = commentList.filter(comment => 
                    comment.itemType === metricType
                );
                
                if (metricComments.length > 0) {
                    filtered[itemId] = metricComments;
                }
            });
            
            return filtered;
        },

        convertMetricCommentsToCSV(metricComments, metricType) {
            const headers = [
                'Metric', 'VS', 'Application', 'ITSO', 'Severity', 
                'Action Type', 'Action Label', 'User', 'Timestamp', 'Explanation'
            ];
            
            const rows = [headers.join(',')];

            Object.entries(metricComments).forEach(([itemId, commentList]) => {
                commentList.forEach(comment => {
                    const itemData = this.getItemData(itemId, metricType);
                    
                    const row = [
                        metricType,
                        itemData.vs || 'N/A',
                        itemData.appName || 'N/A',
                        itemData.itso || 'N/A',
                        itemData.severity || 'N/A',
                        comment.actionType,
                        comment.actionLabel,
                        comment.user,
                        new Date(comment.timestamp).toLocaleDateString(),
                        `"${comment.explanation || ''}"`
                    ].join(',');
                    
                    rows.push(row);
                });
            });

            return rows.join('\n');
        },

        downloadCSV(content, filename) {
            const blob = new Blob([content], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            window.URL.revokeObjectURL(url);
        },

        getCommentCountByMetric(metricType) {
            const allComments = JSON.parse(localStorage.getItem('control_comments') || '{}');
            let count = 0;
            
            Object.values(allComments).forEach(commentList => {
                commentList.forEach(comment => {
                    if (comment.itemType === metricType) {
                        count++;
                    }
                });
            });
            
            return count;
        },

        getTotalCommentCount() {
            const allComments = JSON.parse(localStorage.getItem('control_comments') || '{}');
            let total = 0;
            
            Object.values(allComments).forEach(commentList => {
                total += commentList.length;
            });
            
            return total;
        }
    };

    // Initialize CommentManager when the script loads
    document.addEventListener('DOMContentLoaded', () => {
        if (window.CommentManager) {
            window.CommentManager.ensureCommentManagerInitialized();
        }
    });
}
```

## File: `js\pages\component-templates.js`

```plaintext
// Check if ComponentTemplates already exists
if (typeof window.ComponentTemplates === 'undefined') {
    window.ComponentTemplates = {
            renderMetricCard(title, description, data) {
                return `
                <div class="metric-card bg-white p-4 lg:p-6 rounded-xl shadow-lg border-t-4 border-${data.color}-500">
                    <div class="flex justify-between items-start">
                        <div>
                            <p class="text-sm font-medium text-gray-600">${title}</p>
                            <p class="text-2xl lg:text-4xl font-bold text-gray-900 mt-1">${data.value}%</p>
                        </div>
                        <div class="flex flex-col items-end">
                            <span class="text-2xl lg:text-3xl text-${data.color}-600 font-extrabold">${data.trendIcon}</span>
                            <span class="text-xs text-gray-500">Target: ${data.target}%</span>
                        </div>
                    </div>
                    <p class="text-sm mt-3 text-gray-500">${description}</p>
                    <div class="mt-4 text-sm font-semibold">
                        Status: <span class="text-${data.color}-600">${data.status}</span>
                    </div>
                </div>
            `;
            },

            renderKPICard(metric, title, description, target) {
                const data = window.getMetricData(metric, target);
                const isPassing = data.value >= data.target;
                const bgColor = isPassing ? 'bg-green-600' : 'bg-red-600';
                const textColor = 'text-white';

                return `
                    <div class="metric-card p-4 lg:p-5 rounded-xl shadow-lg border border-gray-200 flex flex-col justify-between bg-white">
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <span class="text-lg lg:text-xl font-bold text-gray-900">${metric}</span>
                                <span class="text-xs lg:text-sm text-gray-500">Target: ${target}%</span>
                            </div>
                            <p class="text-3xl lg:text-4xl font-extrabold text-blue-700">${data.value}%</p>
                            <p class="text-xs lg:text-sm text-gray-600 mt-2">${description}</p>
                        </div>
                        <div class="mt-4 flex justify-between items-center">
                            <span class="px-3 py-1 text-xs font-semibold rounded-full ${bgColor} ${textColor} shadow-md">
                                ${isPassing ? 'Compliant' : 'Non-Compliant'}
                            </span>
                            <!-- FIXED: Use NavigationManager for proper URL update -->
                            <button class="text-xs lg:text-sm text-blue-700 hover:text-blue-500 font-medium" 
                                    onclick="window.NavigationManager.navigateTo('GRAS.${metric}')">
                                View Details &rarr;
                            </button>
                        </div>
                    </div>
                `;
            },

            renderStatusBadge(status, size = 'md') {
                const sizes = {
                    sm: 'px-2 py-1 text-xs',
                    md: 'px-3 py-1 text-sm',
                    lg: 'px-4 py-2 text-base'
                };

                const statusConfig = {
                    critical: { bg: 'bg-red-100', text: 'text-red-800', label: 'Critical' },
                    warning: { bg: 'bg-yellow-100', text: 'text-yellow-800', label: 'Warning' },
                    good: { bg: 'bg-green-100', text: 'text-green-800', label: 'Good' },
                    high: { bg: 'bg-green-100', text: 'text-green-800', label: 'High' },
                    medium: { bg: 'bg-yellow-100', text: 'text-yellow-800', label: 'Medium' },
                    low: { bg: 'bg-red-100', text: 'text-red-800', label: 'Low' }
                };

                const config = statusConfig[status.toLowerCase()] || statusConfig.medium;

                return `
                <span class="${sizes[size]} ${config.bg} ${config.text} font-semibold rounded-full">
                    ${config.label}
                </span>
            `;
            },

            renderDataTable(headers, rows, options = {}) {
                const { sortable = false, selectable = false, actions = [] } = options;

                const headerRow = headers.map(header => `
                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider ${sortable ? 'cursor-pointer hover:bg-gray-50' : ''}">
                    ${header}
                    ${sortable ? '<i class="fas fa-sort ml-1 text-gray-400"></i>' : ''}
                </th>
            `).join('');

                const tableRows = rows.map(row => `
                <tr class="border-t border-gray-100 hover:bg-blue-50 transition duration-150">
                    ${selectable ? `
                        <td class="p-3 lg:p-4 whitespace-nowrap">
                            <input type="checkbox" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500">
                        </td>
                    ` : ''}
                    ${row.map(cell => `
                        <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${cell}</td>
                    `).join('')}
                    ${actions.length > 0 ? `
                        <td class="p-3 lg:p-4 whitespace-nowrap text-sm font-medium">
                            <div class="flex space-x-2">
                                ${actions.map(action => `
                                    <button class="text-${action.color}-600 hover:text-${action.color}-900" onclick="${action.onclick}">
                                        ${action.icon ? `<i class="${action.icon}"></i>` : action.label}
                                    </button>
                                `).join('')}
                            </div>
                        </td>
                    ` : ''}
                </tr>
            `).join('');
            
            return `
                <div class="overflow-x-auto rounded-xl border border-gray-300 shadow-inner">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                ${selectable ? '<th scope="col" class="relative w-12 px-6"><input type="checkbox" class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"></th>' : ''}
                                ${headerRow}
                                ${actions.length > 0 ? '<th scope="col" class="relative px-6"><span class="sr-only">Actions</span></th>' : ''}
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 bg-white">
                            ${tableRows}
                        </tbody>
                    </table>
                </div>
            `;
        }
    };
}
```

## File: `js\pages\gov-itop2.js`

```plaintext
// ITOP.2 Component - Critical Configuration Compliance
if (typeof window.GOVITOP2Component === 'undefined') {
    window.GOVITOP2Component = () => {
        const elements = window.getDOMElements();
        elements.pageTitle.textContent = "ITOP.2: Critical Config Compliance";
        elements.pageSubtitle.textContent = "Monitoring of overdue critical configuration compliance items across KCIs.";

        // Load ITOP.2 data
        const itop2Data = window.DataManager.getPageDataSync('GOV.ITOP2');

        return renderITOP2Page(itop2Data);
    };

    // Main rendering method
    const renderITOP2Page = (itop2Data) => {
            const items = itop2Data.items || window.itop2RawData || [];
            const currentKCI = window.AppState.currentKCI || 'all';

            // Apply current KCI filter
            const currentData = window.ITOP2Utils.filterData(items, currentKCI);

            // Calculate metrics
            const vsData = window.ITOP2Utils.getOverdueByVS(currentData);
            const summary = window.ITOP2Utils.getSummary(currentData);

            // Update global state
            window.AppState.currentData = currentData;
            window.AppState.currentVSData = vsData;

            // Generate table rows
            const tableRows = currentData.map(item => {
                        const severityColor = item.severity === 'Critical' ? 'red' :
                            item.severity === 'High' ? 'yellow' : 'green';
                        const itemId = `ITOP2_${item.kci}_${item.vs}_${item.svs}`;
                        const comments = window.CommentManager.getCommentsForItem(itemId);
                        const hasComments = comments.length > 0;

                        return `
                <tr class="border-t border-gray-100 hover:bg-blue-50 transition duration-150">
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-800 font-medium">${item.kci}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.vs}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.itService}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.itso}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap">
                        <button onclick="ITOP2ActionManager.openPorDetails('${item.vs}', '${item.svs}', '${item.kci}')" 
                                class="text-blue-600 hover:text-blue-800 font-semibold text-sm p-1 rounded hover:bg-blue-100 transition-colors">
                            ${item.por}
                        </button>
                    </td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm font-medium">
                        <div class="flex space-x-2">
                            <button data-item-id="${itemId}" 
                                    onclick="CommentManager.openCommentModal('${itemId}', 'ITOP2')"
                                    class="${hasComments ? 'text-green-600 border-green-200 bg-green-50' : 'text-blue-600 border-blue-200 bg-blue-50'} hover:opacity-80 text-xs p-2 border rounded-lg transition-colors">
                                ${hasComments ? 
                                    '<i class="fas fa-comment-check mr-1"></i>Commented' : 
                                    '<i class="fas fa-comment-medical mr-1"></i>Add Comment'}
                            </button>
                            ${hasComments ? `
                                <button onclick="CommentManager.viewComments('${itemId}')"
                                        class="text-gray-600 hover:text-gray-800 text-xs p-2 border border-gray-200 bg-gray-50 rounded-lg transition-colors">
                                    <i class="fas fa-list mr-1"></i>View (${comments.length})
                                </button>
                            ` : ''}
                            <button onclick="ITOP2ActionManager.viewDetails('${item.kci}', '${item.vs}', '${item.svs}')" 
                                    class="text-green-600 hover:text-green-800 text-xs p-2 border border-green-200 bg-green-50 rounded-lg transition-colors">
                                <i class="fas fa-eye mr-1"></i>Details
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');

        return `
            <!-- Key Performance Overview -->
            <div class="lg:col-span-3 grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 mb-6 lg:mb-8">
                <div class="lg:col-span-1">
                    <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-4">Compliance Summary</h3>
                    <div class="metric-card bg-white p-4 lg:p-6 rounded-xl shadow-lg border-t-4 border-${summary.status}-500">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-sm font-medium text-gray-600">Total Overdue Items</p>
                                <p class="text-2xl lg:text-4xl font-bold text-gray-900 mt-1">${summary.total}</p>
                            </div>
                            <div class="flex flex-col items-end">
                                <span class="text-2xl lg:text-3xl text-${summary.status}-600 font-extrabold">
                                    ${summary.status === 'critical' ? '⚠️' : summary.status === 'warning' ? '🔶' : '✅'}
                                </span>
                                <span class="text-xs text-gray-500">Total POR: ${summary.totalPor}</span>
                            </div>
                        </div>
                        <div class="mt-4 space-y-2">
                            <div class="flex justify-between text-sm">
                                <span class="text-blue-600 font-semibold">KCI 1A:</span>
                                <span class="text-blue-600 font-bold">${summary.kci1a}</span>
                            </div>
                            <div class="flex justify-between text-sm">
                                <span class="text-purple-600 font-semibold">KCI 1B:</span>
                                <span class="text-purple-600 font-bold">${summary.kci1b}</span>
                            </div>
                        </div>
                        <div class="mt-4 text-sm font-semibold">
                            Status: <span class="text-${summary.status}-600 capitalize">
                                ${summary.status}
                            </span>
                        </div>
                    </div>

                    <!-- KCI Selection -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">KCI Filter</h4>
                        <div class="space-y-3">
                            <button onclick="ITOP2ActionManager.setKCIFilter('all')" 
                                    class="w-full p-3 text-left rounded-lg border-2 ${currentKCI === 'all' ? 'border-blue-500 bg-blue-50' : 'border-gray-200 hover:bg-gray-50'} transition duration-200">
                                <div class="flex items-center">
                                    <i class="fas fa-layer-group ${currentKCI === 'all' ? 'text-blue-600' : 'text-gray-400'} mr-3"></i>
                                    <span class="font-semibold ${currentKCI === 'all' ? 'text-blue-800' : 'text-gray-700'}">All KCIs</span>
                                </div>
                                <p class="text-sm ${currentKCI === 'all' ? 'text-blue-600' : 'text-gray-500'} mt-1">Show all configuration items</p>
                            </button>
                            <button onclick="ITOP2ActionManager.setKCIFilter('ITOP.2.1A')" 
                                    class="w-full p-3 text-left rounded-lg border-2 ${currentKCI === 'ITOP.2.1A' ? 'border-blue-500 bg-blue-50' : 'border-gray-200 hover:bg-gray-50'} transition duration-200">
                                <div class="flex items-center">
                                    <i class="fas fa-shield-alt ${currentKCI === 'ITOP.2.1A' ? 'text-blue-600' : 'text-gray-400'} mr-3"></i>
                                    <span class="font-semibold ${currentKCI === 'ITOP.2.1A' ? 'text-blue-800' : 'text-gray-700'}">KCI 1A Only</span>
                                </div>
                                <p class="text-sm ${currentKCI === 'ITOP.2.1A' ? 'text-blue-600' : 'text-gray-500'} mt-1">Violation of high critical config 1a</p>
                            </button>
                            <button onclick="ITOP2ActionManager.setKCIFilter('ITOP.2.1B')" 
                                    class="w-full p-3 text-left rounded-lg border-2 ${currentKCI === 'ITOP.2.1B' ? 'border-purple-500 bg-purple-50' : 'border-gray-200 hover:bg-gray-50'} transition duration-200">
                                <div class="flex items-center">
                                    <i class="fas fa-cog ${currentKCI === 'ITOP.2.1B' ? 'text-purple-600' : 'text-gray-400'} mr-3"></i>
                                    <span class="font-semibold ${currentKCI === 'ITOP.2.1B' ? 'text-purple-800' : 'text-gray-700'}">KCI 1B Only</span>
                                </div>
                                <p class="text-sm ${currentKCI === 'ITOP.2.1B' ? 'text-purple-600' : 'text-gray-500'} mt-1">Violation of high critical config 1b</p>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-2">
                    <h3 class="text-lg lg:text-xl font-semibold text-gray-900 mb-4">Overdue Items by Virtual System</h3>
                    ${window.ITOP2Utils.renderBarChart(vsData, currentKCI)}
                    <p class="text-xs text-gray-500 mt-2">Click on any bar to view detailed items for that Virtual System</p>

                    <!-- Quick Stats -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">Quick Stats</h4>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="text-center p-3 bg-blue-50 rounded-lg">
                                <p class="text-2xl font-bold text-blue-600">${summary.kci1a}</p>
                                <p class="text-sm text-blue-800">KCI 1A Items</p>
                            </div>
                            <div class="text-center p-3 bg-purple-50 rounded-lg">
                                <p class="text-2xl font-bold text-purple-600">${summary.kci1b}</p>
                                <p class="text-sm text-purple-800">KCI 1B Items</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Overdue Items Summary Table -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">
                <div class="flex flex-col gap-4 mb-6">
                    <div class="flex flex-wrap gap-2">
                        <button onclick="ITOP2ActionManager.exportCommentsByMetric('ITOP2')" 
                                class="bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            <i class="fas fa-file-export mr-1"></i>Export ITOP2 Comments
                        </button>
                        <button onclick="ITOP2ActionManager.exportData()" 
                                class="bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            <i class="fas fa-download mr-1"></i>Export Data
                        </button>
                    </div>
                
                    <!-- Responsive filters -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
                        <input type="text" placeholder="Filter by VS..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <input type="text" placeholder="Filter by IT Service..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <input type="text" placeholder="Filter by ITSO..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <button class="bg-blue-700 hover:bg-blue-800 text-white font-semibold py-2 px-4 rounded-lg text-sm transition duration-200 shadow-md">
                            APPLY FILTERS
                        </button>
                    </div>
                </div>

                <!-- Table -->
                <div class="overflow-x-auto rounded-xl border border-gray-300 shadow-inner">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">KCI</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">VS</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">IT Service</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">ITSO</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">POR</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 bg-white">
                            ${tableRows || '<tr><td colspan="6" class="p-4 text-center text-gray-500">No overdue items match the current filter</td></tr>'}
                        </tbody>
                    </table>
                </div>

                <div class="flex flex-col lg:flex-row justify-between items-center text-sm text-gray-600 mt-4 gap-2">
                    <span>Showing ${currentData.length} of ${items.length} Overdue Items</span>
                    <div class="flex space-x-4 items-center">
                        <button class="text-blue-700 hover:text-blue-500 disabled:opacity-50 font-medium p-1" disabled>&#8592; Previous</button>
                        <span class="px-3 py-1 bg-gray-100 rounded-md">1</span>
                        <button class="text-blue-700 hover:text-blue-500 font-medium p-1">Next &#8594;</button>
                    </div>
                </div>
            </div>

            <!-- Commentary Section -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">
                <h3 class="text-lg lg:text-xl font-bold text-gray-900 mb-4">Add Audit Commentary</h3>
                <textarea placeholder="Enter commentary about the current configuration compliance status for audit/review..." rows="4" class="w-full p-3 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"></textarea>
                <button class="mt-3 bg-blue-700 hover:bg-blue-800 text-white font-bold py-2 px-4 rounded-lg transition duration-200 shadow-md">
                    Submit Commentary
                </button>
            </div>
        `;
    };
}

// ITOP.2 Action Manager
if (typeof window.ITOP2ActionManager === 'undefined') {
    window.ITOP2ActionManager = {
        setKCIFilter(kciFilter) {
            window.AppState.currentKCI = kciFilter;
            this.updateITOP2Content();
        },

        updateITOP2Content() {
            const { contentContainer } = window.getDOMElements();

            // Show loading state
            contentContainer.innerHTML = `
                <div class="col-span-3 flex justify-center items-center h-64">
                    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-700"></div>
                    <span class="ml-3 text-gray-600">Updating ITOP.2 data...</span>
                </div>
            `;

            // Update content
            setTimeout(() => {
                if (typeof window.GOVITOP2Component !== 'undefined') {
                    const html = window.GOVITOP2Component();
                    contentContainer.innerHTML = html;
                    this.initializeITOP2Handlers();
                }
            }, 150);
        },

        initializeITOP2Handlers() {
            // Chart bar handlers for VS details
            const chartBars = document.querySelectorAll('.chart-bar');
            chartBars.forEach(bar => {
                bar.addEventListener('click', (e) => {
                    e.preventDefault();
                    const vsContainer = e.target.closest('[data-vs]');
                    if (vsContainer) {
                        const vs = vsContainer.getAttribute('data-vs');
                        this.openVSDetailsModal(vs);
                    }
                });
            });
        },

        openPorDetails(vs, svs, kci) {
            const items = window.itop2RawData.filter(item => 
                item.vs === vs && item.svs === svs && item.kci === kci
            );
            
            if (items.length === 0) return;

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-6xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">POR Details - ${vs} / ${svs} / ${kci}</h3>
                    
                    <div class="mb-6 grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="bg-blue-50 p-4 rounded-lg text-center">
                            <p class="text-2xl font-bold text-blue-600">${items[0].por}</p>
                            <p class="text-sm text-blue-800">Total Items</p>
                        </div>
                        <div class="bg-gray-50 p-4 rounded-lg text-center">
                            <p class="text-sm font-semibold text-gray-800">${items[0].itService}</p>
                            <p class="text-sm text-gray-600">IT Service</p>
                        </div>
                        <div class="bg-gray-50 p-4 rounded-lg text-center">
                            <p class="text-sm font-semibold text-gray-800">${items[0].itso}</p>
                            <p class="text-sm text-gray-600">ITSO</p>
                        </div>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Config Item</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Description</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Due Date</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Severity</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Status</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                ${items.map(item => `
                                    <tr class="border-t border-gray-100">
                                        <td class="p-3 text-sm text-gray-800">${item.configItem}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.description}</td>
                                        <td class="p-3 text-sm text-gray-600">${window.ITOP2Utils.formatDate(item.dueDate)}</td>
                                        <td class="p-3 text-sm">${window.ComponentTemplates.renderStatusBadge(item.severity.toLowerCase(), 'sm')}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.status}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="mt-6 flex justify-between">
                        <button onclick="ITOP2ActionManager.exportVSData('${vs}', '${svs}', '${kci}')" 
                                class="px-4 py-2 bg-green-600 hover:bg-green-700 text-white font-medium rounded-lg transition duration-200">
                            <i class="fas fa-download mr-2"></i>Export This Data
                        </button>
                        <button onclick="window.ModalManager.closeModal()" 
                                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, `POR Details - ${vs}/${svs}`);
        },

        openVSDetailsModal(vs) {
            const vsData = window.AppState.currentVSData.find(item => item.vs === vs);
            if (!vsData) return;

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-6xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">${vs} - Overdue Configuration Items</h3>
                    
                    <div class="mb-6 grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-blue-50 p-4 rounded-lg text-center">
                            <p class="text-2xl font-bold text-blue-600">${vsData.kci1a}</p>
                            <p class="text-sm text-blue-800">KCI 1A Items</p>
                        </div>
                        <div class="bg-purple-50 p-4 rounded-lg text-center">
                            <p class="text-2xl font-bold text-purple-600">${vsData.kci1b}</p>
                            <p class="text-sm text-purple-800">KCI 1B Items</p>
                        </div>
                        <div class="bg-gray-50 p-4 rounded-lg text-center">
                            <p class="text-2xl font-bold text-gray-600">${vsData.total}</p>
                            <p class="text-sm text-gray-800">Total Items</p>
                        </div>
                        <div class="bg-gray-50 p-4 rounded-lg text-center">
                            <p class="text-sm font-semibold text-gray-800 capitalize">${window.ITOP2Utils.calculateSeverityStatus(vsData.total)}</p>
                            <p class="text-sm text-gray-600">Status</p>
                        </div>
                    </div>
                    
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">KCI</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">SVS</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">IT Service</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">ITSO</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">POR</th>
                                    <th class="p-3 text-left text-xs font-bold text-gray-600 uppercase">Due Date</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                ${vsData.items.map(item => `
                                    <tr class="border-t border-gray-100">
                                        <td class="p-3 text-sm text-gray-800">${item.kci}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.svs}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.itService}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.itso}</td>
                                        <td class="p-3 text-sm text-gray-600">${item.por}</td>
                                        <td class="p-3 text-sm text-gray-600">${window.ITOP2Utils.formatDate(item.dueDate)}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="mt-6 flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" 
                                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, `${vs} Configuration Items`);
        },

        viewDetails(kci, vs, svs) {
            const item = window.itop2RawData.find(i => 
                i.kci === kci && i.vs === vs && i.svs === svs
            );
            
            if (!item) return;

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-4xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Configuration Item Details</h3>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Basic Information</h4>
                            <div class="space-y-2">
                                <p><strong>KCI:</strong> ${item.kci}</p>
                                <p><strong>VS:</strong> ${item.vs}</p>
                                <p><strong>SVS:</strong> ${item.svs}</p>
                                <p><strong>IT Service:</strong> ${item.itService}</p>
                                <p><strong>ITSO:</strong> ${item.itso}</p>
                            </div>
                        </div>
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Compliance Details</h4>
                            <div class="space-y-2">
                                <p><strong>Config Item:</strong> ${item.configItem}</p>
                                <p><strong>Description:</strong> ${item.description}</p>
                                <p><strong>Due Date:</strong> ${window.ITOP2Utils.formatDate(item.dueDate)}</p>
                                <p><strong>Status:</strong> ${item.status}</p>
                                <p><strong>Severity:</strong> ${window.ComponentTemplates.renderStatusBadge(item.severity.toLowerCase(), 'sm')}</p>
                                <p><strong>POR:</strong> ${item.por}</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-6 flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" 
                                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, 'Configuration Item Details');
        },

        exportCommentsByMetric(metricType) {
            if (window.CommentManager) {
                window.CommentManager.exportCommentsByMetric(metricType);
            }
        },

        exportData() {
            const data = window.itop2RawData;
            const csvContent = this.convertToCSV(data);
            const filename = `ITOP2_export_${new Date().toISOString().split('T')[0]}.csv`;
            this.downloadCSV(csvContent, filename);
        },

        exportVSData(vs, svs, kci) {
            const data = window.itop2RawData.filter(item => 
                item.vs === vs && item.svs === svs && item.kci === kci
            );
            const csvContent = this.convertToCSV(data);
            const filename = `ITOP2_${vs}_${svs}_${kci}_export_${new Date().toISOString().split('T')[0]}.csv`;
            this.downloadCSV(csvContent, filename);
        },

        convertToCSV(data) {
            const headers = ['KCI', 'VS', 'SVS', 'IT Service', 'ITSO', 'Config Item', 'Description', 'Due Date', 'Status', 'Severity', 'POR'];
            const rows = [headers.join(',')];

            data.forEach(item => {
                const row = [
                    item.kci,
                    item.vs,
                    item.svs,
                    `"${item.itService}"`,
                    item.itso,
                    `"${item.configItem}"`,
                    `"${item.description}"`,
                    item.dueDate,
                    item.status,
                    item.severity,
                    item.por
                ].join(',');
                rows.push(row);
            });

            return rows.join('\n');
        },

        downloadCSV(content, filename) {
            const blob = new Blob([content], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            window.URL.revokeObjectURL(url);
        }
    };
}

// Initialize ITOP.2 when the script loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('ITOP.2 Component initialized');
    
    // Initialize action handlers if on ITOP.2 page
    if (window.AppState && window.AppState.currentPage === 'GOV.ITOP2') {
        setTimeout(() => {
            if (window.ITOP2ActionManager) {
                window.ITOP2ActionManager.initializeITOP2Handlers();
            }
        }, 100);
    }
});
```

## File: `js\pages\gras-g3.js`

```plaintext
// Check if GRASG3Component already exists
if (typeof window.GRASG3Component === 'undefined') {
    window.GRASG3Component = () => {
        // Only access DOM elements when the function is called
        const elements = window.getDOMElements();
        elements.pageTitle.textContent = "GRAS Metric: G3 (Control Status)";
        elements.pageSubtitle.textContent = "Real-time compliance status of critical IT controls.";

        // FIXED: Remove async and use DataManager synchronously for now
        const g3Data = window.DataManager.getPageDataSync('GRAS.G3');

        // Process and render the data
        return renderG3Page(g3Data);
    };

    // Main rendering method
    const renderG3Page = (g3Data) => {
            const items = g3Data.items || window.g3RawData || [];

            // Apply current filter to data
            const currentData = window.G3Utils.filterData(items, window.AppState.currentFilter);

            // Calculate metrics from filtered data
            const totalNonCompliantPercentage = window.G3Utils.calculateTotalNonCompliantPercentage(currentData);
            const currentVSData = window.G3Utils.getNonComplianceByVS(currentData);
            const complianceSummary = window.G3Utils.getComplianceSummary(currentData);
            const topNonCompliant = window.G3Utils.getTopNonCompliantApps(currentData, 3);

            // Update global state
            window.AppState.currentData = currentData;
            window.AppState.currentVSData = currentVSData;

            // Determine status color based on percentage
            const statusColor = totalNonCompliantPercentage > 30 ? 'red' :
                totalNonCompliantPercentage > 15 ? 'yellow' : 'green';

            // Generate table rows for non-compliant summary WITH ACTION COLUMN (matching G5 design)
            const tableRows = currentData.map(item => {
                        const porPercentage = window.G3Utils.calculatePoR(item.nonCompliant, item.totalAccount);
                        const severity = window.G3Utils.getSeverity(porPercentage);
                        const severityColor = severity === 'critical' ? 'red' : severity === 'warning' ? 'yellow' : 'green';
                        const itemId = `G3_${item.vs}_${item.appName.replace(/\s+/g, '_')}`;
                        const comments = window.CommentManager ? window.CommentManager.getCommentsForItem(itemId) : [];
                        const hasComments = comments.length > 0;

                        return `
                <tr class="border-t border-gray-100 hover:bg-blue-50 transition duration-150">
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-800 font-medium">${item.vs}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.appName}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.itso}</td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm font-semibold text-${severityColor}-600">
                        ${porPercentage}% ${item.nonCompliant}/${item.totalAccount}
                    </td>
                    <td class="p-3 lg:p-4 whitespace-nowrap text-sm font-medium">
                        <div class="flex space-x-2">
                            <button data-item-id="${itemId}" 
                                    onclick="CommentManager.openCommentModal('${itemId}', 'G3')"
                                    class="${hasComments ? 'text-green-600 border-green-200 bg-green-50' : 'text-blue-600 border-blue-200 bg-blue-50'} hover:opacity-80 text-xs p-2 border rounded-lg transition-colors">
                                ${hasComments ? 
                                    '<i class="fas fa-comment-check mr-1"></i>Commented' : 
                                    '<i class="fas fa-comment-medical mr-1"></i>Add Comment'}
                            </button>
                            ${hasComments ? `
                                <button onclick="CommentManager.viewComments('${itemId}')"
                                        class="text-gray-600 hover:text-gray-800 text-xs p-2 border border-gray-200 bg-gray-50 rounded-lg transition-colors">
                                    <i class="fas fa-list mr-1"></i>View (${comments.length})
                                </button>
                            ` : ''}
                            <button onclick="G3ActionManager.viewDetails('${item.appName}')" 
                                    class="text-green-600 hover:text-green-800 text-xs p-2 border border-green-200 bg-green-50 rounded-lg transition-colors">
                                <i class="fas fa-eye mr-1"></i>Details
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        }).join('');

        return `
            <!-- Key Performance Overview and Trend Analysis -->
            <div class="lg:col-span-3 grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 mb-6 lg:mb-8">
                <div class="lg:col-span-1">
                    <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-4">Overall Compliance Score</h3>
                    <div class="metric-card bg-white p-4 lg:p-6 rounded-xl shadow-lg border-t-4 border-${statusColor}-500">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-sm font-medium text-gray-600">Non-Compliant Percentage</p>
                                <p class="text-2xl lg:text-4xl font-bold text-gray-900 mt-1">${totalNonCompliantPercentage}%</p>
                            </div>
                            <div class="flex flex-col items-end">
                                <span class="text-2xl lg:text-3xl text-${statusColor}-600 font-extrabold">
                                    ${totalNonCompliantPercentage > 15 ? '⚠️' : '✅'}
                                </span>
                                <span class="text-xs text-gray-500">Target: < 15%</span>
                            </div>
                        </div>
                        <p class="text-sm mt-3 text-gray-500">Percentage of accounts that are non-compliant with G3 controls</p>
                        <div class="mt-4 text-sm font-semibold">
                            Status: <span class="text-${statusColor}-600">
                                ${totalNonCompliantPercentage > 30 ? 'Critical' : 
                                  totalNonCompliantPercentage > 15 ? 'Warning' : 'Good'}
                            </span>
                        </div>
                    </div>

                    <!-- Compliance Summary -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">Compliance Summary</h4>
                        <div class="space-y-3">
                            <div class="flex justify-between items-center">
                                <span class="text-sm text-gray-600">Total Applications</span>
                                <span class="font-semibold">${complianceSummary.totalApps}</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-sm text-red-600">Critical</span>
                                <span class="font-semibold text-red-600">${complianceSummary.criticalApps}</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-sm text-yellow-600">Warning</span>
                                <span class="font-semibold text-yellow-600">${complianceSummary.warningApps}</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span class="text-sm text-green-600">Good</span>
                                <span class="font-semibold text-green-600">${complianceSummary.goodApps}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-2">
                    <h3 class="text-lg lg:text-xl font-semibold text-gray-900 mb-4">Non-Compliance by VS</h3>
                    ${window.G3Utils.renderBarChart(currentVSData)}
                    <p class="text-xs text-gray-500 mt-2">Click on any bar to view detailed information about that Virtual System</p>

                    <!-- Top Non-Compliant Apps -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">Top Non-Compliant Applications</h4>
                        <div class="space-y-3">
                            ${topNonCompliant.map(app => {
                                const porPercentage = window.G3Utils.calculatePoR(app.nonCompliant, app.totalAccount);
                                const severity = window.G3Utils.getSeverity(porPercentage);
                                const severityColor = severity === 'critical' ? 'red' : severity === 'warning' ? 'yellow' : 'green';

                                return `
                                    <div class="flex justify-between items-center p-2 hover:bg-gray-50 rounded">
                                        <div>
                                            <p class="font-medium text-gray-900">${app.appName}</p>
                                            <p class="text-xs text-gray-500">${app.vs}</p>
                                        </div>
                                        <span class="text-${severityColor}-600 font-semibold">${porPercentage}%</span>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Non-Compliant Summary Table -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">
                <div class="flex flex-col gap-4 mb-6">
                    <div class="flex flex-wrap gap-2">
                        <button id="show-critical-btn" class="${window.AppState.currentFilter === 'critical' ? 'filter-active bg-red-600' : 'bg-red-500 hover:bg-red-600'} text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            Show Critical
                        </button>
                        <button id="clear-filter-btn" class="bg-gray-500 hover:bg-gray-600 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            Show All
                        </button>
                        <button onclick="CommentManager.exportCommentsByMetric('G3')" 
                                class="bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            <i class="fas fa-file-export mr-1"></i>Export G3 Comments
                        </button>
                    </div>

                    <!-- Responsive filters -->
                    <div class="flex flex-col sm:flex-row gap-2">
                        <input type="text" placeholder="Filter by VS..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 flex-1 text-sm">
                        <input type="text" placeholder="Filter by App Name..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 flex-1 text-sm">
                        <button class="bg-blue-700 hover:bg-blue-800 text-white font-semibold py-2 px-4 rounded-lg text-sm transition duration-200 shadow-md sm:w-auto w-full">
                            APPLY FILTERS
                        </button>
                    </div>
                </div>

                <div class="overflow-x-auto rounded-xl border border-gray-300 shadow-inner">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">VS</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">App Name</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">ITSO</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">PoR (Point of Risk)</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 bg-white">
                            ${tableRows || '<tr><td colspan="5" class="p-4 text-center text-gray-500">No items match the current filter</td></tr>'}
                        </tbody>
                    </table>
                </div>

                <div class="flex flex-col lg:flex-row justify-between items-center text-sm text-gray-600 mt-4 gap-2">
                    <span>Showing ${currentData.length} of ${items.length} Items</span>
                    <div class="flex space-x-4 items-center">
                        <button class="text-blue-700 hover:text-blue-500 disabled:opacity-50 font-medium p-1" disabled>&#8592; Previous</button>
                        <span class="px-3 py-1 bg-gray-100 rounded-md">1</span>
                        <button class="text-blue-700 hover:text-blue-500 font-medium p-1">Next &#8594;</button>
                    </div>
                </div>
            </div>

            <!-- Commentary Section -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">
                <h3 class="text-lg lg:text-xl font-bold text-gray-900 mb-4">Add Audit Commentary</h3>
                <textarea placeholder="Enter commentary about the current data for audit/review..." rows="4" class="w-full p-3 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"></textarea>
                <button class="mt-3 bg-blue-700 hover:bg-blue-800 text-white font-bold py-2 px-4 rounded-lg transition duration-200 shadow-md">
                    Submit Commentary
                </button>
            </div>
        `;
    };
}

// G3 Action Manager - Updated to match G5 design exactly
if (typeof window.G3ActionManager === 'undefined') {
    window.G3ActionManager = {
        openCommentModal(itemId) {
            console.log('G3ActionManager.openCommentModal called with:', itemId);

            // Parse the itemId to get appName and vs
            // Format: G3_VS-001_App_Name1
            const parts = itemId.split('_');
            if (parts.length < 3) {
                console.error('Invalid itemId format:', itemId);
                this.showErrorModal('Invalid item ID format');
                return;
            }

            const vs = parts[1]; // This should be "VS-001"
            const appName = parts.slice(2).join(' '); // Join remaining parts with spaces

            console.log('Looking for app:', appName, 'with VS:', vs);

            // Find the app data
            const appData = window.g3RawData.find(item => {
                const match = item.appName === appName && item.vs === vs;
                if (!match) {
                    console.log('Checking:', item.appName, 'vs', item.vs, '- no match');
                }
                return match;
            });

            if (!appData) {
                console.error('App data not found for:', appName, 'with VS:', vs);
                console.log('Available apps in g3RawData:');
                window.g3RawData.forEach(item => {
                    console.log('-', item.appName, '(', item.vs, ')');
                });
                this.showErrorModal(`Application "${appName}" with VS "${vs}" not found in data.`);
                return;
            }

            console.log('Found app data:', appData);
            this.showCommentModal(itemId, appName, vs, appData);
        },

        showCommentModal(itemId, appName, vs, appData) {
            const existingComments = window.CommentManager ? window.CommentManager.getCommentsForItem(itemId) : [];
            const currentComment = existingComments.length > 0 ? existingComments[existingComments.length - 1].text : '';

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-2xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Add/Edit Comment</h3>
                    <div class="mb-4">
                        <p class="text-sm text-gray-600 mb-2"><strong>Application:</strong> ${appName}</p>
                        <p class="text-sm text-gray-600"><strong>VS:</strong> ${vs}</p>
                        <p class="text-sm text-gray-600"><strong>PoR:</strong> ${window.G3Utils.calculatePoR(appData.nonCompliant, appData.totalAccount)}%</p>
                    </div>
                    <textarea 
                        id="comment-text" 
                        placeholder="Enter your comment here..." 
                        rows="6" 
                        class="w-full p-3 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"
                    >${currentComment}</textarea>
                    <div class="flex justify-end space-x-3 mt-4">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 text-gray-600 hover:text-gray-800 font-medium">
                            Cancel
                        </button>
                        <button onclick="G3ActionManager.saveComment('${itemId}')" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Save Comment
                        </button>
                    </div>
                </div>
            `;

            console.log('Opening modal for G3 comment');
            window.ModalManager.openModal(modalContent, 'Application Comment');
        },

        showErrorModal(message) {
            const errorContent = `
                <div class="bg-white p-6 rounded-lg max-w-2xl">
                    <h3 class="text-xl font-bold text-red-600 mb-4">Data Not Found</h3>
                    <div class="mb-4">
                        <p class="text-sm text-gray-600">${message}</p>
                    </div>
                    <div class="bg-yellow-50 p-4 rounded-lg mb-4">
                        <p class="text-sm text-yellow-800">
                            Please check the browser console for more details.
                        </p>
                    </div>
                    <div class="flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;
            window.ModalManager.openModal(errorContent, 'Data Error');
        },

        saveComment(itemId) {
            console.log('G3ActionManager.saveComment called with:', itemId);

            const commentText = document.getElementById('comment-text').value;

            if (!commentText.trim()) {
                alert('Please enter a comment before saving.');
                return;
            }

            if (window.CommentManager) {
                window.CommentManager.saveComment(itemId, commentText, 'G3');
            } else {
                // Fallback if CommentManager is not available
                console.log(`Saving comment for ${itemId}:`, commentText);

                // Store in localStorage as fallback
                const comments = JSON.parse(localStorage.getItem('g3_comments') || '{}');
                if (!comments[itemId]) {
                    comments[itemId] = [];
                }
                comments[itemId].push({
                    text: commentText,
                    timestamp: new Date().toISOString(),
                    user: 'Current User'
                });
                localStorage.setItem('g3_comments', JSON.stringify(comments));

                // Show success notification
                this.showSuccessNotification('Comment saved successfully!');
            }

            window.ModalManager.closeModal();

            // Refresh the page to show updated comment status
            setTimeout(() => {
                if (window.Router && window.AppState.currentPage) {
                    window.Router.renderPage(window.AppState.currentPage);
                }
            }, 500);
        },

        showSuccessNotification(message) {
            const notification = document.createElement('div');
            notification.className = 'fixed top-4 right-4 bg-green-500 text-white px-4 py-2 rounded-lg shadow-lg z-50';
            notification.textContent = message;
            document.body.appendChild(notification);

            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 3000);
        },

        viewComments(itemId) {
            console.log('G3ActionManager.viewComments called with:', itemId);

            if (window.CommentManager) {
                window.CommentManager.viewComments(itemId);
            } else {
                // Fallback implementation
                const comments = JSON.parse(localStorage.getItem('g3_comments') || '{}');
                const itemComments = comments[itemId] || [];

                const commentsHtml = itemComments.length > 0 
                    ? itemComments.map(comment => `
                        <div class="border-b border-gray-200 pb-3 mb-3">
                            <div class="flex justify-between items-start mb-1">
                                <span class="font-semibold text-gray-800">${comment.user}</span>
                                <span class="text-xs text-gray-500">${new Date(comment.timestamp).toLocaleString()}</span>
                            </div>
                            <p class="text-sm text-gray-600">${comment.text}</p>
                        </div>
                    `).join('')
                    : '<p class="text-gray-500 text-center py-4">No comments yet</p>';

                const modalContent = `
                    <div class="bg-white p-6 rounded-lg max-w-2xl">
                        <h3 class="text-xl font-bold text-gray-900 mb-4">Comments</h3>
                        <div class="max-h-96 overflow-y-auto">
                            ${commentsHtml}
                        </div>
                        <div class="flex justify-end mt-4">
                            <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                                Close
                            </button>
                        </div>
                    </div>
                `;
                window.ModalManager.openModal(modalContent, 'View Comments');
            }
        },

        viewDetails(appName) {
            console.log('G3ActionManager.viewDetails called with:', appName);

            // Find app data by appName only (since we don't have VS context here)
            const appData = window.g3RawData.find(item => item.appName === appName);
            if (!appData) {
                console.error('App data not found for:', appName);
                this.showErrorModal(`Application "${appName}" not found in data.`);
                return;
            }

            const porPercentage = window.G3Utils.calculatePoR(appData.nonCompliant, appData.totalAccount);
            const severity = window.G3Utils.getSeverity(porPercentage);

            const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-4xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Application Details - ${appName}</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Basic Information</h4>
                            <div class="space-y-2">
                                <p><strong>VS:</strong> ${appData.vs}</p>
                                <p><strong>SVS:</strong> ${appData.svs}</p>
                                <p><strong>ITSO:</strong> ${appData.itso}</p>
                                <p><strong>Total Accounts:</strong> ${appData.totalAccount}</p>
                            </div>
                        </div>
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Compliance Status</h4>
                            <div class="space-y-2">
                                <p><strong>Compliant Accounts:</strong> ${appData.compliant}</p>
                                <p><strong>Non-Compliant Accounts:</strong> ${appData.nonCompliant}</p>
                                <p><strong>Non-Compliant Unique Accounts:</strong> ${appData.nonCompliantAccounts}</p>
                                <p><strong>Point of Risk (PoR):</strong> ${porPercentage}%</p>
                                <p><strong>Severity:</strong> ${window.ComponentTemplates.renderStatusBadge(severity, 'sm')}</p>
                            </div>
                        </div>
                    </div>
                    <div class="mt-6">
                        <h4 class="font-semibold text-gray-800 mb-3">Additional Information</h4>
                        <div class="bg-gray-50 p-4 rounded-lg">
                            <p class="text-sm text-gray-600">
                                <strong>Other Metrics:</strong> Other1: ${appData.other1}, Other2: ${appData.other2}, Other3: ${appData.other3}
                            </p>
                        </div>
                    </div>
                    <div class="mt-6 flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, 'Application Compliance Details');
        },

        exportCommentsByMetric(metricType) {
            console.log('G3ActionManager.exportCommentsByMetric called with:', metricType);

            if (window.CommentManager) {
                window.CommentManager.exportCommentsByMetric(metricType);
            } else {
                // Fallback export
                const comments = JSON.parse(localStorage.getItem('g3_comments') || '{}');
                const commentCount = Object.keys(comments).length;
                alert(`Exporting ${commentCount} G3 comments (fallback mode)`);
            }
        }
    };
}

// Initialize G3 Action Manager when the script loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('G3 Action Manager initialized');
});
```

## File: `js\pages\gras-g5.js`

```plaintext
// G5 Component - Critical & High Vulnerabilities
if (typeof window.GRASG5Component === 'undefined') {
    window.GRASG5Component = () => {
        const elements = window.getDOMElements();
        elements.pageTitle.textContent = "GRAS Metric: G5 (Critical & High Vulnerabilities)";
        elements.pageSubtitle.textContent = "Management of Critical and High severity vulnerabilities across all systems.";

        // Load G5 data
        const g5Data = window.DataManager.getPageDataSync('GRAS.G5');

        return renderG5Page(g5Data);
    };

    // Main rendering method
    const renderG5Page = (g5Data) => {
            const items = g5Data.items || window.g5RawData || [];

            // Apply current filter
            const currentData = window.G5Utils.filterData(items, window.AppState.currentFilter || 'all');

            // Calculate metrics
            const vsData = window.G5Utils.getVulnerabilitiesByVS(currentData);
            const summary = window.G5Utils.getSummary(currentData);

            // Update global state
            window.AppState.currentData = currentData;
            window.AppState.currentVSData = vsData;

            // Generate table rows
            // Update the vulnerability rows
            const tableRows = currentData.map(item => {
                        const severityColor = item.severity === 'Critical' ? 'red' : 'yellow';
                        const itemId = `G5_${item.vulnerabilityId}`;
                        const comments = window.CommentManager.getCommentsForItem(itemId);
                        const hasComments = comments.length > 0;

                        return `
                            <tr class="border-t border-gray-100 hover:bg-blue-50 transition duration-150">
                                <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-800 font-medium">${item.vs}</td>
                                <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.appName}</td>
                                <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${item.itso}</td>
                                <td class="p-3 lg:p-4 whitespace-nowrap text-sm text-gray-600">${window.G5Utils.formatDate(item.dueDate)}</td>
                                <td class="p-3 lg:p-4 whitespace-nowrap">
                                    ${window.ComponentTemplates.renderStatusBadge(item.severity.toLowerCase(), 'sm')}
                                </td>
                                <td class="p-3 lg:p-4 whitespace-nowrap text-sm font-medium">
                                    <div class="flex space-x-2">
                                        <button data-item-id="${itemId}" 
                                                onclick="CommentManager.openCommentModal('${itemId}', 'G5')"
                                                class="${hasComments ? 'text-green-600' : 'text-blue-600'} hover:opacity-80 text-xs p-2 border rounded-lg transition-colors">
                                            ${hasComments ? 
                                                '<i class="fas fa-comment-check mr-1"></i>Commented' : 
                                                '<i class="fas fa-comment-medical mr-1"></i>Add Comment'}
                                        </button>
                                        ${hasComments ? `
                                            <button onclick="CommentManager.viewComments('${itemId}')"
                                                    class="text-gray-600 hover:text-gray-800 text-xs p-2 border rounded-lg transition-colors">
                                                <i class="fas fa-list mr-1"></i>View (${comments.length})
                                            </button>
                                        ` : ''}
                                        <button onclick="G5CommentManager.viewDetails('${item.vulnerabilityId}')" 
                                                class="text-green-600 hover:text-green-800 text-xs p-2 border rounded-lg transition-colors">
                                            <i class="fas fa-eye mr-1"></i>Details
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        `;
                    }).join('');

        return `
            <!-- Key Performance Overview -->
            <div class="lg:col-span-3 grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 mb-6 lg:mb-8">
                <div class="lg:col-span-1">
                    <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-4">Vulnerability Summary</h3>
                    <div class="metric-card bg-white p-4 lg:p-6 rounded-xl shadow-lg border-t-4 border-${summary.status}-500">
                        <div class="flex justify-between items-start">
                            <div>
                                <p class="text-sm font-medium text-gray-600">Total Vulnerabilities</p>
                                <p class="text-2xl lg:text-4xl font-bold text-gray-900 mt-1">${summary.total}</p>
                            </div>
                            <div class="flex flex-col items-end">
                                <span class="text-2xl lg:text-3xl text-${summary.status}-600 font-extrabold">
                                    ${summary.status === 'critical' ? '⚠️' : summary.status === 'warning' ? '🔶' : '✅'}
                                </span>
                                <span class="text-xs text-gray-500">Target: 0 Critical, ≤100 High</span>
                            </div>
                        </div>
                        <div class="mt-4 space-y-2">
                            <div class="flex justify-between text-sm">
                                <span class="text-red-600 font-semibold">Critical:</span>
                                <span class="text-red-600 font-bold">${summary.critical}</span>
                            </div>
                            <div class="flex justify-between text-sm">
                                <span class="text-yellow-600 font-semibold">High:</span>
                                <span class="text-yellow-600 font-bold">${summary.high}</span>
                            </div>
                        </div>
                        <div class="mt-4 text-sm font-semibold">
                            Status: <span class="text-${summary.status}-600">
                                ${summary.status === 'critical' ? 'Critical' : summary.status === 'warning' ? 'Warning' : 'Good'}
                            </span>
                        </div>
                    </div>

                    <!-- Severity Thresholds -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">Severity Thresholds</h4>
                        <div class="space-y-3">
                            <div class="flex justify-between items-center p-2 bg-red-50 rounded">
                                <span class="text-sm text-red-800 font-medium">Critical</span>
                                <span class="text-sm text-red-800 font-bold">> 0 = Red</span>
                            </div>
                            <div class="flex justify-between items-center p-2 bg-yellow-50 rounded">
                                <span class="text-sm text-yellow-800 font-medium">High</span>
                                <span class="text-sm text-yellow-800 font-bold">> 100 = Red</span>
                            </div>
                            <div class="flex justify-between items-center p-2 bg-yellow-50 rounded">
                                <span class="text-sm text-yellow-800 font-medium">High</span>
                                <span class="text-sm text-yellow-800 font-bold">≤ 100 = Yellow</span>
                            </div>
                            <div class="flex justify-between items-center p-2 bg-green-50 rounded">
                                <span class="text-sm text-green-800 font-medium">High</span>
                                <span class="text-sm text-green-800 font-bold">= 0 = Green</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="lg:col-span-2">
                    <h3 class="text-lg lg:text-xl font-semibold text-gray-900 mb-4">Vulnerabilities by Virtual System</h3>
                    ${window.G5Utils.renderBarChart(vsData)}
                    <p class="text-xs text-gray-500 mt-2">Click on any bar to view detailed vulnerabilities for that Virtual System</p>

                    <!-- Quick Actions -->
                    <div class="mt-6 bg-white p-4 rounded-xl shadow-lg border border-gray-200">
                        <h4 class="text-lg font-semibold text-gray-900 mb-3">Quick Actions</h4>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <button class="p-3 bg-red-50 hover:bg-red-100 rounded-lg border border-red-200 transition duration-200 text-left">
                                <div class="flex items-center">
                                    <i class="fas fa-exclamation-triangle text-red-600 text-lg mr-3"></i>
                                    <span class="font-semibold text-red-800">Critical Vulnerabilities</span>
                                </div>
                                <p class="text-sm text-red-600 mt-1">${summary.critical} items requiring immediate attention</p>
                            </button>
                            <button class="p-3 bg-yellow-50 hover:bg-yellow-100 rounded-lg border border-yellow-200 transition duration-200 text-left">
                                <div class="flex items-center">
                                    <i class="fas fa-shield-alt text-yellow-600 text-lg mr-3"></i>
                                    <span class="font-semibold text-yellow-800">High Vulnerabilities</span>
                                </div>
                                <p class="text-sm text-yellow-600 mt-1">${summary.high} items to be addressed</p>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Vulnerabilities Summary Table -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">                
                <div class="flex flex-col gap-4 mb-6">
                    <div class="flex flex-wrap gap-2">
                        <button id="show-critical-btn" class="${window.AppState.currentFilter === 'critical' ? 'filter-active bg-red-600' : 'bg-red-500 hover:bg-red-600'} text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            Critical Only
                        </button>
                        <button id="show-high-btn" class="${window.AppState.currentFilter === 'high' ? 'filter-active bg-yellow-600' : 'bg-yellow-500 hover:bg-yellow-600'} text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            High Only
                        </button>
                        <button id="clear-filter-btn" class="bg-gray-500 hover:bg-gray-600 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            Show All
                        </button>
                        <button onclick="CommentManager.exportCommentsByMetric('G5')" 
                                class="bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 px-3 rounded-lg text-xs sm:text-sm transition duration-200 shadow-md flex-1 sm:flex-none">
                            <i class="fas fa-file-export mr-1"></i>Export G5 Comments
                        </button>
                    </div>
                
                    <!-- Responsive filters -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
                        <input type="text" placeholder="Filter by VS..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <input type="text" placeholder="Filter by App Name..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <input type="text" placeholder="Filter by ITSO..." class="p-2 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-sm">
                        <button class="bg-blue-700 hover:bg-blue-800 text-white font-semibold py-2 px-4 rounded-lg text-sm transition duration-200 shadow-md">
                            APPLY FILTERS
                        </button>
                    </div>
                </div>

                <!-- Table -->
                <div class="overflow-x-auto rounded-xl border border-gray-300 shadow-inner">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">VS</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">App Name</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">ITSO</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Due Date</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Severity</th>
                                <th scope="col" class="p-3 lg:p-4 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 bg-white">
                            ${tableRows || '<tr><td colspan="6" class="p-4 text-center text-gray-500">No vulnerabilities match the current filter</td></tr>'}
                        </tbody>
                    </table>
                </div>

                <div class="flex flex-col lg:flex-row justify-between items-center text-sm text-gray-600 mt-4 gap-2">
                    <span>Showing ${currentData.length} of ${items.length} Vulnerabilities</span>
                    <div class="flex space-x-4 items-center">
                        <button class="text-blue-700 hover:text-blue-500 disabled:opacity-50 font-medium p-1" disabled>&#8592; Previous</button>
                        <span class="px-3 py-1 bg-gray-100 rounded-md">1</span>
                        <button class="text-blue-700 hover:text-blue-500 font-medium p-1">Next &#8594;</button>
                    </div>
                </div>
            </div>

            <!-- Commentary Section -->
            <div class="lg:col-span-3 bg-white p-4 lg:p-8 rounded-xl shadow-lg mt-6 lg:mt-8 border border-gray-100">
                <h3 class="text-lg lg:text-xl font-bold text-gray-900 mb-4">Add Audit Commentary</h3>
                <textarea placeholder="Enter commentary about the current vulnerability status for audit/review..." rows="4" class="w-full p-3 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"></textarea>
                <button class="mt-3 bg-blue-700 hover:bg-blue-800 text-white font-bold py-2 px-4 rounded-lg transition duration-200 shadow-md">
                    Submit Commentary
                </button>
            </div>
        `;
    };
}

// G5 Comment Manager
if (typeof window.G5CommentManager === 'undefined') {
    window.G5CommentManager = {
            openCommentModal(vulnerabilityId) {
                const vulnerability = window.g5RawData.find(v => v.vulnerabilityId === vulnerabilityId);
                if (!vulnerability) return;

                const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-2xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Add/Edit Comment</h3>
                    <div class="mb-4">
                        <p class="text-sm text-gray-600 mb-2"><strong>Vulnerability:</strong> ${vulnerability.vulnerabilityId}</p>
                        <p class="text-sm text-gray-600"><strong>Description:</strong> ${vulnerability.description}</p>
                    </div>
                    <textarea 
                        id="comment-text" 
                        placeholder="Enter your comment here..." 
                        rows="6" 
                        class="w-full p-3 rounded-lg bg-gray-50 text-gray-900 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 transition duration-150"
                    >${vulnerability.comment || ''}</textarea>
                    <div class="flex justify-end space-x-3 mt-4">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 text-gray-600 hover:text-gray-800 font-medium">
                            Cancel
                        </button>
                        <button onclick="G5CommentManager.saveComment('${vulnerabilityId}')" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Save Comment
                        </button>
                    </div>
                </div>
            `;

                window.ModalManager.openModal(modalContent, 'Vulnerability Comment');
            },

            saveComment(vulnerabilityId) {
                const commentText = document.getElementById('comment-text').value;
                // In a real application, you would save this to your backend
                console.log(`Saving comment for ${vulnerabilityId}:`, commentText);

                // Update local data (for demo purposes)
                const vulnerability = window.g5RawData.find(v => v.vulnerabilityId === vulnerabilityId);
                if (vulnerability) {
                    vulnerability.comment = commentText;
                }

                window.ModalManager.closeModal();
                // Show success message
                alert('Comment saved successfully!');
            },

            viewDetails(vulnerabilityId) {
                const vulnerability = window.g5RawData.find(v => v.vulnerabilityId === vulnerabilityId);
                if (!vulnerability) return;

                const modalContent = `
                <div class="bg-white p-6 rounded-lg max-w-4xl">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Vulnerability Details</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Basic Information</h4>
                            <div class="space-y-2">
                                <p><strong>ID:</strong> ${vulnerability.vulnerabilityId}</p>
                                <p><strong>VS:</strong> ${vulnerability.vs}</p>
                                <p><strong>App Name:</strong> ${vulnerability.appName}</p>
                                <p><strong>ITSO:</strong> ${vulnerability.itso}</p>
                                <p><strong>Severity:</strong> ${window.ComponentTemplates.renderStatusBadge(vulnerability.severity.toLowerCase(), 'sm')}</p>
                            </div>
                        </div>
                        <div>
                            <h4 class="font-semibold text-gray-800 mb-3">Details</h4>
                            <div class="space-y-2">
                                <p><strong>Due Date:</strong> ${window.G5Utils.formatDate(vulnerability.dueDate)}</p>
                                <p><strong>Status:</strong> ${vulnerability.status}</p>
                                <p><strong>Description:</strong> ${vulnerability.description}</p>
                                ${vulnerability.comment ? `<p><strong>Comment:</strong> ${vulnerability.comment}</p>` : ''}
                            </div>
                        </div>
                    </div>
                    <div class="mt-6 flex justify-end">
                        <button onclick="window.ModalManager.closeModal()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition duration-200">
                            Close
                        </button>
                    </div>
                </div>
            `;

            window.ModalManager.openModal(modalContent, 'Vulnerability Details');
        }
    };
}
```

## File: `js\pages\gras-overview.js`

```plaintext
// // Check if GRASOverviewComponent already exists
// if (typeof window.GRASOverviewComponent === 'undefined') {
//     window.GRASOverviewComponent = () => {
//         // Only access DOM elements when the function is called
//         const elements = window.getDOMElements();
//         elements.pageTitle.textContent = "GRAS Metrics Overview";
//         elements.pageSubtitle.textContent = "Key Performance Indicators across all risk categories.";

//         // Helper methods for comment counting
//         const getCommentCount = (metricType) => {
//             const allComments = JSON.parse(localStorage.getItem('control_comments') || '{}');
//             let count = 0;

//             Object.values(allComments).forEach(commentList => {
//                 commentList.forEach(comment => {
//                     if (comment.itemType === metricType) {
//                         count++;
//                     }
//                 });
//             });

//             return count;
//         };

//         const getTotalCommentCount = () => {
//             const allComments = JSON.parse(localStorage.getItem('control_comments') || '{}');
//             let total = 0;

//             Object.values(allComments).forEach(commentList => {
//                 total += commentList.length;
//             });

//             return total;
//         };

//         return `
//             <div class="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 lg:gap-6">
//                 ${window.ComponentTemplates.renderKPICard('G3', 'Critical Control Status', '% of controls passing audits', 98)}
//                 ${window.ComponentTemplates.renderKPICard('G5', 'High-Risk Reduction', '% of critical risks closed on time', 90)}
//                 ${window.ComponentTemplates.renderKPICard('G43', 'Patching Coverage', '% of in-scope assets patched', 98)}
//                 ${window.ComponentTemplates.renderKPICard('G46', 'Vulnerability Age', 'Avg. days open for critical vulns', 70)}
//                 ${window.ComponentTemplates.renderKPICard('G51', 'IAM Compliance', '% of privileged accounts reviewed', 95)}
//                 ${window.ComponentTemplates.renderKPICard('G52', 'Access Reviews', '% of access reviews completed', 85)}
//                 ${window.ComponentTemplates.renderKPICard('G60', 'Incident Volume', '% reduction in repeat incidents', 50)}
//                 ${window.ComponentTemplates.renderKPICard('GXX', 'Future Metric', 'Placeholder for a new control metric', 99)}
//             </div>

//             <!-- Performance Summary -->
//             <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
//                 <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Performance Summary</h3>
//                 <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
//                     <div class="text-center">
//                         <div class="text-2xl lg:text-3xl font-bold text-green-600">8</div>
//                         <div class="text-sm text-gray-600 mt-1">Metrics Tracked</div>
//                     </div>
//                     <div class="text-center">
//                         <div class="text-2xl lg:text-3xl font-bold text-blue-600">6</div>
//                         <div class="text-sm text-gray-600 mt-1">On Target</div>
//                     </div>
//                     <div class="text-center">
//                         <div class="text-2xl lg:text-3xl font-bold text-yellow-600">1</div>
//                         <div class="text-sm text-gray-600 mt-1">Needs Attention</div>
//                     </div>
//                     <div class="text-center">
//                         <div class="text-2xl lg:text-3xl font-bold text-red-600">1</div>
//                         <div class="text-sm text-gray-600 mt-1">Critical</div>
//                     </div>
//                 </div>
//             </div>

//             <!-- Comments Summary -->
//             <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
//                 <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Export Commentary Summary</h3>
//                 <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
//                     <div class="text-center p-4 bg-blue-50 rounded-lg">
//                         <div class="text-2xl lg:text-3xl font-bold text-blue-600">${getCommentCount('G3')}</div>
//                         <div class="text-sm text-gray-600 mt-1">G3 Comments</div>
//                         <button onclick="CommentManager.exportCommentsByMetric('G3')" 
//                                 class="mt-2 text-xs text-blue-600 hover:text-blue-800">
//                             <i class="fas fa-download mr-1"></i>Export
//                         </button>
//                     </div>
//                     <div class="text-center p-4 bg-green-50 rounded-lg">
//                         <div class="text-2xl lg:text-3xl font-bold text-green-600">${getCommentCount('G5')}</div>
//                         <div class="text-sm text-gray-600 mt-1">G5 Comments</div>
//                         <button onclick="CommentManager.exportCommentsByMetric('G5')" 
//                                 class="mt-2 text-xs text-green-600 hover:text-green-800">
//                             <i class="fas fa-download mr-1"></i>Export
//                         </button>
//                     </div>
//                     <div class="text-center p-4 bg-yellow-50 rounded-lg">
//                         <div class="text-2xl lg:text-3xl font-bold text-yellow-600">${getCommentCount('G43')}</div>
//                         <div class="text-sm text-gray-600 mt-1">G43 Comments</div>
//                         <button onclick="CommentManager.exportCommentsByMetric('G43')" 
//                                 class="mt-2 text-xs text-yellow-600 hover:text-yellow-800">
//                             <i class="fas fa-download mr-1"></i>Export
//                         </button>
//                     </div>
//                     <div class="text-center p-4 bg-purple-50 rounded-lg">
//                         <div class="text-2xl lg:text-3xl font-bold text-purple-600">${getTotalCommentCount()}</div>
//                         <div class="text-sm text-gray-600 mt-1">Total Comments</div>
//                         <button onclick="CommentManager.exportAllMetricsComments()" 
//                                 class="mt-2 text-xs text-purple-600 hover:text-purple-800">
//                             <i class="fas fa-download mr-1"></i>Export All
//                         </button>
//                     </div>
//                 </div>
//             </div>

//             <!-- Recent Activities -->
//             <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
//                 <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Recent Activities</h3>
//                 <div class="space-y-4">
//                     <div class="flex items-start space-x-3 p-3 bg-green-50 rounded-lg">
//                         <i class="fas fa-check-circle text-green-500 mt-1"></i>
//                         <div>
//                             <p class="font-semibold text-green-800">G43 - Patching Coverage Improved</p>
//                             <p class="text-sm text-green-600">Increased from 92% to 96% this week</p>
//                         </div>
//                     </div>
//                     <div class="flex items-start space-x-3 p-3 bg-yellow-50 rounded-lg">
//                         <i class="fas fa-exclamation-triangle text-yellow-500 mt-1"></i>
//                         <div>
//                             <p class="font-semibold text-yellow-800">G46 - Vulnerability Age Alert</p>
//                             <p class="text-sm text-yellow-600">5 critical vulnerabilities older than 90 days</p>
//                         </div>
//                     </div>
//                     <div class="flex items-start space-x-3 p-3 bg-blue-50 rounded-lg">
//                         <i class="fas fa-info-circle text-blue-500 mt-1"></i>
//                         <div>
//                             <p class="font-semibold text-blue-800">G51 - Access Review Completed</p>
//                             <p class="text-sm text-blue-600">Quarterly privileged access review finalized</p>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         `;
//     };
// }

// Check if GRASOverviewComponent already exists
if (typeof window.GRASOverviewComponent === 'undefined') {
    window.GRASOverviewComponent = () => {
        const elements = window.getDOMElements();
        elements.pageTitle.textContent = "GRAS Metrics Overview";
        elements.pageSubtitle.textContent = "Key Performance Indicators across all risk categories.";

        // Get real data for metrics
        const g3Data = window.DataManager.getPageDataSync('GRAS.G3');
        const g5Data = window.DataManager.getPageDataSync('GRAS.G5');

        // Calculate real metrics
        const g3Value = calculateG3Metric(g3Data);
        const g5Value = calculateG5Metric(g5Data);

        return `
            <div class="lg:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 lg:gap-6">
                ${renderKPICardWithRealData('G3', 'Critical Control Status', '% of controls passing audits', 98, g3Value)}
                ${renderKPICardWithRealData('G5', 'High-Risk Reduction', '% of critical risks closed on time', 90, g5Value)}
                ${window.ComponentTemplates.renderKPICard('G43', 'Patching Coverage', '% of in-scope assets patched', 98)}
                ${window.ComponentTemplates.renderKPICard('G46', 'Vulnerability Age', 'Avg. days open for critical vulns', 70)}
                ${window.ComponentTemplates.renderKPICard('G51', 'IAM Compliance', '% of privileged accounts reviewed', 95)}
                ${window.ComponentTemplates.renderKPICard('G52', 'Access Reviews', '% of access reviews completed', 85)}
                ${window.ComponentTemplates.renderKPICard('G60', 'Incident Volume', '% reduction in repeat incidents', 50)}
                ${window.ComponentTemplates.renderKPICard('GXX', 'Future Metric', 'Placeholder for a new control metric', 99)}
            </div>

            <!-- Performance Summary -->
            <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
                <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Performance Summary</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="text-center">
                        <div class="text-2xl lg:text-3xl font-bold text-green-600">8</div>
                        <div class="text-sm text-gray-600 mt-1">Metrics Tracked</div>
                    </div>
                    <div class="text-center">
                        <div class="text-2xl lg:text-3xl font-bold text-blue-600">6</div>
                        <div class="text-sm text-gray-600 mt-1">On Target</div>
                    </div>
                    <div class="text-center">
                        <div class="text-2xl lg:text-3xl font-bold text-yellow-600">1</div>
                        <div class="text-sm text-gray-600 mt-1">Needs Attention</div>
                    </div>
                    <div class="text-center">
                        <div class="text-2xl lg:text-3xl font-bold text-red-600">1</div>
                        <div class="text-sm text-gray-600 mt-1">Critical</div>
                    </div>
                </div>
            </div>

            <!-- Recent Activities -->
            <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
                <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Recent Activities</h3>
                <div class="space-y-4">
                    <div class="flex items-start space-x-3 p-3 bg-green-50 rounded-lg">
                        <i class="fas fa-check-circle text-green-500 mt-1"></i>
                        <div>
                            <p class="font-semibold text-green-800">G43 - Patching Coverage Improved</p>
                            <p class="text-sm text-green-600">Increased from 92% to 96% this week</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-3 p-3 bg-yellow-50 rounded-lg">
                        <i class="fas fa-exclamation-triangle text-yellow-500 mt-1"></i>
                        <div>
                            <p class="font-semibold text-yellow-800">G46 - Vulnerability Age Alert</p>
                            <p class="text-sm text-yellow-600">5 critical vulnerabilities older than 90 days</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-3 p-3 bg-blue-50 rounded-lg">
                        <i class="fas fa-info-circle text-blue-500 mt-1"></i>
                        <div>
                            <p class="font-semibold text-blue-800">G51 - Access Review Completed</p>
                            <p class="text-sm text-blue-600">Quarterly privileged access review finalized</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
    };

    // Helper function to calculate G3 metric from real data
    const calculateG3Metric = (g3Data) => {
        const items = g3Data.items || window.g3RawData || [];
        if (items.length === 0) return 85; // Default fallback

        const totalNonCompliantPercentage = window.G3Utils.calculateTotalNonCompliantPercentage(items);
        // Convert to compliance percentage (100 - non-compliance)
        return Math.max(0, 100 - parseFloat(totalNonCompliantPercentage));
    };

    // Helper function to calculate G5 metric from real data
    const calculateG5Metric = (g5Data) => {
        const items = g5Data.items || window.g5RawData || [];
        if (items.length === 0) return 75; // Default fallback

        const summary = window.G5Utils.getSummary(items);
        // Calculate compliance score based on vulnerabilities
        // Lower vulnerabilities = higher score
        let score = 100;
        if (summary.critical > 0) score -= 30;
        if (summary.high > 0) score -= Math.min(25, summary.high * 2);

        return Math.max(0, score);
    };

    // Custom KPI card renderer that uses real data
    const renderKPICardWithRealData = (metric, title, description, target, realValue) => {
        const isPassing = realValue >= target;
        const bgColor = isPassing ? 'bg-green-600' : 'bg-red-600';
        const textColor = 'text-white';

        return `
            <div class="metric-card p-4 lg:p-5 rounded-xl shadow-lg border border-gray-200 flex flex-col justify-between bg-white">
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-lg lg:text-xl font-bold text-gray-900">${metric}</span>
                        <span class="text-xs lg:text-sm text-gray-500">Target: ${target}%</span>
                    </div>
                    <p class="text-3xl lg:text-4xl font-extrabold text-blue-700">${Math.round(realValue)}%</p>
                    <p class="text-xs lg:text-sm text-gray-600 mt-2">${description}</p>
                </div>
                <div class="mt-4 flex justify-between items-center">
                    <span class="px-3 py-1 text-xs font-semibold rounded-full ${bgColor} ${textColor} shadow-md">
                        ${isPassing ? 'Compliant' : 'Non-Compliant'}
                    </span>
                    <button class="text-xs lg:text-sm text-blue-700 hover:text-blue-500 font-medium" 
                            onclick="window.NavigationManager.navigateTo('GRAS.${metric}')">
                        View Details &rarr;
                    </button>
                </div>
            </div>
        `;
    };
}
```

## File: `js\pages\overview.js`

```plaintext
// Check if OverviewComponent already exists
if (typeof window.OverviewComponent === 'undefined') {
    window.OverviewComponent = () => {
        const elements = window.getDOMElements();
        elements.pageTitle.textContent = "Dashboard Overview";
        elements.pageSubtitle.textContent = "Welcome to the IT Control & Governance Dashboard. High-level summary.";

        const overallData = {
            GRAS: window.getMetricData('GRAS.Overall', 90),
            OKR: window.getMetricData('OKR.Overall', 80),
            GOV: window.getMetricData('GOV.Overall', 95),
        };

        return `
            <!-- Dashboard Summary Cards -->
            <div class="lg:col-span-3 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8 mb-6 lg:mb-8">
                ${window.ComponentTemplates.renderMetricCard('GRAS Compliance Score', 'Consolidated risk adherence score across all cyber controls.', overallData.GRAS)}
                ${window.ComponentTemplates.renderMetricCard('Cyber OKR Achievement', 'Overall progress towards annual cybersecurity goals.', overallData.OKR)}
                ${window.ComponentTemplates.renderMetricCard('Governance Maturity', 'Compliance score for critical operational controls.', overallData.GOV)}
            </div>
            
            <!-- Detailed Intro & Status Box -->
            <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100">
                <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-4 border-b pb-2">Quarterly Control Status</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 lg:gap-6">
                    <div class="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-600">
                        <p class="text-base lg:text-lg font-semibold text-blue-800">Key Focus</p>
                        <p class="text-xs lg:text-sm text-gray-600 mt-1">Immediate action required on critical vulnerabilities (G46) older than 60 days.</p>
                    </div>
                    <div class="bg-green-50 p-4 rounded-lg border-l-4 border-green-600">
                        <p class="text-base lg:text-lg font-semibold text-green-800">Success Story</p>
                        <p class="text-xs lg:text-sm text-gray-600 mt-1">Patching coverage (G43) hit a record 99.2% last month due to automation rollout.</p>
                    </div>
                    <div class="bg-yellow-50 p-4 rounded-lg border-l-4 border-yellow-600">
                        <p class="text-base lg:text-lg font-semibold text-yellow-800">Upcoming Audit</p>
                        <p class="text-xs lg:text-sm text-gray-600 mt-1">External audit for ITAM.3 and ITOP.1 scheduled for next week.</p>
                    </div>
                </div>
            </div>

            <!-- Quick Actions - FIXED NAVIGATION -->
            <div class="lg:col-span-3 bg-white p-6 lg:p-8 rounded-xl shadow-lg border border-gray-100 mt-6 lg:mt-8">
                <h3 class="text-xl lg:text-2xl font-bold text-gray-900 mb-6">Quick Actions</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <!-- FIXED: Use NavigationManager.navigateTo() for proper URL updates -->
                    <button onclick="window.NavigationManager.navigateTo('GRAS.G3')" class="p-4 bg-blue-50 hover:bg-blue-100 rounded-lg border border-blue-200 transition duration-200">
                        <div class="flex items-center">
                            <i class="fas fa-shield-alt text-blue-600 text-xl mr-3"></i>
                            <span class="font-semibold text-blue-800">G3 Controls</span>
                        </div>
                        <p class="text-sm text-blue-600 mt-2">Review control status</p>
                    </button>
                    
                    <button onclick="window.NavigationManager.navigateTo('GRAS.Overview')" class="p-4 bg-green-50 hover:bg-green-100 rounded-lg border border-green-200 transition duration-200">
                        <div class="flex items-center">
                            <i class="fas fa-chart-line text-green-600 text-xl mr-3"></i>
                            <span class="font-semibold text-green-800">GRAS Metrics</span>
                        </div>
                        <p class="text-sm text-green-600 mt-2">View all metrics</p>
                    </button>
                    
                    <button class="p-4 bg-purple-50 hover:bg-purple-100 rounded-lg border border-purple-200 transition duration-200">
                        <div class="flex items-center">
                            <i class="fas fa-file-export text-purple-600 text-xl mr-3"></i>
                            <span class="font-semibold text-purple-800">Export Report</span>
                        </div>
                        <p class="text-sm text-purple-600 mt-2">Generate PDF</p>
                    </button>
                    
                    <button class="p-4 bg-orange-50 hover:bg-orange-100 rounded-lg border border-orange-200 transition duration-200">
                        <div class="flex items-center">
                            <i class="fas fa-cog text-orange-600 text-xl mr-3"></i>
                            <span class="font-semibold text-orange-800">Settings</span>
                        </div>
                        <p class="text-sm text-orange-600 mt-2">Dashboard config</p>
                    </button>
                </div>
            </div>
        `;
    };
}
```

## File: `styles\main.css`

```plaintext
:root {
    --primary-bg: #f3f4f6;
    --secondary-bg: #ffffff;
    --accent-color: #1d4ed8;
    --text-color: #111827;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--primary-bg);
    color: var(--text-color);
}

.menu {
    position: fixed;
    top: 0;
    left: -100%;
    width: 280px;
    height: 100vh;
    background-color: var(--secondary-bg);
    box-shadow: 2px 0 20px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
    z-index: 1000;
    overflow-y: auto;
}

.menu.active {
    left: 0;
}

.overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
}

.overlay.active {
    display: block;
}

.nav-item {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    margin: 0.25rem 0;
    cursor: pointer;
    border-radius: 0.5rem;
    color: #4b5563;
    transition: all 0.2s;
    overflow: hidden;
    white-space: nowrap;
}

.nav-item:hover {
    background-color: #eff6ff;
    color: var(--accent-color);
}

.nav-item.active {
    background-color: var(--accent-color);
    color: white;
    font-weight: 600;
}

.metric-card {
    transition: transform 0.2s, box-shadow 0.2s;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.chart-container {
    height: 16rem;
    position: relative;
    cursor: pointer;
}

.chart-bar {
    transition: all 0.3s ease;
}

.chart-bar:hover {
    opacity: 0.8;
    transform: scale(1.05);
}

.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    z-index: 1100;
    overflow-y: auto;
}

.modal.active {
    display: block;
}

.modal-content {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.filter-active {
    background-color: #dc2626 !important;
    color: white !important;
}


/* Custom scrollbar for modal */

.modal::-webkit-scrollbar {
    width: 8px;
}

.modal::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.modal::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 4px;
}

.modal::-webkit-scrollbar-thumb:hover {
    background: #a8a8a8;
}


/* Responsive design */

@media (max-width: 768px) {
    .modal-content {
        padding: 1rem;
    }
    .chart-container {
        height: 12rem;
    }
}


/* Loading animations */

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.animate-spin {
    animation: spin 1s linear infinite;
}


/* Action type color classes */

.action-green-icon {
    color: #10b981;
}

.action-red-icon {
    color: #ef4444;
}

.action-yellow-icon {
    color: #f59e0b;
}

.action-orange-icon {
    color: #f97316;
}

.action-blue-icon {
    color: #3b82f6;
}

.action-purple-icon {
    color: #8b5cf6;
}

.action-gray-icon {
    color: #6b7280;
}

.action-green-bg {
    background-color: #ecfdf5;
    border-color: #10b981;
}

.action-red-bg {
    background-color: #fef2f2;
    border-color: #ef4444;
}

.action-yellow-bg {
    background-color: #fffbeb;
    border-color: #f59e0b;
}

.action-orange-bg {
    background-color: #fff7ed;
    border-color: #f97316;
}

.action-blue-bg {
    background-color: #eff6ff;
    border-color: #3b82f6;
}

.action-purple-bg {
    background-color: #faf5ff;
    border-color: #8b5cf6;
}

.action-gray-bg {
    background-color: #f9fafb;
    border-color: #6b7280;
}

.action-green-badge {
    background-color: #ecfdf5;
    color: #065f46;
}

.action-red-badge {
    background-color: #fef2f2;
    color: #991b1b;
}

.action-yellow-badge {
    background-color: #fffbeb;
    color: #92400e;
}

.action-orange-badge {
    background-color: #fff7ed;
    color: #9a3412;
}

.action-blue-badge {
    background-color: #eff6ff;
    color: #1e40af;
}

.action-purple-badge {
    background-color: #faf5ff;
    color: #5b21b6;
}

.action-gray-badge {
    background-color: #f9fafb;
    color: #374151;
}

.action-type-btn.action-selected {
    transform: scale(1.02);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
```

