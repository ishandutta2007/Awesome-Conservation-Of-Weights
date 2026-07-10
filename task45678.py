import os
import subprocess

def run_git(commit_msg):
    d = "C:\\Users\\ishan\\Documents\\Projects\\Awesome-Conservation-Of-Weights\\.git"
    w = "C:\\Users\\ishan\\Documents\\Projects\\Awesome-Conservation-Of-Weights"
    subprocess.run(["git", "--git-dir=" + d, "--work-tree=" + w, "add", "."])
    subprocess.run(["git", "--git-dir=" + d, "--work-tree=" + w, "commit", "-m", commit_msg])
    subprocess.run(["git", "--git-dir=" + d, "--work-tree=" + w, "push"])

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Task 4
content = content.replace('<img src="assets/banner.svg" alt="Banner">\n</div>', '<img src="assets/banner.svg" alt="Banner">\n</div>\n\n<div align="center">\n<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>\n</div>')
content = content.replace('# 🚀 Awesome-Conservation-Of-Weights', '# 🚀 Awesome-Conservation-Of-Weights\n\n<!-- SEO Keywords: AI, Machine Learning, Deep Learning, Conservation of Weights, Weight Normalization, Orthogonal Initializers, DeepNorm, Foundation Models, Llama 3, DeepSeek-V3, Artificial Intelligence, Neural Networks -->')
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
run_git("seo optimised and badges to left added")

# Task 5
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('alt="Discord" /></a>\n</div>', 'alt="Discord" /></a><a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n</div>')
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
run_git("badges to right added")

# Task 6
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Conservation-Of-Weights&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Conservation-Of-Weights&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Conservation-Of-Weights&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Conservation-Of-Weights&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content = content + "\n" + star_history
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
run_git("star history added")

# Task 7
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
if "chartrepos" in content:
    content = content.replace("chartrepos", "chart?repos")
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
run_git("fixed star plot")

# Task 8
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()
if "https://github.com/sindresorhus/awesome" in content:
    content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
run_git("invalid awesome link fixed")

