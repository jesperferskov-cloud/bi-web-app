const fs = require('fs');

const files = [
    'dashboard.html',
    'profil.html',
    'portefoelje.html',
    'laer.html',
    'analyse.html',
    'markeder.html',
    'vaerktoejer.html'
];

const scriptTag = `
    <!-- Dark Mode Init -->
    <script>
        if (localStorage.getItem('bi_theme') === 'dark' && localStorage.getItem('bi_is_supporter') === 'true') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    </script>
`;

const themeToggleHtml = `
                <!-- Theme Switcher -->
                <button onclick="toggleTheme()" class="w-full flex items-center justify-between px-3 py-2 text-on-surface-variant dark:text-[#94a3b8] hover:text-deep-indigo dark:hover:text-[#c3c0ff] hover:bg-slate-surface dark:hover:bg-[#131b2e] rounded-xl transition-all font-body-md font-medium group">
                    <div class="flex items-center gap-3">
                        <span class="material-symbols-outlined text-lg group-hover:scale-110 transition-transform">dark_mode</span>
                        Mørk Tilstand
                    </div>
                    <div class="flex items-center gap-2">
                        <span id="theme-lock" class="material-symbols-outlined text-amber-500 text-sm" style="display: none;">lock</span>
                        <div class="relative inline-flex items-center h-5 rounded-full w-9 transition-colors bg-slate-border dark:bg-indigo-600" id="theme-switch-bg">
                            <span class="inline-block w-3.5 h-3.5 transform bg-white rounded-full transition-transform translate-x-1 dark:translate-x-4" id="theme-switch-knob"></span>
                        </div>
                    </div>
                </button>
`;

const toggleLogicScript = `
    <!-- Theme Toggle Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            const themeLock = document.getElementById('theme-lock');
            
            if (!isSupporter && themeLock) {
                themeLock.style.display = 'inline-block';
            }
        });

        function toggleTheme() {
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            if (!isSupporter) {
                const modal = document.getElementById('supporter-modal');
                if (modal) {
                    modal.classList.remove('hidden');
                    // Change modal text slightly if wanted, or just show it.
                } else {
                    alert("Dark Mode er en eksklusiv funktion for vores Supporters. Støt serverdriften og lås op for mørkt tema med det samme.");
                }
                return;
            }

            const html = document.documentElement;
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.setItem('bi_theme', 'light');
            } else {
                html.classList.add('dark');
                localStorage.setItem('bi_theme', 'dark');
            }
        }
    </script>
`;

for (let file of files) {
    if (!fs.existsSync(file)) {
        console.log("File not found: " + file);
        continue;
    }
    
    let content = fs.readFileSync(file, 'utf8');

    // Add head script if not there
    if (!content.includes('Dark Mode Init')) {
        content = content.replace('</head>', scriptTag + '</head>');
    }

    // Add theme toggle html to sidebar
    if (!content.includes('Mørk Tilstand')) {
        // Look for Hjælp & Support
        const helpIndex = content.indexOf('<a href="#" class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:text-deep-indigo hover:bg-slate-surface rounded-xl transition-all font-body-md font-medium group">\n                    <span class="material-symbols-outlined text-lg group-hover:scale-110 transition-transform">help</span>\n                    Hjælp & Support\n                </a>');
        
        if (helpIndex > -1) {
            content = content.replace('<a href="#" class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:text-deep-indigo hover:bg-slate-surface rounded-xl transition-all font-body-md font-medium group">\n                    <span class="material-symbols-outlined text-lg group-hover:scale-110 transition-transform">help</span>\n                    Hjælp & Support\n                </a>', themeToggleHtml + '\n                <a href="#" class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:text-deep-indigo hover:bg-slate-surface rounded-xl transition-all font-body-md font-medium group">\n                    <span class="material-symbols-outlined text-lg group-hover:scale-110 transition-transform">help</span>\n                    Hjælp & Support\n                </a>');
        } else {
            // fallback replacement
            content = content.replace('Hjælp & Support\n                </a>', 'Hjælp & Support\n                </a>\n' + themeToggleHtml);
        }
    }

    // Add logic script before </body>
    if (!content.includes('Theme Toggle Logic')) {
        content = content.replace('</body>', toggleLogicScript + '\n</body>');
    }

    // Body classes
    content = content.replace('<body class="bg-background text-on-background font-body-md flex h-screen overflow-hidden">', '<body class="bg-background dark:bg-[#0b1326] text-on-background dark:text-[#f8fafc] font-body-md flex h-screen overflow-hidden">');
    // For other variants of body classes
    if (!content.includes('dark:bg-[#0b1326]')) {
        content = content.replace('<body class="bg-background text-on-background', '<body class="bg-background dark:bg-[#0b1326] text-on-background dark:text-[#f8fafc]');
    }

    // Bento cards
    // Usually classes like "bg-white border border-slate-border rounded-2xl"
    content = content.replace(/bg-white border border-slate-border rounded-2xl/g, 'bg-white dark:bg-[#131b2e] border border-slate-border dark:border-[#1e293b] rounded-2xl');
    
    // Header/Sidebar bg (which is often bg-white border-r/b border-slate-border)
    content = content.replace(/bg-white border-b border-slate-border/g, 'bg-white dark:bg-[#0b1326] border-b border-slate-border dark:border-[#1e293b]');
    content = content.replace(/bg-white border-r border-slate-border/g, 'bg-white dark:bg-[#0b1326] border-r border-slate-border dark:border-[#1e293b]');

    // Subtexts (text-on-surface-variant)
    content = content.replace(/text-on-surface-variant/g, 'text-on-surface-variant dark:text-[#94a3b8]');

    fs.writeFileSync(file, content);
    console.log("Updated " + file);
}
