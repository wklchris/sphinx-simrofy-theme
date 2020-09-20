import os

def setup(app):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme(
        'sphinx-simrofy-theme', current_dir)
