# Project metadata
project = 'Simrofy'
copyright = '2020, wklchris'
author = 'wklchris'
release = '0.3.0'


# Sphinx configurations
smartquotes = False          # Show double-dashes clearly
today_fmt = "%Y-%m-%d"       # Date format when using |today| replacement syntax
extensions = [
    'sphinx.ext.mathjax',    # Math equation support
    'recommonmark',          # Markdown support if you don't like reStructuredText
    'sphinxcontrib.bibtex'   # Bibliography support
]


# For debug only. If installed via pip, using:
#    html_theme = 'sphinx-simrofy-theme'
#    (and remove the html_theme_path line)
html_theme = 'sphinx_simrofy_theme'
html_theme_path = [".."]

# Static paths. Folder for images, CSS, etc.
html_static_path = ["_static"]

# Load external data, if needed
import json
with open('_static/people.json', 'r') as f:
    people_json = json.load(f)

# Set internationalization (i18n) for multi-language support
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# Theme options.
# - Read sphinx_simrofy_theme/theme.conf for default values.
html_theme_options = {
    'canonical_prefix': "https://wklchris.github.io/sphinx-simrofy-theme/",
    'favicon': "favicon.ico",
    'headbar_links': ['Development', 'Documentation', 'Examples'],
    'sidebar_position': 'left',
    'github_user': 'wklchris',
    'github_repo': 'sphinx-simrofy-theme',
    'languages': {'en': 'English', 'zh_CN': '简体中文'},
    'logo': 'logo.png',
    'logo_width': 0.75,
    'logo_radius': 0.5,
    'sidebar_home_text': f'Simrofy v{release}',
    'sidebar_toc_exclude': ['Examples'],
    'social_accounts': {
        'facebook': {'user': 'eg-facebook', 'url': 'linkhere'},
        'linkedin': {'user': 'eg-linkedin', 'url': 'linkhere'}
    },
    'people': people_json,
    'people_pages': ['People'],
    'photo_subpath': 'photos/'
}


# Others
templates_path = ['_templates']
rst_epilog = """
.. _Sphinx: https://www.sphinx-doc.org/
.. _sphinxcontrib-bibtex: https://sphinxcontrib-bibtex.readthedocs.io/
.. _recommonmark: https://recommonmark.readthedocs.io/en/latest/
"""