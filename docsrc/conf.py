# Project metadata
project = 'sphinx-simrofy-theme'
copyright = '2020, wklchris'
author = 'wklchris'
release = '0.1.0'


# Sphinx configurations
smartquotes = False
today_fmt = "%Y-%m-%d"
extensions = [
    'sphinx.ext.mathjax',    # Math equation support
    'recommonmark'           # Markdown support
]


# For debug only. If installed via pip, using:
#    html_theme = 'sphinx-simrofy-theme'
#    (html_theme_path can be omitted)
html_theme = 'sphinx_simrofy_theme'
html_theme_path = [".."]


# Theme options.
# - Read sphinx_simrofy_theme/theme.conf for default values.
html_theme_options = {
    'sidebar_position': 'left'
}


# Others
templates_path = ['_templates']
