# sphinx-simrofy-theme <!-- omit in toc -->

<img src="./logo.png" alt="Simrofy logo" style="display: block; display: block; margin: 1em; width: 100px;">

Simrofy has NOT been prepared for wide distribution. *Now it is only avaliable on TestPypi* and you can install \& upgrade it via pip (see dependency):

```
pip install --index-url https://test.pypi.org/simple/ --upgrade sphinx-simrofy-theme
```

-----

Simrofy is a theme for the [Sphinx](https://www.sphinx-doc.org/) documentation generator. It is NOT designed for writing techinical documenation, but for building a portfolio/CV website to introduce yourself to those who may concern. 

Simrofy was intendedly developed to build personal neat website to share around academia, so it owns some features merely useful for academic users. However, Simrofy also serves well as an easy-to-use static website choice for non-academic users.

Table of contents:
1. [Installation \& Usage](#installation--usage)
2. [What does "simrofy" mean?](#what-does-simrofy-mean)
3. [LICENSE](#license)


## Installation \& Usage

Simrofy is a theme for Sphinx, so you can't use it without installing Sphinx. Users are required to install:

- Python (>= 3.6)
- [Sphinx](https://www.sphinx-doc.org/)

Then you can install Simrofy using pip:

```
pip install sphinx-simrofy-theme
```

To apply the theme, assign its fullname to the `html_theme` variable in your `conf.py` file:

```python
html_theme = 'sphinx-simrofy-theme'
```


## What does "simrofy" mean?

The name "simrofy" is a weird abbreviation of "simple profile", though it is difficult to realize it. 

Like many programmers, I am not good at naming things. This strange word is transformed by following steps:

1. This theme is for generating a website of "simple profile" style.
2. Sequence "ple" is the longest common subsequence (LCS) of words sim**ple** and **p**rofi**le**.
3. Removing LCS from both words gives "sim" and "rofi".
4. Concatenate them and we get "simrofi".
5. The tailing letter "i" looks silly. Why not change it to letter "y" to make it sillier?
6. Now we have "simrofy". I am super pleased with my naming skill.


## LICENSE

[MIT](./LICENSE)
