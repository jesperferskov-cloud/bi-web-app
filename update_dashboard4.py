import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# 1. Update the sidebar
# Find the bottom user area where the avatar and name are.
sidebar_user_area = '''<div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-lg hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">
                <div class="w-8 h-8 rounded-full bg-white text-deep-indigo flex items-center justify-center text-xs font-bold shrink-0">
                    <span id="sidebar-initials">AL</span>
                </div>
                <div class="hidden md:flex flex-col overflow-hidden">
                    <span class="text-sm font-medium text-white truncate" id="sidebar-name">Alex</span>
                    <span class="text-xs text-indigo-300 truncate">Begynder</span>
                </div>
            </div>'''
sidebar_user_area_new = '''<div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-lg hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">
                <div class="w-8 h-8 rounded-full bg-white text-deep-indigo flex items-center justify-center text-xs font-bold shrink-0">
                    <span id="sidebar-initials">AL</span>
                </div>
                <div class="hidden md:flex flex-col overflow-hidden">
                    <span class="text-sm font-medium text-white truncate" id="sidebar-name">Alex</span>
                    <div id="sidebar-supporter-badge" class="hidden mt-0.5">
                        <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-400/20 text-amber-300 border border-amber-400/40">⭐ Supporter</span>
                    </div>
                    <span id="sidebar-user-role" class="text-xs text-indigo-300 truncate mt-0.5">Begynder</span>
                </div>
            </div>'''
content = content.replace(sidebar_user_area, sidebar_user_area_new)

# Replace the old sidebar supporter banner
old_sidebar_banner_regex = re.compile(r'<!-- Supporter Banner -->.*?</div>\n        </div>\n    </aside>', re.DOTALL)
new_sidebar_banner = '''<!-- Supporter Banner -->
        <div id="sidebar-supporter-banner" class="hidden mt-auto mb-4">
            <div class="bg-indigo-950/70 border border-indigo-500/30 rounded-xl p-3.5 mx-3 shadow-inner text-left">
                <div class="flex items-center gap-1.5 text-amber-400 text-xs font-bold uppercase tracking-wider mb-1">
                    <span class="text-sm">⭐</span> Støt Projektet
                </div>
                <p class="text-[11px] text-indigo-200 leading-relaxed mb-2.5">
                    Hold platformen uafhængig og dæk vores AI- og serveromkostninger.
                </p>
                <button id="open-supporter-modal-btn" onclick="openSupporterModal()" class="w-full bg-amber-400 hover:bg-amber-300 text-indigo-950 font-bold text-xs py-1.5 px-3 rounded-lg transition-all shadow-sm">
                    Bliv Supporter (29 kr.)
                </button>
            </div>
        </div>
    </aside>'''
content = old_sidebar_banner_regex.sub(new_sidebar_banner, content)

# 2. Update the Supporter Modal
old_modal_regex = re.compile(r'<!-- Supporter Modal -->.*?</div>\n    </div>', re.DOTALL)
new_modal = '''<!-- Supporter Modal -->
    <div id="supporter-modal" class="fixed inset-0 bg-on-background/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 transition-opacity duration-300 opacity-0" onclick="closeSupporterModal()">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden flex flex-col transform transition-transform duration-300 scale-95" id="supporter-modal-inner" onclick="event.stopPropagation()">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-slate-surface">
                <h3 class="font-headline-md text-xl font-bold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined text-amber-500">star</span>
                    Bliv Supporter
                </h3>
                <button onclick="closeSupporterModal()" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            
            <div class="p-6 space-y-4">
                <h4 class="font-headline-md text-lg font-bold text-on-background">⭐ Bliv Supporter af Begynder Investor</h4>
                <div class="space-y-3">
                    <div class="flex items-start gap-3">
                        <span class="text-xl shrink-0">⚡</span>
                        <p class="text-sm text-on-surface-variant">Ubegrænsede AI-aktieanalyser og prompt-kald.</p>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-xl shrink-0">🛡️</span>
                        <p class="text-sm text-on-surface-variant">Eksklusivt Supporter Badge på dit dashboard og profil.</p>
                    </div>
                    <div class="flex items-start gap-3">
                        <span class="text-xl shrink-0">❤️</span>
                        <p class="text-sm text-on-surface-variant">100% uafhængigt læringsunivers uden reklamer og skjulte dagsordener.</p>
                    </div>
                </div>
                
                <div class="bg-slate-50 border border-slate-border rounded-xl p-4 mt-4">
                    <p class="text-xs text-on-surface-variant leading-relaxed text-center italic">
                        "Kun 29 kr./md. eller valgfrit engangsbeløb. Ingen binding, ingen skjulte gebyrer. Udelukkende til dækning af server- og API-drift."
                    </p>
                </div>
            </div>

            <div class="p-6 border-t border-slate-border bg-slate-surface flex flex-col gap-3">
                <button onclick="becomeSupporter()" class="w-full py-3 bg-amber-400 hover:bg-amber-500 text-indigo-950 font-bold rounded-xl transition-colors shadow-sm flex items-center justify-center gap-2">
                    Aktivér Supporter Medlemskab &rarr;
                </button>
                <button onclick="closeSupporterModal()" class="w-full py-2 bg-transparent text-on-surface-variant text-sm font-semibold hover:underline transition-colors">
                    Luk
                </button>
            </div>
        </div>
    </div>'''
