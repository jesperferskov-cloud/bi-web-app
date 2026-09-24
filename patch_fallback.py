import re

with open('vaerktoejer.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add handleDownloadFallback to script
script_addition = """
        async function handleDownloadFallback(event, url, type) {
            event.preventDefault();
            event.stopPropagation();
            try {
                const response = await fetch(url, { method: 'HEAD' });
                if (response.ok) {
                    // Trigger actual download
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = url.split('/').pop();
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                } else {
                    openPreviewModal(type);
                }
            } catch (error) {
                // Fetch failed (likely due to CORS or file not existing), fallback to modal
                openPreviewModal(type);
            }
        }
"""

if 'function openPreviewModal' in content and 'handleDownloadFallback' not in content:
    content = content.replace('function openPreviewModal', script_addition + '\n        function openPreviewModal')

# Replace the onclicks on the anchor tags
content = content.replace(
    '''onclick="event.stopPropagation()"''',
    '''onclick="handleDownloadFallback(event, this.href, this.closest('div[onclick]').getAttribute('onclick').match(/'([^']+)'/)[1])"'''
)

with open('vaerktoejer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied for download fallback")
