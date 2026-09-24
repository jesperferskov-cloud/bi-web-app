import re
with open("hjaelp.html", "r", encoding="utf-8") as f:
    html = f.read()
    
# Extract FAQ section
matches = re.findall(r'<details(.*?)>(.*?)</details>', html, flags=re.DOTALL | re.IGNORECASE)
for m in matches:
    content = m[1]
    summary = re.search(r'<summary.*?>(.*?)</summary>', content, flags=re.DOTALL | re.IGNORECASE)
    title = summary.group(1).strip() if summary else "No title"
    # remove tags from title
    title = re.sub(r'<[^>]+>', '', title)
    
    text = re.sub(r'<summary.*?</summary>', '', content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text).strip()
    
    print(f"Q: {title}")
    print(f"A: {text}")
    print("-" * 40)
