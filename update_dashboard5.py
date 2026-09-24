import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# 1. Update the sidebar button (remove onclick, ensure ID)
content = content.replace(
    'id="open-supporter-modal-btn" onclick="openSupporterModal()"',
    'id="open-supporter-modal-btn"'
)

# 2. Update the modal HTML
# Need to make sure close buttons have id="close-supporter-modal-btn"
# Need to make sure activate button has id="activate-supporter-btn"
old_modal_regex = re.compile(r'<!-- Supporter Modal -->.*?</div>\n    </div>', re.DOTALL)
new_modal = '''<!-- Supporter Modal -->
    <div id="supporter-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm hidden">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden flex flex-col" id="supporter-modal-inner">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-slate-surface">
                <h3 class="font-headline-md text-xl font-bold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined text-amber-500">star</span>
                    Bliv Supporter
                </h3>
                <button id="close-supporter-modal-btn" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
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
                <button id="activate-supporter-btn" class="w-full py-3 bg-amber-400 hover:bg-amber-500 text-indigo-950 font-bold rounded-xl transition-colors shadow-sm flex items-center justify-center gap-2">
                    Aktivér Supporter Medlemskab &rarr;
                </button>
                <button id="close-supporter-modal-btn-2" class="w-full py-2 bg-transparent text-on-surface-variant text-sm font-semibold hover:underline transition-colors">
                    Luk
                </button>
            </div>
        </div>
    </div>'''
content = old_modal_regex.sub(new_modal, content)

# 3. Update the freemium pill button (remove inline onclick)
content = content.replace(
    '<span id="freemium-pill-btn" onclick="openSupporterModal()"',
    '<span id="freemium-pill-btn"'
)

# 4. Remove old modal script logic
old_modal_js = """        function openSupporterModal() {
            const modal = document.getElementById('supporter-modal');
            const inner = document.getElementById('supporter-modal-inner');
            modal.classList.remove('hidden');
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                inner.classList.remove('scale-95');
                inner.classList.add('scale-100');
            }, 10);
        }

        function closeSupporterModal() {
            const modal = document.getElementById('supporter-modal');
            const inner = document.getElementById('supporter-modal-inner');
            modal.classList.add('opacity-0');
            inner.classList.remove('scale-100');
            inner.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300);
        }

        function becomeSupporter() {
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
content = content.replace(old_modal_js, "")

# 5. Add new robust JS logic inside DOMContentLoaded
# We need to find the DOMContentLoaded block and insert it there.
js_insert = """
            // Event Listeners for Supporter Modal
            const supporterModal = document.getElementById('supporter-modal');
            const openSupporterBtn = document.getElementById('open-supporter-modal-btn');
            const closeSupporterBtn = document.getElementById('close-supporter-modal-btn');
            const closeSupporterBtn2 = document.getElementById('close-supporter-modal-btn-2');
            const activateSupporterBtn = document.getElementById('activate-supporter-btn');
            const freemiumPillBtn = document.getElementById('freemium-pill-btn');

            const openModal = (e) => {
                if (e) e.preventDefault();
                if (supporterModal) supporterModal.classList.remove('hidden');
            };

            const closeModal = (e) => {
                if (e) e.preventDefault();
                if (supporterModal) supporterModal.classList.add('hidden');
            };

            if (openSupporterBtn) openSupporterBtn.addEventListener('click', openModal);
            // We need to attach to freemiumPillBtn, but since it's injected dynamically, 
            // we will re-attach below when rendering UI.
            if (closeSupporterBtn) closeSupporterBtn.addEventListener('click', closeModal);
            if (closeSupporterBtn2) closeSupporterBtn2.addEventListener('click', closeModal);

            if (supporterModal) {
                supporterModal.addEventListener('click', (e) => {
                    if (e.target === supporterModal) closeModal();
                });
            }

            if (activateSupporterBtn) {
                activateSupporterBtn.addEventListener('click', (e) => {
                    e.preventDefault();
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
                    
                    closeModal();
                    setTimeout(() => {
                        window.location.reload();
                    }, 2000);
                });
            }
"""
content = content.replace("const holdings = JSON.parse(localStorage.getItem('bi_portfolio_holdings') || '[]');", js_insert + "\n            const holdings = JSON.parse(localStorage.getItem('bi_portfolio_holdings') || '[]');")

# 6. Update the UI rendering to reattach listener to dynamically created pill
# Update the previous UI logic that I injected.
old_ui_logic = """
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
                    badgeContainer.innerHTML = '<span id="freemium-pill-btn" class="bg-indigo-50 text-deep-indigo border border-indigo-200 font-semibold px-2.5 py-1 rounded-full text-xs cursor-pointer hover:bg-indigo-100 transition-colors flex items-center">🌱 Freemium Medlem (Opgrader)</span>';
                }
                if (supportBanner) supportBanner.classList.remove('hidden');
                if (sidebarBadge) sidebarBadge.classList.add('hidden');
                if (sidebarRole) sidebarRole.classList.remove('hidden');
            }
"""
new_ui_logic = """
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
                if (supportBanner) supportBanner.classList.add('hidden');
                
                // Sidebar avatar badge wrapper
                const sidebarBadgeContainer = document.getElementById('sidebar-initials').parentElement.nextElementSibling;
                if (sidebarBadgeContainer) {
                    let existingBadge = document.getElementById('sidebar-supporter-badge');
                    if (existingBadge) existingBadge.remove(); // Reset if exists
                    
                    const badgeHtml = `<div class="mt-1" id="sidebar-supporter-badge"><span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-400/20 text-amber-300 border border-amber-400/40">⭐ Supporter</span></div>`;
                    
                    // Insert before the role
                    const roleEl = sidebarBadgeContainer.querySelector('#sidebar-user-role');
                    if(roleEl) {
                        roleEl.insertAdjacentHTML('beforebegin', badgeHtml);
                        roleEl.classList.add('hidden');
                    } else {
                        sidebarBadgeContainer.insertAdjacentHTML('beforeend', badgeHtml);
                    }
                }
            } else {
                if (badgeContainer) {
                    badgeContainer.innerHTML = '<span id="freemium-pill-btn" class="bg-indigo-50 text-deep-indigo border border-indigo-200 font-semibold px-2.5 py-1 rounded-full text-xs cursor-pointer hover:bg-indigo-100 transition-colors flex items-center gap-1">🌱 Freemium Medlem (Opgrader)</span>';
                    
                    // Re-attach event listener since it was dynamically created
                    setTimeout(() => {
                        const newFreemiumBtn = document.getElementById('freemium-pill-btn');
                        if (newFreemiumBtn) {
                            newFreemiumBtn.addEventListener('click', (e) => {
                                e.preventDefault();
                                document.getElementById('supporter-modal').classList.remove('hidden');
                            });
                        }
                    }, 50);
                }
                if (supportBanner) supportBanner.classList.remove('hidden');
            }
"""
content = content.replace(old_ui_logic, new_ui_logic)

with open('dashboard.html', 'w') as f:
    f.write(content)

print("dashboard.html updated with clean event listeners.")
