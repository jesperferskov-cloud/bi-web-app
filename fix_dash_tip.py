with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = '<p class="text-[10px] text-deep-indigo leading-tight">Ligger du under markedet? Tjek satellit-risiko eller kontantandel.</p>'
new_text = '<p class="text-[10px] text-deep-indigo leading-tight"><strong>💡 CTO Læringstip:</strong> Dit benchmark er din rettesnor. Ligger din portefølje under markedsindekset, skyldes det ofte for høj satellit-risiko eller kontantandel. Overvej opadgående rebalancering mod din Core (MSCI World).</p>'

content = content.replace(old_text, new_text)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

