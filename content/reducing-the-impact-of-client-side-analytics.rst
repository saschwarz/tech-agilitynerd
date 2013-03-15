Reducing the Cost of Client Side Analytics 
###########################################
:date: 2012-01-12 22:10
:author: Steve Schwarz
:category: webdev
:tags: analytics, boomerang, javascript, sessionstorage, webdevelopment
:slug: reducing-the-impact-of-client-side-analytics

I read \ `Andy McKay's blog post on timing user experience`_ on the
`Mozilla Webdev blog`_ the other day and it reminded me of an idea I was
thinking about for measuring client side timings at work. I had been
toying with the idea of rolling our own library to capture JavaScript
rendering time for our JS heavy pages (grids of hundreds of lines of
data).

Andy's post mentions the `boomerang JavaScript library`_ and when I was
reading it's docs they pointed out potential for abuse/load on the URL
used to report the timings. For each instrumented page boomerang can hit
the "beacon" URL to report the statistics it collects. So in the worst
case you could double your page hits - although for specific
pages/samples recording a few statistics shouldn't be too costly for low
volume sites.

One solution is to only sample the pages/users of interest; selecting
the sample could occur on the server and/or client. But another solution
would be to collect statistics across multiple pages and periodically
send batches of analytics to the beacon URL.

I've been playing with mobile web development for
`agilitycourses.com`_ lately and will soon let users store the courses
they create in localStorage on their browser. That got me thinking that
`sessionStorage`_ could be used to store analytics across pages and then
periodically send the stats to the server. This would reduce the number
of hits on the beacon, allowing deployment to a larger sample of
clients. It also gets flushed once the session is closed and (if kept
small) doesn't prompt the user to approve storing the data.

A lot of modern `browsers support session storage`_ and for my purposes
only ones with support would be relevant - due to our browser support
policy at work.

The other problem the boomerang docs discuss is\ `abuse of the beacon`_
(accidental or malicious). A solution would be to piggyback reporting of
analytics into application form post payloads. This is trickier to
implement and it suffers from coupling analytic reporting into the
application itself.

To try to solve it some what generally... The client side JS library
could add a hidden field to any/some/specific forms into which it writes
the analytics data collected thus far. If it hooked the form submit
callback it could know if the form was successfully submitted and clear
the session storage.

Server side middleware could detect the hidden analytics field in the
form and extract/store the data. It could also remove the field before
passing the request data along to the app server. 

All in all a fair amount of twiddling to keep from exposing a recording
URL to the outside world. 

Of course if an authenticated session was being used then abusers would
have to have a valid session to post to the beacon URL.

I don't know if I will have time to play with the sessionStorage idea
but I think it might be a worthwhile extension to boomerang or other
client side analytics capture libraries.

.. _Andy McKay's blog post on timing user experience: http://blog.mozilla.com/webdev/2012/01/06/timing-amo-user-experience/
.. _Mozilla Webdev blog: http://blog.mozilla.com/webdev
.. _boomerang JavaScript library: http://yahoo.github.com/boomerang/doc/
.. _agilitycourses.com: http://m.agilitycourses.com/
.. _sessionStorage: http://en.wikipedia.org/wiki/Web_Storage#Local_and_session_storage
.. _browsers support session storage: http://www.delicious.com/redirect?url=http%3A//dev-test.nemikor.com/web-storage/support-test/
.. _abuse of the beacon: http://yahoo.github.com/boomerang/doc/howtos/howto-7.html
