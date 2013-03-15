Using django-sitemap with django-tagging
########################################
:date: 2009-11-27 17:33
:author: Steve Schwarz
:category: webdev
:tags: django, djangositemap, djangotagging, python, webdevelopment
:slug: using-django-sitemap-with-django-tagging

I was adding `django-sitemap`_ to `googility.com`_ yesterday and found
that Tags don't implement ``get\_absolute\_url()``. Which makes sense since
the site developer would want to decide how to expose them in the URL
space.

It is also arguable that links to pages displaying the tag view already
exist in the page for models that are already in the sitemap so they
don't need to be put in the sitemap explicitly. For example, a page for
an Article might be at ``/article/django-11-release`` and that page would
contain the links to pages linked with the tags for that article e.g.
``/tag/django/`` and ``/tag/python/``

But I figured having the tag pages indexed by Google would be useful. It
also allows a different priority to be specified for the pages. So I
made a little class that derives from ``GenericSitemap`` that allows the url
and suffix for the Tag name to be specified::

    class SlugSitemap(GenericSitemap):
    """Use for objects that don't implement get_absolute_url 
       but have a slug field used in creating their url"""     

    def __init__(self, info_dict, priority=None, changefreq=None):
        GenericSitemap.__init__(self, info_dict, 
                                priority=priority,
                                changefreq=changefreq)
        self.url = info_dict.get('url', '/')
        self.slugfield = info_dict['slugfield']
        self.suffix = info_dict.get('suffix', '')

    def location(self, obj):
        return "%s%s%s" % (self.url,
                           getattr(obj, self.slugfield),
                           self.suffix)

Here's how I use it::

    sitemaps = {'tag_detail': SlugSitemap({'queryset':Tag.objects,
                                           'url':'/tag/',
                                           'slugfield':'name',
                                           'suffix':'/'},
                                           changefreq='monthly',
                                           priority='0.5'),
    }

The urls for tags are at /tag/*slugname*/ where /tag/ is prepended to
tag.name and / is appended to the end

This class can be used to create sitemap entries for any url
parameterized on a single field of an instance returned by the QuerySet.

.. _django-sitemap: http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/
.. _googility.com: http://googility.com/
