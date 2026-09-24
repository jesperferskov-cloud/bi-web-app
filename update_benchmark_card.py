import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    card_html = """
            <!-- Bento-kort: Markeds-Benchmark & Udvikling -->
            <div id="benchmark-card" class="bg-white rounded-2xl border border-slate-border p-6 shadow-sm flex flex-col mb-6">
                <!-- Header -->
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
                    <div class="flex items-center gap-3 flex-wrap">
                        <h2 class="text-xl font-bold font-headline-md text-deep-indigo flex items-center gap-2">
                            📈 Portefølje Benchmark
                        </h2>
                        <span class="bg-indigo-50 text-deep-indigo border border-indigo-200 text-[11px] font-semibold px-2.5 py-0.5 rounded-full whitespace-nowrap">
                            💡 Simuleret data til læringsøvelse
                        </span>
                    </div>
                    
                    <!-- Kontrol-knapper (Selector pills) -->
                    <div class="flex items-center gap-2 bg-slate-surface p-1 rounded-xl border border-slate-border self-start md:self-auto">
                        <button class="px-4 py-1.5 text-sm font-semibold rounded-lg bg-white border border-slate-border text-deep-indigo shadow-sm" id="btn-bench-sp500">
                            S&P 500 Index (+9.8%)
                        </button>
                        <button class="px-4 py-1.5 text-sm font-semibold rounded-lg text-on-surface-variant hover:text-deep-indigo transition-colors" id="btn-bench-msci">
                            MSCI World Index (+8.2%)
                        </button>
                    </div>
                </div>

                <!-- Visuel Sammenligning & Udvikling -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <!-- Venstre: Din Portefølje -->
                    <div class="bg-slate-surface p-5 rounded-xl border border-slate-border flex flex-col">
                        <p class="text-sm font-semibold text-on-surface-variant uppercase tracking-wider mb-2">Din Portefølje (TWR)</p>
                        <h3 class="text-2xl font-bold text-deep-indigo mb-1" id="bench-port-return">+4.2%</h3>
                        <p class="text-xs text-on-surface-variant">Ud fra 50.000 kr. basis</p>
                    </div>
                    <!-- Højre: Valgt Benchmark -->
                    <div class="bg-emerald-50/50 p-5 rounded-xl border border-emerald-100 flex flex-col">
                        <p class="text-sm font-semibold text-emerald-800 uppercase tracking-wider mb-2" id="bench-index-title">Valgt Benchmark (S&P 500)</p>
                        <h3 class="text-2xl font-bold text-emerald-700 mb-1" id="bench-index-return">+9.8%</h3>
                        <p class="text-xs text-emerald-600/80">Fast mock-reference</p>
                    </div>
                </div>

                <!-- Visuel Sammenligningsbar / Mock-Graf -->
                <div class="mb-6 flex flex-col gap-4">
                    <div class="w-full">
                        <div class="flex justify-between text-xs font-semibold mb-1.5">
                            <span class="text-deep-indigo">Din Portefølje</span>
                            <span class="text-deep-indigo" id="bench-bar-port-val">+4.2%</span>
                        </div>
                        <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden">
                            <div class="h-full bg-deep-indigo rounded-full transition-all duration-500" style="width: 42%;" id="bench-bar-port"></div>
                        </div>
                    </div>
                    <div class="w-full">
                        <div class="flex justify-between text-xs font-semibold mb-1.5">
                            <span class="text-emerald-700" id="bench-bar-index-title">Benchmark Indeks</span>
                            <span class="text-emerald-700" id="bench-bar-index-val">+9.8%</span>
                        </div>
                        <div class="w-full h-3 bg-slate-100 rounded-full overflow-hidden">
                            <div class="h-full bg-emerald-500 rounded-full transition-all duration-500" style="width: 98%;" id="bench-bar-index"></div>
                        </div>
                    </div>
                </div>

                <!-- Pædagogisk Rebalancerings-Feedback -->
                <div class="bg-indigo-50/50 rounded-xl p-4 border border-indigo-100 mb-6 flex gap-3 items-start">
                    <span class="material-symbols-outlined text-deep-indigo shrink-0 mt-0.5">lightbulb</span>
                    <p class="text-sm text-deep-indigo leading-relaxed">
                        <strong>CTO Læringstip:</strong> Dit benchmark er din rettesnor. Ligger din portefølje under markedsindekset, skyldes det ofte for høj satellit-risiko eller kontantandel. Overvej opadgående rebalancering mod din Core (MSCI World).
                    </p>
                </div>

                <!-- Datasikkerhed & Disclaimer i bunden af kortet -->
                <div class="mt-auto border-t border-slate-border pt-4">
                    <p class="text-xs text-on-surface-variant flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-[14px]">info</span>
                        Bemærk: Dette er et simuleret uddannelsesværktøj. Kurser og indeksdata er mockups til brug for læringsøvelsen og udgør ikke finansiel rådgivning.
                    </p>
                </div>
            </div>
            
            <script>
                document.addEventListener('DOMContentLoaded', () => {
                    const btnSp500 = document.getElementById('btn-bench-sp500');
                    const btnMsci = document.getElementById('btn-bench-msci');
                    if(btnSp500 && btnMsci) {
                        const setBenchmark = (type) => {
                            if(type === 'sp500') {
                                btnSp500.className = "px-4 py-1.5 text-sm font-semibold rounded-lg bg-white border border-slate-border text-deep-indigo shadow-sm";
                                btnMsci.className = "px-4 py-1.5 text-sm font-semibold rounded-lg text-on-surface-variant hover:text-deep-indigo transition-colors";
                                document.getElementById('bench-index-title').innerText = "Valgt Benchmark (S&P 500)";
                                document.getElementById('bench-index-return').innerText = "+9.8%";
                                document.getElementById('bench-bar-index-title').innerText = "Benchmark (S&P 500)";
                                document.getElementById('bench-bar-index-val').innerText = "+9.8%";
                                document.getElementById('bench-bar-index').style.width = "98%";
                            } else {
                                btnMsci.className = "px-4 py-1.5 text-sm font-semibold rounded-lg bg-white border border-slate-border text-deep-indigo shadow-sm";
                                btnSp500.className = "px-4 py-1.5 text-sm font-semibold rounded-lg text-on-surface-variant hover:text-deep-indigo transition-colors";
                                document.getElementById('bench-index-title').innerText = "Valgt Benchmark (MSCI World)";
                                document.getElementById('bench-index-return').innerText = "+8.2%";
                                document.getElementById('bench-bar-index-title').innerText = "Benchmark (MSCI World)";
                                document.getElementById('bench-bar-index-val').innerText = "+8.2%";
                                document.getElementById('bench-bar-index').style.width = "82%";
                            }
                        };
                        
                        btnSp500.addEventListener('click', () => setBenchmark('sp500'));
                        btnMsci.addEventListener('click', () => setBenchmark('msci'));
                    }
                });
            </script>
"""

    if filepath == 'portefoelje.html':
        # Insert before <!-- Positionstabel -->
        if '<!-- Positionstabel -->' in content and 'id="benchmark-card"' not in content:
            new_content = content.replace('<!-- Positionstabel -->', card_html + '\n            <!-- Positionstabel -->')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Could not find injection point or already injected in {filepath}")
    
    elif filepath == 'dashboard.html':
        # Insert before <!-- E. Simuleret Portefølje -> if it's there? Wait, E is inside a grid grid-cols-1 lg:grid-cols-3. 
        # Better to add it inside the grid, or just after the first top row. 
        # Actually in dashboard, there is 
        # <!-- Bento Grid Layout -->
        # <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        # Let's insert it before <!-- F. AI Assistant -> actually before <!-- E. Simuleret Portefølje -->
        # Let's see dashboard structure first
        pass

update_file('portefoelje.html')
