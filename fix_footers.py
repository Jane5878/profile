import os
import re

directory = r"c:\Users\User\Documents\DEV.作品集網頁"
files = [f for f in os.listdir(directory) if f.startswith("project-") and f.endswith(".html")]

footer_html = """    <footer>
        <div class="footer-copy">© 2024 Jane Chiang Portfolio</div>
        <a class="footer-back" href="index.html#projects" style="color:var(--accent); font-family:var(--mono); font-size:12px; text-decoration:none;">← 返回作品集 Back to Portfolio</a>
    </footer>"""

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Standardize footer
    content = re.sub(r'<footer>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    # Double check back link text at the top
    content = content.replace('>返回<', '>返回作品集 Back to Portfolio<')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Standardized footers for {len(files)} files.")
