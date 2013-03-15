Firediff: track and save CSS edits in Firebug
#############################################
:date: 2010-07-25 16:36
:author: Steve Schwarz
:category: webdev
:tags: css, firefoxaddon, webdevelopment
:slug: firediff-track-and-save-css-edits-in-firebug

When I'm making fiddly changes to a web page I like to tweak the CSS
using the Firefox Firebug plugin. It has the advantage of letting you
try changes quickly and see the effect. The downside has always been
that you had to then change the source CSS file to include your changes.
Which increases the risk that you forget to include a change.

I was thinking about that recently when I changed the color scheme on my
AgilityNerd blog and went searching for a way to at least identify the
changes. Turns out there is a nice plugin that provides exactly that
functionality. The `Firediff plugin`_ not only tracks changes to the CSS
it also allows you to save those changes for overwriting or diff'ing
into you CSS file(s).

Like other firebug related extensions you need to enable this feature
per page by clicking on the arrow next to the new Changes tab.

Here is a screenshot of the plugin in action:

.. raw:: html

   <div class="thumbnail">

|Firediff|

.. raw:: html

   </div>

You can see I've changed the line-height attribute - it shows the
previous and final values. A right mouse menu lets you save those
changes to a file or revert them.

Another feature that can be configured in the Changes menu is whether to
track changes made by other JavaScript to the page. This is an
interesting feature if you were wondering how a JQuery or other
JavaScript modified the page for a given effect.

This is a great plugin that I'll continue to use regularly.

.. _Firediff plugin: https://addons.mozilla.org/en-US/firefox/addon/13179/

.. |Firediff| image:: /static/images/2010/07/12587332-firediff.png
