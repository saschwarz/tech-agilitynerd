Google Analytics for JQuery Mobile With Internal and AJAX Pages
###############################################################
:date: 2013-01-21 02:00
:author: Steve Schwarz
:category: webdev
:tags: ajax, googleanalytics, jquery, jquerymobile
:slug: google-analytics-for-jquery-mobile-withwithou

I added google analytics to my `agilitycourses.com`_ website and was
having problems getting the mobile version of the site to log analytics
data after the first page. Google found this very helpful blog
post: \ `Using Google Analytics with jQuery Mobile`_ and it got me very
close to my final solution.

Since that time jQuery Mobile has changed to \ `pageinit events`_ and
`jqmData`_ for page selectors, so I had to change the first line below
to match the recomendations for the 1.x version of jQuery Mobile that
I'm using: 


.. code:: javascript

    $("div:jqmData(role='page')").live('pageinit',
      function (event, ui) {
        var url = '';
        var hash;
        try {
          /* urls begin with locale but track urls independent of locale: strip off leading locale */
          url = location.pathname.replace(/^/[-a-zA-Z_]{2,5}//, '');
          hash = location.hash;
          if (hash) {
            url = '/' + hash.substr(1); /* strip # from hash */
          }
          _gaq.push(['_setAccount', 'UA-XXXXXXX-X'],
                    ['_setDomainName', 'example.com'],
                    ['_setSiteSpeedSampleRate', 100],
                    ['_trackPageLoadTime'],
                    ['_trackPageview', url]);
        } catch(err) {}
    });

My mobile site uses both internal pages and AJAX loaded pages. So unlike
the blog post's solution, I needed to use URLs with and without
hashtags. Per the `Google docs on _trackPageview`_ I also added a
leading slash to the hashed URL.

Another change for my site is urls are localized, they begin with the
locale for the user's language via `django-localeurl`_. So I strip the
leading "/es/", "/ca-FR/" or "/en_GB/" from the URL before sending it
to Google.

There are a couple other variables I push on the _gaq array. I log my
mobile site (m.agilitycourses.com) as a subdomain of my desktop site so
I followed the settings from the `Google analytics`_ and set the domain
name. I also enabled client side page load and site speed settings.

So I put the code in the head of the original post in the head of my
pages and the code snippet above in the foot of the pages.

Hope this is helpful for others.

.. _agilitycourses.com: http://agilitycourses.com
.. _Using Google Analytics with jQuery Mobile: http://www.jongales.com/blog/2011/01/10/google-analytics-and-jquery-mobile/
.. _pageinit events: http://jquerymobile.com/demos/1.0/docs/api/events.html
.. _jqmData: http://jquerymobile.com/demos/1.0/docs/api/methods.html
.. _Google docs on _trackPageview: http://_trackPageview
.. _django-localeurl: https://github.com/carljm/django-localeurl
.. _Google analytics: https://developers.google.com/analytics/devguides/collection/gajs/gaTrackingSite#domainAndSubDirectory
