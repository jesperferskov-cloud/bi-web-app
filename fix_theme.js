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
                <button onclick="toggleTheme()" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-sm font-medium text-indigo-200 hover:text-white hover:bg-white/10 transition-all group mb-1">
                    <div class="flex items-center gap-3">
                        <span class="material-symbols-outlined text-lg">dark_mode</span>
                        <span>Mørk Tilstand</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span id="theme-lock-sidebar" class="text-xs" style="display: none;" title="Kræver Supporter">🔒</span>
                        <div class="relative inline-flex items-center h-4 rounded-full w-8 transition-colors bg-indigo-900/60 dark:bg-indigo-500" id="theme-switch-bg">
                            <span class="inline-block w-3 h-3 transform bg-white rounded-full transition-transform translate-x-0.5 dark:translate-x-4" id="theme-switch-knob"></span>
                        </div>
                    </div>
                </button>
`;

const toggleLogicScript = `
    <!-- Theme Toggle Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            const themeLock = document.getElementById('theme-lock-sidebar');
            
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
                    const modalTitle = modal.querySelector('h4');
                    if (modalTitle) modalTitle.textContent = "⭐ Dark Mode er eksklusivt for Supporters";
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
        console.log("Not found: " + file);
        continue;
    }
    let content = fs.readFileSync(file, 'utf8');

    // 1. Add Init Script
    if (!content.includes('Dark Mode Init')) {
        content = content.replace('</head>', scriptTag + '\n</head>');
    }

    // 2. Add Theme Switcher
    if (!content.includes('Mørk Tilstand')) {
        content = content.replace('<!-- Hjælp Link -->', themeToggleHtml + '\n                <!-- Hjælp Link -->');
    }

    // 3. Add Toggle Logic
    if (!content.includes('Theme Toggle Logic')) {
        content = content.replace('</body>', toggleLogicScript + '\n</body>');
    }

    // 4. Update Classes (Idempotent approach)

    // Helper to add classes if they don't exist in the class string
    const addClass = (match, classStr, newClasses) => {
        let classes = classStr.split(/\s+/);
        let toAdd = newClasses.split(/\s+/);
        for (let c of toAdd) {
            if (!classes.includes(c)) classes.push(c);
        }
        return `class="${classes.join(' ')}"`;
    };

    content = content.replace(/class="([^"]*?bg-slate-surface[^"]*?)"/g, (m, p1) => addClass(m, p1, 'dark:bg-[#0b1326]'));
    
    // Bento cards (bg-white and rounded-something or border)
    content = content.replace(/class="([^"]*?bg-white[^"]*?)"/g, (m, p1) => {
        if (p1.includes('rounded-') || p1.includes('border')) {
             return addClass(m, p1, 'dark:bg-[#131b2e] dark:border-[#1e293b]');
        }
        return m;
    });

    content = content.replace(/class="([^"]*?border-slate-border[^"]*?)"/g, (m, p1) => addClass(m, p1, 'dark:border-[#1e293b]'));
    content = content.replace(/class="([^"]*?text-on-surface-variant[^"]*?)"/g, (m, p1) => addClass(m, p1, 'dark:text-[#94a3b8]'));
    content = content.replace(/class="([^"]*?text-on-background[^"]*?)"/g, (m, p1) => addClass(m, p1, 'dark:text-[#f8fafc]'));
    
    // Also main background `bg-background` needs dark mode `dark:bg-[#0b1326]`
    content = content.replace(/class="([^"]*?bg-background[^"]*?)"/g, (m, p1) => addClass(m, p1, 'dark:bg-[#0b1326] dark:text-[#f8fafc]'));

    // Fix up potential issue with text-on-background inside headers making them invisible in dark mode:
    // Wait, text-deep-indigo might need to be adjusted for dark mode if it's too dark. 
    // The prompt says "Active/Primary knapper og accenter bevarer deres genkendelige Deep Indigo/Emerald accenter." So we leave them.
    // However, some text might be hard to read if it's deep-indigo on dark bg. We'll leave it as requested for now.
    
    fs.writeFileSync(file, content);
    console.log("Processed " + file);
}
