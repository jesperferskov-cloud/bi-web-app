(function() {
    // Only init if ?debug=true or localStorage bi_debug_mode is true
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('debug') === 'true') {
        localStorage.setItem('bi_debug_mode', 'true');
    }
    // We can also allow it to be always included as requested, but user mentioned "eller aktiveres via URL parameter '?debug=true' eller localStorage 'bi_debug_mode' = 'true'". Wait, the prompt says:
    // "Denne fil skal fungere som en diskret, flydende widget, der kan inkluderes på alle sider (eller aktiveres via URL parameter '?debug=true' eller localStorage 'bi_debug_mode' = 'true')."
    // So let's just make it always visible if included, or we check the condition. Let's make it always visible if the script is loaded for now, or check the flag. Let's make it check the flag, but also if it's explicitly included maybe they want it always. The safest is to show it if debug is true or if it's just always injected. Let's just render it always, as it's an Alpha Dev panel, and it says "Diskret, flydende widget". Or actually, let's just render it.

    // Styles
    const style = document.createElement('style');
    style.innerHTML = `
        #bi-dev-panel-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
            font-family: 'Inter', sans-serif;
        }
        #bi-dev-panel-toggle {
            background-color: #0f172a; /* slate-900 */
            color: #ffffff;
            font-size: 0.75rem; /* text-xs */
            padding: 0.375rem 0.75rem; /* px-3 py-1.5 */
            border-radius: 9999px; /* rounded-full */
            border: 1px solid #334155; /* slate-700 */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-lg */
            cursor: pointer;
            transition: background-color 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 500;
        }
        #bi-dev-panel-toggle:hover {
            background-color: #1e293b; /* slate-800 */
        }
        #bi-dev-panel {
            display: none;
            position: absolute;
            bottom: 40px;
            right: 0;
            width: 320px;
            background-color: #0f172a;
            border: 1px solid #334155;
            border-radius: 12px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            color: #f8fafc;
            padding: 16px;
            flex-direction: column;
            gap: 16px;
            max-height: 80vh;
            overflow-y: auto;
        }
        #bi-dev-panel.open {
            display: flex;
        }
        .bi-dev-header {
            font-family: 'IBM Plex Sans', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 8px;
            border-bottom: 1px solid #334155;
            padding-bottom: 8px;
        }
        .bi-dev-section {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .bi-dev-section-title {
            font-family: 'IBM Plex Sans', sans-serif;
            font-size: 0.875rem;
            color: #94a3b8;
            font-weight: 500;
        }
        .bi-dev-btn {
            background-color: #1e293b;
            color: #e2e8f0;
            border: 1px solid #334155;
            border-radius: 6px;
            padding: 8px 12px;
            font-size: 0.75rem;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
            font-family: 'Inter', sans-serif;
        }
        .bi-dev-btn:hover {
            background-color: #334155;
            border-color: #475569;
        }
        .bi-dev-textarea {
            background-color: #020617;
            border: 1px solid #334155;
            border-radius: 6px;
            padding: 8px;
            color: #f8fafc;
            font-size: 0.75rem;
            resize: vertical;
            min-height: 60px;
            font-family: 'Inter', sans-serif;
        }
        .bi-dev-textarea:focus {
            outline: none;
            border-color: #3b82f6;
        }
        .bi-dev-toast {
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #10b981;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.875rem;
            font-family: 'Inter', sans-serif;
            z-index: 10000;
            display: none;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .bi-dev-error-list {
            font-size: 0.7rem;
            color: #cbd5e1;
            background: #020617;
            border: 1px solid #1e293b;
            padding: 8px;
            border-radius: 6px;
            max-height: 100px;
            overflow-y: auto;
        }
    `;
    document.head.appendChild(style);

    // Toast element
    const toast = document.createElement('div');
    toast.className = 'bi-dev-toast';
    document.body.appendChild(toast);

    function showToast(msg) {
        toast.textContent = msg;
        toast.style.display = 'block';
        setTimeout(() => {
            toast.style.display = 'none';
        }, 3000);
    }

    // Container
    const container = document.createElement('div');
    container.id = 'bi-dev-panel-container';

    // Panel
    const panel = document.createElement('div');
    panel.id = 'bi-dev-panel';

    // Panel Content
    panel.innerHTML = `
        <div class="bi-dev-header">🛠️ Alpha Dev/Test Panel</div>

        <!-- Section 1 -->
        <div class="bi-dev-section">
            <div class="bi-dev-section-title">Hurtig-Nulstilling & Test-Cykler</div>
            <button class="bi-dev-btn" id="bi-dev-btn-reset">🧹 Fuld Nulstilling (Slet Data & Genstart)</button>
            <button class="bi-dev-btn" id="bi-dev-btn-modules">🎓 Gennemfør Alle 12 Moduler</button>
        </div>

        <!-- Section 2 -->
        <div class="bi-dev-section">
            <div class="bi-dev-section-title">Hurtige Profil-Presets</div>
            <button class="bi-dev-btn" id="bi-dev-btn-preset1">👤 Senior (50+, Pension, Lav risiko)</button>
            <button class="bi-dev-btn" id="bi-dev-btn-preset2">👤 Vækst-investor (18-35, Høj risiko, Enkeltaktier)</button>
            <button class="bi-dev-btn" id="bi-dev-btn-preset3">👤 Begynder (Core 80/20, Formuepleje)</button>
        </div>

        <!-- Section 3 -->
        <div class="bi-dev-section">
            <div class="bi-dev-section-title">Alpha Fejllogger</div>
            <textarea class="bi-dev-textarea" id="bi-dev-bug-note" placeholder="Beskriv observeret fejl eller forbedring..."></textarea>
            <button class="bi-dev-btn" id="bi-dev-btn-log">Gem i Fejllog 📝</button>
            <div id="bi-dev-error-list-container" style="display:none;">
                <div class="bi-dev-error-list" id="bi-dev-error-list"></div>
                <button class="bi-dev-btn" id="bi-dev-btn-copy-logs" style="margin-top: 4px; width: 100%; text-align: center;">Kopiér samlet fejllog</button>
            </div>
            <button class="bi-dev-btn" id="bi-dev-btn-mail">Send Fejl via Mail ✉️</button>
        </div>
    `;

    // Toggle Button
    const toggleBtn = document.createElement('div');
    toggleBtn.id = 'bi-dev-panel-toggle';
    toggleBtn.innerHTML = '🛠️ Dev / Test';
    toggleBtn.onclick = () => {
        panel.classList.toggle('open');
    };

    container.appendChild(panel);
    container.appendChild(toggleBtn);
    document.body.appendChild(container);

    // Event Listeners
    document.getElementById('bi-dev-btn-reset').onclick = () => {
        const keys = Object.keys(localStorage);
        keys.forEach(key => {
            if (key.startsWith('bi_')) {
                localStorage.removeItem(key);
            }
        });
        showToast("Data nulstillet. Omdirigerer til onboarding...");
        setTimeout(() => {
            window.location.href = 'onboarding.html';
        }, 300);
    };

    document.getElementById('bi-dev-btn-modules').onclick = () => {
        for (let i = 1; i <= 12; i++) {
            localStorage.setItem(`bi_module_${i}_completed`, 'true');
        }
        showToast("Alle moduler gennemført. Genindlæser...");
        setTimeout(() => {
            window.location.reload();
        }, 300);
    };

    document.getElementById('bi-dev-btn-preset1').onclick = () => {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: '50+', goal: 'Pension', risk: 'Lav' }));
        showToast("Profil sat til Senior. Genindlæser...");
        setTimeout(() => { window.location.reload(); }, 300);
    };

    document.getElementById('bi-dev-btn-preset2').onclick = () => {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: '18-35', goal: 'Vækst', risk: 'Høj', style: 'Enkeltaktier' }));
        showToast("Profil sat til Vækst-investor. Genindlæser...");
        setTimeout(() => { window.location.reload(); }, 300);
    };

    document.getElementById('bi-dev-btn-preset3').onclick = () => {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: 'Begynder', goal: 'Formuepleje', risk: 'Middel', style: 'Core 80/20' }));
        showToast("Profil sat til Begynder. Genindlæser...");
        setTimeout(() => { window.location.reload(); }, 300);
    };

    function updateErrorList() {
        const logsStr = localStorage.getItem('bi_alpha_error_log');
        if (!logsStr) return;
        let logs = [];
        try { logs = JSON.parse(logsStr); } catch(e) {}
        if (logs.length > 0) {
            document.getElementById('bi-dev-error-list-container').style.display = 'block';
            const listEl = document.getElementById('bi-dev-error-list');
            listEl.innerHTML = logs.slice(-3).reverse().map(l => 
                `<div style="margin-bottom: 4px; border-bottom: 1px solid #1e293b; padding-bottom: 2px;">
                    <span style="color:#94a3b8;">${new Date(l.timestamp).toLocaleTimeString()}</span>: ${l.note}
                </div>`
            ).join('');
        }
    }

    document.getElementById('bi-dev-btn-log').onclick = () => {
        const note = document.getElementById('bi-dev-bug-note').value;
        if (!note.trim()) {
            alert("Beskriv fejlen først.");
            return;
        }
        const errorEntry = {
            timestamp: Date.now(),
            url: window.location.pathname,
            screenWidth: window.innerWidth,
            note: note
        };
        let logs = [];
        const existing = localStorage.getItem('bi_alpha_error_log');
        if (existing) {
            try { logs = JSON.parse(existing); } catch(e) {}
        }
        logs.push(errorEntry);
        localStorage.setItem('bi_alpha_error_log', JSON.stringify(logs));
        document.getElementById('bi-dev-bug-note').value = '';
        updateErrorList();
        showToast("Fejl gemt i loggen!");
    };

    document.getElementById('bi-dev-btn-copy-logs').onclick = () => {
        const logsStr = localStorage.getItem('bi_alpha_error_log');
        if (logsStr) {
            navigator.clipboard.writeText(logsStr).then(() => {
                showToast("Fejllog kopieret til udklipsholder!");
            });
        }
    };

    document.getElementById('bi-dev-btn-mail').onclick = () => {
        const note = document.getElementById('bi-dev-bug-note').value || "(Ingen beskrivelse)";
        const subject = encodeURIComponent("[BI Bug Report] " + window.location.pathname);
        const body = encodeURIComponent(
            "URL: " + window.location.pathname + "\n" +
            "Skærmopløsning: " + window.innerWidth + "x" + window.innerHeight + "\n" +
            "User Agent: " + navigator.userAgent + "\n\n" +
            "Beskrivelse:\n" + note
        );
        window.location.href = `mailto:jesper.ferskov@gmail.com?subject=${subject}&body=${body}`;
    };

    // Init list
    updateErrorList();

})();
