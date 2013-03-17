AgilityNerd Blosxom Plugins
###########################
:date: 2004-08-10 19:00
:author: Steve Schwarz
:category: webdev
:tags: blosxom, perl, plugin
:slug: agilitynerd-blosxom-plugins-1

**Updated 20-Jun-08 for addition of storytitle**

I'm really impressed with the `Blosxom`_ `plugin`_ mechanism. `Rael
Dornfest`_, author of Blosxom, put hooks at strategic points in the page
generation process. At each hook point the main script iterates all the
plugins present in the plugin directory. Plugins that implement the hook
function can then modify the state or add additional data for use in the
page presentation.

Consequently, a plugin only implements the hook functions it needs
invoked to provide its features. Some powerful plugins need only
implement one or two hook functions and are implemented with a couple
dozen lines of Perl code.

When I started building this site I found it a little confusing to sort
through all the plugins and understand their functionality. The ease of
creating and modifying plugins has allowed a lot of developers to
contribute to the Blosxom plugin `registry`_. I found it helpful when
Blosxom sites listed the plugins that implemented their site's features.
So here is the list of plugins I use.

`atomfeed`_ - Provides the AgilityNerd Atom feed. Point
your browser to http://agilitynerd.com/blog/index.atom

`breadcrumbs`_ - Creates the click-able trail to the current position in
the weblog's path shown at the top of all .index pages and at the bottom
of each article.

`binary`_ - Used to supply images from the directory in which an article
exists. Modified to use LWP::MediaTypes since MIME::Types isn't
installed on this web server. I also commented out the interpolate()
function and added it to the one in interpolate\_fancy to make this
plugin coexist with interpolate fancy.

I no longer use binary because it is faster to just have Apache serve
binary files directly from one or more directories outside of the
Blosxom src tree.

I've stopped using this plugin since it requires Blosxom to look at each
file to determine whether or not it should be skipped. So I'm starting
to put all binary files in my images directory outside of Blosxom. This
has the added advantage that I can just put "/images" and "/video" in by
robots.txt file so my images and videos don't get indexed by search
engine robots.

`categories`_ - Displays the tree of paths/categories of articles on the
`navigate <http://agilitynerd.com/blog/navigate/>`_ page. Slightly modified to remove the root directory from
the display. Added a hide feature to hide specified directories entirely
- used this to prune subdirectories for my side bar menu. Removed
flavour ending from all generated links since all paths are valid links,
are shorter for people emailing links around, and would always use the
default flavour. Modified to not calculate breadcrumbs since I use the
breadcrumbs plugin for that feature.

`config`_ - Allows any Perl variable to be set differently in any
category/directory. I use this to change the sort order for my
`glossary`_ page to be alphabetical order by changing the sort\_order
plugin's sorder variable.

`entries\_cache`_ - Speeds up processing of the site by caching the
article index to avoid scanning directories until a configured amount of
time has elapsed. Also caches article creation time to allow for editing
of articles without changing their timestamps.

`favorites`_ - Used to automatically generate my `Favorites page`_ based on the visitor hit counts recorded by my hitcounter plugin.

`file`_ - Used to include the navigational side div into all pages
without copy/paste of the same HTML.

`find`_ - Provides search capabilities for all articles, comments, and
linkbacks on the web site. HTML slightly modified to remove the advanced
search link. Also set the hidden "path" input to the empty string so the
entire site is searched regardless of where in the hierarchy the search
was initiated.

`foreshortened`_ - Ends articles at the end of the first sentence. Used
to provide the shortened version of articles for use in RSS and Atom
feeds.

`headlines`_ - Used to determine all the entries in my `glossary`_
category and create links in alphabetical order. Requires
interpolate\_fancy.

`hide`_ - Excludes directories of articles from the index views (like
the agilitynerd.com main page) but still allows them to be searched by
find.

`hitcounter`_ - Used to automatically generate the
number of visitors displayed in the footer for each page on my site.
These hit counts per page are used by my favorites plugin to generate my
`Favorites page`_.

`interpolate\_fancy`_ - Used to remove the space allocated for the
results of find and the breadcrumbs plugin when their variables aren't
defined. I think I'll use this more in the future to dynamically change
the page format.

`lastcommented`_ - Used to automatically
generate the list of the last 10 articles that were commented shown in
the side bar on each page of the site.

`lastread`_ - Used to automatically generate
the list of the last 10 articles that were read shown in the side bar on
each page of the site.

`moreentries`_ - Creates the "Previous" and "Next" links at the bottom
of each index or search page when there are more than
``$blosxom::num\_entries`` entries. I've modified this plugin as I described
`here`_.

`postheadprefoot`_ - Allows each category/directory to have unique text
inserted after the header and/or before the footer. I use this on my
`glossary`_ page to add a category specific subsection. I had to `modify
the script`_ to have paths resolve correctly.

`redirect`_ - Unmodified version of this plugin. I had to use it when I
moved a directory within my tree so search engine and email list links
would redirect correctly.

`refererblock`_ - A blacklist driven plugin to permanently
redirect referer spam. The redirect probably has little effect on the
receipt of referer spam but the 301 redirect code keeps the spammer's
sites out of my site statistics.

`rss10`_ - Provides the extra information to provide a valid RSS 1.0
feed for syndication. Slightly modified to work with the writeback
plugin.

`seemore`_ - Adds "See more..." link within the text of a post when the
post is shown in an index page. The location of the link is controlled
by placing a special tag in the posting source file. I have `modified`_
this plugin to show the first "n" entries of an index page in full.
Furthe

