Mobile Web Site Redirects in Django
###################################
:date: 2010-10-05 14:34
:author: Steve Schwarz
:category: python
:tags: django, gunicorn, minidetector, mobile
:slug: conditional-mobile-web-site-redirect-in-djang

For the mobile version of agilitycourses.com I wanted to follow the
approach Google appears to be using on some of its sites:

-  If the user views agilitycourses.com from a desktop browser they
   should see the standard/desktop version of the site.
-  If the user views agilitycourses.com from a mobile browser they
   should be redirected to a mobile domain (m.agilitycourses.com).
-  The mobile version of the website includes a link to the standard
   version.
-  If the mobile user chooses the standard website they should "stick"
   on that site and not be redirected to the mobile site.

I wanted to run two different websites but share templates and have the
templates and css change for the mobile site. That meant that I'd need
to set a variable(s) in the request to use to generate the appropriate
HTML. So I found the simplest mobile device detector `minidetector`_ and
initially used that. I later found `Chris Drackett's fork`_ has a number
of useful enhancements and switched to it.

But minidetector didn't provide the ability to redirect to another site.
I found `Scott Newman's article`_ on using multiple templates which had
a section on performing the redirect and storing the user's selection in
the session. So I forked Chris' minidetector and modified it to include
the redirect and session storage. At the same time I decided to store
all the minidetector variables into the session and add them, via
middleware, to the request so the raw request wouldn't have to be parsed
each time. My fork is `available here`_ with details on the new
configuration options.

I'm using two domains so I can track analytics for the mobile and
non-mobile sites separately and allow users to bookmark the desired
site's pages. I use Google Analytics (via django-google-analytics) and
Awstats for analytics.

Since I'm using two separate domain and sharing everything else I'm
using a setup similar to the one described by `Dustin Davis`_. I have a
settings.py file and a mobile_settings.py that only overrides the
features I need::

  from settings import *
  SITE_ID = 2
  CACHE_MIDDLEWARE_KEY_PREFIX = "m.ac-"

I use a different memcached key prefix so the cached pages for the
mobile site don't clash with those for the desktop site.

I setup m.agilitycourses on my server using the same `Gunicorn setup I
used for agilitycourses.com`_ with the only changes being specifying the
``--bind address/port`` and the name of the mobile settings file::

  #!/bin/sh
  GUNICORN=/home/user/virtualenvs/myapp/bin/gunicorn_django
  ROOT=/home/user/source/myapp
  PID=/var/run/myapp.pid
  if [ -f $PID ]
      then rm $PID fi
  cd $ROOT
  exec $GUNICORN --bind 127.0.0.1:8001 -c $ROOT/gunicorn.conf.py --pid=$PID $ROOT/mobile_settings.py

If my templates/content start to diverge more significantly between the
mobile and desktop sites I may set the TEMPLATE_DIRS differently in the
mobile_settings file. Or I can move to Dustin's approach and create a
new application containing the urls.py and views.py specific to my
mobile deployment. I would think diverging further would call for a
refactoring of the common functionality to its own application which
could be imported into separate code branches for each domain.

.. _minidetector: http://code.google.com/p/minidetector/
.. _Chris Drackett's fork: http://github.com/shelfworthy/minidetector
.. _Scott Newman's article: http://www.packtpub.com/article/multiple-templates-in-django
.. _available here: http://github.com/saschwarz/minidetector
.. _Dustin Davis: http://www.nerdydork.com/mobile-app-on-subdomain-with-django.html
.. _Gunicorn setup I used for agilitycourses.com: http://tech.agilitynerd.com/configuring-runit-for-gunicorn-and-django-ins
