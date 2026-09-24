import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# Replace Bento card
old_card = """<div class="bg-white rounded-2xl border border-slate-border p-6 shadow-sm flex-1 flex flex-col">
                        <div class="flex items-center justify-between mb-4">
                            <h2 class="font-headline-md text-lg font-semibold text-deep-indigo flex items-center gap-2">
                                <span class="material-symbols-outlined text-xl">pie_chart</span>
                                Simuleret Portefølje
                            </h2>
                        </div>"""

new_card = """<div class="bg-white rounded-2xl border border-slate-border p-6 shadow-sm flex-1 flex flex-col cursor-pointer hover:shadow-md transition-shadow relative" onclick="openPortfolioQuickModal(event)">
                        <div class="flex items-center justify-between mb-4">
                            <h2 class="font-headline-md text-lg font-semibold text-deep-indigo flex items-center gap-2">
                                <span class="material-symbols-outlined text-xl">pie_chart</span>
                                Simuleret Portefølje
                            </h2>
                            <a href="portefoelje.html" class="text-xs font-bold text-deep-indigo hover:underline flex items-center gap-1 relative z-10" onclick="event.stopPropagation()">
                                Fuld Visning ↗
                            </a>
                        </div>"""

content = content.replace(old_card, new_card)

# Insert the quick modal at the end before </body>
quick_modal_html = """
    <!-- Portfolio Quick Modal -->
    <div id="portfolio-quick-modal" class="fixed inset-0 bg-on-background/40 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4" onclick="closePortfolioQuickModal()">
        <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden flex flex-col" onclick="event.stopPropagation()">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-slate-surface">
                <h3 class="font-headline-md text-xl font-semibold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined">pie_chart</span>
                    Portefølje Oversigt
                </h3>
                <button onclick="closePortfolioQuickModal()" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            
            <div class="p-6 space-y-4">
                <div class="flex justify-between items-center bg-indigo-50 p-4 rounded-xl border border-indigo-100">
                    <div>
                        <p class="text-xs text-on-surface-variant font-semibold uppercase tracking-wide">Samlet Værdi</p>
                        <p class="text-2xl font-bold text-deep-indigo" id="quick-modal-total">50.000 kr.</p>
                    </div>
                    <div class="text-right">
                        <p class="text-sm font-bold text-emerald-success">+1,8%</p>
                        <p class="text-xs text-emerald-600">+900 kr.</p>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-sm font-bold text-on-background mb-2">Dine Aktier</h4>
                    <div class="flex flex-col gap-2" id="quick-modal-holdings">
                        <!-- Dynamic holdings go here -->
                    </div>
                </div>
            </div>

            <div class="p-6 border-t border-slate-border bg-slate-surface">
                <a href="portefoelje.html" class="block w-full py-3 bg-deep-indigo text-white text-center font-semibold rounded-lg hover:opacity-90 transition-opacity">
                    Åbn Fuld Portefølje →
                </a>
            </div>
        </div>
    </div>
"""

content = content.replace('</body>', quick_modal_html + '\n</body>')

js_funcs = """
        function openPortfolioQuickModal(e) {
            if (e) e.stopPropagation();
            document.getElementById('portfolio-quick-modal').classList.remove('hidden');
            
            // Render holdings in quick modal
            const holdings = JSON.parse(localStorage.getItem('bi_portfolio_holdings') || '[]');
            const modalHoldings = document.getElementById('quick-modal-holdings');
            if (modalHoldings) {
                if (holdings.length === 0) {
                    modalHoldings.innerHTML = '<p class="text-sm text-on-surface-variant italic">Ingen aktier endnu.</p>';
                } else {
                    modalHoldings.innerHTML = holdings.map(h => `
                        <div class="flex justify-between items-center text-sm border-b border-slate-border pb-2 last:border-0 last:pb-0">
                            <span class="font-medium text-on-background">${h.name}</span>
                            <span class="font-bold text-deep-indigo">${h.value.toLocaleString('da-DK')} kr.</span>
                        </div>
                    `).join('');
                }
            }
            
            // Set total based on cash + portfolio values
            let cash = parseInt(localStorage.getItem('bi_cash_balance') || '7500');
            let invested = holdings.reduce((sum, h) => sum + h.value, 0);
            document.getElementById('quick-modal-total').textContent = (cash + invested).toLocaleString('da-DK') + ' kr.';
        }

        function closePortfolioQuickModal() {
            document.getElementById('portfolio-quick-modal').classList.add('hidden');
        }
"""

content = content.replace('// Format Currency', js_funcs + '\n        // Format Currency')

with open('dashboard.html', 'w') as f:
    f.write(content)
print("Updated dashboard.html with Quick Modal")
