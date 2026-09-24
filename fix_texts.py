import os
import glob
import re

files_to_check = ['dashboard.html', 'laer.html'] + glob.glob('modul*.html')

replacements = [
    (r'(?i)P/E[\s\-]*tallet skåret i pap', 'Forstå P/E-tallet i praksis'),
    (r'(?i)Skåret i pap', 'Nøgleindsigt'),
    (r'(?i)Skåret ud i pap', 'Nøgleindsigt'),
    (r'(?i)Skåret ind til benet', 'Kerneanalyse'),
    (r'(?i)Konceptet\s*\(Teori i øjenhøjde\)', 'Konceptuel Forståelse'),
    (r'(?i)Teori i øjenhøjde', 'Metodisk Fundament'),
    (r'(?i)vi skærer det i pap', 'vi forklarer det klart og direkte'),
    (r'(?i)forklarer det til børn', 'forklarer det klart og pædagogisk')
]

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes in {filepath}")

