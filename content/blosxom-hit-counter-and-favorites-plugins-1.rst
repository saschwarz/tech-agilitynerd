Blosxom - Hit Counter and Favorites Plugins
###########################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: blosxom-hit-counter-and-favorites-plugins-1

I added a `Favorites page`_ to the side menu of my AgilityNerd site.
Since then I've been updating it manually about once a month based on
the AWStats reports from my web hosting provider (HostMagix). This task
is unnecessarily complicated because AWStats keeps page counts
independently for each URL, which includes the `Blosxom`_ flavour
(filename extension). For my purposes I don't want to distinguish
between say HitCounterFavorites.html and HitCounterFavorites.htm

So I decided to write a plugin to track the hits per page and "lump"
together counts independently from the file extension. This plugin
allows me to display the hit count of visitors for each page on each
page. I wrote a second plugin to use the hit count data to automatically
generate my Favorites page.

Hitcounter Plugin
-----------------

I based the hitcounter plugin on the categories plugin written by `Todd
Larason`_. The plugin has a couple features of interest:

-  The ``$reset\_count`` flag within the plugin lets you provide a starting
   count value for any page. For example to set a page's count to 10
   append "?count=10" to the page's URL. Disable this flag once you've
   set your counts to avoid mischevious count setting by outsiders.
-  The ``$retrieve\_only\_flavour flag`` within the plugin can be set to a
   flavour you want to use for retrieving counts without incrementing
   the count. Use this flavour to view the counts for URLs of interest.
-  You can add filters to the `start()` subroutine to exclude certain
   requests from updating your counters. I exclude RSS and Atom feed
   requests from my counts.
-  As of version 0.5 you can filter out loading and incrementing page
   counts for specific user agents via the ``ignore\_agents array``.

The hitcounter plugin stores the ``$blosxom::path`` as the key in a hash
whose value is the count of hits. The hash is stored in a file in the
data directory. The same hash is used for the entire site. As each page
is "hit" the value is incremented and stored in the ``$hitcounter::count``
variable. I put this variable in the footer of my pages.

Favorites Plugin
----------------

My favorites plugin uses the data file containing the hash of paths and
counts as its input. This plugin generates an HTML unordered list of the
most visited URLs with the following configuration options:

-  The ``$num\_entries`` variable controls how many URLs are listed.
-  The ``$include\_counts`` variable controls if directories will be
   included in the list of entries.
-  The ``$include\_counts`` variable controls whether or not the number of
   counts is appended to each list entry.
-  The ``$anchor\_format variable`` controls if the full path or only the
   filename is displayed in the list entry.
-  The ``$anchor\_link`` variable controls whether or not the entry is
   wrapped in an anchor <a>.
-  The ``$excludes`` variable controls which pages are excluded from
   consideration. I exclude the main URL for my site from showing up in
   the list.
-  The ``$groups`` array holds regexps that will generate separate unordered
   lists grouping together pages matching each regexp of ``$num\_entries``
   list elements. See the configuration section for an example. I use
   this feature for my Favorites page to group pages for agility and
   tech categories into separate lists.
-  The ``$url\_flavour`` variable lets you specify the flavour to use for
   anchors to non-category URLs. It defaults to to
   ``$$blosxom::default\_flavour``.
-  You can add filters to the ``start()`` subroutine to exclude certain
   requests from doing the work to generate the HTML. For example, I
   only run this plugin for my Favorites page.

When this plugin runs the ``$favorites::count`` variable is populated with
the HTML. I then put this variable in my Favorites.txt page.

Download version 0.5 of the hitcounter plugin `here`_.

Download version 0.1 of the favorites plugin
`here <http://data.agilitynerd.com/downloads/favorites>`__.

Comments/bug reports are welcome.

.. _Favorites page: http://agilitynerd.com/static/Favorites.html
.. _Blosxom: http://blosxom.sourceforge.net/
.. _Todd Larason: http://molelog.molehill.org/
.. _here: http://data.agilitynerd.com/downloads/hitcounter
