import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace button text
content = content.replace(
    'Prøv universet som gæst &rarr;',
    'Opret gratis profil & start læring &rarr;'
)

# Update the JS click handler
# We'll replace the existing JS block for guest-explore-btn
old_js = """        document.addEventListener('DOMContentLoaded', () => {
            const guestBtn = document.getElementById('guest-explore-btn');
            if (guestBtn) {
                guestBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Visuel feedback
                    const originalText = guestBtn.innerHTML;
                    guestBtn.style.opacity = '0.9';
                    guestBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">autorenew</span> Gør klar...';
                    guestBtn.disabled = true;

                    setTimeout(() => {
                        // 1. Opret og gem standard gæsteprofil i localStorage
                        const guestProfile = {
                            navn: 'Gæst',
                            alder: '18–35 år',
                            erfaring: 'Lidt kendskab',
                            risiko: 'Middel',
                            maal: 'Lær om aktier',
                            horisont: '5+ år'
                        };
                        
                        localStorage.setItem('bi_user_name', 'Gæst');
                        localStorage.setItem('bi_user_profile', JSON.stringify(guestProfile));
                        
                        // 2. Initialiser demosaldo hvis ikke allerede sat
                        if (!localStorage.getItem('bi_cash_balance')) {
                            localStorage.setItem('bi_cash_balance', '10000');
                        }
                        
                        // 3. Viderestil til dashboardet
                        window.location.href = 'dashboard.html';
                    }, 500); // 500ms delay for visual feedback
                });
            }
        });"""

new_js = """        document.addEventListener('DOMContentLoaded', () => {
            const guestBtn = document.getElementById('guest-explore-btn');
            if (guestBtn) {
                guestBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Visuel feedback
                    guestBtn.style.opacity = '0.9';
                    guestBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">autorenew</span> Gør klar...';
                    guestBtn.disabled = true;

                    setTimeout(() => {
                        window.location.href = 'onboarding.html';
                    }, 300);
                });
            }
        });"""

content = content.replace(old_js, new_js)

with open('index.html', 'w') as f:
    f.write(content)

print("index.html updated.")
