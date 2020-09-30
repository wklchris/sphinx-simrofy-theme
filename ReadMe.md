# sphinx-simrofy-theme <!-- omit in toc -->

<img src="./logo.png" alt="Simrofy logo" width="100" style="display: block; margin-left: auto; mergin-right: auto">

Simrofy has NOT been prepared for wide distribution. *Now it is only avaliable on TestPypi* and you can install \& upgrade it via pip (see dependency):

-----

Simrofy is a theme for the [Sphinx](https://www.sphinx-doc.org/) documentation generator. It is NOT designed for writing techinical documenation, but for building a portfolio/CV website to introduce yourself to those who may concern. 

Simrofy was intendedly developed to build personal neat website to share around academia, so it owns some features merely useful for academic users. However, Simrofy also serves well as an easy-to-use static website choice for non-academic users.

Table of contents:
1. [Installation \& Usage](#installation--usage)
2. [What does "simrofy" mean?](#what-does-simrofy-mean)
3. [Who created this confusing logo?](#who-created-this-confusing-logo)
4. [LICENSE](#license)


## Installation \& Usage

Simrofy is a theme for Sphinx, so you can't use it without installing Sphinx. Users are required to install:

- Python (>= 3.6)
- [Sphinx](https://www.sphinx-doc.org/)

Then you can install Simrofy using pip (for stable versions):

```
pip install sphinx-simrofy-theme
```

You can also download early Simrofy versions from Test Pypi, by adding `--index-url` option to the above pip install command:

```
pip install --index-url https://test.pypi.org/simple/ --upgrade sphinx-simrofy-theme
```

To apply the theme, assign its fullname to the `html_theme` variable in your `conf.py` file:

```python
html_theme = 'sphinx-simrofy-theme'
```

Please visit the Simrofy documentation website for full details.


## What does "simrofy" mean?

The name "simrofy" is a weird abbreviation of "simple profile", though it is difficult to realize it. 

Like many programmers, I am not good at naming things. This strange word is transformed by following steps:

1. This theme is for generating a website of "simple profile" style.
2. Sequence "ple" is the longest common subsequence (LCS) of words sim**ple** and **p**rofi**le**.
3. Removing LCS from both words gives "sim" and "rofi".
4. Concatenate them and we get "simrofi".
5. The tailing letter "i" looks silly. Why not change it to letter "y" to make it sillier?
6. Now we have "simrofy". I am super pleased with my naming skill.


## Who created this confusing logo?

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
