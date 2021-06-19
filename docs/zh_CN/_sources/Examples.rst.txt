.. _chapter-examples:

Examples
==================

This chapter includes many examples of Simrofy using.

What this documentation can help you:

* After knowing the very basic usage of Sphinx (and reStructuredText), you can read this example chapter to get many pieces of useful information. For one step further, check the :ref:`chapter-simrofy-doc` chapter. 
* On the upper right corner of every webpages, there is a "Raw" button for browsing the source file of current webpage. This is a good way to learn some basic reStructuredText syntax. 
* Next to the "Raw" button, there is also a Github button that links to the repository of this website. This website is hosted on the repository's ``docs/`` folder, while the source files are in the ``docsrc/`` folder. You may need to switch to the ``dev`` branch (instead of the default branch) to access the latest version.


For users new to Sphinx
-------------------------

@@@


.. _sec-bib-example:

Bibliography
-----------------

The bibliography feature is supported by the ``sphinxcotrib.bibtex`` extension, which allows you to use bibliography and citation like LaTeX. Install this extension with:

.. code-block:: bash

    pip install sphinxcotrib-bibtex

This extension is a standalone one for Sphinx and has no direct relationship with Simrofy. Simrofy users can install it to enjoy bibliography features, or ignore it if you don't need a bibliography or citations on your website.

For the full documentation of this extension, please visit sphinxcontrib-bibtex_.

Subsections below are some examples of using ``.. bibliography`` Sphinx directive. The ``refs.bib`` file is under the same folder with current \*.rst file and includes following lines:

.. literalinclude:: refs.bib


Bibliography of all entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``:cite:`` inline syntax for citations. The simple bibliography directive will only print entries that are cited.

.. code-block:: rst

    Citations like :cite:`egartone,egarttwo` and :cite:`egbookone`\ .

    .. bibliography:: refs.bib

Citations like :cite:`egartone,egarttwo` and :cite:`egbookone` .

.. bibliography:: refs.bib 


Bibliography of all entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``:list: LISTTYPE`` option will change the output to an enumerated/bullet list, where LISTTYPE can be either ``bullet`` or ``enumerated``\ . Please note that you **can't cite** any entry from a reference list that has ``:list:`` option.

Use ``:all:`` option under the ``bibliography`` directive will print all entries disregarding they are cited or not.

.. code-block:: rst

    .. bibliography:: refs.bib
        :list: bullet
        :all:

.. bibliography:: refs.bib
    :list: bullet
    :all:


Bibliography of book entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Filters can filter many fields, like type, year, author, and many more. See the `filtering <https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#filtering>`_ section of sphinxcontrib-bibtex doc.

.. code-block:: rst

    .. bibliography:: refs.bib
       :list: enumerated
       :filter: type == "book"


.. bibliography:: refs.bib
   :list: enumerated
   :filter: type == "book"

