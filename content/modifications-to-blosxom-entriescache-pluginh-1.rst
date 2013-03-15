Modifications to Blosxom entriescache PluginHandles Articles With Future meta-creation_date
###########################################################################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: modifications-to-blosxom-entriescache-pluginh-1

`Fletcher Penney`_ created the original `entriescache`_ `Blosxom`_
plugin. It is designed to cache all the articles and their creation
dates in a Blosxom blog to avoid the overhead of scanning the file
system for new/modified files. He merged the meta plugin functionality
into the plugin to allow authors to date their entries without relying
on the file creation date (this makes it easy to move from one web
hosting provider to another without having your article dates get
reset).

Unfortunately, articles posted to a Blosxom blog with
meta-creation\_date's in the future would be displayed immediately. I
had wanted to modify Blosxom to allow me post articles with future
creation dates and have them hidden until that date. After a `request
for this functionality on the Blosxom email list`_, I looked into the
required modifications and found it wasn't too difficult to make them.

You can download the modified plugin `here`_. Let me know if you have
any questions or comments.

.. _Fletcher Penney: http://fletcher.freeshell.org
.. _entriescache: http://fletcher.freeshell.org/computers/web/blosxom/entries_cache/
.. _Blosxom: http://blosxom.sourceforge.net/
.. _request for this functionality on the Blosxom email list: http://groups.yahoo.com/group/blosxom/message/10664
.. _here: http://data.agilitynerd.com/downloads/entriescache
