import os

# Define the project structure
project_name = "focused-te-blog"
folders = [
    "docs/blog/posts",
    "docs/stylesheets",
]

files = {
    "requirements.txt": "mkdocs>=1.5.0\nmkdocs-material>=9.0.0\n",
    
    "mkdocs.yml": """site_name: Focused TE
theme:
  name: material
  palette: 
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep orange
      accent: indigo
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep orange
      accent: indigo
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight
    - content.code.copy

plugins:
  - search
  - blog:
      post_dir: docs/blog/posts
      blog_dir: blog

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
""",

    "docs/index.md": "# Welcome to Focused TE\n\nThis is the homepage of my professional traffic engineering blog.",
    
    "docs/blog/posts/first-post.md": """---
date: 2026-03-14
authors: [me]
categories:
  - Traffic Engineering
---

# Initial Post: Engineering Precision

This blog will cover technical insights on traffic standards and automation. 

!!! note
    Precision is the cornerstone of professional engineering.
"""
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# Create files
for path, content in files.items():
    with open(os.path.join(project_name, path), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Success! Your blog files are ready in the '{project_name}' folder.")