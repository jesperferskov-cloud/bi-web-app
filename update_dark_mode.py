import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Body background and text (Main Canvas)
    # Original body classes: dark:bg-dark-canvas dark:text-dark-text
    content = re.sub(r'dark:bg-dark-canvas', r'dark:bg-[#161922]', content)
    
    # 2. Sidebar background and border
    # <aside class="... dark:border-dark-border"> -> add dark:bg-[#11141c] dark:border-[#1e2433]
    # Remove existing dark:bg-* and dark:border-* on <aside>
    def aside_repl(m):
        cls = m.group(1)
        cls = re.sub(r'dark:bg-\S+', '', cls)
        cls = re.sub(r'dark:border-\S+', '', cls)
        cls = cls.strip() + ' dark:bg-[#11141c] dark:border-[#1e2433]'
        return f'<aside class="{cls}">'
    content = re.sub(r'<aside class="([^"]*)">', aside_repl, content)

    # 3. Active menu item (Dashboard / active link)
    # The active one usually has `bg-indigo-900/60 text-white`
    def active_menu_repl(m):
        cls = m.group(1)
        # Ensure it has the dark active classes
        cls = re.sub(r'dark:bg-\S+', '', cls)
        cls = re.sub(r'dark:text-\S+', '', cls)
        cls = cls.strip() + ' dark:bg-[#1e2433] dark:text-white font-semibold'
        return f'<a href="{m.group(0).split("\"")[1]}" class="{cls}">'
    # Wait, the active link does not have `dark:bg-dark-card` usually, let's just do a generic replacement for menu links
    
    # 4. Bento-cards & Main Panels
    # Replace dark:bg-dark-card with dark:bg-[#1e2330]
    content = re.sub(r'dark:bg-dark-card', r'dark:bg-[#1e2330]', content)
    # Replace dark:border-dark-border (where used on cards) with dark:border-[#2b3245]
    content = re.sub(r'dark:border-dark-border', r'dark:border-[#2b3245]', content)
    
    # 5. Embedded Boxes (dark-elevated)
    # Replace dark:bg-dark-elevated with dark:bg-[#252b3b] dark:border-[#323b52]
    # We might need to handle this carefully if borders aren't currently there.
    
    # Let's do this step by step. I will write a simple test script to see the matches first.
    pass

