import os
import re

files_to_update = [
    'dashboard.html',
    'portefoelje.html',
    'laer.html',
    'analyse.html',
    'markeder.html',
    'vaerktoejer.html',
    'hjaelp.html'
]

# Add any modul-*.html files to the list
for f in os.listdir('.'):
    if f.startswith('modul-') and f.endswith('.html'):
        files_to_update.append(f)

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Update "Indstillinger" -> "Indstillinger / Profil" and href="#" -> href="profil.html"
    content = re.sub(
        r'<a href="#"([^>]*?)(>\s*<span class="material-symbols-outlined text-lg">settings</span>\s*<span class="hidden md:inline">)Indstillinger(</span>\s*</a>)',
        r'<a href="profil.html"\1\2Indstillinger / Profil\3',
        content,
        flags=re.DOTALL
    )

    # 2. Make avatar clickable to profil.html
    # Look for the avatar block
    # It looks like: <div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">
    # We will change the <div ... cursor-pointer ...> to an <a href="profil.html" ...>
    
    avatar_pattern = r'<div class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">'
    replacement = r'<a href="profil.html" class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">'
    
    if avatar_pattern in content:
        # Replace the opening div with opening a
        content = content.replace(avatar_pattern, replacement)
        
        # Now we need to find the matching closing div for this block and change it to </a>
        # We know it ends after the sidebar-badge span and its closing div
        
        # A simpler regex to replace the specific structure's closing div:
        # We can look for the block starting with the replacement and ending with </div>\n        </div>
        # Actually, let's just use regex to capture the inner content
        block_pattern = r'(<a href="profil\.html" class="flex items-center gap-3 md:px-3 py-3 mt-2 rounded-xl hover:bg-white/10 cursor-pointer transition-colors justify-center md:justify-start">.*?<span class="text-xs text-indigo-300 truncate" id="sidebar-badge">.*?</span>\s*</div>)\s*</div>'
        
        content = re.sub(block_pattern, r'\1\n            </a>', content, flags=re.DOTALL)

    # 3. Add the "Admin Terminal" link under the profile.
    # We need to insert a hidden link right after the profile, or inside the profile?
    # The prompt says: "tilføjes et diskret link under profilen: "⚡ Admin Terminal" der linker direkte til 'admin.html'."
    # I can append it right after the </a> tag of the profile.
    
    admin_link = '''
            <a href="admin.html" id="admin-link" class="hidden flex items-center gap-2 mt-2 px-3 py-2 rounded-lg text-indigo-300 hover:text-white hover:bg-indigo-900/50 transition-colors text-xs font-semibold justify-center md:justify-start border border-indigo-800/30">
                <span>⚡ Admin Terminal</span>
            </a>'''
            
    # Insert after </a> of the profile
    # Let's find the `</a>` we just created.
    # We'll use a regex that matches the end of the profile link
    content = re.sub(
        r'(<a href="profil\.html" class="flex items-center gap-3 md:px-3 py-3 mt-2[^>]*>.*?</a>)',
        r'\1' + admin_link,
        content,
        flags=re.DOTALL
    )
    
    # 4. Add JS to show the admin link if user is Admin
    # Look for </script>\n</body>
    js_snippet = """
            const userRole = localStorage.getItem('bi_user_role');
            const adminLink = document.getElementById('admin-link');
            if (adminLink && (userRole === 'Admin' || localStorage.getItem('bi_demo_mode') === 'true')) {
                adminLink.classList.remove('hidden');
                adminLink.classList.add('flex');
            }"""
            
    # We can inject this inside the existing DOMContentLoaded block if it exists, or before </body>
    if "document.addEventListener('DOMContentLoaded', () => {" in content:
        content = content.replace(
            "document.addEventListener('DOMContentLoaded', () => {",
            "document.addEventListener('DOMContentLoaded', () => {" + js_snippet
        )
    else:
        # If no DOMContentLoaded, append before </body>
        content = content.replace('</body>', f'<script>document.addEventListener("DOMContentLoaded", () => {{{js_snippet}}});</script>\n</body>')
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated sidebar files.")
