const fs = require('fs');
const path = require('path');

const files = [
  'dashboard.html',
  'profil.html',
  'portefoelje.html',
  'laer.html',
  'analyse.html',
  'markeder.html',
  'vaerktoejer.html'
];

for (const file of files) {
  const filePath = path.join(process.cwd(), file);
  if (!fs.existsSync(filePath)) continue;
  let content = fs.readFileSync(filePath, 'utf8');

  content = content.replace(/class="([^"]*)"/g, (match, classes) => {
    let cls = classes.split(/\s+/);
    
    // Check if it's a secondary panel that needs elevated
    if (cls.includes('bg-slate-50') || cls.includes('bg-slate-surface')) {
        // Remove existing wrong dark:bgs if we want to ensure it is dark-elevated
        // But user said: "Sekundære paneler / indre elementer: bg-slate-50 dark:bg-dark-elevated"
        // And earlier we converted dark:bg-[#0b1326] -> dark:bg-dark-canvas on them by accident if it had that.
        // Let's just ensure if it has bg-slate-50 or bg-slate-surface, it gets dark:bg-dark-elevated
        cls = cls.filter(c => !c.startsWith('dark:bg-dark-canvas') && !c.startsWith('dark:bg-dark-card'));
        if (!cls.includes('dark:bg-dark-elevated')) {
            cls.push('dark:bg-dark-elevated');
        }
    }
    
    return `class="${cls.join(' ')}"`;
  });

  fs.writeFileSync(filePath, content, 'utf8');
}
