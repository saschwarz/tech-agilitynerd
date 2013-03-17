Blosxom Plugin to Block Referer Spam
####################################
:date: 2005-02-12 20:00
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin, spam
:slug: blosxom-plugin-to-block-referer-spam-1


Like so many other bloggers who allow comments on their websites and
blog articles, I was facing increasing `comment spam`_ as my blog got
noticed by more spammers. The size of this problem is illustrated by
`this Google query for "comment spam"`_ that returned 1.5 million hits.
For the uninitiated comment spam is like email spam for blogs; the
spammer inserts fake comments in a blog where either the comment text
contains from one to dozens of links to the spammer's websites. When web
search sites "spider" the blog the links to the spammer's site are
treated as "endorsements" of the spammer's sites and the spammer's sites
are raised to the top of the search site's result lists.

There is another growing type of blog spam called `referer spam`_ (yes
it is `officially misspelled`_). When a web surfer clicks on a link in a
web page that sends them to another web page most web browsers fill in
the URL of the referring page into the request called the HTTP\_REFERER.
Some websites and blogs capture that page link information when they are
on the receiving end of a web request. These sites might have a section
on each page indicating the sites that link to that page. These links
are referer links.

Referer spam uses the same mechanism as comment spam to raise the search
sites ranking of the spammer's websites. But referer spammer's don't
post comments; they post fake referrals to a website. The are hoping
that the website or blog displays links of the sites that refer to them.
So when the website is spidered the search ranking is raised.

Blosxom Plugins Addressing Spam
-------------------------------

Like so many bloggers once I started getting comment spam I was able to
manually delete them as they occurred. But that got old fast. After some
Googling I discovered `Doug Alcorn's`_ `Blosxom`_ `writeback blacklist
plugin`_. I had been using the original `writeback`_ plugin. Doug's
improvements provided enough protection (so far) with less than a dozen
regular expressions removing all my comment spam.

Referer spam started hitting me three weeks ago. What was most
infuriating was that I don't display any links of referring sites on my
site at all. So all these spammers were succeeding in doing was skewing
my site statistics and using my bandwidth with their fake referer
attacks several times a day.

Of course all the referer spam site's addresses contained one or more of
the same dozen blacklisted words I had already configured for comment
spam. About the same time I saw `Jason Clark`_ post his `deferer
plugin`_ to return a 301 permanent redirect for the IP address of one
particular referer spammer who was attacking his site. I thought that by
combining Doug's blacklisting plugin with Jason's immediate redirect
plugin I could reduce the referer spam from my log files.

This plugin hasn't removed the entries entirely from my logs, since the
initial request is still logged with a 301 status. But it has stopped
the subsequent downloading of images for the pages whose content is now
not served. Now that the log contains 301 status messages for these
requests they are ignored by my host's statistics program (`Advanced Web
Statistics - AWStats`_).

On a re-reading of Jason's blog entry for deferer he also mentions the
idea of white and black lists for referer filtering. So I might have
subliminally remembered his idea and implemented my refererblock plugin
based on his idea. In any event, I fully credit Jason and Doug for
giving me the ideas and code with which to put together my plugin.

Referer Block Plugin
--------------------

The refererblock plugin's tar file can be downloaded `here`_. It
contains the refererblock plugin already named 000refererblock so that
it runs before all other plugins (you want to discard the blacklisted
requests before all legitimate requests). A sample blacklist.txt file is
provided and contains some example regexs. It uses the same blacklist
file format and file name as Doug's writeback modification (I took the
code from his plugin with only cosmetic changes). See Doug's website for
links to the Movable Type and other blacklists.

The only configuration variable you can set is $log\_blacklisted. If set
to a full path file name the script logs the UTC date/time, referer
string, and the page to which they were referring. You could use the
frequency of words in the rejected referer strings to fine tune the
content and ordering of your blacklist.txt file to match the spammers
hitting your site. Be aware that this file isn't trimmed so you might
want to keep an eye on its size.

Lastly, the zip file contains a simple Perl script you can use to test
the plugin. Execute it as:

.. code:: 

  referer_test.pl http://example.com http://referer-spam.com
  where the first URL is your website and the second URL is the referer

to be sent in the request. This script uses HTTP::Request to send the
request. The script returns the status "200 OK" for the requested page
if it isn't blacklisted and "301 Moved Permanently" if the referer is
blacklisted.

Please let me know if you use this plugin or if you have comments or
suggestions for improving it.

.. _comment spam: http://en.wikipedia.org/wiki/Blog_spam
.. _this Google query for "comment spam": http://www.google.com/search?q=%22comment+spam%22
.. _referer spam: http://www.spywareinfo.com/articles/referer_spam/
.. _officially misspelled: http://dictionary.reference.com/search?q=referer
.. _Doug Alcorn's: http://www.lathi.net
.. _Blosxom: http://blosxom.sourceforge.net/
.. _writeback blacklist plugin: http://www.lathi.net/twiki-bin/view/Main/BlogSpam
.. _writeback: http://www.blosxom.com/plugins/input/writeback.htm
.. _Jason Clark: http://jclark.org
.. _deferer plugin: http://jclark.org/weblog/WebDev/Blosxom/plugins/deferer/deferer-0-1i.html
.. _Advanced Web Statistics - AWStats: http://awstats.sourceforge.net
.. _here: http://data.agilitynerd.com/downloads/refererblock_0.1.tar
