import re
import os

target_files = [
    "dashboard.html", "laer.html", "analyse.html", 
    "markeder.html", "vaerktoejer.html", "portefoelje.html", "profil.html"
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Main Canvas (Background) ---
    content = content.replace('dark:bg-dark-canvas', 'dark:bg-[#161922]')
    content = content.replace('dark:text-dark-text', 'dark:text-[#f8fafc]')

    # --- 2. Sidebar Dark Styling ---
    # Find <aside class="..."> and replace its dark mode styles
    def replace_aside(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
        cls = re.sub(r'dark:border-[^\s"]+', '', cls)
        cls = re.sub(r'\s+', ' ', cls).strip()
        cls += ' dark:bg-[#11141c] dark:border-[#1e2433]'
        return f'<aside class="{cls}">'
    content = re.sub(r'<aside class="([^"]+)">', replace_aside, content)

    # Sidebar Navigation links
    # Active
    content = content.replace(
        'bg-indigo-900/60 text-white font-semibold shadow-sm',
        'bg-indigo-900/60 text-white font-semibold shadow-sm dark:bg-[#1e2433] dark:text-white'
    )
    # Inactive
    def replace_inactive_links(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
        cls = re.sub(r'dark:border-[^\s"]+', '', cls)
        cls = re.sub(r'dark:text-[^\s"]+', '', cls)
        cls = re.sub(r'hover:dark:[^\s"]+', '', cls)
        cls = re.sub(r'\s+', ' ', cls).strip()
        cls += ' dark:text-[#94a3b8] hover:dark:text-white hover:dark:bg-white/5'
        return f'class="{cls}"'
    # We find class strings containing text-indigo-200 and hover:text-white
    content = re.sub(r'class="([^"]*text-indigo-200[^"]*)"', replace_inactive_links, content)

    # Toggle & Profil i bunden
    # They might use specific classes. 
    # The user asks: "Toggle & Profil i bunden: Integreret i rolige mørkegrå nuancer med gylden ⭐ Supporter accent."
    
    # --- 3. Bento-kort & Hovedpaneler ---
    # dark:bg-dark-card -> dark:bg-[#1e2330]
    content = content.replace('dark:bg-dark-card', 'dark:bg-[#1e2330]')
    
    # dark:border-dark-border on cards -> dark:border-[#2b3245]
    content = content.replace('dark:border-dark-border', 'dark:border-[#2b3245]')
    
    # "Fjern enhver forceret mørkeblå baggrund på kort og bento-kasser"
    # Might refer to bg-indigo-900/something or dark:bg-indigo-900 etc. We'll replace dark:bg-indigo-[0-9]+ with nothing on these if they exist, or they are covered by changing config/removing them.

    # --- 4. Indlejrede Bokse (Læringssti, Anti-FOMO, AI assistent) ---
    # typically dark:bg-dark-elevated -> dark:bg-[#252b3b] dark:border-[#323b52]
    content = content.replace('dark:bg-dark-elevated', 'dark:bg-[#252b3b] dark:border-[#323b52]')

    # Primær CTA (Start modul)
    # They might just be dark:bg-indigo-600 hover:dark:bg-indigo-500 ...
    
    # Sekundær CTA
    # They might have classes like dark:bg-slate-700 etc.

    # --- 5. Typografi ---
    # Secondary text: dark-muted -> #94a3b8
    content = content.replace('dark:text-dark-muted', 'dark:text-[#94a3b8]')
    
    # Labels/badges: we'll have to see.

    # --- 6. Finansielle & Status Indikatorer ---
    # Positivt: dark:bg-emerald-950/60 dark:text-emerald-400 dark:border-emerald-800/40
    # Advarsel: dark:bg-amber-950/60 dark:text-amber-400 dark:border-amber-800/40
    # Supporter Badge: dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in target_files:
    update_file(f)
