import os

files = [
    'dashboard.html',
    'analyse.html',
    'laer.html',
    'markeder.html',
    'vaerktoejer.html',
    'portefoelje.html'
]

script_tag = '    <script src="ai-assistant.js"></script>\n'

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'ai-assistant.js' not in content:
            # Find the last occurrence of </body>
            idx = content.rfind('</body>')
            if idx != -1:
                new_content = content[:idx] + script_tag + content[idx:]
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Injected into {filename}')
            else:
                print(f'</body> not found in {filename}')
        else:
            print(f'ai-assistant.js already in {filename}')
    else:
        print(f'{filename} not found')

print("Done.")
