import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Top bar Nav
content = content.replace(
    '<a href="onboarding.html" class="bg-deep-indigo text-white text-xs font-semibold px-4 py-2 rounded-lg glow-indigo hover:opacity-90 transition-opacity inline-flex items-center justify-center">Opret konto</a>',
    '<a href="login.html?mode=signup" class="bg-deep-indigo text-white text-xs font-semibold px-4 py-2 rounded-lg glow-indigo hover:opacity-90 transition-opacity inline-flex items-center justify-center">Opret konto</a>'
)

# 2. Hero button
content = content.replace(
    '''<a href="onboarding.html" class="bg-white text-deep-indigo hover:bg-slate-100 font-semibold text-sm px-6 py-3.5 rounded-xl transition-all shadow-md inline-flex items-center gap-2">
                            Udforsk universet
                            <span class="material-symbols-outlined text-sm font-bold">arrow_forward</span>
                        </a>''',
    '''<button onclick="openExploreModal()" class="bg-white text-deep-indigo hover:bg-slate-100 font-semibold text-sm px-6 py-3.5 rounded-xl transition-all shadow-md inline-flex items-center gap-2">
                            Udforsk universet
                            <span class="material-symbols-outlined text-sm font-bold">arrow_forward</span>
                        </button>'''
)

# 3. Interactive 'Sammenlign Aktier'
old_compare = """                        <p class="text-sm text-on-surface-variant leading-relaxed">
                            Brug 'Kerneanalyse: Sammenlign Aktier' til at analysere svære emner. Prøv f.eks.: <span class="font-bold text-deep-indigo">"Volvo vs Daimler – hvem vinder på den lange bane?"</span>
                        </p>
                        <div class="flex flex-col gap-2 mt-2">
                            <div class="flex items-center gap-2 text-xs text-on-surface-variant">
                                <span class="material-symbols-outlined text-emerald-success text-base">check_circle</span>
                                <span>Automatisk opsamling af årsrapporter</span>
                            </div>
                            <div class="flex items-center gap-2 text-xs text-on-surface-variant">
                                <span class="material-symbols-outlined text-emerald-success text-base">check_circle</span>
                                <span>Konkurrent-benchmark på 30 sekunder</span>
                            </div>
                        </div>
                        <a href="vaerktoejer.html" class="bg-deep-indigo text-white text-xs font-semibold px-6 py-3.5 rounded-lg glow-indigo hover:opacity-90 transition-opacity w-fit mt-2">Prøv værktøjet nu</a>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-lg border border-slate-border p-5">
                        <div class="flex items-center gap-2 mb-4 border-b border-slate-border pb-2 text-deep-indigo">
                            <span class="material-symbols-outlined text-base">smart_toy</span>
                            <span class="text-xs font-bold">AI Analyse: Volvo vs Daimler</span>
                        </div>
                        <div class="space-y-2.5">
                            <div class="h-3 bg-slate-100 rounded w-3/4"></div>
                            <div class="h-3 bg-slate-100 rounded w-full"></div>
                            <div class="grid grid-cols-2 gap-3 mt-4">
                                <div class="p-2.5 bg-emerald-50 border border-emerald-200 rounded-lg">
                                    <div class="text-[10px] text-emerald-700 font-bold uppercase">Volvo</div>
                                    <div class="text-xs font-bold mt-0.5">Stærk vækst</div>
                                </div>
                                <div class="p-2.5 bg-indigo-50 border border-indigo-200 rounded-lg">
                                    <div class="text-[10px] text-deep-indigo font-bold uppercase">Daimler</div>
                                    <div class="text-xs font-bold mt-0.5">Højere udbytte</div>
                                </div>
                            </div>
                        </div>
                    </div>"""

