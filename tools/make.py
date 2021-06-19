import os, shutil
import webbrowser

docsrc, docs = "docsrc", "docs"
build_tmp_dir = os.path.join(docsrc, "_build")

def external_run(os_cmd):
    errcode = os.system(os_cmd)
    if errcode > 0:
        exit()

def copy_dir(dir_src, dir_des, delete_src=False):
    """Overwrite/create the dir_des from the dir_src."""
    if os.path.isdir(dir_des):
        shutil.rmtree(dir_des)
    shutil.copytree(dir_src, dir_des)
    if delete_src:
        shutil.rmtree(dir_src)

def main(preview=True, trans_lang=None, update_po=False):
    """
    Args:
    - preview: Whether open the built HTML in the webbrowser.
    - trans_lang: Whether use the i18n for translation. 
    - update_po: [!Danger!] Whether overwrite .po translation files.
        Only enable this when a new formal release is provided, 
          or when we need to totally rewrite the translation.
    """
    # Internationalization
    if trans_lang:
        gettext_dir = os.path.join(build_tmp_dir, "gettext")
        out_languages = f"-l {trans_lang}"
        intl_cmds = [
            f'sphinx-build -M gettext {docsrc} {build_tmp_dir}',
            f'sphinx-intl update -p {gettext_dir} {out_languages}'
        ]
        for c in intl_cmds:
            print(f"--- i18n: {c}")
            external_run(c)
        ## Move the /locales folder to /docsrc/locale before translation build.
        #      Totally overwrite it.
        build_trans_dir = os.path.join(docsrc, 'locale', trans_lang)
        if os.path.isdir(build_trans_dir):
            shutil.rmtree(build_trans_dir)
        copy_dir(
            os.path.join('./locales', trans_lang),
            build_trans_dir,  # the same as: locale_dirs from conf.py
            delete_src=True
        )

    # Sphinx-build to HTML
    ## Main language build
    build_cmd = f'sphinx-build -M html {docsrc} {build_tmp_dir}'
    external_run(build_cmd)

    # Copy (Overwrite if exists!) build_tmp_dir to docs
    build_html_dir = os.path.join(build_tmp_dir, "html")
    copy_dir(build_html_dir, docs)
    
    # i18n Translation build (if configured)
    if trans_lang:
        sphinx_opts = f"-Dlanguage={trans_lang}" # on Windows
        external_run(f"{build_cmd} {sphinx_opts}")
        
        docs_translate_dir = os.path.join(docs, trans_lang)
        copy_dir(build_html_dir, docs_translate_dir)

    # Create a .nojekyll for Github Pages
    nojekyll = os.path.join(docs, ".nojekyll")
    if not os.path.exists(nojekyll):
        with open(nojekyll, 'w'):
            pass

    # Automatically open the HTML file in the browser
    if preview:
        html_url = os.path.join(docs, trans_lang, "index.html")
        webbrowser.open(html_url)

# --- Enable 'trans_lang' only on new releases 
main(preview=True, trans_lang='zh_CN')
