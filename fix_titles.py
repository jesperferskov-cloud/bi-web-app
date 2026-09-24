with open('markeder.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('<title>Begynder Investor - Dashboard</title>', '<title>Begynder Investor - Markeder</title>')
with open('markeder.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('vaerktoejer.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('<title>Begynder Investor - Dashboard</title>', '<title>Begynder Investor - Værktøjer</title>')
with open('vaerktoejer.html', 'w', encoding='utf-8') as f:
    f.write(text)