content = old_modal_regex.sub(new_modal, content)

# 3. Dynamic Badge in Header
# In JS, update the badge logic
old_js_logic = """
            // Check supporter status
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            if (isSupporter) {
                const badgeContainer = document.getElementById('supporter-badge-container');
                if (badgeContainer) {
                    badgeContainer.innerHTML = '<span class="bg-amber-50 text-amber-700 border border-amber-300 font-bold px-3 py-1 rounded-full text-xs flex items-center gap-1"><span class="material-symbols-outlined text-sm">star</span> Supporter</span>';
                }
            } else {
                const supportBanner = document.getElementById('sidebar-supporter-banner');
                if (supportBanner) {
                    supportBanner.classList.remove('hidden');
                }
            }
"""
new_js_logic = """
            // Check supporter status
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            const badgeContainer = document.getElementById('supporter-badge-container');
            const supportBanner = document.getElementById('sidebar-supporter-banner');
            const sidebarBadge = document.getElementById('sidebar-supporter-badge');
            const sidebarRole = document.getElementById('sidebar-user-role');
            
            if (isSupporter) {
                if (badgeContainer) {
                    badgeContainer.innerHTML = '<span class="bg-amber-50 text-amber-700 border border-amber-300 font-bold px-2.5 py-1 rounded-full text-xs flex items-center gap-1 shadow-sm">⭐ Supporter</span>';
                }
                if (sidebarBadge) sidebarBadge.classList.remove('hidden');
                if (sidebarRole) sidebarRole.classList.add('hidden');
            } else {
                if (badgeContainer) {
                    badgeContainer.innerHTML = '<span id="freemium-pill-btn" onclick="openSupporterModal()" class="bg-indigo-50 text-deep-indigo border border-indigo-200 font-semibold px-2.5 py-1 rounded-full text-xs cursor-pointer hover:bg-indigo-100 transition-colors flex items-center">🌱 Freemium Medlem (Opgrader)</span>';
                }
                if (supportBanner) supportBanner.classList.remove('hidden');
                if (sidebarBadge) sidebarBadge.classList.add('hidden');
                if (sidebarRole) sidebarRole.classList.remove('hidden');
            }
"""
content = content.replace(old_js_logic, new_js_logic)

# Replace the becomeSupporter JS
old_become = """        function becomeSupporter() {
            localStorage.setItem('bi_is_supporter', 'true');
            window.location.reload();
        }"""
new_become = """        function becomeSupporter() {
            localStorage.setItem('bi_is_supporter', 'true');
            
            // Show toast
            const toast = document.getElementById('toast-banner');
            const toastText = document.getElementById('toast-text');
            const toastIcon = document.getElementById('toast-icon');
            const toastIconWrapper = document.getElementById('toast-icon-wrapper');
            
            if (toast && toastText && toastIcon) {
                toastIcon.textContent = 'star';
                toastIconWrapper.className = 'w-8 h-8 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0';
                toastIcon.className = 'material-symbols-outlined text-amber-500 text-sm font-bold';
                toastText.textContent = `Tusind tak for din støtte! ⭐ Du er nu Supporter.`;
                
                toast.classList.remove('translate-y-full', 'opacity-0');
            }
            
            closeSupporterModal();
            setTimeout(() => {
                window.location.reload();
            }, 2000);
        }"""
content = content.replace(old_become, new_become)


with open('dashboard.html', 'w') as f:
    f.write(content)

print("dashboard.html updated with Supporter UI")
