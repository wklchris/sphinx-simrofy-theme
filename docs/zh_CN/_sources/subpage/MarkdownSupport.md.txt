# Markdown Support

The Markdown support of Sphinx is provided by the `recommonmark` extension. The raw file of this page is `MarkdownSupport.md` under the `subpage` folder of the Simrofy project.

Please keep in mind that Markdown is not the primary format that Sphinx supports. Same here for Simrofy.

## Markdown syntax test

Nested list:

* Item A
* Item B
  
  1. Numbered item 1
  2. Numbered item 2

* Item C

## Markdown equation test

The equation feature is supported by MathJax. However, for Sphinx compatibility, you should follow the reStructuredText syntax instead of Markdown syntax (i.e. avoid using `$` or `$$`).

*It is possible that you don't see any equation shown below. The recommonmark extension is known to have difficulty working properly with recent Sphinx versions.*

---

For example, inline math equation :math:`a^2 + b^2 = c^2` and display equation

.. math::
   
   e^\pi + 1 = 0

The above paragraph is given by:

```
For example, inline math equation :math:`a^2 + b^2 = c^2` and display equation

.. math::
   
   e^\pi + 1 = 0
```
