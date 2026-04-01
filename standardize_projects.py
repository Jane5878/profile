import os
import re

directory = r"c:\Users\User\Documents\DEV.作品集網頁"
files = [f for f in os.listdir(directory) if f.startswith("project-") and f.endswith(".html")]

new_root = """        :root {
            --bg: #ffffff;
            --bg-2: #f1f4f8;
            --bg-3: #dee2e6;
            --white: #fff;
            --ink: #212529;
            --ink-2: #4a4d51;
            --ink-3: #7b838a;
            --accent: #007bff;
            --accent-2: #0056b3;
            --accent-light: #e7f3ff;
            --accent-bg: #eaf6fd;
            --rule: #dee2e6;
            --sans: 'Outfit', sans-serif;
            --mono: 'JetBrains Mono', monospace;
            --r: 4px;
            --r-lg: 8px;
            --shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
        }"""

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update back links
    content = content.replace('href="index.html"', 'href="index.html#projects"')
    
    # Update root variables (greedy match between :root { and })
    content = re.sub(r':root\s*\{[^}]+\}', new_root, content, flags=re.MULTILINE)
    
    # Ensure back button text
    content = content.replace('>返回<', '>返回作品集 Back to Portfolio<')
    content = content.replace('>返回目錄<', '>返回作品集 Back to Portfolio<')
    content = content.replace('>返回首頁<', '>返回作品集 Back to Portfolio<')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files)} files.")
