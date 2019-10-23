Contributing to this Wiki
##############################

.. note:: This article is about contributing pages and edits to this wiki.

You can fork this documentation from the `MAD-docs`_ GitHub repository and open pull requests for changes.

Adding or Editing Pages
************************

A few guidelines to help keep things clean and organized...

Keep filenames short and to the point, for example: ``installation.rst``

Always begin your new page with a title:

.. code-block:: rst

  Awesome Wiki Page
  ################

Titles will be shown at the top of a page and in the site navigation. A title should describe a page in a glance. The rest of the file is written in ReST or Markdown structured text. Here is a `cheatsheet`_ for RST formatting, and one for `markdown`_.

Once done editing your page, add it under one of the ``toctree`` sections in ``index.rst``.

Now to preview your changes, open a terminal and use ``make html``. This will generates html files in ``_build/html/``. You can see the final documentation by opening them up with a browser.

Finally, when you are finished, submit your changes as a Pull Request to be reviewed.

.. _`MAD-docs`: https://github.com/Map-A-Droid/MAD-docs
.. _`cheatsheet`: http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
.. _`markdown`: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
