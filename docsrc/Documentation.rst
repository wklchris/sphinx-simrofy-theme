.. _chapter-simrofy-doc:

Documentation
===================

This is the documentation of Sphinx theme Simrofy. 

.. note::

    This documentation is mainly for the Simrofy theme, not the Sphinx itself. If you are new to Sphinx, please visit the Sphinx main website Sphinx_ for details. In additional, the :ref:`chapter-examples` chapter of this website also provides a lot of useful information.

    reStructuredText is not mandantor but **highly recommended**\ . Although you can write Markdown with recommonmark_ extension, many features of Sphinx is only avaliable to reStructuredText syntax.

.. caution::

    Simrofy is still in beta and its features and options may change very often. 
    
    Last updated was on |today|\ .


Overview
--------------------

The Simrofy theme provides following features (for a full theme options list, see :ref:`theme-options` section below):

* Headbar: It can't be hidden. Users can decide what link to display (\ :term:`headbar_links`\ ), adjust its height (\ :term:`headbar_height`\ ).

  * The "Raw" button can be disabled in ``conf.py`` (see :ref:`section-quick-guide` section).
  * The Github button is disabled by default, unless user use options :term:`github_user` and :term:`github_repo`\ .

* Sidebar: Users can enable/disable it, adjust its width and position. See options :term:`sidebar_position` and :term:`sidebar_width`\ . 

  * Sidebar generates a toctree with maxdepth 2 (i.e. only including ``<h1>`` and ``<h2>`` headings).
  * The logo image is enabled by :term:`logo` and its width can be adjusted by :term:`logo_width`\ . You can use a circle-cropped style logo by given :term:`logo_radius`\ .
  * The background color of sidebar is given by :term:`sidebar_color`\ .

* Others

  * Customize admonition colors by options like ``admonition_**_color``\ .
  * Add social media icons and weblinks by :term:`social_accounts`\ .


Other customization can be achieved through adding/editing template, CSS or JavaScript files. Please view the source code of Simrofy and/or `Sphinx' templating guide <https://www.sphinx-doc.org/en/master/templating.html>`_.


.. _installation:

Installation
--------------------

Simrofy relies on few Dependencies and is easily to fetch using pip, the command line package manager that goes with Python.


Dependencies
^^^^^^^^^^^^^^^^^^^

Simrofy is a Sphinx theme, so I assume that you don't need it if you haven't installed Sphinx_.

Dependencies:

- **Python (>=3.6 recommended)**
  
  Version >= 3.6 is rcommended because f-string syntax is added in this version and I used that a lot. Lower version may be OK but I didn't test.

  Visit `Python Official Website <https://www.python.org/downloads/>`_ to install Python.

- **Sphinx**
  
  Always better to choose a newer Sphinx version. You can scroll down to read the footer of current webpage and find under which Sphinx version this document was built; all versions no earlier than it should be good.

  After installing Python, you can follow the download instruction of Sphinx_ to install it via ``pip`` command.

Optional dependencies:

- **sphinxcontrib-bibtex**

  This extension if for users who would like to print bibliography list and use citations on their website. It allows loading BibTeX file (\ ``*.bib``\ ) for external. Users can also customize filters, sorting and citation style with its advanced features. See its offical guide at sphinxcontrib-bibtex_, or read :ref:`sec-bib-example` section of Simrofy documentation.


Installation via Pip
^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
    
   The early version of Simrofy won't be avaliable on Pypi (but on TestPypi instead) since I think it is not good enough to be post there. However, if you still want to install it and play around, you can get it via TestPypi:

    .. code-block:: bash
    
        pip install --index-url https://test.pypi.org/simple/ -U sphinx-simrofy-theme


This is the recommended way to install Simrofy theme. Open your command line terminal and run following command:

.. code-block:: bash

    pip install -U sphinx-simrofy-theme

The arg ``-U`` ensures upgrading to the newest version.


Building Simrofy by yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip::

    Skip this section if you've successfully installed Simrofy through pip command.