new_compare = """                        <p class="text-sm text-on-surface-variant leading-relaxed">
                            Brug 'Kerneanalyse: Sammenlign Aktier' til at analysere svære emner. Vælg et eksempel herunder for at se, hvordan vi lynhurtigt benchmark'er konkurrenter.
                        </p>
                        
                        <div class="flex flex-col gap-2 mt-2" id="compare-buttons">
                            <button onclick="updateCompareCard('novo')" class="compare-btn w-full text-left px-4 py-2 rounded-lg border-2 border-deep-indigo bg-indigo-50 text-deep-indigo text-sm font-semibold transition-colors flex justify-between items-center">
                                Novo Nordisk vs. Eli Lilly <span class="material-symbols-outlined text-sm">chevron_right</span>
                            </button>
                            <button onclick="updateCompareCard('volvo')" class="compare-btn w-full text-left px-4 py-2 rounded-lg border-2 border-slate-border bg-white text-on-surface-variant text-sm font-semibold hover:border-deep-indigo/50 transition-colors flex justify-between items-center">
                                Volvo vs. Daimler Truck <span class="material-symbols-outlined text-sm hidden">chevron_right</span>
                            </button>
                            <button onclick="updateCompareCard('apple')" class="compare-btn w-full text-left px-4 py-2 rounded-lg border-2 border-slate-border bg-white text-on-surface-variant text-sm font-semibold hover:border-deep-indigo/50 transition-colors flex justify-between items-center">
                                Apple vs. Microsoft <span class="material-symbols-outlined text-sm hidden">chevron_right</span>
                            </button>
                        </div>
                        
                        <a href="vaerktoejer.html" class="bg-deep-indigo text-white text-xs font-semibold px-6 py-3.5 rounded-lg glow-indigo hover:opacity-90 transition-opacity w-fit mt-4">Prøv værktøjet nu</a>
                    </div>
                    
                    <div class="bg-white rounded-xl shadow-lg border border-slate-border p-5 h-full flex flex-col transition-all duration-300" id="compare-result-card">
                        <div class="flex items-center gap-2 mb-4 border-b border-slate-border pb-2 text-deep-indigo">
                            <span class="material-symbols-outlined text-base">smart_toy</span>
                            <span class="text-xs font-bold" id="compare-title">AI Analyse: Novo Nordisk vs Eli Lilly</span>
                        </div>
                        <div class="flex-1 flex flex-col gap-4">
                            <!-- P/E -->
                            <div>
                                <div class="text-[10px] text-on-surface-variant font-bold uppercase tracking-wider mb-1">Værdiansættelse (P/E)</div>
                                <div class="grid grid-cols-2 gap-2" id="compare-pe">
                                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                                        <span>Novo (38.5)</span>
                                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                                    </div>
                                    <div class="p-2 bg-rose-critical/10 border border-rose-critical/20 rounded text-xs font-semibold text-rose-700 flex justify-between">
                                        <span>Lilly (62.1)</span>
                                        <span class="material-symbols-outlined text-sm">warning</span>
                                    </div>
                                </div>
                            </div>
                            <!-- Moat -->
                            <div>
                                <div class="text-[10px] text-on-surface-variant font-bold uppercase tracking-wider mb-1">Konkurrencefordel (Moat)</div>
                                <div class="p-2 bg-indigo-50 border border-indigo-100 rounded text-sm text-on-background leading-relaxed" id="compare-moat">
                                    Begge har en stærk moat via patenter og duopol på GLP-1 markedet. Novo vinder på produktionskapacitet.
                                </div>
                            </div>
                            <!-- Risikofaktor -->
                            <div>
                                <div class="text-[10px] text-on-surface-variant font-bold uppercase tracking-wider mb-1">Største Risikofaktor</div>
                                <div class="p-2 bg-slate-50 border border-slate-border rounded text-sm text-on-background leading-relaxed" id="compare-risk">
                                    Prispres i USA og politisk regulering af medicinpriser.
                                </div>
                            </div>
                        </div>
                    </div>"""
content = content.replace(old_compare, new_compare)

# 4. Modals and Scripts
explore_modal_html = """
    <!-- Explore Modal -->
    <div id="explore-modal" class="fixed inset-0 bg-on-background/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4" onclick="closeExploreModal()">
        <div class="bg-slate-surface rounded-2xl shadow-xl w-full max-w-2xl overflow-hidden flex flex-col" onclick="event.stopPropagation()">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-white">
                <h3 class="font-headline-md text-xl font-bold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined">rocket_launch</span>
                    Smagsprøve på Universet
                </h3>
                <button onclick="closeExploreModal()" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            
            <div class="p-6 md:p-8 space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- Step 1 -->
                    <div class="bg-white p-5 rounded-xl border border-slate-border shadow-sm flex flex-col items-center text-center">
                        <div class="w-12 h-12 rounded-full bg-indigo-50 flex items-center justify-center mb-3">
                            <span class="material-symbols-outlined text-deep-indigo text-xl">school</span>
                        </div>
                        <h4 class="font-bold text-on-background text-sm mb-2">1. Læring uden støj</h4>
                        <p class="text-xs text-on-surface-variant leading-relaxed">
                            Følg 4 modulære spor inklusiv hands-on skatteguides og praktisk viden.
                        </p>
                    </div>
                    <!-- Step 2 -->
                    <div class="bg-white p-5 rounded-xl border border-slate-border shadow-sm flex flex-col items-center text-center">
                        <div class="w-12 h-12 rounded-full bg-emerald-50 flex items-center justify-center mb-3">
                            <span class="material-symbols-outlined text-emerald-success text-xl">pie_chart</span>
                        </div>
                        <h4 class="font-bold text-on-background text-sm mb-2">2. Simuleret Portefølje</h4>
                        <p class="text-xs text-on-surface-variant leading-relaxed">
                            Start med 50.000 fiktive kr. og afprøv 80/20 Core-Satellite strategien.
                        </p>
                    </div>
                    <!-- Step 3 -->
                    <div class="bg-white p-5 rounded-xl border border-slate-border shadow-sm flex flex-col items-center text-center">
                        <div class="w-12 h-12 rounded-full bg-rose-50 flex items-center justify-center mb-3">
                            <span class="material-symbols-outlined text-rose-critical text-xl">psychology</span>
                        </div>
                        <h4 class="font-bold text-on-background text-sm mb-2">3. Mental Disciplin</h4>
                        <p class="text-xs text-on-surface-variant leading-relaxed">
                            48t anti-FOMO tænkepause og Pre-flight tjeklister til hver handel.
                        </p>
                    </div>
                </div>
            </div>

            <div class="p-6 border-t border-slate-border bg-white flex justify-center">
                <button onclick="exploreAsGuest()" class="w-full md:w-auto px-8 py-3 bg-deep-indigo text-white font-bold rounded-xl hover:opacity-90 transition-opacity shadow-md flex items-center justify-center gap-2">
                    Prøv som gæst nu <span class="material-symbols-outlined text-sm">arrow_forward</span>
                </button>
            </div>
        </div>
    </div>
"""

