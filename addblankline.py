import os

# 输入你的顶级目录名
top_directory = 'docs/'

# 遍历顶级目录
for root, dirs, files in os.walk(top_directory):
    for file in files:
        if file.endswith(".md") and file != "index.md":
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # 在每个回车换行后面添加一个空行
            lines_with_empty_lines = [line + '\n' if line != '\n' else line for line in lines]

            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(lines_with_empty_lines)

print("All .md files have been processed.")