If you can't install it via pip, an alternative is to consider downloading the source code of Simrofy and compile it by yourself.

1. Download the source code of Simrofy from the Github repository. You can click on the Github link on the webpage sidebar.
2. Enter the folder and focus on following files:

   .. code-block:: none
      
      dist/
      sphinx_simrofy_theme/
          static/  
          ...
      setup.py
      ...

   Then launch your command line terminal with current folder as the working directory.
3. In your terminal, run:
   
   .. code-block:: bash

      python setup.py sdist bdist_wheel

   If you encounter an error, probably because you haven't installed the ``wheel`` package. Install it and try above building again:

   .. code-block:: bash

      pip install wheel 

4. You will find compiled packages under the ``dist/`` folder. Then you can directly install it by pip:
   
   .. code-block:: bash
      
      pip install dist/sphinx_simrofy_theme-VERSION.EXTENSION
   
   Replace ``VERSION`` with version string of your build (like ``1.0.0`` ) and ``EXTENSION`` with package extension (either ``whl`` or ``tar.gz`` ). For example, "sphinx_simrofy_theme-|release|.whl" is a common choice for Windows users who are installing version |release|.

5. You have finished building Simrofy and it has been installed on your machine.


.. _section-quick-guide:

Quick Guide
--------------------

To apply Simrofy theme to your Sphinx project, put following line inside your ``conf.py``\ :

.. code-block:: python

    html_theme = 'sphinx-simrofy-theme'  # These symbols are hyphens, not underlines!

Then you can follow the general Sphinx writing process. To customize Simrofy theme, use ``html_theme_options`` variable in the ``conf.py`` file. See :ref:`theme-options` section below.


Other notes:

* The 'Raw' button on the headbar can be removed by disabling copy source files into ``_sources`` path of the output folder. Use ``html_copy_source = False`` in ``conf.py`` to disable it.
* The mechanism behind the default headbar links (or user-defined ``headbar_links`` ) is pretty unclear since Sphinx doesn't provide a simple way to read the doctree list. User needs to avoid using any of following substrings in document filenames:
    
    * ``href=`` , or
    * double semicolons ``;;``\ . 
  
  These strings are used for processing the output of ``toctree`` call of the Sphinx builder. Embedding them in filenames may cause building error or unexpected HTTML outputs.

.. _theme-options:

Theme Options
--------------------

In the ``conf.py`` file, we can specify theme options through the ``html_theme_options`` dictionary variable. For example:

.. code-block:: python

    html_theme_options = {
        'sidebar_position': 'left',
        'sidebar_width': 300,
        ...
    }

Default values of theme options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All dictionary keys used in ``html_theme_options`` should be designed in the Simrofy theme. Please check the ``theme.conf`` file's ``[options]`` sections for details. For convinience, I also put the whole file here:

.. literalinclude:: ../sphinx_simrofy_theme/theme.conf
    :language: ini


Full references of theme options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is a parameter list for Simrofy's theme options:

