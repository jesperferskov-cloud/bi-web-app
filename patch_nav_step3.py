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

new_bottom_nav = '''
   <!-- Admin Konsol Link -->
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
'''

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the bottom part of the sidebar.
    # The part to replace starts after "Hjælp" </a> and ends at </div> \n </aside>
    # In admin.html, it starts after "Audit Log" </a> or "Invite New User".
    # Wait, in admin.html it's completely different: "Bottom Actions & Profile" starts with <div class="px-2 md:px-4 py-4 mt-auto"> ...
    
    # Let's target the exact block in each file.
    if filename == 'admin.html':
        content = re.sub(
            r'<!-- Bottom Actions & Profile -->\s*<div class="px-2 md:px-4 py-4 mt-auto">.*?</div>\s*</aside>',
            '<!-- Bottom Actions & Profile -->\n        <div class="px-2 md:px-4 py-4 mt-auto">' + new_bottom_nav + '\n    </aside>',
            content,
            flags=re.DOTALL
        )
    else:
        # In non-admin files:
        # It's after the </a> of Hjælp, but we have <a href="admin.html" ... we just added in step 2.
        # Let's replace the whole bottom section:
        content = re.sub(
            r'<a href="admin\.html" id="sidebar-admin-link".*?</a>\s*</div>\s*<a href="profil\.html" class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">.*?</a>\s*</div>\s*</aside>',
            '</div>' + new_bottom_nav + '\n    </aside>',
            content,
            flags=re.DOTALL
        )
        
        # Also clean up any lingering JS that messes with the badge
        # Remove anything updating `sidebar-badge` or `sidebar-initials` or `sidebar-name`
        js_cleanup_regex1 = r'const elBadge = document\.getElementById\(\'sidebar-badge\'\);.*?}\s*}'
        content = re.sub(js_cleanup_regex1, '', content, flags=re.DOTALL)
        
        js_cleanup_regex2 = r'const isSupporter = localStorage\.getItem\(\'bi_is_supporter\'\);'
        content = re.sub(js_cleanup_regex2, '', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated bottom sidebars to match requirement!")
