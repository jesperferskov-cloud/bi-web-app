import os
import re

files_to_update = [
    'dashboard.html',
    'profil.html',
    'admin.html',
    'portefoelje.html',
    'laer.html',
    'analyse.html',
    'markeder.html',
    'vaerktoejer.html',
    'hjaelp.html'
]

for f in os.listdir('.'):
    if f.startswith('modul-') and f.endswith('.html'):
        files_to_update.append(f)

new_bottom = '''
        <div class="px-2 md:px-4 py-4 mt-auto">
            <div class="border-t border-indigo-900/40 my-3"></div>
            <div class="flex flex-col gap-1">
                <!-- Hjælp Link -->
                <a href="hjaelp.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm font-medium text-indigo-200 hover:text-white hover:bg-white/10 transition-all">
                    <span class="material-symbols-outlined text-lg">help</span>
                    <span>Hjælp</span>
                </a>
            </div>

            <!-- Admin Konsol (Kun 1 instans) -->
            <div class="px-1 pt-2">
                <a href="admin.html" class="flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-semibold text-amber-300 hover:text-amber-200 bg-amber-400/10 hover:bg-amber-400/20 border border-amber-400/30 transition-all">
                    <div class="flex items-center gap-2">
                        <span class="material-symbols-outlined text-base text-amber-400">shield_person</span>
                        <span>Admin Konsol</span>
                    </div>
                    <span class="text-[9px] uppercase tracking-wider font-bold bg-amber-400/20 text-amber-300 border border-amber-400/40 px-1.5 py-0.5 rounded">SUPER</span>
                </a>
            </div>

            <!-- Brugerprofil / Avatar (Eneansvarlig for profil.html) -->
            <div class="pt-2">
                <a href="profil.html" class="flex items-center gap-3 p-2 rounded-xl hover:bg-white/5 transition-all group">
                    <div class="w-9 h-9 rounded-full bg-white flex items-center justify-center font-bold text-xs text-deep-indigo shrink-0 shadow-sm">
                        JF
                    </div>
                    <div class="flex flex-col min-w-0">
                        <span class="text-sm font-semibold text-white truncate group-hover:text-amber-300 transition-colors">Jesper Ferskov</span>
                        <span class="text-[11px] text-amber-400 font-medium flex items-center gap-1">
                            ⭐ Supporter
                        </span>
                    </div>
                </a>
            </div>
        </div>
    </aside>'''

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace everything from </nav> to </aside>
    content = re.sub(
        r'</nav>.*?</aside>',
        '</nav>' + new_bottom,
        content,
        flags=re.DOTALL
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated nav bottoms across all files")
