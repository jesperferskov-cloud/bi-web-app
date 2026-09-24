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


for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the JS logic for sidebar badge injection
    # It starts with "// Sidebar avatar badge wrapper" or similar
    # We can match from "const sidebarBadgeContainer" to the end of the if block.
    
    js_cleanup_regex3 = r'// Sidebar avatar badge wrapper.*?}\s*}\s*}'
    content = re.sub(js_cleanup_regex3, '', content, flags=re.DOTALL)
    
    # Also another regex to be more general:
    content = re.sub(r'const sidebarBadgeContainer = document\.getElementById\(\'sidebar-initials\'\).*?}\s*}\s*}', '', content, flags=re.DOTALL)
    
    # Also if there's any elBadge logic left over
    content = re.sub(r'const elBadge = document\.getElementById\(\'sidebar-badge\'\);.*?}\s*}', '', content, flags=re.DOTALL)
    content = re.sub(r'const elInitials = document\.getElementById\(\'sidebar-initials\'\);.*?elInitials\.textContent = initials \|\| \'JF\';', '', content, flags=re.DOTALL)

    # Let's remove anything related to sidebar-user-role or sidebar-supporter-badge being added dynamically
    content = re.sub(r'const sidebarBadge = document\.getElementById\(\'sidebar-supporter-badge\'\);.*?const sidebarRole = document\.getElementById\(\'sidebar-user-role\'\);', '', content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleaned up lingering JS from sidebars!")
