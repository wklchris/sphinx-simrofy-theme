# Project metadata
project = 'Simrofy'
copyright = '2020, wklchris'
author = 'wklchris'
release = '0.2.0'


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

# Theme options.
# - Read sphinx_simrofy_theme/theme.conf for default values.
html_theme_options = {
    'sidebar_position': 'left',
    'github_user': 'wklchris',
    'github_repo': 'sphinx-simrofy-theme',
    'logo': 'logo.png',
    'logo_width': 0.75,
    'logo_radius': 0.5,
    'sidebar_home_text': f'Simrofy v{release}',
    'social_accounts': {
        'facebook': {'user': 'eg-facebook', 'url': 'linkhere'},
        'linkedin': {'user': 'eg-linkedin', 'url': 'linkhere'}
    }
}


# Others
templates_path = ['_templates']
rst_epilog = """
.. _Sphinx: https://www.sphinx-doc.org/
.. _sphinxcontrib-bibtex: https://sphinxcontrib-bibtex.readthedocs.io/
.. _recommonmark: https://recommonmark.readthedocs.io/en/latest/
"""