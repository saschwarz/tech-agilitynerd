Debug Site for Website Redirects By Referer String
##################################################
:date: 2010-09-29 18:42
:author: Steve Schwarz
:category: webdev
:tags: django, mobile, referrer, webdevelopment
:slug: debug-tool-for-mobile-website-selection-by-re

I'm adding an "m" subdomain to agilitycourses.com to provide a better
mobile browsing experience. I'm using the referrer string in Django
middleware (currently using `minidetector`_) to detect whether the
client is mobile and redirect them to the mobile site. Since it is
likely that some folks will/won't get appropriately redirected I was
looking for an easy way for them to tell me when they were incorrectly
redirected. I'd need to know their referer string.

A little googling turned up a nice one purpose website:
`www.whatismyreferrer.com/`_

.. _minidetector: http://code.google.com/p/minidetector/
.. _www.whatismyreferrer.com/: http://www.whatismyreferrer.com/
