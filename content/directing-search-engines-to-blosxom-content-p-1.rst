Directing Search Engines to Blosxom Content Pages
#################################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: directing-search-engines-to-blosxom-content-p-1

I've noticed that folks who come to my site by querying through a search
engine often end up on my main page and the article they are searching
for has already rolled off the front page. This is because the search
engine robots tend to choose the index pages as more relevant than the
content pages linked to by the index pages. This is especially
frustrating to me since I want my blog to serve as a reference for other
Agility enthusiasts - so making my articles easily retrievable from
search engines is important to me. It turns out this is a pretty common
problem faced by many blogs.

I found that `Jason Clark`_ had run into this problem with his
`Blosxom`_ blog and resolved it by using the following meta element on
his index pages: <meta name="robots" content="noindex,follow" >. `His
post describes`_ how he conditionally includes these robot meta tags
through his head flavour files (using the interpolate_fancy plugin and
his storystate plugin) only on his index pages and not on other pages.

For my site it is even easier. I use separate head.index pages to style
my index pages differently from my htm/html pages. So I just directly
inserted the <meta name="robots" content="noindex,follow" > into my
head.index pages.

There are a number of other robots meta tags that I might consider
adding in the future. `Websnob`_ has a `thorough explanation`_ of the
tags and the robots that use them.

Hopefully over the next few months these changes will cause search
engines to give their users links directly to the articles in my site.

.. _Jason Clark: http://jclark.org
.. _Blosxom: http://blosxom.sourceforge.net/
.. _His post describes: http://jclark.org/weblog/WebDev/Blosxom/robottweak2.html
.. _Websnob: http://www.bauser.com/websnob/
.. _thorough explanation: http://www.bauser.com/websnob/meta/robots.html
