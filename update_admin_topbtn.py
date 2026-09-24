import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_btn = r'<a href="dashboard\.html" class="text-xs font-medium text-slate-600 hover:text-deep-indigo flex items-center gap-1\.5 px-3 py-1\.5 rounded-lg border border-slate-border hover:bg-slate-50 transition-all mr-4">.*?</a>'
new_btn = '''<a href="dashboard.html" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-border text-xs font-medium text-slate-700 hover:text-deep-indigo hover:bg-slate-50 transition-all mr-4">
                &larr; Tilbage til Bruger Dashboard
            </a>'''
            
content = re.sub(old_btn, new_btn, content, flags=re.DOTALL)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admin.html topbtn")
