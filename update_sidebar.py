import os
import re

SIDEBAR_TEMPLATE = """<aside class="w-16 md:w-64 bg-deep-indigo text-white flex flex-col border-r border-slate-border flex-shrink-0 relative z-20 shadow-xl transition-all duration-300">
        <!-- Logo -->
        <div class="h-20 flex items-center justify-center md:justify-start md:px-6 border-b border-indigo-900/40">
            <a href="index.html" class="flex items-center gap-2.5 group">
                <span class="material-symbols-outlined text-white text-3xl md:text-2xl" style="font-variation-settings: 'FILL' 0, 'wght' 400;">pie_chart</span>
                <span class="hidden md:inline text-lg font-bold tracking-tight font-headline-md leading-tight">Begynder<br/>Investor</span>
            </a>
        </div>

        <!-- Navigation Items -->
        <nav class="flex-grow px-2 md:px-4 py-6 flex flex-col gap-2">
            <a href="dashboard.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_DASH}">
                <span class="material-symbols-outlined text-xl">dashboard</span>
                <span class="hidden md:inline">Dashboard</span>
            </a>
            <a href="portefoelje.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_PORT}">
                <span class="material-symbols-outlined text-xl">account_balance_wallet</span>
                <span class="hidden md:inline">Min Portefølje</span>
            </a>
            <a href="laer.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_LAER}">
                <span class="material-symbols-outlined text-xl">school</span>
                <span class="hidden md:inline">Lær at Investere</span>
            </a>
            <a href="analyse.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_ANAL}">
                <span class="material-symbols-outlined text-xl">analytics</span>
                <span class="hidden md:inline">Min Analyse</span>
            </a>
            <a href="markeder.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_MARK}">
                <span class="material-symbols-outlined text-xl">candlestick_chart</span>
                <span class="hidden md:inline">Marked</span>
            </a>
            <a href="vaerktoejer.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_VAERK}">
                <span class="material-symbols-outlined text-xl">construction</span>
                <span class="hidden md:inline">Værktøjer</span>
            </a>
        </nav>

        <!-- Bottom Links -->
        <div class="px-2 md:px-4 py-4 mt-auto">
            <div class="border-t border-indigo-900/40 my-3"></div>
            <div class="flex flex-col gap-2">
                <a href="#" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-indigo-200 hover:text-white hover:bg-white/10 font-medium text-sm transition-all justify-center md:justify-start">
                    <span class="material-symbols-outlined text-lg">settings</span>
                    <span class="hidden md:inline">Indstillinger</span>
                </a>
                <a href="hjaelp.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start {ACTIVE_HJAELP}">
                    <span class="material-symbols-outlined text-lg">help</span>
                    <span class="hidden md:inline">Hjælp</span>
                </a>
            </div>
            
            <div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">
                <div class="w-8 h-8 rounded-full bg-white text-deep-indigo flex items-center justify-center text-xs font-bold shrink-0">
                    <span id="sidebar-initials">JF</span>
                </div>
                <div class="hidden md:flex flex-col overflow-hidden">
                    <span class="text-sm font-medium text-white truncate" id="sidebar-name">Jesper Ferskov</span>
                    <span class="text-xs text-indigo-300 truncate" id="sidebar-badge">Begynder</span>
                </div>
            </div>
        </div>
    </aside>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const userName = localStorage.getItem('bi_user_name') || 'Jesper Ferskov';
            const initials = userName.split(' ').map(n => n[0]).join('').substring(0,2).toUpperCase();
            const elName = document.getElementById('sidebar-name');
            const elInitials = document.getElementById('sidebar-initials');
            if(elName) elName.textContent = userName;
            if(elInitials) elInitials.textContent = initials || 'JF';
            
            const isSupporter = localStorage.getItem('bi_is_supporter');
            const elBadge = document.getElementById('sidebar-badge');
            if(elBadge) {
                if(isSupporter === 'true') {
                    elBadge.innerHTML = '⭐ Supporter';
                    elBadge.classList.remove('text-indigo-300');
                    elBadge.classList.add('text-amber-400');
                } else {
                    elBadge.textContent = 'Begynder';
                }
            }
        });
    </script>"""

ACTIVE_CLASS = "bg-indigo-900/60 text-white font-semibold shadow-sm"
INACTIVE_CLASS = "text-indigo-200 hover:text-white hover:bg-white/10"

files = [f for f in os.listdir('.') if f.endswith('.html')]

# Ensure we don't duplicate the injected script if we run multiple times
sidebar_regex = re.compile(r'<aside.*?</aside>', re.DOTALL)
script_regex = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const userName = localStorage\.getItem\(\'bi_user_name\'\).*?</script>', re.DOTALL)

for fname in files:
    if fname in ['index.html', 'login.html', 'onboarding.html']:
        continue # Usually these don't have this sidebar, but let's check
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<aside' not in content:
        continue

    # Determine active classes
    classes = {
        '{ACTIVE_DASH}': INACTIVE_CLASS,
        '{ACTIVE_PORT}': INACTIVE_CLASS,
        '{ACTIVE_LAER}': INACTIVE_CLASS,
        '{ACTIVE_ANAL}': INACTIVE_CLASS,
        '{ACTIVE_MARK}': INACTIVE_CLASS,
        '{ACTIVE_VAERK}': INACTIVE_CLASS,
        '{ACTIVE_HJAELP}': INACTIVE_CLASS,
    }
    
    if fname == 'dashboard.html': classes['{ACTIVE_DASH}'] = ACTIVE_CLASS
    elif fname == 'portefoelje.html': classes['{ACTIVE_PORT}'] = ACTIVE_CLASS
    elif fname.startswith('laer') or fname.startswith('modul'): classes['{ACTIVE_LAER}'] = ACTIVE_CLASS
    elif fname == 'analyse.html': classes['{ACTIVE_ANAL}'] = ACTIVE_CLASS
    elif fname == 'markeder.html': classes['{ACTIVE_MARK}'] = ACTIVE_CLASS
    elif fname == 'vaerktoejer.html': classes['{ACTIVE_VAERK}'] = ACTIVE_CLASS
    elif fname == 'hjaelp.html': classes['{ACTIVE_HJAELP}'] = ACTIVE_CLASS
    
    new_sidebar = SIDEBAR_TEMPLATE
    for k, v in classes.items():
        new_sidebar = new_sidebar.replace(k, v)
        
    # Remove old injected script if present
    content = script_regex.sub('', content)
    
    # Replace aside
    new_content = sidebar_regex.sub(new_sidebar.replace('\\', '\\\\'), content, count=1)
    
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {fname}")

