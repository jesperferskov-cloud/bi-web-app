import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
regex = re.compile(r'document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*const userName = localStorage\.getItem\(\'bi_user_name\'\).*?\}\);', re.DOTALL)

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove the specific old listener if it has 'Alex' or similar.
    # Actually, the python script above injected a NEW block that looks exactly like this.
    # So we should be careful not to delete the NEW block!
    pass

