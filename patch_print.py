import re

with open('vaerktoejer.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Card 1
content = content.replace(
    '''<div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">checklist</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Den Store Aktie-Tjekliste</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Gennemgå de 10 vigtigste punkter før du investerer i en ny aktie.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>''',
    '''<div onclick="openPreviewModal('tjekliste')" class="cursor-pointer hover:border-indigo-300 dark:hover:border-slate-500/50 bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245] transition-all">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">checklist</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Den Store Aktie-Tjekliste</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Gennemgå de 10 vigtigste punkter før du investerer i en ny aktie.</p>
                        <a href="assets/guides/aktie-tjekliste.pdf" download="Den_Store_Aktie_Tjekliste.pdf" onclick="event.stopPropagation()" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </a>
                    </div>'''
)

# Replace Card 2
content = content.replace(
    '''<div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">pie_chart</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Portefølje-Skabelon</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Design din Core/Satellite struktur og hold styr på din spredning.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>''',
    '''<div onclick="openPreviewModal('portefolje')" class="cursor-pointer hover:border-indigo-300 dark:hover:border-slate-500/50 bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245] transition-all">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">pie_chart</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Portefølje-Skabelon</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Design din Core/Satellite struktur og hold styr på din spredning.</p>
                        <a href="assets/guides/portefolje-skabelon.pdf" download="Portefolje_Skabelon_80_20.pdf" onclick="event.stopPropagation()" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </a>
                    </div>'''
)

# Replace Card 3
content = content.replace(
    '''<div class="bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245]">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">functions</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Nøgletal i Praksis (P/E, Moat & ROIC)</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Hurtig guide til tolkning af markedets vigtigste nøgletal og værdiansættelse.</p>
                        <button class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </button>
                    </div>''',
    '''<div onclick="openPreviewModal('noegletal')" class="cursor-pointer hover:border-indigo-300 dark:hover:border-slate-500/50 bg-white border border-slate-border rounded-xl p-6 shadow-sm flex flex-col h-full dark:bg-[#1e2330] dark:border-[#2b3245] transition-all">
                        <div class="flex items-center justify-center w-12 h-12 rounded-lg bg-indigo-50 text-deep-indigo mb-4 dark:bg-indigo-900/30 dark:text-[#c3c0ff]">
                            <span class="material-symbols-outlined text-2xl">functions</span>
                        </div>
                        <h4 class="font-semibold text-xl mb-2 text-deep-indigo dark:text-white">Nøgletal i Praksis (P/E, Moat & ROIC)</h4>
                        <p class="text-sm text-on-surface-variant dark:text-[#94a3b8] flex-1 mb-4">Hurtig guide til tolkning af markedets vigtigste nøgletal og værdiansættelse.</p>
                        <a href="assets/guides/noegletal-i-praksis.pdf" download="Noegletal_i_Praksis_PE_Moat.pdf" onclick="event.stopPropagation()" class="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 dark:bg-[#252b3b] dark:hover:bg-[#2a3245] dark:text-slate-300 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined text-sm">download</span> Download PDF
                        </a>
                    </div>'''
)

modal_html = '''
    <!-- Guide Preview Modal -->
    <div id="guide-preview-modal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4 sm:p-6">
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm transition-opacity" onclick="closePreviewModal()"></div>
        <div class="relative w-full max-w-4xl bg-white dark:bg-[#1e2330] rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
            <div class="flex items-center justify-between p-4 border-b border-slate-border dark:border-[#2b3245] no-print">
                <h3 class="font-semibold text-lg text-deep-indigo dark:text-white flex items-center gap-2" id="preview-modal-title">
                    <span class="material-symbols-outlined">visibility</span> Forhåndsvisning
                </h3>
                <div class="flex gap-2">
                    <button onclick="window.print()" class="bg-indigo-50 text-indigo-700 hover:bg-indigo-100 dark:bg-indigo-900/30 dark:text-indigo-300 dark:hover:bg-indigo-900/50 font-medium text-sm px-4 py-2 rounded-lg transition-colors flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">print</span> Udskriv / Gem som PDF
                    </button>
                    <button onclick="closePreviewModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors p-1">
                        <span class="material-symbols-outlined">close</span>
                    </button>
                </div>
            </div>
            <div class="p-6 md:p-10 overflow-y-auto flex-1 bg-slate-50 dark:bg-[#161922] print-area" id="preview-modal-content">
                <!-- Dynamic Content -->
            </div>
        </div>
    </div>

    <style>
        @media print {
            body * {
                visibility: hidden;
            }
            #guide-preview-modal, #guide-preview-modal * {
                visibility: visible;
            }
            .no-print {
                display: none !important;
            }
            #guide-preview-modal {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background: white !important;
            }
            #preview-modal-content {
                background: white !important;
                color: black !important;
                padding: 0 !important;
            }
        }
    </style>

    <script>
        function openPreviewModal(type) {
            const modal = document.getElementById('guide-preview-modal');
            const title = document.getElementById('preview-modal-title');
            const content = document.getElementById('preview-modal-content');
            
            if(type === 'tjekliste') {
                title.innerHTML = '<span class="material-symbols-outlined">visibility</span> Den Store Aktie-Tjekliste';
                content.innerHTML = `
                    <div class="max-w-2xl mx-auto bg-white p-8 rounded border border-slate-200 shadow-sm text-slate-900">
                        <h1 class="text-2xl font-bold text-deep-indigo mb-4 border-b pb-2">Den Store Aktie-Tjekliste</h1>
                        <p class="mb-4 italic text-sm">Udfyld denne tjekliste før du eksekverer en handel, for at sikre metodisk disciplin.</p>
                        <ul class="space-y-4">
                            <li class="flex items-start gap-3"><input type="checkbox" class="mt-1 w-4 h-4"> <span><strong>Forretningsmodel:</strong> Forstår jeg præcis hvordan selskabet tjener penge?</span></li>
                            <li class="flex items-start gap-3"><input type="checkbox" class="mt-1 w-4 h-4"> <span><strong>Moat:</strong> Har selskabet en varig konkurrencefordel?</span></li>
                            <li class="flex items-start gap-3"><input type="checkbox" class="mt-1 w-4 h-4"> <span><strong>Gæld:</strong> Er gælden (Net Debt / EBITDA) på et bæredygtigt niveau?</span></li>
                            <li class="flex items-start gap-3"><input type="checkbox" class="mt-1 w-4 h-4"> <span><strong>Vækst:</strong> Er der en realistisk katalysator for fremtidig vækst?</span></li>
                            <li class="flex items-start gap-3"><input type="checkbox" class="mt-1 w-4 h-4"> <span><strong>Værdiansættelse:</strong> Er P/E-tallet rimeligt sammenlignet med sektoren?</span></li>
                        </ul>
                    </div>
                `;
            } else if(type === 'portefolje') {
                title.innerHTML = '<span class="material-symbols-outlined">visibility</span> Portefølje-Skabelon';
                content.innerHTML = `
                    <div class="max-w-2xl mx-auto bg-white p-8 rounded border border-slate-200 shadow-sm text-slate-900">
                        <h1 class="text-2xl font-bold text-deep-indigo mb-4 border-b pb-2">Portefølje-Skabelon (80/20 Core-Satellite)</h1>
                        <div class="space-y-6">
                            <div>
                                <h3 class="font-bold text-lg mb-2">80% Core (Kernen)</h3>
                                <p class="text-sm mb-2">Brede, passive ETF'er med lav ÅOP, der sikrer langsigtet markedsafkast og stabilitet.</p>
                                <div class="h-24 border-2 border-dashed border-slate-300 rounded bg-slate-50 flex items-center justify-center text-slate-400">Noter dine udvalgte fonde her...</div>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg mb-2">20% Satellite (Satellitter)</h3>
                                <p class="text-sm mb-2">Enkeltaktier eller sektor-specifikke fonde med højere risiko/afkast potentiale.</p>
                                <div class="h-24 border-2 border-dashed border-slate-300 rounded bg-slate-50 flex items-center justify-center text-slate-400">Noter dine udvalgte aktier her...</div>
                            </div>
                        </div>
                    </div>
                `;
            } else if(type === 'noegletal') {
                title.innerHTML = '<span class="material-symbols-outlined">visibility</span> Nøgletal i Praksis';
                content.innerHTML = `
                    <div class="max-w-2xl mx-auto bg-white p-8 rounded border border-slate-200 shadow-sm text-slate-900">
                        <h1 class="text-2xl font-bold text-deep-indigo mb-4 border-b pb-2">Nøgletal i Praksis</h1>
                        <table class="w-full text-left text-sm">
                            <thead class="bg-slate-100 font-bold border-b">
                                <tr>
                                    <th class="p-3">Nøgletal</th>
                                    <th class="p-3">Hvad det betyder</th>
                                    <th class="p-3">Tommelfingerregel</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100">
                                <tr>
                                    <td class="p-3 font-semibold">P/E (Price/Earnings)</td>
                                    <td class="p-3">Prisen for 1 krones overskud.</td>
                                    <td class="p-3">Sammenlign altid med konkurrenter og branchens gennemsnit.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-semibold">ROIC</td>
                                    <td class="p-3">Afkast på den investerede kapital. Måler ledelsens effektivitet.</td>
                                    <td class="p-3">Helst over 10-12% konsistent.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-semibold">EBIT-margin</td>
                                    <td class="p-3">Overskudsgraden på selve driften.</td>
                                    <td class="p-3">Høj margin indikerer ofte "pricing power" (Moat).</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                `;
            }
            
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }

        function closePreviewModal() {
            const modal = document.getElementById('guide-preview-modal');
            modal.classList.add('hidden');
            document.body.style.overflow = '';
        }
    </script>
'''

# Insert the modal html before </body>
if '</body>' in content:
    content = content.replace('</body>', modal_html + '\n</body>')

with open('vaerktoejer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied to vaerktoejer.html")
