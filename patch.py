import re

with open('analyse.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = """                <div class="w-full max-w-2xl mx-auto md:mx-0 flex flex-col gap-3">
                    <div class="relative">
                        <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
                        <input type="text" placeholder="Find en aktie at analysere (f.eks. Apple eller Novo Nordisk)" class="w-full pl-12 pr-4 py-3 rounded-xl border border-slate-border bg-white shadow-sm focus:border-deep-indigo focus:ring-deep-indigo text-sm font-medium">
                    </div>
                    <div class="flex flex-wrap gap-2">"""

new_str = """                <div class="w-full max-w-3xl mx-auto md:mx-0 flex flex-col gap-3">
                    <div class="flex gap-2">
                        <div class="relative flex-1">
                            <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
                            <input type="text" placeholder="Find en aktie at analysere (f.eks. Apple eller Novo Nordisk)" class="w-full pl-12 pr-4 py-3 rounded-xl border border-slate-border bg-white shadow-sm focus:border-deep-indigo focus:ring-deep-indigo text-sm font-medium">
                        </div>
                        <button onclick="resetAnalysis()" class="flex items-center gap-2 px-4 py-3 bg-white border border-slate-border rounded-xl text-on-surface-variant hover:text-deep-indigo hover:border-deep-indigo transition-colors text-sm font-semibold shadow-sm shrink-0">
                            <span class="material-symbols-outlined text-[18px]">add</span> Ny Analyse
                        </button>
                    </div>
                    <div class="flex flex-wrap gap-2">"""

if old_str in content:
    content = content.replace(old_str, new_str)
    with open('analyse.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("analyse.html patched successfully.")
else:
    print("Could not find the target string in analyse.html.")
