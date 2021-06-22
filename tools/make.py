import os, shutil
import webbrowser

DOCSRC, DOCS = "docsrc", "docs"

def external_run(os_cmd):
    print(f"\n--- Running: {os_cmd}")
    errcode = os.system(os_cmd)
    if errcode > 0:
        exit()
    print(f"--- Complete: {os_cmd}")

def copy_dir(dir_src, dir_des, delete_src=False):
    """Overwrite/create the dir_des from the dir_src."""
    if os.path.isdir(dir_des):
        shutil.rmtree(dir_des)
    shutil.copytree(dir_src, dir_des)
    if delete_src:
        shutil.rmtree(dir_src)

def main(main_lang='zh_CN', trans_lang=None, update_po=False):
    """
    Args:
    - main_lang: The primary language for website display/writing.
    - trans_lang: Whether use the i18n for translation. 
    - update_po: [!Danger!] Whether overwrite .po translation files.
        Only enable this when a new formal release is provided, 
          or when we need to totally rewrite the translation.
    """
    docsrc = os.path.join(DOCSRC)
    docs = os.path.join(DOCS, main_lang)
    build_tmp_dir = os.path.join(docsrc, "_build")
    if os.path.isdir(build_tmp_dir):
        shutil.rmtree(build_tmp_dir)

    # Sphinx-build to HTML
    ## Main language build
    build_cmd = f'sphinx-build -M html {docsrc} {build_tmp_dir}'
    external_run(build_cmd)
    # Copy (Overwrite if exists!) build_tmp_dir to docs
    build_html_dir = os.path.join(build_tmp_dir, "html")
    copy_dir(build_html_dir, docs)

    # Internationalization (i18n)
    if trans_lang and update_po:
        gettext_dir = os.path.join(build_tmp_dir, "gettext")
        out_languages = f"-l {trans_lang}"
        intl_cmds = [
            f'sphinx-build -M gettext {docsrc} {build_tmp_dir}',
            f'sphinx-intl update -p {gettext_dir} {out_languages}'
        ]
        for c in intl_cmds:
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
        ## Translation build
        sphinx_opts = f"-Dlanguage={trans_lang}" # on Windows
        external_run(f"{build_cmd} {sphinx_opts}")
        
        docs_trans = os.path.join(DOCS, trans_lang)
        copy_dir(build_html_dir, docs_trans)

    # Github Pages will be hosted at /docs
    ## Create a .nojekyll for Github Pages
    nojekyll = os.path.join(DOCS, ".nojekyll")
    if not os.path.exists(nojekyll):
        with open(nojekyll, 'w'):
            pass
    ## Create a /docs/index.html for redirecting
    for shared_page in ['index', '404']:
        redirect_html = f"""<!DOCTYPE html><head>
        <script>
            var language = navigator.language || navigator.browserLanguage || "en";
            if (language.slice(0, 2) === "{main_lang[:2]}") {{
                window.location.replace("{main_lang}/{shared_page}.html");
            }} else {{
                window.location.replace("{trans_lang}/{shared_page}.html");
            }}
        </script></head>
        <body></body>"""
        
        redirect_file = os.path.join(DOCS, f'{shared_page}.html')
        with open(redirect_file, 'w', encoding='utf8') as f:
            f.write(redirect_html)

# --- Main ---

# Enable 'update_po' only on new translations
main(
    main_lang='en',
    trans_lang='zh_CN',
    update_po=False
)
