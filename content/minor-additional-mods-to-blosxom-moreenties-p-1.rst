Minor Additional Mods to Blosxom moreenties Plugin
##################################################
:date: 2008-02-24 16:24
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: minor-additional-mods-to-blosxom-moreenties-p-1

I had previously extended Jason Clark's `moreentries`_ plugin for
`Blosxom`_ to allow adding images to links to the previous and next
group of articles/entries in the head or foot of a Blosxom weblog. While
attempting to have valid HTML on my blogs I found that I had left an img
tag unclosed. I also found that it wasn't as easy to change the styling
of the links as I had originally planned.

So I've closed the open img tags and added the configuration variable
``$selfstyle`` into which you can place any CSS style information you'd
like added to the ``td`` containing each page link. For example::

    # Set to the CSS style for $moreentries::links
    $selfstyle = 'style="padding: 0 3px;"'; # set to '' for no style

.. _moreentries: http://jclark.org/weblog/WebDev/Blosxom/plugins/moreentries
.. _Blosxom: http://blosxom.sourceforge.net/
.. _here: /downloads/moreentries.zip
