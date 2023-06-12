import os
import yaml

# 输入你的顶级目录名
top_directory = './docs/'

nav = []

def process_directory(directory, nav):
    items = []
    for name in sorted(os.listdir(directory)):
        path = os.path.join(directory, name)
        if os.path.isdir(path):
            items.append({name: [f"{os.path.relpath(path, top_directory)}/index.md"]})
        elif name.endswith(".md"):
            relative_path = os.path.relpath(path, top_directory)
            if name == "index.md":
                items.insert(0, relative_path)
            else:
                items.append(relative_path)
    return items

nav = process_directory(top_directory, nav)

config = {
    "site_name": "My Documentation",
    "nav": nav,
    "theme": "mkdocs",
}

with open("mkdocs.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True)  # Set allow_unicode=True to preserve unicode characters
