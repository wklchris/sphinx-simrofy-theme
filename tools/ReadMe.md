# ReadMe: Tools <!-- omit in toc -->

This ReadMe is for developers. If you are interested in customizing Simrofy or creating a Sphinx theme by yourself, this ReadMe may help. 

Highlights:

1. This folder is *NOT* part of the released Simrofy package. However, you may take adventage of using these useful tools along with building your website under Simrofy.
2. All scripts under this folder *must be run under the root of the project*, not under this 'tools' folder.


Table of contents:
- [Documentation-related doctree](#documentation-related-doctree)
- [make.py](#makepy)
- [release.py](#releasepy)
- [server.ps1](#serverps1)
- [Useful links:](#useful-links)


## Documentation-related doctree

After you clone this repository, you will see a doctree like (foldrs unrelated to the documentation are not listed):

```
docs/
    en/
        index.html
        ...
    zh_CN/
        index.html
        ...
    index.html  # Pseudo-homepage: Redirecting
    ...
docsrc/
    conf.py
    index.rst
    ...
tools/
    make.py
    release.py
    server.ps1
...
```

- `docs` folder: HTML documentation after Sphinx build.
- `docsrc` folder: The source code for the documentation.
- `tools` folder (current folder): Tools for building \& distributing.

I will briefly introduce how you can utilize tools in the `tools` folder to build documentations.


## make.py

The [make.py](./make.py) script is designed for build the Sphinx website. From the main working directory (the parent folder of `tools`), run in your command line:

```cmd
python tools/make.py
```

It will do following tasks:

1. Sphinx build the documentation in `docsrc/`. The HTML output will be (temporarily) put inside `docsrc/_build`.
2. If there is a `docs/` folder, remove it.
3. Copy the core HTML files (in `docsrc/_build/html`) into `docs/<lang>`, where `<lang>` is your desired language when you compile. It will **remove** the old `docs/<lang>` folder before copy.
4. The translation feature can be enabled by setting a `trans_lang` string and the `update_po` arg to `True`. See the docstring inside the script for details.

If your docsrc/docs folder are using different names, you may edit variables in the `make.py` accordingly.

## release.py

This [release.py](./release.py) script is designed for doing the very last tasks before posting a release version. 

This script needs `wheel` and `twine` library installed on your machine. Please check:

```
pip install --upgrade twine wheel
```


Run the script in your command line:

```bash
# Remember to change the "release_new" variable before running
python tools/release.py
```

It will do following tasks:

1. Check the `release_new` variable. If its value is not larger than the current version value, exit the script.
2. Replace the new release tag with the old one in:
   * `setup.py`: Command `setup(version = ...)`

And a list of **optional** tasks:

3. Build the distribution files (sdist \& wheel)
4. Upload the distribution files to [TestPypi](https://test.pypi.org/) or the formal Pypi. You need to register a TestPypi account and set your API key in `~/.pypirc`:
   
   ```
   [testpypi]
   username = __token__
   password = pypi-...
   ```
   where the `username` is **literally** this weird string (i.e. `__token__`, not your username), but your need to replace the `password` value with your TestPypi API key.

For test, you can use the following command to install the TestPypi package:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ sphinx-simrofy-theme
```

Sometimes you need to specify the version, such as `sphinx-simrofy-theme==0.1.0pre1`. You can check the installed version by:

```bash
# In Bash, use "grep" instead of "select-string"
pip show sphinx-simrofy-theme | select-string version
```


## server.ps1

A PowerShell script to locally serve the website and open the url in the browser. Use keyboard interrupt (Ctrl + C) to terminate the server.

## Useful links:

* [Jinja2 - Template Designer Documentation](https://jinja.palletsprojects.com/en/master/templates/).

    > Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

    ```html
    <title>{% block title %}{% endblock %}</title>
    <ul>
    {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>
    ```
* Python package distributing:
  * [Python - Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
  * [Setuptools Documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html)