r modified to always create a link to my html flavoured pages.

`sort\_order`_ - Allows sorting by date, directory names, or file name.
I modified it to not read the URI parameters and just use a
configuration variable. Then I used the config plugin to change the sort
order for my `glossary`_ page to sort by file name instead of in reverse
chronological order.

`storytitle`_ - sets the <title> element in the HTML <head> with the
title of the article or the name of the category. I use it
to aid in navigation and site statistics]].

`timezone`_ - Adjusts timestamps automatically created or entered using
meta-creation\_date: to be offset correctly to my timezone; which is
different from the web server's timezone.

I no longer use timezone since I can set the timezone on my
Slicehost server.

`defaultflavour`_ - Provides the user with the
default Blosxom flavoured feed when an unknown flavour is requested.
This keeps the user from getting the Unknown Flavour error across the
top of the page.

`wbcaptcha`_ - Provides an ASCII image via `FIGlet`_ when visitors enter
comments to stop spam bots from saturating my blog comments. See this article for `my modifications`_ to this plugin.

`wikiwordish`_ - Provides WikiWord-like linking to Wiki articles, local
article file names and modified to replace WikiWords with HTML <a>
links. This plugin saves me from having to enter links to common sites
to which I always refer. I had to name this file 00wikiwordish so that
WikiWords would be correctly replaced in RSS and Atom feeds.

`writeback blacklist plugin`_ - Provides comment and TrackBack
capability. This is Doug Alcorn's blacklist modified version to help
fight comment spam. I've slightly modified mine to try to protect
comment poster's from spam by obfuscating their email addresses.

In case anyone is trying to get these plugins to "play" together I have
them named as follows:

-  000refererblock
-  001redirect
-  002defaultflavour
-  005wikiwordish
-  007google\_highlight
-  008wbcaptcha
-  01atomfeed
-  01breadcrumbs
-  01categories
-  01config
-  01entriescache
-  01favorites
-  01file
-  01find
-  01foreshortened
-  01fullcategories
-  01headlines
-  01hide
-  01moreentries
-  01postheadprefoot
-  01rss10
-  01seemore
-  01sort\_order
-  01storytitle
-  01writeback
-  02hitcounter
-  02lastcommented
-  02lastread
-  02recentwritebacks
-  50interpolate\_fancy

.. _Blosxom: http://blosxom.sourceforge.net/
.. _plugin: http://blosxom.com/documentation/users/plugins.html
.. _Rael Dornfest: http://www.raelity.org/
.. _registry: http://blosxom.com/plugins
.. _atomfeed: http://www.blosxom.com/plugins/syndication/atomfeed.htm
.. _breadcrumbs: http://www.blosxom.com/plugins/display/breadcrumbs.htm
.. _binary: http://www.blosxom.com/plugins/display/binary.htm
.. _categories: http://www.blosxom.com/plugins/category/categories.htm
.. _config: http://www.blosxom.com/plugins/general/config.htm
.. _glossary: http://agilitynerd.com/blog/agility/glossary/
.. _entries\_cache: http://www.blosxom.com/plugins/indexing/entries_cache.htm
.. _Favorites page: http://agilitynerd.com/blog/static/Favorites.html
.. _file: http://www.blosxom.com/plugins/include/file.htm
.. _find: http://www.blosxom.com/plugins/search/find.htm
.. _foreshortened: http://www.blosxom.com/plugins/text/foreshortened.htm
.. _headlines: http://www.blosxom.com/plugins/display/headlines.htm
.. _hide: http://www.blosxom.com/plugins/files/hide.htm
.. _interpolate\_fancy: http://www.blosxom.com/plugins/interpolate/interpolate_fancy.htm
.. _moreentries: http://www.blosxom.com/plugins/display/moreentries.htm
.. _here: /minor-additional-mods-to-blosxom-moreenties-p-1.html
.. _postheadprefoot: http://www.blosxom.com/plugins/display/postheadprefoot.htm
.. _modify the script: http://groups.yahoo.com/group/blosxom/message/9364
.. _redirect: http://www.blosxom.com/plugins/general/redirect.htm
.. _rss10: http://www.blosxom.com/plugins/syndication/rss10.htm
.. _seemore: http://www.blosxom.com/plugins/display/seemore.htm
.. _modified: /see-more-added-to-article-display-on-index-pa-1.html
.. _sort\_order: http://blosxom.ookee.com/blosxom/plugins/v2/sort_order-v0i85
.. _storytitle: http://www.leverton.org/blosxom/Software/Projects/Blosxom/storytitle.html
.. _timezone: http://www.blosxom.com/plugins/date/timezone2.htm
.. _wbcaptcha: http://varg.dyndns.org/psi/pub/code/misc/wbcaptcha.html
.. _FIGlet: http://www.figlet.org
.. _wikiwordish: http://www.blosxom.com/plugins/text/wikiwordish.htm
.. _writeback blacklist plugin: http://www.lathi.net/twiki-bin/view/Main/BlogSpam
.. _favorites: /blosxom-hit-counter-and-favorites-plugins-1.html
.. _hitcounter: /blosxom-hit-counter-and-favorites-plugins-1.html
.. _lastcommented: /blosxom-plugins-lastcommented-and-lastread-1.html
.. _lastread: /blosxom-plugins-lastcommented-and-lastread-1.html
.. _refererblock: /refererblock-version-02-1.html
.. _defaultflavour: /blosxom-default-flavour-plugin-fixes-unknown-1.html
.. _my modifications: /comment-spam-and-wbcaptcha-plugin-enhancement-1.html
