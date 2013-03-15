Firefox Web Developer Add-on AJAX NON-Caching Problem
#####################################################
:date: 2008-12-30 04:08
:author: Steve Schwarz
:category: webdev
:tags: ajax, firefox, firefoxaddon, webdevelopment
:slug: firefox-web-developer-add-on-ajax-non-caching-1

I ran across some "interesting" behavior of the Firefox `Web Developer
Add-on`_ today. When editing JavaScript code I normally leave Web
Developer set to "disable cache". This causes all images and,
significantly for my purposes, the JavaScript files to be downloaded
from the server on every page request. But I ran into a unexpected
problem with this setting that cost me a couple hours today.

I was working on a legacy page today that uses an AJAX POST and the
response is sent to an IFRAME. The POST was successful, the results were
valid and present in the IFRAME. The problem was as soon as the content
of the IFRAME was eval'd() a GET was being sent to the server for the
URL of the page. This GET was a problem because it had a side effect of
clearing the session data (which contained the POSTed AJAX data) for the
current page. So when the page's FORM was finally POSTed the server
couldn't find the data in the session.

After trying numerous code changes including disabling event handlers
and events, it finally occurred to me that the cache disable feature of
the add-on might be causing the unexpected GET. Sure enough, once I
re-enabled caching the GET stopped being sent.

It was strange that the ``eval()`` caused the GET to be requested. All
the other code around processing the IFRAME's data didn't trigger it,
only the eval. Strange but true.

So just something to keep in mind when strange behavior occurs on AJAX
pages where session data is being used.

.. _Web Developer Add-on: https://addons.mozilla.org/en-US/firefox/addon/60
