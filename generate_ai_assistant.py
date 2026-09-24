import re

with open('ai-assistant.js', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to construct the new JS file.
# The user wants this exact DOM injection structure wrapped in DOMContentLoaded.
new_html = """
    // Tjek om elementerne findes, ellers opret dem direkte i DOM'en
    if (!document.getElementById('ai-assistant-container')) {
      const wrapper = document.createElement('div');
      wrapper.id = 'ai-assistant-container';
      wrapper.innerHTML = `
        <style>
            .ai-hide-scrollbar::-webkit-scrollbar {
                display: none;
            }
            .ai-hide-scrollbar {
                -ms-overflow-style: none;
                scrollbar-width: none;
            }
            #ai-chat-messages::-webkit-scrollbar {
                width: 6px;
            }
            #ai-chat-messages::-webkit-scrollbar-track {
                background: transparent;
            }
            #ai-chat-messages::-webkit-scrollbar-thumb {
                background: #2a3245;
                border-radius: 10px;
            }
        </style>
        <!-- Svævende Trigger Knap -->
        <div class="fixed bottom-6 right-6 z-[9999] flex flex-col items-end pointer-events-none">
          <!-- Nudge Taleboble -->
          <div id="ai-nudge-bubble" class="hidden mb-3 p-3.5 bg-[#18193a] border border-indigo-500/30 rounded-2xl shadow-2xl text-xs text-slate-200 max-w-xs pointer-events-auto backdrop-blur-md flex items-start gap-2.5 transition-all duration-300 opacity-0 translate-y-2">
            <span class="material-symbols-outlined text-amber-400 text-sm mt-0.5">auto_awesome</span>
            <div class="flex-1">
              <p id="ai-nudge-text" class="leading-relaxed"></p>
            </div>
            <button id="ai-close-nudge" class="text-slate-400 hover:text-white transition-colors">✕</button>
          </div>

          <!-- Flydende Cirkulær Knap -->
          <button id="ai-launcher-btn" class="w-14 h-14 rounded-full bg-gradient-to-br from-[#1e1b4b] to-[#2e1065] border border-indigo-400/40 shadow-2xl flex items-center justify-center pointer-events-auto cursor-pointer group hover:scale-105 active:scale-95 transition-all relative">
            <span class="material-symbols-outlined text-cyan-400 group-hover:text-cyan-300 text-2xl">smart_toy</span>
            <span id="ai-launcher-dot" class="absolute top-0 right-0 w-3 h-3 bg-cyan-500 rounded-full border-2 border-[#1e1b4b] animate-pulse hidden"></span>
          </button>
        </div>

        <!-- Slide-Over Drawer -->
        <div id="ai-drawer" class="fixed inset-y-0 right-0 w-full max-w-md bg-gradient-to-b from-[#18193a] via-[#161830] to-[#0e1022] border-l border-indigo-900/40 shadow-2xl z-[10000] transform translate-x-full transition-transform duration-300 flex flex-col text-white">
          <!-- Header -->
          <div class="p-4 border-b border-white/10 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <span class="material-symbols-outlined text-amber-400 text-xl">auto_awesome</span>
              <div>
                <h3 class="font-bold text-sm text-white font-headline">AI Analyse-Assistent</h3>
                <div class="flex items-center gap-1.5 text-[10px] text-emerald-400">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Kører lokalt uden serverkald</span>
                </div>
              </div>
            </div>
            <button id="ai-close-drawer" class="p-1 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors">
              <span class="material-symbols-outlined text-lg">close</span>
            </button>
          </div>

          <!-- Kontekst Chips -->
          <div class="p-3 border-b border-white/5 bg-black/20 overflow-x-auto flex gap-2 ai-hide-scrollbar" id="ai-context-chips">
            <!-- Udfyldes af renderContextualChips() -->
          </div>

          <!-- Chat Historik -->
          <div id="ai-chat-messages" class="flex-1 p-4 overflow-y-auto space-y-3">
            <div class="bg-[#22274c]/80 border border-white/10 rounded-2xl p-3.5 text-xs text-slate-200 leading-relaxed shadow-sm">
              Hej! Jeg er din lokale AI-assistent. Hvad vil du undersøge i dag?
            </div>
          </div>

          <!-- Input felt -->
          <div class="p-3 border-t border-white/10 bg-[#0d0e1a]">
            <form id="ai-chat-form" class="flex items-center gap-2">
              <input type="text" id="ai-input" placeholder="Spørg om alt inden for platformen..." class="flex-1 bg-[#18193a] border border-white/15 focus:border-indigo-400 rounded-xl px-3 py-2.5 text-xs text-white placeholder-slate-400 outline-none transition-all" autocomplete="off">
              <button type="submit" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 p-2.5 rounded-xl transition-all flex items-center justify-center cursor-pointer">
                <span class="material-symbols-outlined text-sm font-bold">send</span>
              </button>
            </form>
          </div>
        </div>
      `;
      document.body.appendChild(wrapper);
      bindAIEvents(); // Kobl event-listeners på de nyoprettede knapper
    }
"""

new_js = f"""document.addEventListener('DOMContentLoaded', () => {{
{new_html}
}});

function bindAIEvents() {{
    const nudgeBubble = document.getElementById('ai-nudge-bubble');
    const nudgeText = document.getElementById('ai-nudge-text');
    const nudgeClose = document.getElementById('ai-close-nudge');
    const launcherBtn = document.getElementById('ai-launcher-btn');
    const launcherDot = document.getElementById('ai-launcher-dot');
    const drawer = document.getElementById('ai-drawer');
    const drawerClose = document.getElementById('ai-close-drawer');
    const chatForm = document.getElementById('ai-chat-form');
    const chatInput = document.getElementById('ai-input');
    const chatHistory = document.getElementById('ai-chat-messages');
    const chipsContainer = document.getElementById('ai-context-chips');

    function renderContextualChips() {{
        const path = window.location.pathname.toLowerCase();
        let chips = [];
        
        if (path.includes('analyse.html')) {{
            chips = [
                "Forklar P/E-tallet for denne aktie",
                "Hvad er den primære voldgrav (Moat)?",
                "Hvad er den største risiko?"
            ];
        }} else if (path.includes('dashboard.html')) {{
            chips = [
                "Hvad er min saldo?",
                "Hvorfor er 48t karantæne vigtig?",
                "Hvordan holder jeg 80/20-balancen?"
            ];
        }} else if (path.includes('laer.html') || path.includes('modul')) {{
            chips = [
                "Hvad er en ETF simpelt?",
                "Hvad betyder renters rente?",
                "Forklar risiko på 1 minut"
            ];
        }} else {{
            chips = [
                "Forklar P/E simpelt",
                "Hvad er 80/20?",
                "Hvad er en Moat?"
            ];
        }}
        
        chipsContainer.innerHTML = '';
        chips.forEach(chipText => {{
            const btn = document.createElement('button');
            btn.className = "bg-white/10 hover:bg-white/20 border border-white/15 rounded-xl px-3 py-2 text-xs text-slate-200 transition-all text-left flex items-center gap-2 cursor-pointer whitespace-nowrap shrink-0";
            btn.textContent = chipText;
            btn.addEventListener('click', () => {{
                handleUserMessage(chipText);
            }});
            chipsContainer.appendChild(btn);
        }});
    }}

    renderContextualChips();

    function normalizeText(text) {{
        return text
            .toLowerCase()
            .replace(/[\\/\\?\\.\\,\\-\\_]/g, ' ')
            .replace(/\\s+/g, ' ')
            .trim();
    }}

    const localKnowledge = [
        {{
            keywords: ['pe', 'p e', 'price to earnings', 'kurs indtjening', 'vaerdiansaettelse', 'p e tallet'],
            answer: "P/E står for Price/Earnings (Pris/Indtjening). Det viser, hvor meget du betaler for 1 krone af virksomhedens overskud. Et lavt tal kan indikere en billig eller moden aktie, mens et højt tal indikerer markedets forventning om kraftig fremtidig vækst."
        }},
        {{
            keywords: ['80 20', 'core satellite', 'kerne satellit', 'allokering', '80 20 balancen'],
            answer: "I Begynder Investor-metodikken anbefaler vi 80/20-fordelingen: Mindst 80% placeres i brede, passive globale indeksfonde (Core) for stabilitet og renters rente, mens maks. 20% investeres i analyserede enkeltaktier (Satellit) til læring."
        }},
        {{
            keywords: ['saldo', 'kontant', 'penge', 'balance', 'hvor mange penge'],
            getDynamicAnswer: () => {{
                const cash = localStorage.getItem('bi_cash_balance') || '50000';
                return `Du har i øjeblikket ${{Number(cash).toLocaleString('da-DK')}} kr. i din simulerede kontantbeholdning.`;
            }}
        }},
        {{
            keywords: ['profil', 'hvem er jeg', 'min profil'],
            getDynamicAnswer: () => {{
                const profile = localStorage.getItem('bi_user_profile');
                if (profile) {{
                    try {{
                        const data = JSON.parse(profile);
                        return `Din nuværende profil er sat op som: **${{data.risk || 'Ukendt'}}** risikoprofil, med en tidshorisont på **${{data.horizon || 'Ukendt'}}**.`;
                    }} catch(e) {{}}
                }}
                return 'Jeg kan se, at du ikke har udfyldt din investeringsprofil endnu. Det kan du gøre under "Profil" i menuen.';
            }}
        }},
        {{
            keywords: ['portefølje', 'aktier', 'beholdning'],
            getDynamicAnswer: () => {{
                const holdings = localStorage.getItem('bi_portfolio_holdings');
                if (holdings && holdings !== '[]') {{
                    return 'Du har allerede aktiver i din portefølje. Gå til "Portefølje" for at se et detaljeret overblik over fordelingen.';
                }} else {{
                    return 'Din portefølje er tom lige nu. Prøv at gå til "Markeder" for at finde din første aktie eller fond.';
                }}
            }}
        }},
        {{
            keywords: ['moat', 'voldgrav', 'konkurrencefordel', 'primære voldgrav'],
            answer: "En økonomisk voldgrav (Moat) er en virksomheds varige konkurrencefordel (f.eks. patenter, stærke brands som Novo Nordisk eller høje skifteomkostninger), som forhindrer konkurrenter i at æde dens overskud."
        }},
        {{
            keywords: ['etf', 'passiv fond', 'indeksfond'],
            answer: "En ETF (Exchange Traded Fund) er en børsnoteret fond, der følger et indeks passivt. Fordelen er lave årlige omkostninger (ÅOP) og øjeblikkelig global risikospredning."
        }},
        {{
            keywords: ['kurtage', 'gebyr'],
            answer: "Kurtage er det transaktionsgebyr, din handelsplatform eller bank opkræver for at købe eller sælge værdipapirer."
        }},
        {{
            keywords: ['volatilitet', 'svingninger', 'udsving', 'risiko', 'største risiko'],
            answer: "Risiko og volatilitet måler, hvor kraftigt og hurtigt kursen svinger. Den største risiko ved aktier er permanent tab af kapital, hvilket vi minimerer gennem 80/20-spredning, analyse af Moat og anti-FOMO regler."
        }},
        {{
            keywords: ['karantæne', 'fomo', '48 timer', '48t karantæne', '48t'],
            answer: "Anti-FOMO karantænen på 48 timer er en obligatorisk tænkepause for satellit-køb. Den tvinger dig til at sove på beslutningen og modvirker impulskøb drevet af markedsstøj."
        }},
        {{
            keywords: ['renters rente', 'rente'],
            answer: "Renters rente er effekten af at geninvestere dit afkast. Over tid begynder dit afkast at skabe sit eget afkast, hvilket giver en sneboldeffekt der vokser eksponentielt."
        }}
    ];

    function processQuery(query) {{
        const q = normalizeText(query);
        
        for (const item of localKnowledge) {{
            if (item.keywords.some(keyword => q.includes(keyword))) {{
                if (item.getDynamicAnswer) {{
                    return item.getDynamicAnswer();
                }}
                return item.answer;
            }}
        }}

        return 'Dette kræver dybere markedsanalyse eller ligger uden for min lokale viden. Opgrader til Supporter for live web-research, eller stil et spørgsmål om investeringsbegreber.';
    }}

    function addMessage(text, isUser = false) {{
        const div = document.createElement('div');
        div.className = 'flex gap-3 ' + (isUser ? 'flex-row-reverse' : '');
        
        let avatarHTML = '';
        if (isUser) {{
            avatarHTML = `
                <div class="w-8 h-8 rounded-full bg-indigo-500/20 border border-indigo-500/50 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-indigo-400 text-sm">person</span>
                </div>
            `;
        }} else {{
            avatarHTML = `
                <div class="w-8 h-8 rounded-full bg-[#22274c] border border-white/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-amber-400 text-sm">auto_awesome</span>
                </div>
            `;
        }}

        const msgClass = isUser 
            ? 'bg-indigo-600 text-white rounded-2xl px-4 py-2.5 text-sm' 
            : 'bg-[#22274c]/80 border border-white/10 rounded-2xl p-4 text-sm text-slate-100 shadow-sm leading-relaxed';
            
        const formattedText = text.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');

        div.innerHTML = `
            ${{avatarHTML}}
            <div class="${{msgClass}} max-w-[85%]">
                ${{formattedText}}
            </div>
        `;
        
        chatHistory.appendChild(div);
        chatHistory.scrollTo({{ top: chatHistory.scrollHeight, behavior: 'smooth' }});
    }}

    function showTypingIndicator() {{
        const div = document.createElement('div');
        div.id = 'ai-typing-indicator';
        div.className = 'flex gap-3';
        div.innerHTML = `
            <div class="w-8 h-8 rounded-full bg-[#22274c] border border-white/10 flex items-center justify-center shrink-0">
                <span class="material-symbols-outlined text-amber-400 text-sm">auto_awesome</span>
            </div>
            <div class="bg-[#22274c]/80 border border-white/10 p-3 rounded-2xl flex items-center gap-1">
                <div class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style="animation-delay: 0s"></div>
                <div class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
                <div class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
            </div>
        `;
        chatHistory.appendChild(div);
        chatHistory.scrollTo({{ top: chatHistory.scrollHeight, behavior: 'smooth' }});
        return div;
    }}

    async function handleUserMessage(msg) {{
        if (!msg) return;
        addMessage(msg, true);
        chatInput.value = '';
        
        const typingIndicator = showTypingIndicator();
        
        const delay = Math.floor(Math.random() * 150) + 250;
        await new Promise(r => setTimeout(r, delay));
        
        typingIndicator.remove();
        const response = processQuery(msg);
        addMessage(response, false);
    }}

    chatForm.addEventListener('submit', (e) => {{
        e.preventDefault();
        handleUserMessage(chatInput.value);
    }});

    function toggleDrawer(forceClose = false) {{
        const isClosed = drawer.classList.contains('translate-x-full');
        if (isClosed && !forceClose) {{
            drawer.classList.remove('translate-x-full');
            hideNudge();
            launcherDot.classList.add('hidden');
            setTimeout(() => chatInput.focus(), 300);
        }} else {{
            drawer.classList.add('translate-x-full');
        }}
    }}

    launcherBtn.addEventListener('click', () => toggleDrawer());
    drawerClose.addEventListener('click', () => toggleDrawer(true));

    let inactivityTimer = null;
    const nudgeCooldownKey = 'bi_ai_nudge_cooldown';

    function getNudgeText() {{
        const path = window.location.pathname.toLowerCase();
        if (path.includes('dashboard.html')) return "Har du brug for hjælp til at balancere dine 50.000 fiktive kroner?";
        if (path.includes('laer.html')) return "Sidder du fast i et af modulerne? Spørg mig om begreberne.";
        if (path.includes('analyse.html')) return "Vil du have forklaret forskellen på Moat og P/E?";
        return "Er der noget investeringsfagligt, jeg kan hjælpe med at forklare?";
    }}

    function showNudge() {{
        const cooldown = sessionStorage.getItem(nudgeCooldownKey);
        if (cooldown && Date.now() < parseInt(cooldown)) return;
        
        if (!drawer.classList.contains('translate-x-full')) return;
        if (!nudgeBubble) return;

        nudgeText.textContent = getNudgeText();
        nudgeBubble.classList.remove('hidden');
        
        setTimeout(() => {{
            nudgeBubble.classList.remove('opacity-0', 'translate-y-2');
            launcherDot.classList.remove('hidden');
        }}, 50);
    }}

    function hideNudge(isDismissed = false) {{
        if (!nudgeBubble) return;
        nudgeBubble.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => {{
            nudgeBubble.classList.add('hidden');
        }}, 300);

        if (isDismissed) {{
            sessionStorage.setItem(nudgeCooldownKey, (Date.now() + 10 * 60 * 1000).toString());
        }}
    }}

    nudgeClose.addEventListener('click', (e) => {{
        e.stopPropagation();
        hideNudge(true);
    }});

    function resetInactivity() {{
        clearTimeout(inactivityTimer);
        inactivityTimer = setTimeout(showNudge, 20000); // 20 seconds
    }}

    ['mousemove', 'keydown', 'scroll', 'click'].forEach(evt => {{
        document.addEventListener(evt, resetInactivity, {{ passive: true }});
    }});

    resetInactivity();
}}
"""

with open('ai-assistant.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

