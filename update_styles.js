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

const basePath = process.cwd();

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) {
    console.log(`Skipping ${file} - not found`);
    continue;
  }
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Tailwind Config
  if (!content.includes('"dark-canvas"')) {
    content = content.replace(
      /"surface-container-lowest":\s*"#ffffff"\s*\}/g,
      `"surface-container-lowest": "#ffffff",
                        "dark-canvas": "#0b1326",
                        "dark-card": "#131b2e",
                        "dark-elevated": "#1c2640",
                        "dark-border": "#1e293b",
                        "dark-text": "#f8fafc",
                        "dark-muted": "#94a3b8"
                    }`
    );
  }

  // 2. Replace hardcoded dark hexes
  content = content.replace(/dark:bg-\[\#0b1326\]/g, 'dark:bg-dark-canvas');
  content = content.replace(/dark:bg-\[\#131b2e\]/g, 'dark:bg-dark-card');
  content = content.replace(/dark:bg-\[\#1c2640\]/g, 'dark:bg-dark-elevated');
  content = content.replace(/dark:border-\[\#1e293b\]/g, 'dark:border-dark-border');
  content = content.replace(/dark:text-\[\#f8fafc\]/g, 'dark:text-dark-text');
  content = content.replace(/dark:text-\[\#94a3b8\]/g, 'dark:text-dark-muted');

  // 3. Body tags modifications
  content = content.replace(/<body([^>]*)>/i, (match, p1) => {
    let classesMatch = p1.match(/class="([^"]*)"/);
    if (classesMatch) {
      let cls = classesMatch[1].split(/\s+/);
      
      // bg-background -> bg-[#f8f9ff]
      cls = cls.map(c => c === 'bg-background' ? 'bg-[#f8f9ff]' : c);
      
      // Add text-[#0b1c30] if not present
      if (!cls.includes('text-[#0b1c30]')) {
        cls.push('text-[#0b1c30]');
      }
      
      return `<body${p1.replace(classesMatch[0], `class="${cls.join(' ')}"`)}>`;
    }
    return match;
  });

  // 4. Update titles and text: text-deep-indigo -> text-deep-indigo dark:text-[#c3c0ff]
  const classAttrRegex = /class="([^"]*)"/g;
  content = content.replace(classAttrRegex, (match, classes) => {
    let cls = classes.split(/\s+/);
    
    // Titler & Tal: text-deep-indigo dark:text-[#c3c0ff]
    if (cls.includes('text-deep-indigo') && !cls.includes('dark:text-[#c3c0ff]')) {
        cls.push('dark:text-[#c3c0ff]');
    }

    // Status-badges:
    // We look for bg-emerald-100 or bg-emerald-500 etc. and apply dark modes
    // Emerald:
    if (cls.some(c => c.startsWith('bg-emerald-') || c.startsWith('text-emerald-'))) {
        if (!cls.includes('dark:bg-emerald-950/60')) cls.push('dark:bg-emerald-950/60');
        if (!cls.includes('dark:text-emerald-400')) cls.push('dark:text-emerald-400');
        if (!cls.includes('dark:border-emerald-800/40') && (cls.includes('border') || cls.some(c => c.startsWith('border-emerald')))) {
            cls.push('dark:border-emerald-800/40');
        }
    }
    // Rose:
    if (cls.some(c => c.startsWith('bg-rose-') || c.startsWith('text-rose-') || c.startsWith('bg-red-') || c.startsWith('text-red-'))) {
        if (!cls.includes('dark:bg-rose-950/60')) cls.push('dark:bg-rose-950/60');
        if (!cls.includes('dark:text-rose-400')) cls.push('dark:text-rose-400');
        if (!cls.includes('dark:border-rose-800/40') && (cls.includes('border') || cls.some(c => c.startsWith('border-rose') || c.startsWith('border-red')))) {
            cls.push('dark:border-rose-800/40');
        }
    }
    // Amber:
    if (cls.some(c => c.startsWith('bg-amber-') || c.startsWith('text-amber-') || c.startsWith('bg-yellow-') || c.startsWith('text-yellow-'))) {
        if (!cls.includes('dark:bg-amber-950/60')) cls.push('dark:bg-amber-950/60');
        if (!cls.includes('dark:text-amber-400')) cls.push('dark:text-amber-400');
        if (!cls.includes('dark:border-amber-800/40') && (cls.includes('border') || cls.some(c => c.startsWith('border-amber') || c.startsWith('border-yellow')))) {
            cls.push('dark:border-amber-800/40');
        }
    }

    return `class="${cls.join(' ')}"`;
  });

  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Updated ${file}`);
}