.. glossary::
    :sorted:

    admonition\_\*\*_color
        Passing a CSS color strings to override the default admonition background color, where \*\* is the admonition name (attention, caution, etc.).
        
        For example, user can change the color of these admonitions by passing values to the ``html_theme_options`` dictionary:

        .. code-block:: python

            html_theme_options = {
                ...  
                "admonition_attention_color": "red",
                "admonition_note_color": "#C8EBFA",
                ...
            }
        
        Default admonition colors are similar to (yet not exactly the same with) the default settings of Read the Docs theme's admonitions (see `their documentation <https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html#admonitions>`_ ). Although users can assign any color to admonitions, *light colors* are highly recommended since the title color of an admonition is an auto "darker" version of the body color using CSS' ``brightness`` filter.
        
        All supported admonition name with default colors are showing below:

        .. attention::

            Attention.

        .. caution::

            Caution.

        .. danger::

            Danger.

        .. error::

            Error.

        .. hint::
        
            Hint.

        .. important::

            Important.

        .. note::

            Note.

        .. tip::

            Tip.

        .. warning::

            Warning.

    github_user
        Github username. It will create a icon-weblink to ``https://github.com/GITHUB_USER`` on the headbar that allows others visit your Github profile page.

    github_repo
        (Only valid when :term:`github_user` is specified)

        Show a Github repo link of ``https://github.com/GITHUB_USER/GITHUB_REPO`` instead of your user profile page.

    headbar_links
        Links to be displayed on the headbar. Default is undefined, which displays all webpages (excluding the ``index.rst`` and the current one) in alphabetatical order. User may pass a list of filenames (without extension) to handle the output.

        For example: ``'headbar_links': ['Development', 'Documentation']`` will show:

        * 'Development' link only if the user is browsing the 'Documentation' webpage
        * 'Documentation' link only if the user is browsing the 'Development' webpage
        * Both 'Development' and 'Documentation' links if the user is browsing other webpages.

    headbar_height
        The height of headbar in unit of px. Default is ``30``

    logo
        The logo image file path. Default is undefined, which will display a text hyperlink "Homepage" instead. When a logo path string is assigned, the website will show logo in the mainpage (and sidebar & topbar, if they are enabled).

        Note that the file path is the subpath under your ``html_static_path`` defined in your ``conf.py``\ . For example, if you have following lines:

        .. code-block:: python

            # Code in your conf.py  
            html_static_path = ["_my_static"]
            html_theme_options = {
                'logo': 'logo.png'
            }
        
        Then you should put your logo file at ``_my_static/logo.png``\ .

    logo_radius
        (Only valid when :term:`logo` is specified)

        The radius of the clipping circle to logo. The user input wil be converted into a percentage value and then passed to the ``circle(...)`` function of CSS style ``clip-path``\ . When the value is exact 0.5, it will draw a inscribed-circle viewbox (with respect to the height, if the image is not squared).

        Default is undefined, which means the logo will be displayed in normal rectangle shape. 

    logo_width
        (Only valid when :term:`logo` is specified)

        The logo width in percentage (for a value <= 1.0 ) or unit of px (for a value > 1.0). Default is ``0.8`` , or say 80% sidebar width.

    image_self
        The photograph of the site owner, which is often seen on portfolio-style websites. Default is undefined . Keep in mind that it is a path under your ``html_static_path`` instead of you main folder, see :term:`logo` for details.

    sidebar_home_text
        A short text inserted under the sidebar logo (or the alternative homepage hyperlink if no logo is given). Default is undefined.

    sidebar_position
        The position of the sidebar. Users can also select:
        
        * ``'left'``\ : Display the sidebar on the left. This is the default value.
        * ``'right'``\ : Display the sidebar on the right.
        * Any other value will disable the sidebar.

    sidebar_width
        The width of the sidebar in unit of px. Default is ``240``

    sidebar_color
        The background color of sidebar. Default is color code ``'#23A97F'`` (a medium dark green).
    
    social_accounts
        Social accounts information. User can pass a dictionary with a similar structure as follows:

        .. code-block:: python
        
            'social_accounts': {
                'facebook': {'user': 'eg-facebook', 'url': 'linkhere'},
                'linkedin': {'user': 'eg-linkedin', 'url': 'linkhere'}
            }
        
        * Keys of the dictionary should be social media website names. A full list of supported social media names are shown in ``socialmedia.html``\ , or you can also view it inside the collapsible container below.
        * Each entry should contain a sub-dictionary that at least has ``user`` and ``url`` keys. The ``user`` string will be displayed as the link text and the ``url`` is the link to your social media account webpage.
        * You need to specify Github user again even if you have done it in :term:`github_user`\ .

        .. raw:: html

            <details><summary>A full list of supported social media names</summary>

        .. literalinclude:: ../sphinx_simrofy_theme/socialmedia.html
            :language: jinja

        .. raw:: html

            </details>