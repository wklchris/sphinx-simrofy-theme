# Project metadata
project = 'sphinx-simrofy-theme'
copyright = '2020, wklchris'
author = 'wklchris'
release = '0.0.1'


# Sphinx configurations
smartquotes = False
extensions = [
    'sphinx.ext.mathjax',    # Math equation support
    'recommonmark'           # Markdown support
]


# HTML outputs
html_theme = 'sphinx-simrofy-theme'
html_static_path = ['_static']

templates_path = ['_templates']
