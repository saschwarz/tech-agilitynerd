Confidently Refactoring Django URLs, Views, and Templates
#########################################################
:date: 2010-08-22 05:12
:author: Steve Schwarz
:category: webdev
:tags: django, googility, python, tdd, testing
:slug: confidently-refactoring-django-urls-views-and

`Googility.com`_\ is my first Django website and under the covers the
oldest code looked like it. I had originally written it with the sole
intent of allowing people to enter dog agility businesses and websites
into a database that I could use to create a Dog Agility `Google Custom
Search Engine`_. The primary mistake I made was making the "project" (in
Django speak) effectively equivalent to the primary application. In
other words I didn't divide the major features of the site into
standalone applications (which would allow them to be more easily
reused, extended and tested).

As I continued to work on it I learned more about organizing Django
projects. When I added the periodical search to the website I created it
as a standalone application. I recently split out my
`django-shrinktheweb`_ application from the main code base.

The Custom Search Engine (CSE) functionality is a worthwhile application
that I'm planning on releasing as its own reusable application. I had
already created an application directory called "cse" into which I had
placed my models, views, urls, and tests specific to the CSE
functionality. But I wanted to make the following changes:

-  Move CSE templates into a cse template subdirectory
-  Name the templates to match the views that use them
-  Name the urls in the urls.py prefixed with the application name
   ("cse\_")
-  Covert all reverse() calls in the views and url template tags to use
   the named urls

Those are enough changes that I was concerned that I might miss
something that would fail either in the view code or in rendering of the
templates.

The Django test client makes it easy to test the forward and reverse url
matching, calling the view and rendering the template. It is kind of a
coarse grained test but the changes I was making were perfect for this
tool. Given a urls.py:

.. code:: python

  urlpatterns = patterns('cse.views',
                      url(r'^site/view/(?P<id>d+)/$', 'view', name='cse_view'),)``

and a view:

.. code:: python

  def view(request, id, template='cse/view.html'):
      """Display an end user read only view of the site information"""
      site = get_object_or_404(Annotation, pk=id)
      return render_to_response(template,
                            {'site': site,
                             'labels': get_labels_for(site, cap=None),
                             },
                            context_instance=RequestContext(request))``

I then wrote a test class to create the required test instances and
tests for each url to verify that the url can be found by name (via
reverse()), the url maps to a view, the view invokes the desired
template(s), and the {% url %} calls within the template can all be
resolved:

.. code:: python

  from django.test import TestCase
  from django.test.client import Client
  from django.conf import settings
  from django.core.urlresolvers import reverse
  from cse.models import Label, Annotation

  class ViewsTestCase(TestCase):
      def setUp(self):
          self.client = Client()
          self.ROOT_URLCONF = settings.ROOT_URLCONF
          # can provide a custom urls.py for testing so the tests can be run when
          # the application is incorporated into another project
          # settings.ROOT_URLCONF = 'cse.tests.cse_test_urls'
          # override the template context processors if there are special ones in place
          # that either you want to test or want to avoid
          self.TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS
          settings.TEMPLATE_CONTEXT_PROCESSORS = ()
          # Create some instances on which we can invoke views
          self.label = Label(name='name', description='description')
          self.label.save()
          self.annotation = Annotation(comment='Site Name', original_url='http://example.com/')
          self.annotation.save()
          self.annotation.labels.add(self.label)
          self.annotation.save()

      def tearDown(self):
          # put settings back so the next tests aren't effected
          settings.ROOT_URLCONF = self.ROOT_URLCONF
          settings.TEMPLATE_CONTEXT_PROCESSORS = self.TEMPLATE_CONTEXT_PROCESSORS
  
      def test_view(self):
          response = self.client.get(reverse('cse_view', kwargs={"id":self.annotation.id}))
          self.assertEquals(200, response.status_code)
          self.assertTemplateUsed(response, 'cse/view.html')

The normal unittest asserts are available in the tests. I'm using one of
the `special asserts provided by the Django test Client`_ to verify that
the template I expected was used. All the templates used (due to
template inheritance) are collected by the client and can also be
verified.

I used these tests in a TDD-ish manner, I wrote the test for a view, ran
the tests and kept resolving errors in the templates as I made the
changes in my bullet list. It made a tedious job simple and gave me good
confidence that I'd found all the renamed urls, views, and templates.

.. _Googility.com: http://googility.com/
.. _Google Custom Search Engine: http://www.google.com/cse/
.. _django-shrinktheweb: http://github.com/saschwarz/django-stw
.. _special asserts provided by the Django test Client: http://docs.djangoproject.com/en/dev/topics/testing/#assertions
