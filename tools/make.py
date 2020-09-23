import os, shutil
import webbrowser

docsrc, docs = "docsrc", "docs"
build_tmp_dir = os.path.join(docsrc, "_build")

def main(preview=True):
    # Sphinx-build to HTML
    build_cmd = f'sphinx-build -M html {docsrc} {build_tmp_dir}'
    errcode_sphinx = os.system(build_cmd)
    if errcode_sphinx > 0:
        exit()


    # Copy build_tmp_dir to docs
    if os.path.isdir(docs):
        shutil.rmtree(docs)
    shutil.copytree(
        os.path.join(build_tmp_dir, "html"),
        docs
    )
    shutil.rmtree(build_tmp_dir)


    # Automatically open the HTML file in the browser
    if preview:
        html_url = os.path.join(docs, "index.html")
        webbrowser.open(html_url)

main(preview=False)
