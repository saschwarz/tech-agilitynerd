Those Darn Spammers Blosxom - Hit Counter and Writeback Changes
###############################################################
:date: 2006-08-11 19:00
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin, spam
:slug: those-darn-spammersblosxom-hit-counter-and-wr-1

Over the past year I'd noticed that comment and trackback spammers had
been hitting the same dozen or so pages of my blog multiple times daily.
(It is probably the same person/group who took a snapshot of the
articles on my front page at that time and just reuses those URLs for
all of their different domains). Last I calculated, about 50% of my
overall website traffic is due to spammers. This constant barrage of
hits skews my `AWStats`_ statistics and, more importantly, skews the
results on my `Favorites page`_. So I took a little time to work on this
problem.

FWIW I'm also starting to see a lot of spam coming from "blogs" being
setup on `BlogSpot`_ that are a single page all of whose links point to
the real site. Some of these bogus blogs use the BlogSpot temmplate
which contains a flag used to alert BlogSpot admins to content in
violation of their Terms of Service. This allows anyone to report the
bogus blog by just clicking on the flag. Other "blogs" just use their
own HTML and BlogSpot support would have to be sent an email with the
offending site's URL.

So anyway, I've taken the following steps:

-  Disabled trackback comments entirely using the configuration variable
   in the writeback plugin. I've never received a legitimate trackback
   ping.
-  Modified my modified version of the writeback plugin to set a
   variable $rejected with a 1 if the comment was rejected or if
   trackback was attempted.
-  Modified my HitCounter plugin to read the $writeback::rejected
   variable and then not increase the counter for the spammed page.
-  I had to change the ordering of the hitcounter plugin to run after
   writeback so the variable would be set correctly when hitcounter ran.
-  Set the $hitcounter::reset_count variable and reset the counts of
   the spammed pages back to "reasonable" counts.

Another couple hours wasted messing around against spammers.

I've `previously written`_ how I've been using comment content
blacklisting to reject comment, trackback, and referer (sic) spam. My
current blacklist file has over 40 regular expressions containing over
250 words and patterns. I update it whenever a spam comment slips
through. So that is an ongoing almost daily effort. I might just have to
go to the trouble of getting a `CAPTCHA`_ plugin to work.

.. _AWStats: http://awstats.sourceforge.net
.. _Favorites page: http://agilitynerd.com/blog/static/Favorites.html
.. _BlogSpot: http://blogspot.com
.. _previously written: /blosxom-plugin-to-block-referer-spam-1.html
.. _CAPTCHA: http://varg.dyndns.org/psi/pub/code/misc/wbcaptcha.html
