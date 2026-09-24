import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the explore-modal HTML
old_modal_start = '<!-- Explore Modal -->'
old_modal_end = '<!-- Footer -->'
modal_regex = re.compile(f'{old_modal_start}.*?(?={old_modal_end})', re.DOTALL)

new_modal_html = """<!-- Explore Modal -->
    <div id="explore-modal" class="fixed inset-0 bg-on-background/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4 transition-opacity duration-300 opacity-0" onclick="closeExploreModal()">
        <div class="bg-slate-surface rounded-2xl shadow-xl w-full max-w-lg overflow-hidden flex flex-col transform transition-transform duration-300 scale-95" id="explore-modal-inner" onclick="event.stopPropagation()">
            <div class="p-6 border-b border-slate-border flex justify-between items-center bg-white">
                <h3 class="font-headline-md text-xl font-bold text-deep-indigo flex items-center gap-2">
                    <span class="material-symbols-outlined">rocket_launch</span>
                    Smagsprøve på Universet
                </h3>
                <button onclick="closeExploreModal()" class="text-on-surface-variant hover:text-deep-indigo transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            
            <div class="p-6 md:p-8 relative min-h-[250px]">
                <!-- Step 1 -->
                <div id="explore-step-1" class="explore-step absolute inset-0 p-6 md:p-8 flex flex-col items-center text-center transition-opacity duration-300">
                    <div class="w-16 h-16 rounded-full bg-indigo-50 flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-deep-indigo text-3xl">school</span>
                    </div>
                    <h4 class="font-bold text-on-background text-lg mb-3">1. Læring uden støj</h4>
                    <p class="text-sm text-on-surface-variant leading-relaxed">
                        Følg 4 modulære læringsspor inklusiv hands-on skatteguides og praktisk viden.
                    </p>
                </div>
                <!-- Step 2 -->
                <div id="explore-step-2" class="explore-step absolute inset-0 p-6 md:p-8 flex flex-col items-center text-center transition-opacity duration-300 opacity-0 pointer-events-none">
                    <div class="w-16 h-16 rounded-full bg-emerald-50 flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-emerald-success text-3xl">pie_chart</span>
                    </div>
                    <h4 class="font-bold text-on-background text-lg mb-3">2. Simuleret Portefølje</h4>
                    <p class="text-sm text-on-surface-variant leading-relaxed">
                        Start med 50.000 fiktive kr. og afprøv 80/20 Core-Satellite strategien.
                    </p>
                </div>
                <!-- Step 3 -->
                <div id="explore-step-3" class="explore-step absolute inset-0 p-6 md:p-8 flex flex-col items-center text-center transition-opacity duration-300 opacity-0 pointer-events-none">
                    <div class="w-16 h-16 rounded-full bg-rose-50 flex items-center justify-center mb-4">
                        <span class="material-symbols-outlined text-rose-critical text-3xl">psychology</span>
                    </div>
                    <h4 class="font-bold text-on-background text-lg mb-3">3. Mental Disciplin</h4>
                    <p class="text-sm text-on-surface-variant leading-relaxed">
                        48-timers Anti-FOMO karantæne og obligatorisk Pre-Flight tjekliste til hver handel.
                    </p>
                </div>
            </div>

            <div class="p-6 border-t border-slate-border bg-white flex justify-between items-center">
                <div class="flex gap-1.5">
                    <div id="dot-1" class="w-2 h-2 rounded-full bg-deep-indigo"></div>
                    <div id="dot-2" class="w-2 h-2 rounded-full bg-slate-300"></div>
                    <div id="dot-3" class="w-2 h-2 rounded-full bg-slate-300"></div>
                </div>
                <div class="flex gap-3">
                    <button id="btn-prev" onclick="prevStep()" class="px-4 py-2 text-sm font-semibold text-on-surface-variant border border-slate-border rounded-lg hover:bg-slate-50 transition-colors hidden">
                        Forrige
                    </button>
                    <button id="btn-next" onclick="nextStep()" class="px-6 py-2 bg-deep-indigo text-white text-sm font-bold rounded-lg hover:opacity-90 transition-opacity flex items-center gap-2">
                        Næste <span class="material-symbols-outlined text-sm">arrow_forward</span>
                    </button>
                    <button id="btn-finish" onclick="exploreAsGuest()" class="px-6 py-2 bg-emerald-600 text-white text-sm font-bold rounded-lg hover:bg-emerald-700 transition-colors hidden flex items-center gap-2 shadow-sm">
                        Prøv universet som gæst &rarr;
                    </button>
                </div>
            </div>
        </div>
    </div>
    """
content = modal_regex.sub(new_modal_html, content)

