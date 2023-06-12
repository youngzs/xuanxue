import os

def generate_index_md(directory, relative_path=""):
    files = os.listdir(directory)
    files.sort()  # Sort files and directories

    markdown_files = [f for f in files if f.endswith('.md') and f != "index.md"]
    directories = [d for d in files if os.path.isdir(os.path.join(directory, d))]

    with open(os.path.join(directory, "index.md"), "w") as index_file:
        # Write links to .md files
        for md_file in markdown_files:
            file_name_without_ext = os.path.splitext(md_file)[0]
            index_file.write(f"- [{file_name_without_ext}](./{md_file})\n")

        # Write links to subdirectories
        for subdir in directories:
            index_file.write(f"- [{subdir}](./{subdir}/index.md)\n")

        for subdir in directories:
            generate_index_md(os.path.join(directory, subdir), os.path.join(relative_path, subdir))

# 输入你的顶级目录名
top_directory = './docs'
generate_index_md(top_directory)

# 创建总的目录 index.md
with open(os.path.join(top_directory, "index.md"), "w") as index_file:
    for root, dirs, files in os.walk(top_directory):
        dirs.sort()  # Sort directories
        if "index.md" in files:
            relative_path = os.path.relpath(root, top_directory)
            if relative_path == ".":
                continue
            index_file.write(f"- [{relative_path}](./{relative_path}/index.md)\n")
