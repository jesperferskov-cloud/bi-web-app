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

new_bottom = '''   <!-- Admin Konsol Link -->
   <div class="px-3 pt-3">
     <a href="admin.html" class="flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs font-semibold text-amber-300 hover:text-amber-200 bg-amber-400/10 hover:bg-amber-400/20 border border-amber-400/30 transition-all group">
       <div class="flex items-center gap-2.5">
         <span class="material-symbols-outlined text-base text-amber-400">shield_person</span>
         <span>Admin Konsol</span>
       </div>
       <span class="text-[9px] uppercase tracking-wider font-bold bg-amber-400/20 text-amber-300 border border-amber-400/40 px-1.5 py-0.5 rounded">SUPER</span>
     </a>
   </div>

   <!-- Brugerprofil / Avatar -->
   <div class="p-3 pt-2">
     <a href="profil.html" class="flex items-center gap-3 p-2 rounded-xl hover:bg-white/5 transition-all text-left group">
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

    # For admin.html
    if filename == 'admin.html':
        # Find the border-t inside "Bottom Actions & Profile" and replace everything after it.
        # Actually, in admin.html there is `<div class="px-2 md:px-4 py-4 mt-auto">`
        # Let's replace the whole bottom section in admin.html
        content = re.sub(
            r'<!-- Bottom Actions & Profile -->\s*<div class="px-2 md:px-4 py-4 mt-auto">.*?</aside>',
            '<!-- Bottom Actions & Profile -->\n        <div class="px-2 md:px-4 py-4 mt-auto">\n' + new_bottom,
            content,
            flags=re.DOTALL
        )
    else:
        # Find where the hjaelp link ends and replace everything until </aside>
        content = re.sub(
            r'(<a href="hjaelp\.html"[^>]*>.*?</a>\s*</div>).*?</aside>',
            r'\1\n' + new_bottom,
            content,
            flags=re.DOTALL
        )
        
    # Remove any JS modifying sidebar badge that I might have missed
    content = re.sub(r'if \(\s*badgeContainer\s*\)\s*\{\s*badgeContainer\.innerHTML\s*=\s*\'<span class="bg-amber-50[^>]*>⭐ Supporter</span>\';\s*\}', '', content, flags=re.DOTALL)
    
    # Check for `elBadge.innerHTML = '⭐ Supporter';` again
    content = re.sub(r'elBadge\.innerHTML\s*=\s*\'⭐ Supporter\';', '', content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied strict replacement of bottom sidebar!")