# Replace the compareData and modal JS
js_regex = re.compile(r'function openExploreModal\(\).*?(?=<script)', re.DOTALL)
new_js = """function openExploreModal() {
            const modal = document.getElementById('explore-modal');
            const inner = document.getElementById('explore-modal-inner');
            modal.classList.remove('hidden');
            // Small delay to allow display:block to apply before animating opacity
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                inner.classList.remove('scale-95');
                inner.classList.add('scale-100');
            }, 10);
            currentStep = 1;
            updateStepView();
        }

        function closeExploreModal() {
            const modal = document.getElementById('explore-modal');
            const inner = document.getElementById('explore-modal-inner');
            modal.classList.add('opacity-0');
            inner.classList.remove('scale-100');
            inner.classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300);
        }

        function exploreAsGuest() {
            localStorage.setItem('bi_user_name', 'Gæst');
            window.location.href = 'dashboard.html';
        }
        
        let currentStep = 1;
        function updateStepView() {
            for (let i = 1; i <= 3; i++) {
                const step = document.getElementById('explore-step-' + i);
                const dot = document.getElementById('dot-' + i);
                if (i === currentStep) {
                    step.classList.remove('opacity-0', 'pointer-events-none');
                    dot.classList.replace('bg-slate-300', 'bg-deep-indigo');
                } else {
                    step.classList.add('opacity-0', 'pointer-events-none');
                    dot.classList.replace('bg-deep-indigo', 'bg-slate-300');
                }
            }
            
            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
            const btnFinish = document.getElementById('btn-finish');
            
            if (currentStep === 1) {
                btnPrev.classList.add('hidden');
                btnNext.classList.remove('hidden');
                btnFinish.classList.add('hidden');
            } else if (currentStep === 2) {
                btnPrev.classList.remove('hidden');
                btnNext.classList.remove('hidden');
                btnFinish.classList.add('hidden');
            } else {
                btnPrev.classList.remove('hidden');
                btnNext.classList.add('hidden');
                btnFinish.classList.remove('hidden');
            }
        }
        
        function nextStep() {
            if (currentStep < 3) {
                currentStep++;
                updateStepView();
            }
        }
        function prevStep() {
            if (currentStep > 1) {
                currentStep--;
                updateStepView();
            }
        }

        const compareData = {
            'novo': {
                title: 'AI Analyse: Novo Nordisk vs Eli Lilly',
                pe: `
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Novo (38.5)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>
                    <div class="p-2 bg-rose-critical/10 border border-rose-critical/20 rounded text-xs font-semibold text-rose-700 flex justify-between">
                        <span>Lilly (62.1)</span>
                        <span class="material-symbols-outlined text-sm">warning</span>
                    </div>`,
                moat: 'GLP-1 duopol og patenter',
                risk: 'Prispres og regulering i USA.'
            },
            'volvo': {
                title: 'AI Analyse: Volvo vs Daimler Truck',
                pe: `
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Volvo (10.8)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>
                    <div class="p-2 bg-emerald-success/10 border border-emerald-success/20 rounded text-xs font-semibold text-emerald-700 flex justify-between">
                        <span>Daimler (9.4)</span>
                        <span class="material-symbols-outlined text-sm">thumb_up</span>
                    </div>`,
                moat: 'Globalt distributionsnet og tunge flåder',
                risk: 'Cyklisk afmatning og grøn omstilling.'
            },
            'apple': {
                title: 'AI Analyse: Apple vs Microsoft',
                pe: `
                    <div class="p-2 bg-slate-100 border border-slate-300 rounded text-xs font-semibold text-on-surface-variant flex justify-between">
                        <span>Apple (32.4)</span>
                        <span class="material-symbols-outlined text-sm">horizontal_rule</span>
                    </div>
                    <div class="p-2 bg-slate-100 border border-slate-300 rounded text-xs font-semibold text-on-surface-variant flex justify-between">
                        <span>Microsoft (34.1)</span>
                        <span class="material-symbols-outlined text-sm">horizontal_rule</span>
                    </div>`,
                moat: 'Økosystem, iOS lock-in og Azure cloud',
                risk: 'Antitrust-undersøgelser og hardware-mætning.'
            }
        };

        function updateCompareCard(caseId) {
            // Update buttons styling
            const buttons = document.querySelectorAll('.compare-btn');
            buttons.forEach(btn => {
                btn.classList.remove('border-deep-indigo', 'bg-indigo-50/40', 'text-deep-indigo', 'bg-indigo-50');
                btn.classList.add('border-slate-border', 'bg-white', 'text-on-surface-variant');
                const icon = btn.querySelector('.material-symbols-outlined');
                if(icon) icon.classList.add('hidden');
            });
            
            const activeBtn = event.currentTarget;
            activeBtn.classList.remove('border-slate-border', 'bg-white', 'text-on-surface-variant');
            activeBtn.classList.add('border-deep-indigo', 'bg-indigo-50/40', 'text-deep-indigo');
            const activeIcon = activeBtn.querySelector('.material-symbols-outlined');
            if(activeIcon) activeIcon.classList.remove('hidden');

            // Update card content
            const data = compareData[caseId];
            document.getElementById('compare-title').textContent = data.title;
            document.getElementById('compare-pe').innerHTML = data.pe;
            document.getElementById('compare-moat').textContent = data.moat;
            document.getElementById('compare-risk').textContent = data.risk;
            
            // Add a subtle blink effect
            const card = document.getElementById('compare-result-card');
            card.classList.add('opacity-50');
            setTimeout(() => card.classList.remove('opacity-50'), 150);
        }
</script>
</body>
</html>
"""
old_script_start = content.find('function openExploreModal()')
if old_script_start != -1:
    content = content[:old_script_start] + new_js
else:
    print("Could not find openExploreModal script")
    
# Let's fix the bg-indigo-50/40 class directly in the buttons as well
content = content.replace("bg-indigo-50", "bg-indigo-50/40")

with open('index.html', 'w') as f:
    f.write(content)

print("Updated index.html modal and compare logic.")
