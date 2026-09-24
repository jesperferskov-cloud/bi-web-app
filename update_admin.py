import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert "<- Gå til Dashboard" to the left of the search
search_block = r'(<!-- Global Search -->\s*<div class="relative w-full max-w-md hidden sm:block">)'
dashboard_btn = '''<a href="dashboard.html" class="text-xs font-medium text-slate-600 hover:text-deep-indigo flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-border hover:bg-slate-50 transition-all mr-4">
                <span class="material-symbols-outlined text-[18px]">arrow_back</span> Gå til Dashboard
            </a>\n            '''
content = re.sub(search_block, dashboard_btn + r'\1', content)

# 2. Make the admin badge clickable
badge_block = r'(<div class="flex items-center gap-3 md:px-3 py-2 rounded-xl bg-indigo-950/40 border border-indigo-900/30 justify-center md:justify-start">)'
content = re.sub(badge_block, r'<a href="profil.html" class="flex items-center gap-3 md:px-3 py-2 rounded-xl bg-indigo-950/40 border border-indigo-900/30 justify-center md:justify-start hover:bg-indigo-900/60 transition-colors cursor-pointer">', content)
content = re.sub(r'(<span class="w-1\.5 h-1\.5 rounded-full bg-emerald-400"></span> Superadmin\s*</span>\s*</div>\s*)</div>', r'\1</a>', content)

# 3. Make logout work
logout_block = r'(<button class="hidden sm:flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-deep-indigo">)'
content = re.sub(logout_block, r'<button onclick="window.location.href=\'login.html\'" class="hidden sm:flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-deep-indigo">', content)


with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(content)
