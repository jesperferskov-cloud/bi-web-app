import os
import glob
import re

files_to_check = glob.glob('*.html')

# We'll use specific exact replacements to maintain capitalization
replacements = [
    (r'Skåret i pap', 'I praksis'),
    (r'skåret i pap', 'i praksis'),
    (r'Skåret ud i pap', 'I praksis'),
    (r'skåret ud i pap', 'i praksis'),
    (r'Pædagogisk', 'Metodisk'),
    (r'pædagogisk', 'struktureret'),
    (r'Børnehøjde', 'Overblik'),
    (r'børnehøjde', 'overblik'),
    (r'Ind til benet', 'Kernefaktorer'),
    (r'ind til benet', 'kernefaktorer'),
    (r'Øve-penge', 'Simuleret startkapital'),
    (r'øve-penge', 'simuleret startkapital'),
    (r'Øvepenge', 'Simuleret startkapital'),
    (r'øvepenge', 'simuleret startkapital'),
    (r'Øve-kapital', 'Simuleret startkapital'),
    (r'øve-kapital', 'simuleret startkapital'),
    (r'Øve-portefølje', 'Simuleret portefølje'),
    (r'øve-portefølje', 'simuleret portefølje'),
    (r'Fiktivt Øve-Miljø', 'Simuleringsmiljø'),
    (r'Legetøjspenge', 'Fiktiv porteføljesaldo'),
    (r'legetøjspenge', 'fiktiv porteføljesaldo'),
    (r'drukne i tal', 'fokusere på de nøgletal, der driver reel værdiskabelse'),
    (r'drukne i grafer', 'fokusere på de nøgletal, der driver reel værdiskabelse'),
    (r'uden at drukne i tal/grafer', 'med fokus på de nøgletal, der driver reel værdiskabelse'),
]

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
