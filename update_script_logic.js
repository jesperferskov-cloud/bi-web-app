const fs = require('fs');
const files = [
    'dashboard.html',
    'profil.html',
    'portefoelje.html',
    'laer.html',
    'analyse.html',
    'markeder.html',
    'vaerktoejer.html'
];

const newScript = `
    <!-- Theme Toggle Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            const themeLock = document.getElementById('theme-lock-sidebar');
            
            if (!isSupporter && themeLock) {
                themeLock.style.display = 'inline-block';
            }
        });

        function toggleTheme() {
            const isSupporter = localStorage.getItem('bi_is_supporter') === 'true';
            if (!isSupporter) {
                const modal = document.getElementById('supporter-modal');
                if (modal) {
                    modal.classList.remove('hidden');
                    const modalTitle = modal.querySelector('h4');
                    if (modalTitle) modalTitle.textContent = "⭐ Dark Mode er eksklusivt for Supporters";
                } else {
                    alert("Dark Mode er en eksklusiv funktion for vores Supporters. Støt serverdriften og lås op for mørkt tema med det samme.");
                }
                return;
            }

            const html = document.documentElement;
            if (html.classList.contains('dark')) {
                html.classList.remove('dark');
                localStorage.setItem('bi_theme', 'light');
            } else {
                html.classList.add('dark');
                localStorage.setItem('bi_theme', 'dark');
            }
        }
    </script>
`;

for (let file of files) {
    let content = fs.readFileSync(file, 'utf8');
    
    // Replace everything from <!-- Theme Toggle Logic --> to the end of the script block
    content = content.replace(/<!-- Theme Toggle Logic -->[\s\S]*?<\/script>/, newScript.trim());
    
    fs.writeFileSync(file, content);
    console.log("Updated logic in " + file);
}
