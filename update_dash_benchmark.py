import re

def update_dash():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()

    card_html = """
                    <!-- Benchmark Card i Dashboard -->
                    <div id="benchmark-card" class="bg-white rounded-2xl border border-slate-border p-5 shadow-sm flex flex-col" onclick="event.stopPropagation()">
                        <div class="flex items-center justify-between mb-3">
                            <h2 class="font-headline-md text-sm font-semibold text-deep-indigo flex items-center gap-1.5">
                                📈 Benchmark
                            </h2>
                            <span class="bg-indigo-50 text-deep-indigo border border-indigo-200 text-[10px] font-semibold px-2 py-0.5 rounded-full">Simuleret</span>
                        </div>
                        
                        <div class="flex flex-col gap-3 mb-4">
                            <div class="flex justify-between items-end">
                                <div>
                                    <p class="text-[10px] font-semibold text-on-surface-variant uppercase">Din Portefølje</p>
                                    <p class="text-lg font-bold text-deep-indigo" id="dash-bench-port">+4.2%</p>
                                </div>
                                <div class="text-right">
                                    <p class="text-[10px] font-semibold text-emerald-800 uppercase" id="dash-bench-idx-name">S&P 500</p>
                                    <p class="text-lg font-bold text-emerald-700" id="dash-bench-idx">+9.8%</p>
                                </div>
                            </div>
                            
                            <div class="flex flex-col gap-2">
                                <div class="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                                    <div class="h-full bg-deep-indigo rounded-full" style="width: 42%;" id="dash-bench-bar-port"></div>
                                </div>
                                <div class="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                                    <div class="h-full bg-emerald-500 rounded-full" style="width: 98%;" id="dash-bench-bar-idx"></div>
                                </div>
                            </div>
                        </div>

                        <div class="flex gap-2 bg-slate-surface p-1 rounded-lg border border-slate-border mt-auto">
                            <button class="flex-1 py-1 text-[11px] font-semibold rounded bg-white border border-slate-border text-deep-indigo shadow-sm" id="dash-btn-sp500">S&P 500</button>
                            <button class="flex-1 py-1 text-[11px] font-semibold rounded text-on-surface-variant hover:text-deep-indigo" id="dash-btn-msci">MSCI World</button>
                        </div>
                        
                        <div class="mt-3 bg-indigo-50/50 p-2 rounded border border-indigo-100 flex items-start gap-1.5">
                            <span class="material-symbols-outlined text-deep-indigo text-[12px] mt-0.5">school</span>
                            <p class="text-[10px] text-deep-indigo leading-tight">Ligger du under markedet? Tjek satellit-risiko eller kontantandel.</p>
                        </div>
                        
                        <script>
                            document.addEventListener('DOMContentLoaded', () => {
                                const btnSp500Dash = document.getElementById('dash-btn-sp500');
                                const btnMsciDash = document.getElementById('dash-btn-msci');
                                if(btnSp500Dash && btnMsciDash) {
                                    const setDashBenchmark = (type) => {
                                        if(type === 'sp500') {
                                            btnSp500Dash.className = "flex-1 py-1 text-[11px] font-semibold rounded bg-white border border-slate-border text-deep-indigo shadow-sm";
                                            btnMsciDash.className = "flex-1 py-1 text-[11px] font-semibold rounded text-on-surface-variant hover:text-deep-indigo";
                                            document.getElementById('dash-bench-idx-name').innerText = "S&P 500";
                                            document.getElementById('dash-bench-idx').innerText = "+9.8%";
                                            document.getElementById('dash-bench-bar-idx').style.width = "98%";
                                        } else {
                                            btnMsciDash.className = "flex-1 py-1 text-[11px] font-semibold rounded bg-white border border-slate-border text-deep-indigo shadow-sm";
                                            btnSp500Dash.className = "flex-1 py-1 text-[11px] font-semibold rounded text-on-surface-variant hover:text-deep-indigo";
                                            document.getElementById('dash-bench-idx-name').innerText = "MSCI World";
                                            document.getElementById('dash-bench-idx').innerText = "+8.2%";
                                            document.getElementById('dash-bench-bar-idx').style.width = "82%";
                                        }
                                    };
                                    btnSp500Dash.addEventListener('click', (e) => { e.stopPropagation(); setDashBenchmark('sp500'); });
                                    btnMsciDash.addEventListener('click', (e) => { e.stopPropagation(); setDashBenchmark('msci'); });
                                }
                            });
                        </script>
                    </div>
"""
    
    # We will inject this into `dashboard.html` right after the Portfolio list block.
    # Look for: <div class="flex-grow flex flex-col gap-3" id="portfolio-holdings-list">
    # And its closing tags: </div> </div>
    # In `dashboard.html`:
    # 255: <div class="flex-grow flex flex-col gap-3" id="portfolio-holdings-list">
    # 256:     <!-- Dynamic content from bi_portfolio_holdings -->
    # 257: </div>
    # 258: </div>
    # We will replace that 258 `</div>` with `</div>\n` + card_html
    
    parts = content.split('id="portfolio-holdings-list">')
    if len(parts) == 2:
        subparts = parts[1].split('</div>\n                    </div>\n', 1)
        if len(subparts) == 2:
            new_content = parts[0] + 'id="portfolio-holdings-list">' + subparts[0] + '</div>\n                    </div>\n' + card_html + subparts[1]
            with open('dashboard.html', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Dashboard updated!")
        else:
            print("Could not find the closing div of the portfolio card.")
    else:
        print("Could not find portfolio-holdings-list in dashboard.")

update_dash()
