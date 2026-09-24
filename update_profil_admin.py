import re

with open('profil.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old admin-top-btn
old_btn = r'<a href="admin.html" id="admin-top-btn".*?</a>'
new_btn = '''<a href="admin.html" class="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-deep-indigo text-white hover:opacity-90 transition-all shadow-sm">
                    <span class="material-symbols-outlined text-sm">admin_panel_settings</span>
                    Åbn Admin Terminal
                </a>'''
content = re.sub(old_btn, new_btn, content, flags=re.DOTALL)

# Remove the JS logic for admin-top-btn
js_logic = r'// Check Admin Status for Top Button\s*const userRole = localStorage\.getItem\(\'bi_user_role\'\);\s*const adminTopBtn = document\.getElementById\(\'admin-top-btn\'\);\s*if \(adminTopBtn.*?}\s*'
content = re.sub(js_logic, '', content, flags=re.DOTALL)

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated profil.html")
