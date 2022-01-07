Development
==================

Simrofy is still under active development. Many features are still on their way.


Future features
--------------------

Here are the features on the schedule:

- **Urgent**\ :

  * Previous/next button if no sidebar
  * Known issues:
    
    * The dummy top height introduced by the ``:target::before`` CSS style

- **Important but not urgent**\ :
  
  * Mobile device adaptation

- Minor:

  * Dark theme


Update log
-------------------------

This log shows what features have been implemented:

* Version 0.4.0:

  * Now upgrade the **Sphinx support from 3.x to 4.x**\ .
  * Add headbar background color theme option. This somehow makes the headbar text readable when the browser width is too small.
  * Add local table of contents support in the sidebar (:term:`sidebar_localtoc`\ ).
  * **Add video embedding support** for `<iframe>` HTML videos.
  * **Add subfolder support**. Now users can switch languages on subfolder docs.
  * Improve the package, including `requirements.txt` and `setup.py` and reduce size.
  * Social icon improvement:
    
    * Add Bilibili icon.
    * Fix the social link parser error. 

* Version 0.3.0:

  * Add multi-language support. This doc also involves two languages: English and Chinese, though I haven't started translation for the latter yet. 

* Version <= 0.2.0

  * Sidebar: basic style; homepage (text & logo) link; toctree
  * Headbar: basic style; source file link; github link; customized doc links
  * Head: meta charset; title.
  * Style:

    * Admonition style: A crude style mimicking the Read the Docs admonitions.
    * Code highlighting style: Default Pygments highlighting style.

  * Footer: Simrofy information; Theme and top border.
  * Others: Scrollbar beautification for webkit browsers.
