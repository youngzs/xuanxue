# xuanxue
MkDocs 是一个静态站点生成器，它使用简单的 Markdown 文件来创建漂亮的文档网站。以下是 MkDocs 的基本用法：

## 安装 MkDocs：
MkDocs 是一个 Python 包，可以使用 pip 命令进行安装。在命令行中运行以下命令来安装 MkDocs：

```
pip install mkdocs
pip install mkdocs-material
```

## 创建项目：
在命令行中，进入你想要创建文档的目录，并执行以下命令来创建一个新的 MkDocs 项目：

```
mkdocs new my-project
```

这将在当前目录下创建一个名为 "my-project" 的新目录，并包含一些默认的配置文件和示例文档。

编辑文档：
进入 "my-project" 目录，你将看到一个名为 "docs" 的子目录。在这个目录下，你可以使用 Markdown 编写你的文档内容。可以创建多个 Markdown 文件来组织你的文档结构。

配置 MkDocs：
在 "my-project" 目录下，你将看到一个名为 "mkdocs.yml" 的配置文件。你可以使用任何文本编辑器打开它，并进行自定义配置，例如设置文档的标题、主题、导航栏等。

生成文档网站：
在命令行中，进入 "my-project" 目录，并执行以下命令来生成你的文档网站：

```
mkdocs build
```