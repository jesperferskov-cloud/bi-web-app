import re

for filename in ['markeder.html', 'vaerktoejer.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the bottom links section with JF and Indstillinger
    bottom_links = '''        <!-- Bottom Links -->
        <div class="px-2 md:px-4 py-4 border-t border-white/10 flex flex-col gap-2 mt-auto">
            <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-indigo-200 hover:bg-white/10 hover:text-white transition-colors justify-center md:justify-start">
                <span class="material-symbols-outlined text-lg">settings</span>
                <span class="hidden md:inline text-sm">Indstillinger</span>
            </a>
            <div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-lg hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">
                <div class="w-8 h-8 rounded-full bg-white text-deep-indigo flex items-center justify-center text-xs font-bold shrink-0">
                    <span id="sidebar-initials">JF</span>
                </div>
                <div class="hidden md:flex flex-col overflow-hidden">
                    <span class="text-sm font-medium text-white truncate" id="sidebar-name">Jesper Ferskov</span>
                    <span class="text-xs text-indigo-300 truncate">Begynder</span>
                </div>
            </div>
        </div>'''
    
    html = re.sub(r'<!-- Bottom Links -->.*?</div>\s*</aside>', bottom_links + '\n    </aside>', html, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
