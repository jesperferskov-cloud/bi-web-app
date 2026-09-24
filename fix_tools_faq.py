import re

# 1. Update vaerktoejer.html
with open('vaerktoejer.html', 'r', encoding='utf-8') as f:
    v_html = f.read()

# Replace Header
v_html = re.sub(
    r'<h1[^>]*>.*?Investor Toolkit & Ressourcer.*?</h1>',
    '<h1 class="text-4xl md:text-5xl text-on-background font-headline-lg font-bold dark:text-[#f8fafc]">\n                    Kerneanalyse: Sammenlign Aktier\n                </h1>',
    v_html,
    flags=re.DOTALL
)

# Replace Subtitle in AI Prompt-Bibliotek
v_html = re.sub(
    r'<p class="text-sm text-on-surface-variant dark:text-\[#94a3b8\] mt-1">Kopier færdige prompter til ChatGPT, Gemini eller Claude for dybdegående analyser.</p>',
    '<p class="text-sm text-on-surface-variant dark:text-[#94a3b8] mt-1">Kopiér disse strukturerede prompter og anvend dem direkte i Gemini eller NotebookLM for at køre dine egne dybdegående, kildekritiske analyser af rigtige aktier.</p>',
    v_html
)

# Replace Workflow intro
v_html = re.sub(
    r'<p class="text-sm text-on-surface-variant dark:text-\[#94a3b8\] mt-1">Fra Idé til Eksekvering.</p>',
    '<p class="text-sm text-on-surface-variant dark:text-[#94a3b8] mt-1">Fra idé til eksekvering. Fasthold et kynisk og disciplineret mindset, der modvirker følelsesmæssig støj på markederne, før du sætter kapital på spil.</p>',
    v_html
)

with open('vaerktoejer.html', 'w', encoding='utf-8') as f:
    f.write(v_html)

# 2. Update hjaelp.html
with open('hjaelp.html', 'r', encoding='utf-8') as f:
    h_html = f.read()

# Make sure "børnehøjde" or "trygt sted" is gone. (Already verified it's replaced with "Et uafhængigt, pædagogisk læringslaboratorium og simuleringsmiljø...")

# Add AI question if missing
ai_q = """
                        <div class="faq-item bg-white border border-slate-border rounded-xl p-5 shadow-sm" data-category="platform">
                            <h3 class="font-semibold text-on-background faq-q">Hvordan bruger Begynder Investor AI?</h3>
                            <p class="text-on-surface-variant text-sm mt-2 faq-a">Platformens AI-integration fungerer som en transparent "analytisk sparringspartner" frem for en magisk sandhedsegnet løsning. Den hjælper med at afkode komplekse mekanismer og strukturere markedsstøj, men den kildekritiske vurdering ligger altid hos dig.</p>
                        </div>
"""
if "Hvordan bruger Begynder Investor AI" not in h_html:
    # Insert it before the last faq-item
    h_html = re.sub(
        r'(<div class="faq-item bg-white border border-slate-border rounded-xl p-5 shadow-sm"[^>]*>\s*<h3 class="font-semibold text-on-background faq-q">Yder Begynder Investor individuel)',
        ai_q + r'\1',
        h_html
    )

with open('hjaelp.html', 'w', encoding='utf-8') as f:
    f.write(h_html)

print("Updates applied.")
