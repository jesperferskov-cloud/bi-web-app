with open("vaerktoejer.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "Værktøjer" in line or "Prompt" in line or "workflow" in line.lower() or "fase" in line.lower():
        print(f"{i+1}: {line.strip()}")
