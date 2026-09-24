import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# Add the supporter modal to the end of the file before </body>
supporter_modal = """
    <!-- Supporter Modal -->
    <div id="supporter-modal" class="fixed inset-0 bg-on-background/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 transition-opacity duration-300 opacity-0" onclick="closeSupporterModal()">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden flex flex-col transform transition-transform duration-300 scale-95" id="supporter-modal-inner" onclick="event.stopPropagation()">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-slate-surface">
                <h3 class="font-headline-md text-xl font-bold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined text-amber-500">favorite</span>
                    Støt Begynder Investor
                </h3>
                <button onclick="closeSupporterModal()" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            
            <div class="p-6 space-y-4">
                <p class="text-sm text-on-surface-variant leading-relaxed">
                    Begynder Investor er et uafhængigt læringsunivers. For kun <strong class="text-on-background">29 kr. om måneden</strong> hjælper du med at dække vores AI-serveromkostninger og holde platformen fri for støj og reklamer.
                </p>
                <div class="bg-amber-50 border border-amber-100 rounded-xl p-4 mt-2">
                    <h4 class="text-xs font-bold text-amber-800 uppercase tracking-wider mb-2">Som Supporter får du:</h4>
                    <ul class="space-y-2 text-sm text-amber-700">
                        <li class="flex items-start gap-2">
                            <span class="material-symbols-outlined text-sm mt-0.5">check_circle</span>
                            <span>Ubegrænsede AI-analyser & Djævelens Advokat</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="material-symbols-outlined text-sm mt-0.5">check_circle</span>
                            <span>Eksklusivt ⭐ Supporter-badge på din profil</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="material-symbols-outlined text-sm mt-0.5">check_circle</span>
                            <span>Adgang til tidlige beta-funktioner</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="p-6 border-t border-slate-border bg-slate-surface flex flex-col gap-3">
                <button onclick="becomeSupporter()" class="w-full py-3 bg-amber-500 text-white font-bold rounded-xl hover:bg-amber-600 transition-colors shadow-sm flex items-center justify-center gap-2">
                    Bliv Supporter (29 kr./md) <span class="material-symbols-outlined text-sm">lock_open</span>
                </button>
                <button onclick="closeSupporterModal()" class="w-full py-2 bg-transparent text-on-surface-variant text-xs font-semibold hover:underline transition-colors">
                    Måske senere
                </button>
            </div>
        </div>
    </div>
"""

content = content.replace('</body>', supporter_modal + '\n</body>')

# Update the Welcome Header in the Bento Grid to add a wrapper for the badge
old_greeting = '''<h1 class="text-2xl md:text-3xl font-bold font-headline-lg text-deep-indigo mb-2 relative z-10">
                        Velkommen, <span id="dash-user-name">Jesper</span>! 👋
                    </h1>'''
new_greeting = '''<div class="flex items-center flex-wrap gap-3 mb-2 relative z-10">
                        <h1 class="text-2xl md:text-3xl font-bold font-headline-lg text-deep-indigo flex items-center gap-2">
                            Velkommen, <span id="dash-user-name">Jesper</span>! 👋
                        </h1>
                        <div id="supporter-badge-container"></div>
                    </div>'''
content = content.replace(old_greeting, new_greeting)

# Find the bottom of the sidebar to inject the support banner
sidebar_bottom_marker = '''                    <span class="text-xs text-indigo-300 truncate">Begynder</span>
                </div>
            </div>
        </div>
    </aside>'''
sidebar_bottom_new = '''                    <span class="text-xs text-indigo-300 truncate">Begynder</span>
                </div>
            </div>
        </div>
        
        <!-- Supporter Banner -->
        <div id="sidebar-supporter-banner" class="hidden mt-auto px-2 md:px-4 mb-4">
            <div class="bg-amber-50 border border-amber-200 rounded-xl p-4 text-center cursor-pointer hover:bg-amber-100 transition-colors" onclick="openSupporterModal()">
                <p class="text-xs font-bold text-amber-800 mb-1">Støt projektet (29 kr.)</p>
                <p class="text-[10px] text-amber-700 leading-relaxed">❤️ Hold Begynder Investor uafhængig og dæk vores AI-serveromkostninger.</p>
            </div>
        </div>
    </aside>'''
content = content.replace(sidebar_bottom_marker, sidebar_bottom_new)

# Inject JS for checking supporter status
js_logic = """
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

# Place it inside DOMContentLoaded
doc_ready_marker = "const sidebarInitials = document.getElementById('sidebar-initials');\n            if (sidebarInitials && userName.length > 0) {\n                sidebarInitials.textContent = userName.substring(0,2).toUpperCase();\n            }"
content = content.replace(doc_ready_marker, doc_ready_marker + "\n" + js_logic)

# Add modal functions to the end of scripts
modal_funcs = """
        function openSupporterModal() {
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
            window.location.reload();
        }
"""
content = content.replace('</script>\n</body>', modal_funcs + '\n</script>\n</body>')

with open('dashboard.html', 'w') as f:
    f.write(content)

print("dashboard.html updated.")
