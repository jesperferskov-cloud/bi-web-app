import re

with open('vaerktoejer.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """
            <!-- Sektion: Print & Download -->
            <section class="space-y-6">
                <header>
                    <div class="flex items-center gap-3 mb-1">
                        <h3 class="text-2xl font-headline-md font-semibold text-deep-indigo dark:text-[#c3c0ff]">🖨️ Fysiske Referenceark & Tjeklister (A4 Print)</h3>
                        <span class="bg-indigo-50 text-indigo-700 dark:bg-[#14171f] dark:text-slate-400 text-[10px] uppercase font-bold px-2 py-0.5 rounded border border-indigo-100 dark:border-[#2a3245]">Metodisk Investeringsværktøj • Høj Opløsning</span>
                    </div>
                    <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] mt-1">Strukturér dit analysearbejde ved skrivebordet. Hent vores 1-sides A4 referenceark og tjeklister til udskrift, så du har et fast metodisk holdepunkt under dine analyser.</p>
                </header>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Kort 1 -->
                    <div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">checklist</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Den Store Aktie-Tjekliste</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Gennemgå de 10 vigtigste punkter før du investerer i en ny aktie.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>

                    <!-- Kort 2 -->
                    <div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">pie_chart</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Portefølje-Skabelon</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Design din Core/Satellite struktur og hold styr på din spredning.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>

                    <!-- Kort 3 -->
                    <div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">functions</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Nøgletal i Praksis (P/E, Moat & ROIC)</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Hurtig guide til tolkning af markedets vigtigste nøgletal og værdiansættelse.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>
                </div>
            </section>
"""

# Insert before Sektion 5
if '<!-- Sektion 5: Søgbar Ordbog -->' in content:
    content = content.replace('<!-- Sektion 5: Søgbar Ordbog -->', new_section + '\n            <!-- Sektion 5: Søgbar Ordbog -->')
    with open('vaerktoejer.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected Print & Download section into vaerktoejer.html")
else:
    print("Could not find insertion point!")
