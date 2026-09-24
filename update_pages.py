import re

# Read dashboard.html to get the sidebar shell
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dash_html = f.read()

# Extract the <head>
head_match = re.search(r'<head>.*?</head>', dash_html, re.DOTALL)
dash_head = head_match.group(0) if head_match else ''

# Extract the <aside>
aside_match = re.search(r'<aside.*?</aside>', dash_html, re.DOTALL)
dash_aside = aside_match.group(0) if aside_match else ''

# Clean up sidebar active states for a given page
def get_sidebar_for_page(aside_html, active_page):
    # reset active state on Dashboard
    aside_html = aside_html.replace('bg-indigo-500/30 text-white font-medium border border-indigo-400/30', 'text-indigo-200 hover:bg-white/10 hover:text-white')
    
    # set active state on target
    if active_page == 'markeder':
        aside_html = aside_html.replace('href="markeder.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-indigo-200 hover:bg-white/10 hover:text-white transition-colors', 'href="markeder.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-indigo-500/30 text-white font-medium border border-indigo-400/30 transition-colors')
    elif active_page == 'vaerktoejer':
        aside_html = aside_html.replace('href="vaerktoejer.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-indigo-200 hover:bg-white/10 hover:text-white transition-colors', 'href="vaerktoejer.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-indigo-500/30 text-white font-medium border border-indigo-400/30 transition-colors')
    return aside_html

def update_page(filename, active_page):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract main content
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    main_content = main_match.group(1) if main_match else ''
    
    # Update tailwind config in head to include both dashboard and markeder themes if needed, but dashboard head is fine.
    # Actually, we should merge the tailwind configs so it looks right.
    # Let's just use the dashboard head but add the extra tailwind classes from markeder.html
    tw_config_match = re.search(r'<script>\s*tailwind\.config = (.*?)\s*</script>', html, re.DOTALL)
    if tw_config_match:
        tw_script = f'<script>\n        tailwind.config = {tw_config_match.group(1)}\n    </script>'
        new_head = dash_head.replace(re.search(r'<script>\s*tailwind\.config = (.*?)\s*</script>', dash_head, re.DOTALL).group(0), tw_script)
    else:
        new_head = dash_head
        
    style_match = re.search(r'<style type="text/tailwindcss">.*?</style>', html, re.DOTALL)
    if style_match:
        new_head = new_head.replace('</head>', style_match.group(0) + '\n</head>')
    
    # Build new html
    sidebar = get_sidebar_for_page(dash_aside, active_page)
    
    # We need to preserve scripts at the end of the body if any
    script_match = re.search(r'</main>\s*(<script>.*?</script>)?\s*</body>', html, re.DOTALL)
    scripts = script_match.group(1) if script_match and script_match.group(1) else ''

    new_html = f'''<!DOCTYPE html>
<html class="light" lang="da">
{new_head}
<body class="flex h-screen font-body-md text-base overflow-hidden bg-background">
    {sidebar}
    <main class="flex-1 overflow-y-auto bg-slate-surface flex flex-col relative">
        <div class="p-4 md:p-8 max-w-[1400px] w-full mx-auto flex flex-col gap-6">
            {main_content}
        </div>
    </main>
    {scripts}
</body>
</html>'''

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)

update_page('markeder.html', 'markeder')
update_page('vaerktoejer.html', 'vaerktoejer')

