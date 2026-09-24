import re

with open('markeder.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add header column
html = html.replace('<th class="p-4 md:p-6 font-semibold text-right">P/E (Prissætning)</th>',
                    '<th class="p-4 md:p-6 font-semibold text-right">P/E (Prissætning)</th>\n                                    <th class="p-4 md:p-6 font-semibold text-center">Handling</th>')

# Add button to Novo Nordisk
novo_td = '''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">38.4</span>
                                        <div class="text-xs text-on-surface-variant">Høj (Vækst)</div>
                                    </td>
                                    <td class="p-4 md:p-6 text-center">
                                        <button onclick="simulerKoeb('Novo Nordisk B', 'novo')" class="bg-deep-indigo text-white px-3 py-1.5 rounded-lg text-xs font-semibold hover:opacity-90 transition-opacity">Simulér Køb</button>
                                    </td>'''
html = html.replace('''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">38.4</span>
                                        <div class="text-xs text-on-surface-variant">Høj (Vækst)</div>
                                    </td>''', novo_td)

# Add button to Volvo Car
volvo_td = '''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">6.2</span>
                                        <div class="text-xs text-on-surface-variant">Lav (Cyklisk)</div>
                                    </td>
                                    <td class="p-4 md:p-6 text-center">
                                        <button onclick="simulerKoeb('Volvo Car AB', 'volvo')" class="bg-deep-indigo text-white px-3 py-1.5 rounded-lg text-xs font-semibold hover:opacity-90 transition-opacity">Simulér Køb</button>
                                    </td>'''
html = html.replace('''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">6.2</span>
                                        <div class="text-xs text-on-surface-variant">Lav (Cyklisk)</div>
                                    </td>''', volvo_td)

# Add button to ASML
asml_td = '''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">45.1</span>
                                        <div class="text-xs text-on-surface-variant">Meget Høj</div>
                                    </td>
                                    <td class="p-4 md:p-6 text-center">
                                        <button onclick="simulerKoeb('ASML Holding', 'asml')" class="bg-deep-indigo text-white px-3 py-1.5 rounded-lg text-xs font-semibold hover:opacity-90 transition-opacity">Simulér Køb</button>
                                    </td>'''
html = html.replace('''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">45.1</span>
                                        <div class="text-xs text-on-surface-variant">Meget Høj</div>
                                    </td>''', asml_td)

# Add button to Microsoft
ms_td = '''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">35.8</span>
                                        <div class="text-xs text-on-surface-variant">Høj</div>
                                    </td>
                                    <td class="p-4 md:p-6 text-center">
                                        <button onclick="simulerKoeb('Microsoft Corp.', 'msft')" class="bg-deep-indigo text-white px-3 py-1.5 rounded-lg text-xs font-semibold hover:opacity-90 transition-opacity">Simulér Køb</button>
                                    </td>'''
html = html.replace('''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">35.8</span>
                                        <div class="text-xs text-on-surface-variant">Høj</div>
                                    </td>''', ms_td)

# Add button to DSV
dsv_td = '''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">18.4</span>
                                        <div class="text-xs text-on-surface-variant">Middel</div>
                                    </td>
                                    <td class="p-4 md:p-6 text-center">
                                        <button onclick="simulerKoeb('DSV A/S', 'dsv')" class="bg-deep-indigo text-white px-3 py-1.5 rounded-lg text-xs font-semibold hover:opacity-90 transition-opacity">Simulér Køb</button>
                                    </td>'''
html = html.replace('''                                    <td class="p-4 md:p-6 text-right">
                                        <span class="text-sm font-medium">18.4</span>
                                        <div class="text-xs text-on-surface-variant">Middel</div>
                                    </td>''', dsv_td)


# Add the script to handle simulerKoeb
script = '''
    <script>
        function simulerKoeb(navn, id) {
            // Sæt karantæne i localStorage
            const now = new Date().getTime();
            const quarantineEnd = now + (48 * 60 * 60 * 1000); // 48 timer frem
            
            let orders = JSON.parse(localStorage.getItem('bi_pending_orders') || '[]');
            orders.push({
                assetName: navn,
                assetId: id,
                timestamp: now,
                quarantineEnd: quarantineEnd
            });
            localStorage.setItem('bi_pending_orders', JSON.stringify(orders));
            
            // Vis toast
            const toast = document.getElementById('toast-banner');
            toast.querySelector('#toast-msg').textContent = `Købsordre på ${navn} er sendt til 48-timers karantæne.`;
            toast.classList.remove('translate-y-full', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-full', 'opacity-0');
            }, 3500);
        }
    </script>

    <!-- Custom Toast Banner -->
    <div id="toast-banner" class="fixed bottom-6 left-1/2 -translate-x-1/2 transform translate-y-full opacity-0 transition-all duration-300 z-50 flex items-center gap-3 bg-white border border-slate-border shadow-lg rounded-xl px-5 py-3">
        <div class="w-8 h-8 rounded-full bg-amber-500/10 flex items-center justify-center shrink-0">
            <span class="material-symbols-outlined text-amber-600 text-sm font-bold">hourglass_empty</span>
        </div>
        <p id="toast-msg" class="text-sm font-medium text-on-background">Købsordre er sendt til karantæne.</p>
    </div>
</body>'''

html = html.replace('</body>', script)

with open('markeder.html', 'w', encoding='utf-8') as f:
    f.write(html)
