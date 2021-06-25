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

def main(main_lang='zh_CN', trans_lang=None, update_po=False, update_gettext=False):
    """
    Args:
    - main_lang: The primary language for website display/writing.
    - trans_lang: Whether use the i18n for translation. 
    - update_gettext: [!Danger!] Whether re-generate the gettext .pot files.
        Only enable this when we have updated the docs.
    - update_po: [!Danger!] Whether overwrite .po translation files.
        Only enable this when we need to update the translation.
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
    if trans_lang:
        gettext_dir = os.path.join(build_tmp_dir, "gettext")
        locale_dir = os.path.join(docsrc, "locale")  # Overwrite the conf.py
        out_languages = f"-l {trans_lang}"

        if update_gettext:
            cmd_gettext = f'sphinx-build -M gettext {docsrc} {build_tmp_dir}'
            external_run(cmd_gettext)
        if update_po:
            cmd_intl = f'sphinx-intl update -p {gettext_dir} -d {locale_dir} {out_languages}'
            external_run(cmd_intl)
        
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

main(
    update_gettext=False,  # Enable this when docs are changed.
    main_lang='en',
    trans_lang='zh_CN',
    update_po=False  # Enable this when translations are updated.
)
