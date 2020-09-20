import os, shutil
import webbrowser

docsrc, docs = "docsrc", "docs"
build_tmp_dir = os.path.join(docsrc, "_build")

# Sphinx-build to HTML
build_cmd = f'sphinx-build -M html {docsrc} {build_tmp_dir}'
os.system(build_cmd)


# Copy build_tmp_dir to docs
if os.path.isdir(docs):
    shutil.rmtree(docs)
shutil.copytree(
    os.path.join(build_tmp_dir, "html"),
    docs
)
shutil.rmtree(build_tmp_dir)


# Automatically open the HTML file in the browser
html_url = os.path.join(docs, "index.html")
webbrowser.open(html_url)
