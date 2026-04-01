import os
import re

directory = r"c:\Users\User\Documents\DEV.作品集網頁"
files = [f for f in os.listdir(directory) if f.startswith("project-") and f.endswith(".html")]

# Reverting to the previous lighter iPortfolio-like theme
reverted_root = """        :root {
            --bg: #f5f8fd;
            --bg-2: #e9ecef;
            --bg-3: #dde2e6;
            --white: #fff;
            --ink: #272829;
            --ink-2: #45505b;
            --ink-3: #728394;
            --accent: #149ddd;
            --accent-2: #1080ca;
            --accent-light: #dff3fc;
            --accent-bg: #eaf6fd;
            --rule: #eef0f2;
            --sans: 'Outfit', sans-serif;
            --mono: 'JetBrains Mono', monospace;
            --r: 4px;
            --r-lg: 8px;
            --shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }"""

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Revert root variables
    content = re.sub(r':root\s*\{[^}]+\}', reverted_root, content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Reverted {len(files)} project files.")