js_injection = """
        function openExploreModal() {
            document.getElementById('explore-modal').classList.remove('hidden');
        }

        function closeExploreModal() {
            document.getElementById('explore-modal').classList.add('hidden');
        }

        function exploreAsGuest() {
            localStorage.setItem('bi_user_name', 'Gæst');
            window.location.href = 'dashboard.html';
        }

        const compareData = {
            'novo': {
                title: 'AI Analyse: Novo Nordisk vs Eli Lilly',
                pe: `
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Novo (38.5)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>
                    <div class="p-2 bg-rose-critical/10 border border-rose-critical/20 rounded text-xs font-semibold text-rose-700 flex justify-between">
                        <span>Lilly (62.1)</span>
                        <span class="material-symbols-outlined text-sm">warning</span>
                    </div>`,
                moat: 'Begge har en stærk moat via patenter og duopol på GLP-1 markedet. Novo vinder på produktionskapacitet.',
                risk: 'Prispres i USA og politisk regulering af medicinpriser.'
            },
            'volvo': {
                title: 'AI Analyse: Volvo vs Daimler Truck',
                pe: `
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Volvo (10.2)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Daimler (11.5)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>`,
                moat: 'Volvo har et af verdens stærkeste brands i lastbilindustrien. Daimler er størst i volumen globalt.',
                risk: 'Cyklisk industri, der er stærkt påvirket af makroøkonomiske udsving og fragtrater.'
            },
            'apple': {
                title: 'AI Analyse: Apple vs Microsoft',
                pe: `
                    <div class="p-2 bg-slate-100 border border-slate-300 rounded text-xs font-semibold text-on-surface-variant flex justify-between">
                        <span>Apple (28.4)</span>
                        <span class="material-symbols-outlined text-sm">horizontal_rule</span>
                    </div>
                    <div class="p-2 bg-rose-critical/10 border border-rose-critical/20 rounded text-xs font-semibold text-rose-700 flex justify-between">
                        <span>Microsoft (35.2)</span>
                        <span class="material-symbols-outlined text-sm">warning</span>
                    </div>`,
                moat: 'Apple ejer økosystemet for forbrugere. Microsoft ejer enterprise økosystemet og AI-infrastruktur.',
                risk: 'Apple: Afhængighed af iPhone-salg. Microsoft: Kraftig konkurrence på AI og Cloud.'
            }
        };

        function updateCompareCard(caseId) {
            // Update buttons styling
            const buttons = document.querySelectorAll('.compare-btn');
            buttons.forEach(btn => {
                btn.classList.remove('border-deep-indigo', 'bg-indigo-50', 'text-deep-indigo');
                btn.classList.add('border-slate-border', 'bg-white', 'text-on-surface-variant');
                btn.querySelector('.material-symbols-outlined').classList.add('hidden');
            });
            
            const activeBtn = event.currentTarget;
            activeBtn.classList.remove('border-slate-border', 'bg-white', 'text-on-surface-variant');
            activeBtn.classList.add('border-deep-indigo', 'bg-indigo-50', 'text-deep-indigo');
            activeBtn.querySelector('.material-symbols-outlined').classList.remove('hidden');

            // Update card content
            const data = compareData[caseId];
            document.getElementById('compare-title').textContent = data.title;
            document.getElementById('compare-pe').innerHTML = data.pe;
            document.getElementById('compare-moat').textContent = data.moat;
            document.getElementById('compare-risk').textContent = data.risk;
            
            // Add a subtle blink effect
            const card = document.getElementById('compare-result-card');
            card.classList.add('opacity-50');
            setTimeout(() => card.classList.remove('opacity-50'), 150);
        }
"""

content = content.replace('</body>', explore_modal_html + '\n</body>')
content = content.replace('</script>\n</body>', js_injection + '\n</script>\n</body>')

with open('index.html', 'w') as f:
    f.write(content)

print("index.html updated.")
