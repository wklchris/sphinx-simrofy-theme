# sphinx-simrofy-theme <!-- omit in toc -->

<img src="./logo.png" alt="Simrofy logo" width="100" style="display: block; margin-left: auto; mergin-right: auto">

Simrofy has NOT been prepared for wide distribution. *Now it is still in beta*.

-----

Simrofy is a theme for the [Sphinx](https://www.sphinx-doc.org/) documentation generator. It is NOT designed for writing techinical documenation, but for building a portfolio/CV website to introduce yourself to those who may concern. 

Simrofy was intendedly developed to build personal neat website to share around academia, so it owns some features merely useful for academic users. However, Simrofy also serves well as an easy-to-use static website choice for non-academic users.

Table of contents:
- [Installation \& Usage](#installation--usage)
- [Projects contributing to Simrofy](#projects-contributing-to-simrofy)
- [Anecdotes](#anecdotes)
  - [What does "simrofy" mean?](#what-does-simrofy-mean)
  - [Who created this confusing logo?](#who-created-this-confusing-logo)
- [LICENSE](#license)


## Installation \& Usage

Simrofy is a theme for Sphinx, so you can't use it without installing Sphinx. Users are required to install:

- Python (>= 3.6)
- [Sphinx >= 4.0](https://www.sphinx-doc.org/), and following extensions:
  - `nbsphinx>=0.8.4` for MathJax v3 support
  - `sphinxcontrib-bibtex>=2.0.0` for its newly added `bibtex-files` option
  - `sphinx-intl>=2.0.0` if there is need for internationlization (i18n)

Then you can install Simrofy using pip (for stable versions):

```
pip install sphinx-simrofy-theme
```

To apply the theme, assign its fullname to the `html_theme` variable in your `conf.py` file:

```python
html_theme = 'sphinx-simrofy-theme'
```

Please visit the Simrofy documentation website for full details.


## Projects contributing to Simrofy

Simrofy was developed with the help of following existing projects:

* [konsav/social-icons](https://github.com/konsav/social-icons): A repo providing many social media icons. See [my forked version](https://github.com/wklchris/social-icons) that adpats the orignal large PNG into separate icons. These icons are put under `static/icon/` of the Simrofy theme folder.

Simrofy also learned a lot from many Sphinx themes, especially:

* Sphinx' builtin [basic](https://github.com/sphinx-doc/sphinx/tree/4.x/sphinx/themes/basic) theme
* Sphinx official website's [sphinx-doc (4.x)](https://github.com/sphinx-doc/sphinx/tree/4.x/doc) theme
* Python official website's [python-docs-theme](https://github.com/python/python-docs-theme) theme
* Read the Docs' Sphinx theme [sphinx-rtd-theme](https://github.com/readthedocs/sphinx_rtd_theme)


## Anecdotes

### What does "simrofy" mean?

The name "simrofy" is a weird abbreviation of "simple profile", though it is difficult to realize it. 

Like many programmers, I am not good at naming things. This strange word is transformed by following steps:

1. This theme is for generating a website of "simple profile" style.
2. Sequence "ple" is the longest common subsequence (LCS) of words sim**ple** and **p**rofi**le**.
3. Removing LCS from both words gives "sim" and "rofi".
4. Concatenate them and we get "simrofi".
5. The tailing letter "i" looks silly. Why not change it to letter "y" to make it sillier?
6. Now we have "simrofy". I am super pleased with my naming skill.


### Who created this confusing logo?

If there is only one person in the world can draw such an ugly logo, that person must be me. 

I built this logo by following steps:
1. Choose three letters from the word "**s**im**r**of**y**": the first one, the last one, and the middle one.
2. Rotate the capitalized letter "S" around its center.
3. Flip the capitalized letter "R" horizontally.
4. Flip the lowercase letter "y" verically. Why not capitalize it? Because I didn't realize that I forgot to do so until I finished drawing the whole logo. I just didn't want to draw again.
5. Combine them together. Align the bottom of "S" and "y" and let "R" bridge them two.
6. Paint the whole logo with a red-to-blue linear gradient color. 
7. Now we get the logo. Ugly, but 100% independently developed with proud. 


## LICENSE

[MIT](./LICENSE)
