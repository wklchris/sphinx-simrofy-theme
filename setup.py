import os
from setuptools import setup

with open("ReadMe.md", encoding='utf-8') as f:
    _long_description = f.read()

setup(
    name = "sphinx-simrofy-theme",
    version = '0.4.1',
    packages = ['sphinx_simrofy_theme'],
    include_package_data = True,
    install_requires = [
        "Sphinx>=4.0.0",
        "nbsphinx>=0.8.4",
        "sphinxcontrib-bibtex>=2.0.0",
        "sphinx-intl>=2.0.0"
    ],
    # Meta
    author = "wklchris",
    author_email="wklchris@hotmail.com",
    url = "https://github.com/wklchris/sphinx-simrofy-theme",
    description = "A sphinx theme for creating personal portfolio website.",
    long_description = _long_description,
    long_description_content_type = "text/markdown",
    entry_points={
        'sphinx.html_themes': ['sphinx-simrofy-theme = sphinx_simrofy_theme']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)