(function() {
    // Sørg for at den kun initialiseres én gang
    if (document.getElementById('bi-alpha-dev-panel')) return;

    // Opret container
    const panelWrapper = document.createElement('div');
    panelWrapper.id = 'bi-alpha-dev-panel';
    panelWrapper.style.position = 'fixed';
    panelWrapper.style.bottom = '20px';
    panelWrapper.style.right = '20px';
    panelWrapper.style.zIndex = '99999';
    panelWrapper.style.fontFamily = 'Inter, sans-serif';

    // Styles
    const style = document.createElement('style');
    style.innerHTML = `
        #bi-alpha-dev-panel-content {
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
        #bi-alpha-dev-panel-content.open {
            display: flex;
        }
        #bi-dev-panel-toggle {
            background-color: #0f172a;
            color: #ffffff;
            font-size: 0.75rem;
            padding: 0.375rem 0.75rem;
            border-radius: 9999px;
            border: 1px solid #334155;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 500;
            margin-left: auto;
        }
        #bi-dev-panel-toggle:hover {
            background-color: #1e293b;
        }
        .bi-dev-header {
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
            z-index: 100000;
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
        setTimeout(function() {
            toast.style.display = 'none';
        }, 3000);
    }

    panelWrapper.innerHTML = `
        <div id="bi-alpha-dev-panel-content">
            <div class="bi-dev-header">🛠️ Alpha Dev/Test Panel</div>
            
            <div class="bi-dev-section">
                <div class="bi-dev-section-title">Hurtig-Nulstilling & Test-Cykler</div>
                <button class="bi-dev-btn" id="bi-dev-btn-reset">🧹 Fuld Nulstilling (Slet alt)</button>
                <button class="bi-dev-btn" id="bi-dev-btn-modules">🎓 Gennemfør Alle 12 Moduler</button>
            </div>

            <div class="bi-dev-section">
                <div class="bi-dev-section-title">Hurtige Profil-Presets</div>
                <button class="bi-dev-btn" id="bi-dev-btn-preset1">👤 Senior (50+, Pension, Lav risiko)</button>
                <button class="bi-dev-btn" id="bi-dev-btn-preset2">👤 Vækst (18-35, Høj risiko)</button>
                <button class="bi-dev-btn" id="bi-dev-btn-preset3">👤 Begynder (Core 80/20, Middel)</button>
            </div>

            <div class="bi-dev-section">
                <div class="bi-dev-section-title">Alpha Fejllogger</div>
                <textarea class="bi-dev-textarea" id="bi-dev-bug-note" placeholder="Beskriv fejl..."></textarea>
                <button class="bi-dev-btn" id="bi-dev-btn-log">Gem i Fejllog 📝</button>
                <div id="bi-dev-error-list-container" style="display:none;">
                    <div class="bi-dev-error-list" id="bi-dev-error-list"></div>
                    <button class="bi-dev-btn" id="bi-dev-btn-copy-logs" style="margin-top:4px;width:100%;text-align:center;">Kopiér fejllog</button>
                </div>
                <button class="bi-dev-btn" id="bi-dev-btn-mail">Send via Mail ✉️</button>
            </div>
        </div>
        <div id="bi-dev-panel-toggle">🛠️ Dev / Test</div>
    `;

    document.body.appendChild(panelWrapper);

    // Toggle logic
    document.getElementById('bi-dev-panel-toggle').onclick = function() {
        document.getElementById('bi-alpha-dev-panel-content').classList.toggle('open');
    };

    // Actions
    document.getElementById('bi-dev-btn-reset').onclick = function() {
        Object.keys(localStorage).forEach(function(key) {
            if (key.indexOf('bi_') === 0) {
                localStorage.removeItem(key);
            }
        });
        showToast("Data nulstillet. Genindlæser...");
        setTimeout(function() {
            window.location.href = 'onboarding.html';
        }, 300);
    };

    document.getElementById('bi-dev-btn-modules').onclick = function() {
        // Bruger string concatenation i stedet for template literals for at undgå problemer
        for (let i = 1; i <= 12; i++) {
            localStorage.setItem('bi_module_' + i + '_completed', 'true');
        }
        // Gennemfør også de navngivne moduler
        const namedModules = ['core', 'infla', 'skat', 'moat', 'pe', 'advokat', 'fomo', 'market', 'preflight', 'rebalancering', 'dynamik', 'exit'];
        for (let j = 0; j < namedModules.length; j++) {
            localStorage.setItem('bi_module_' + namedModules[j] + '_completed', 'true');
        }
        showToast("Alle moduler gennemført. Genindlæser...");
        setTimeout(function() {
            window.location.reload();
        }, 300);
    };

    document.getElementById('bi-dev-btn-preset1').onclick = function() {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: '50+', goal: 'Pension', risk: 'Lav' }));
        showToast("Profil sat. Genindlæser...");
        setTimeout(function() { window.location.reload(); }, 300);
    };

    document.getElementById('bi-dev-btn-preset2').onclick = function() {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: '18-35', goal: 'Vækst', risk: 'Høj', style: 'Enkeltaktier' }));
        showToast("Profil sat. Genindlæser...");
        setTimeout(function() { window.location.reload(); }, 300);
    };

    document.getElementById('bi-dev-btn-preset3').onclick = function() {
        localStorage.setItem('bi_user_profile', JSON.stringify({ age: 'Begynder', goal: 'Formuepleje', risk: 'Middel', style: 'Core 80/20' }));
        showToast("Profil sat. Genindlæser...");
        setTimeout(function() { window.location.reload(); }, 300);
    };

    function updateErrorList() {
        const logsStr = localStorage.getItem('bi_alpha_error_log');
        if (!logsStr) return;
        let logs = [];
        try { logs = JSON.parse(logsStr); } catch(e) {}
        if (logs.length > 0) {
            document.getElementById('bi-dev-error-list-container').style.display = 'block';
            const listEl = document.getElementById('bi-dev-error-list');
            listEl.innerHTML = logs.slice(-3).reverse().map(function(l) {
                return '<div style="margin-bottom:4px;border-bottom:1px solid #1e293b;padding-bottom:2px;">' +
                       '<span style="color:#94a3b8;">' + new Date(l.timestamp).toLocaleTimeString() + '</span>: ' + l.note +
                       '</div>';
            }).join('');
        }
    }

    document.getElementById('bi-dev-btn-log').onclick = function() {
        const note = document.getElementById('bi-dev-bug-note').value;
        if (!note.trim()) {
            alert("Beskriv fejlen først.");
            return;
        }
        let logs = [];
        const existing = localStorage.getItem('bi_alpha_error_log');
        if (existing) {
            try { logs = JSON.parse(existing); } catch(e) {}
        }
        logs.push({
            timestamp: Date.now(),
            url: window.location.pathname,
            screenWidth: window.innerWidth,
            note: note
        });
        localStorage.setItem('bi_alpha_error_log', JSON.stringify(logs));
        document.getElementById('bi-dev-bug-note').value = '';
        updateErrorList();
        showToast("Fejl gemt i loggen!");
    };

    document.getElementById('bi-dev-btn-copy-logs').onclick = function() {
        const logsStr = localStorage.getItem('bi_alpha_error_log');
        if (logsStr) {
            navigator.clipboard.writeText(logsStr).then(function() {
                showToast("Fejllog kopieret til udklipsholder!");
            });
        }
    };

    document.getElementById('bi-dev-btn-mail').onclick = function() {
        const note = document.getElementById('bi-dev-bug-note').value || "(Ingen beskrivelse)";
        const subject = encodeURIComponent("[BI Bug Report] " + window.location.pathname);
        const body = encodeURIComponent(
            "URL: " + window.location.pathname + "\\n" +
            "Skærm: " + window.innerWidth + "x" + window.innerHeight + "\\n" +
            "Beskrivelse:\\n" + note
        );
        window.location.href = 'mailto:jesper.ferskov@gmail.com?subject=' + subject + '&body=' + body;
    };

    updateErrorList();
})();
