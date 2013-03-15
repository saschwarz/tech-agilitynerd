hitcounter, favorites, lastcommented and lastread Blosxom Plugin Updates
########################################################################
:date: 2008-01-01 18:44
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: hitcounter-favorites-lastcommented-and-lastre-1

I found a bug in my hitcounter, favorites, lastread and lastcommented
plugins due to my not using the correct Perl Storable functions. For
some reason I didn't use the locking versions of retrieve() and
nstore(). So when my old webhost had some problem causing long page load
times (and many simultaneous requests) I ended up having my favorites
data file written as zero sized.

So I changed to Storable::lock\_retrieve() and Storable::lock\_nstore()
for all four plugins. The new versions are here:

-  `favorites`_
-  `hitcounter`_
-  `lastcommented`_
-  `lastread`_

I never heard any bug reports about these plugins, but I'm sorry if
anyone ran into any difficulties due to these bugs.

.. _favorites: http://data.agilitynerd.com/downloads/favorites
.. _hitcounter: http://data.agilitynerd.com/downloads/hitcounter
.. _lastcommented: http://data.agilitynerd.com/downloads/lastcommented
.. _lastread: http://data.agilitynerd.com/downloads/lastread
