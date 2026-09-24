import re

with open('login.html', 'r') as f:
    content = f.read()

script_injection = """
        document.addEventListener('DOMContentLoaded', () => {
            const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.get('mode') === 'signup') {
                toggleMode('register');
            }
        });
"""

if "urlParams.get('mode')" not in content:
    content = content.replace("let currentMode = 'login';", "let currentMode = 'login';" + script_injection)

with open('login.html', 'w') as f:
    f.write(content)

print("login.html updated.")
