Improving Site Navigation - Add Titles to Blosxom Pages With storytitle
#######################################################################
:date: 2008-06-20 22:03
:author: Steve Schwarz
:category: webdev
:tags: agilitynerd, blosxom, googleanalytics
:slug: improving-site-navigation-add-titles-to-blosx-1

I've always wanted my `AgilityNerd`_ blog to serve as a reference for
interesting dog agility subjects. Consequently, I'm interested in making
it as easy as possible for readers to locate, explore, and learn more
about the sport. So improving navigation is a strong interest to me.

I have been reading `Designing Web Navigation by James Kalbach`_. In the
section discussing Browser Mechanisms Kalbach discusses the back and
forward buttons and the Session History drop down. The session history
is usually a menu that drops down from the back button (or near it). It
lists the pages the user has visited in reverse order showing their page
titles. Kalbach states: "Session history is a good reason to supply
meaningful browser titles". That reminded me that for my blog the
session history has always just displayed "AgilityNerd" for each page
visited on my site. I was leaving out a valuable aid to my readers who
use the session history to find where they had been previously.

Another benefit of setting the title in pages is in tracking site
statistics. It had always bothered me that GoogleAnalytics never showed
statistics for my pages by page title.

So these two things finally moved me to take some action. I had been
thinking about writing a `Blosxom`_ plugin to set the title element in
the HTML head section but I've always been too busy. Luckily I didn't
have to.

I found out about the storytitle plugin from Nick Leverton's
`Serendipity`_ blog. He had made some changes and released `version 0.7
of the plugin`_. It was trivial to setup, I just followed the directions
in the plugin and had this site and agilitynerd.com/blog working within
minutes.

So if you are a Blosxom user just grab this plugin. Otherwise, take the
time to set your page title sections so you can help your readers and
help analyzing your own site's statistics

.. _AgilityNerd: http://agilitynerd.com/blog/
.. _Designing Web Navigation by James Kalbach: http://www.amazon.com/Designing-Web-Navigation-Optimizing-Experience/dp/0596528108?t=agili-20
.. _Blosxom: http://blosxom.sourceforge.net/
.. _Serendipity: http://www.leverton.org/blosxom
.. _version 0.7 of the plugin: http://www.leverton.org/blosxom/Software/Projects/Blosxom/storytitle.html
