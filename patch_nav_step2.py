import os
import re

files_to_update = [
    'dashboard.html',
    'profil.html',
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

new_admin_link = '''
                <a href="admin.html" id="sidebar-admin-link" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-xs font-semibold text-amber-400/90 hover:text-amber-300 hover:bg-white/10 transition-all border border-amber-400/30 my-2">
                    <span class="material-symbols-outlined text-sm text-amber-400">shield_person</span>
                    <span class="hidden md:inline">Admin Konsol</span>
                    <span class="hidden md:inline ml-auto text-[9px] bg-amber-400/20 text-amber-300 border border-amber-400/40 px-1.5 py-0.5 rounded font-bold">SUPER</span>
                </a>'''

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the old hidden admin link block
    content = re.sub(
        r'<a href="admin\.html" id="admin-link"[^>]*>.*?</a>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove the JS logic for the old admin link
    js_logic_regex = r'const userRole = localStorage\.getItem\(\'bi_user_role\'\);\s*const adminLink = document\.getElementById\(\'admin-link\'\);\s*if \(adminLink[^}]+}\s*'
    content = re.sub(js_logic_regex, '', content)

    # Inject the new permanent admin link after the 'Hjælp' link
    # Find the end of the "hjaelp.html" </a> block
    content = re.sub(
        r'(<a href="hjaelp\.html"[^>]*>.*?</a>)',
        r'\1' + new_admin_link,
        content,
        flags=re.DOTALL
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated sidebars!")
