Blosxom Plugins: lastcommented and lastread
###########################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: blosxom-plugins-lastcommented-and-lastread-1

In preparation for an overhaul of my website I wrote two new `Blosxom`_
plugins. The lastread plugin allows me to create a list of links to the
last *n* articles that were viewed by readers. The lastcommented plugin
allows me to create a list of links to the last *n* articles that had
comments added by readers.

I took pains with these plugins so they only write their state files to
disk when a single article is read (not when the index pages are hit) or
when a comment is actually posted. I've also made it optional to not
rewrite the state file if an already existing entry in the list is
visited/commented again. There are a lot of Blosxom plugins that do a
lot of work on every page access and I didn't want to add to the server
load.

The configuration of each plugin is pretty straightforward. Both plugins
require the Storable plugin for storing the state files. Only the
lastcommented plugin requires any coding; whatever comment plugin you
use needs to set a variable in order for lastcommented to do any work.

`Download the lastread plugin`_

**Updated 2007-06-23 to version 0.3 to fix unshift() error and ignore
unknown file requests and filter out user defined HTTP Agents.**

**`Download the lastcommented plugin`_
Updated 2007-06-23 to version 0.2 to fix unshift() error.**

Hopefully I'll have my new site design using these plugins available in
a few weeks.

.. _Blosxom: http://blosxom.sourceforge.net/
.. _Download the lastread plugin: http://agilitynerd.com/downloads/lastread
.. _Download the lastcommented plugin: http://agilitynerd.com/downloads/lastcommented
