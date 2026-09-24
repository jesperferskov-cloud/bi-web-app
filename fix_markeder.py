import re

with open('markeder.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Grid Layout
# Replace <div class="grid grid-cols-1 lg:grid-cols-3 gap-8"> with <div class="flex flex-col lg:flex-row gap-8">
html = html.replace('<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">', '<div class="flex flex-col lg:flex-row gap-8">')

# Left Col: <div class="lg:col-span-2 space-y-6"> -> <div class="flex-1 space-y-6 min-w-0">
html = html.replace('<div class="lg:col-span-2 space-y-6">', '<div class="flex-1 space-y-6 min-w-0">')

# Right Col: <div class="lg:col-span-1 space-y-6"> -> <div class="w-full lg:w-80 flex flex-col gap-6 flex-shrink-0">
html = html.replace('<div class="lg:col-span-1 space-y-6">', '<div class="w-full lg:w-80 flex flex-col gap-6 flex-shrink-0">')

# 2. Update Table
# Remove overflow-x-auto class from table wrapper
html = html.replace('<div class="overflow-x-auto">', '<div class="overflow-x-auto sm:overflow-visible">')

# Add table-fixed and column widths
thead_old = '''<table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-border bg-surface-container-low text-label-xs font-bold text-on-surface-variant uppercase tracking-wider">
                                    <th class="p-4 md:p-6 font-semibold">Aktie</th>
                                    <th class="p-4 md:p-6 font-semibold hidden sm:table-cell">Sektor</th>
                                    <th class="p-4 md:p-6 font-semibold">Kurs (Valuta)</th>
                                    <th class="p-4 md:p-6 font-semibold">Dagsændring</th>
                                    <th class="p-4 md:p-6 font-semibold text-right">P/E (Prissætning)</th>
                                    <th class="p-4 md:p-6 font-semibold text-center">Handling</th>
                                </tr>
                            </thead>'''

thead_new = '''<table class="w-full table-fixed text-left border-collapse">
                            <thead>
                                <tr class="border-b border-slate-border bg-surface-container-low text-[10px] font-bold text-on-surface-variant uppercase tracking-wider">
                                    <th class="p-3 md:p-4 font-semibold w-[35%]">Aktie</th>
                                    <th class="p-3 md:p-4 font-semibold w-[20%] hidden sm:table-cell">Sektor</th>
                                    <th class="p-3 md:p-4 font-semibold w-[15%]">Kurs</th>
                                    <th class="p-3 md:p-4 font-semibold w-[15%]">Dagsændring</th>
                                    <th class="p-3 md:p-4 font-semibold text-center w-[15%]">Handling</th>
                                </tr>
                            </thead>'''
html = html.replace(thead_old, thead_new)

# Remove P/E column from tbody
pe_td_pattern = r'<td class="p-4 md:p-6 text-right">\s*<span class="text-sm font-medium">.*?</span>\s*<div class="text-xs text-on-surface-variant">.*?</div>\s*</td>'
html = re.sub(pe_td_pattern, '', html)

# Change remaining td padding from p-4 md:p-6 to p-3 md:p-4 for better fit in table-fixed
html = html.replace('<td class="p-4 md:p-6">', '<td class="p-3 md:p-4">')
html = html.replace('<td class="p-4 md:p-6 text-sm text-on-surface-variant hidden sm:table-cell">', '<td class="p-3 md:p-4 text-xs md:text-sm text-on-surface-variant hidden sm:table-cell truncate">')
html = html.replace('<td class="p-4 md:p-6 font-metric">', '<td class="p-3 md:p-4 text-xs md:text-sm font-metric truncate">')
html = html.replace('<td class="p-4 md:p-6 text-center">', '<td class="p-3 md:p-4 text-center">')

# 3. Update 'Dagens Overblik' and 'Ordbogen'
right_col_old_pattern = r'<!-- Hvad skal du kigge efter i dag\? -->.*?<!-- Ordbogs-widget -->'
right_col_new_partial = '''<!-- Hvad skal du kigge efter i dag? -->
                <div class="border border-slate-border bg-white rounded-2xl p-5">
                    <div class="flex items-center gap-2 mb-4 text-deep-indigo">
                        <span class="material-symbols-outlined text-lg">lightbulb</span>
                        <h3 class="font-bold text-xs uppercase tracking-wider">Dagens Overblik</h3>
                    </div>
                    <p class="text-on-surface-variant text-xs leading-relaxed">
                        Markedet er præget af regnskabssæsonen i USA. Store tech-selskaber har leveret pæne tal, hvilket løfter humøret. Herhjemme er der stille og roligt. Hold øje med dine mere risikable vækstaktier – de kan svinge lidt ekstra i dag.
                    </p>
                </div>

                <!-- Ordbogs-widget -->'''
html = re.sub(right_col_old_pattern, right_col_new_partial, html, flags=re.DOTALL)

ordbogen_old = '''<div class="bento-card">
                    <div class="flex items-center gap-2 text-primary border-b border-slate-border pb-4 mb-4">
                        <span class="material-symbols-outlined">menu_book</span>
                        <h3 class="font-headline font-semibold text-lg">Ordbogen</h3>
                    </div>
                    
                    <div class="space-y-4">
                        <div>
                            <h4 class="font-semibold text-on-surface mb-1">Volatilitet</h4>
                            <p class="text-sm text-on-surface-variant">
                                Et udtryk for, hvor meget kursen på en aktie svinger op og ned. Høj volatilitet = store udsving (større risiko, men også chance for større afkast på kort sigt).
                            </p>
                        </div>
                        <div>
                            <h4 class="font-semibold text-on-surface mb-1">Moat (Voldgrav)</h4>
                            <p class="text-sm text-on-surface-variant">
                                En virksomheds konkurrencefordel, som gør det svært for andre at stjæle deres kunder. Novo Nordisk har f.eks. en stærk 'moat' pga. deres patenter.
                            </p>
                        </div>
                    </div>
                </div>'''
ordbogen_new = '''<div class="border border-slate-border bg-white rounded-2xl p-5">
                    <div class="flex items-center gap-2 text-deep-indigo border-b border-slate-border pb-4 mb-4">
                        <span class="material-symbols-outlined text-lg">menu_book</span>
                        <h3 class="font-bold text-xs uppercase tracking-wider">Ordbogen</h3>
                    </div>
                    
                    <div class="space-y-4">
                        <div>
                            <h4 class="font-bold text-on-background text-xs mb-1">Volatilitet</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">
                                Et udtryk for, hvor meget kursen på en aktie svinger op og ned. Høj volatilitet = store udsving (større risiko, men også chance for større afkast på kort sigt).
                            </p>
                        </div>
                        <div>
                            <h4 class="font-bold text-on-background text-xs mb-1">Moat (Voldgrav)</h4>
                            <p class="text-xs text-on-surface-variant leading-relaxed">
                                En virksomheds konkurrencefordel, som gør det svært for andre at stjæle deres kunder. Novo Nordisk har f.eks. en stærk 'moat' pga. deres patenter.
                            </p>
                        </div>
                    </div>
                </div>'''
html = html.replace(ordbogen_old, ordbogen_new)

with open('markeder.html', 'w', encoding='utf-8') as f:
    f.write(html)
