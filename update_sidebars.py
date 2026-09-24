import glob

files = ["dashboard.html", "portefoelje.html", "laer.html", "analyse.html", "markeder.html", "vaerktoejer.html", "profil.html", "admin.html", "hjaelp.html"]
for f in glob.glob("modul*.html") + glob.glob("index.html") + glob.glob("login.html") + glob.glob("onboarding.html"):
    if f not in files:
        files.append(f)

insert_text = """
            <a href="maal.html" class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl font-medium text-sm transition-all justify-center md:justify-start text-indigo-200 hover:text-white hover:bg-white/10 dark:text-[#94a3b8] hover:dark:text-white hover:dark:bg-white/5">
                <span class="material-symbols-outlined text-xl">track_changes</span>
                <span class="hidden md:inline">Målsætning</span>
            </a>"""

for file in files:
    try:
        with open(file, 'r') as f_in:
            content = f_in.read()
        
        target_str = '<span class="hidden md:inline">Min Portefølje</span>\n            </a>'
        if target_str in content and 'href="maal.html"' not in content:
            content = content.replace(target_str, target_str + insert_text)
            with open(file, 'w') as f_out:
                f_out.write(content)
            print(f"Updated {file}")
    except Exception as e:
        print(f"Error on {file}: {e}")
