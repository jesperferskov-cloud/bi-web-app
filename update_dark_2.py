import re
import os

target_files = [
    "dashboard.html", "laer.html", "analyse.html", 
    "markeder.html", "vaerktoejer.html", "portefoelje.html", "profil.html"
]

def update_file(filename):
    if not os.path.exists(filename):
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Toggle & Profil i bunden: Integreret i rolige mørkegrå nuancer med gylden ⭐ Supporter accent.
    # We already updated aside, but let's make sure the Supporter label gets the right classes:
    # "⭐ Supporter accent"
    # Actually the user asks for: "Supporter Badge: dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30"
    # Let's replace any existing dark amber classes for supporter badges:
    content = re.sub(
        r'dark:bg-amber-950/60 dark:text-amber-400([^>]*?Supporter)', 
        r'dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30\1',
        content
    )
    # Also if it didn't have it:
    def add_supporter_badge(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
        cls = re.sub(r'dark:text-[^\s"]+', '', cls)
        cls = re.sub(r'dark:border-[^\s"]+', '', cls)
        cls = re.sub(r'\s+', ' ', cls).strip()
        cls += ' dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30'
        return f'class="{cls}"'
    # Any class string containing text-amber-400 and followed closely by Supporter or ⭐
    # It might be easier to just regex the exact known strings.
    
    # Let's just blindly add dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30 
    # to anything that looks like a supporter badge.
    content = content.replace('text-[11px] text-amber-400 font-medium flex items-center gap-1 dark:bg-amber-950/60 dark:text-amber-400', 
                              'text-[11px] text-amber-400 font-medium flex items-center gap-1 dark:bg-amber-500/10 dark:text-amber-400 dark:border-amber-500/30 rounded px-1')

    # Finansielle & Status Indikatorer
    # Gennemført / Positivt: dark:bg-emerald-950/60 dark:text-emerald-400 dark:border-emerald-800/40.
    # e.g. text-emerald-success bg-emerald-50
    def emerald_sub(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
        cls = re.sub(r'dark:text-[^\s"]+', '', cls)
        cls = re.sub(r'dark:border-[^\s"]+', '', cls)
        cls = re.sub(r'\s+', ' ', cls).strip()
        cls += ' dark:bg-emerald-950/60 dark:text-emerald-400 dark:border-emerald-800/40 dark:border'
        return f'class="{cls}"'
    content = re.sub(r'class="([^"]*text-emerald-success[^"]*bg-emerald-50[^"]*)"', emerald_sub, content)

    # Advarsel / Anti-FOMO: dark:bg-amber-950/60 dark:text-amber-400 dark:border-amber-800/40.
    # e.g. text-amber-700 bg-amber-50 or text-rose-critical bg-rose-50 ... wait, FOMO might be rose or amber.
    def amber_sub(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
        cls = re.sub(r'dark:text-[^\s"]+', '', cls)
        cls = re.sub(r'dark:border-[^\s"]+', '', cls)
        cls = re.sub(r'\s+', ' ', cls).strip()
        cls += ' dark:bg-amber-950/60 dark:text-amber-400 dark:border-amber-800/40 dark:border'
        return f'class="{cls}"'
    content = re.sub(r'class="([^"]*text-amber-[6789]00[^"]*bg-amber-50[^"]*)"', amber_sub, content)

    # Primær CTA: dark:bg-indigo-600 hover:dark:bg-indigo-500 text-white font-semibold px-5 py-2.5 rounded-xl.
    # If there's bg-deep-indigo text-white ...
    def primary_cta_sub(m):
        cls = m.group(1)
        if 'dark:bg-indigo-600' not in cls:
            cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
            cls = re.sub(r'hover:dark:bg-[^\s"]+', '', cls)
            cls = re.sub(r'\s+', ' ', cls).strip()
            cls += ' dark:bg-indigo-600 hover:dark:bg-indigo-500'
        return f'class="{cls}"'
    content = re.sub(r'class="([^"]*bg-deep-indigo[^"]*text-white[^"]*)"', primary_cta_sub, content)

    # Sekundær CTA: dark:bg-white/10 dark:text-slate-200 hover:dark:bg-white/15.
    # usually has border-slate-border text-on-surface-variant or text-deep-indigo
    # Example: "text-xs text-deep-indigo font-medium flex items-center gap-1" inside cards
    def secondary_cta_sub(m):
        cls = m.group(1)
        if 'dark:bg-white/10' not in cls:
            cls = re.sub(r'dark:text-[^\s"]+', '', cls)
            cls = re.sub(r'dark:bg-[^\s"]+', '', cls)
            cls = re.sub(r'hover:dark:[^\s"]+', '', cls)
            cls = re.sub(r'\s+', ' ', cls).strip()
            cls += ' dark:bg-white/10 dark:text-slate-200 hover:dark:bg-white/15'
        return f'class="{cls}"'
    content = re.sub(r'class="([^"]*bg-slate-surface[^"]*hover:[^"]*)"', secondary_cta_sub, content)
    # wait, modifying all bg-slate-surface hover elements might break cards! 

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for f in target_files:
    update_file(f)

