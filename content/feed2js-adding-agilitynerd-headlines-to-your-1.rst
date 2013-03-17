Feed2JS - Adding AgilityNerd Headlines to Your Website
######################################################
:date: 2008-01-11 22:24
:author: Steve Schwarz
:category: webdev
:tags: syndication
:slug: feed2js-adding-agilitynerd-headlines-to-your-1


**Updated 16-Aug-2006 to reflect Feed2JS's move to http://feed2js.org**

I never thought anyone would want me to `syndicate`_ my blog and put
links to my latest articles on their website. But Marj Kibby in
Australia with her very nice dog raising and training blog `Choose and
Raise a Puppy`_ did just that. So I started thinking about how I might
provide an HTML feed that could be included into blogs using client-side
JavaScript as not all web/blog writers are developers who can integrate
this data on the server side.

Well Google to the rescue: the `Feed To JavaScript`_ Open Source project
provides a really great service that exactly fits the bill. If you have
a website or blog and wish to list the latest articles from another
website you can just fill out a form on the Feed2JS site and get the
HTML to paste into your website. All you do is supply the RSS feed from
the source site to Feed2JS, select the options and click Preview or
Generate JavaScript to get the code you need. Feed2JS does all the
"heavy lifting".

Here is an example of the generated HTML as it would appear in your
website using the current data from this site:

The code for the above is a single (long) line of code::

  <script src="http://feed2js.org/feed2js.php?src=http%3A%2F%2Fagilitynerd.com%2Fblog%2Findex.rss10&chan=y&desc=0&date=n" type="text/javascript"></script>


There are many other ways to configure/display the information from
AgilityNerd on your site. Just go to:
http://feed2js.org/index.php?s=build and enter:
http://agilitynerd.com/blog/index.rss10 in the URL text entry box. Then
answer the other questions.

Feed2JS kindly caches the latest RSS feed from the source site you
specify and replies with the above HTML each time someone visits a page
on your site. This has the added advantage of not taxing the webserver
of the source site to feed your website; which is nice for sites like
this one with a small monthly bandwidth quota.

Feed2JS also has a number of ways to style the HTML that is delivered so
you can change the look of the links to match your site. Of course, web
developers fluent in CSS can just style the HTML directly.

For `Blosxom`_ bloggers I've been playing around developing a new plugin
based on the headlines plugin to provide this same functionality. I hope
to post this new plugin when/if I get it working. Either way I strongly
recommend Feed2JS, it is a great project developed in the true spirit of
the Open Source movement.

.. _syndicate: http://en.wikipedia.org/wiki/Web_syndication
.. _Choose and Raise a Puppy: http://marjkibby.blogspot.com/
.. _Feed To JavaScript: http://feed2js.org/
.. _Blosxom: http://blosxom.sourceforge.net/
