reCAPTCHA in Django
###################
:date: 2008-12-23 22:04
:author: Steve Schwarz
:category: webdev
:tags: django, recaptcha
:slug: recaptcha-in-django-1

I first read about `ReCAPTCHA`_ in `this article in Wired magazine`_
last year.

reCAPTCHA provides a free CAPTCHA web service that
pairs together two words from OCR scanned books. One of the words is
known and the other couldn't be recognized. The user types in both words
not knowing which is unknown to the system. As reCAPTCHA collects the
responses for the unknown word they get human verified character
recognition. So the millions of users of the system are clearing up
millions of unrecognized words. It is a very clever human "cloud
computing" system using only seconds of human effort for each use of the
system.

.. raw:: html

   <div class="thumbnail" style="float:right;">

|recaptchalogo|

.. raw:: html

   </div>

I'm using a `FIGLet based ASCII CAPTCHA`_\ on my websites since it was
easy to integrate into the `Blosxom`_ writeback plugin. But I wanted to
give reCAPTCHA a try while converting my `Googility`_ site to `Django`_.
`John DeRosa`_ made my job trivial by `writing up the steps with a clear example`_.

So I followed his directions which involved installing the
recaptcha-client python library on my dev and production systems and
obtaining a free public/private license key from the reCAPTCHA site.
Then I updated my Django view and template files for the one form that
needed CAPTCHA protection. It was dead simple and working within
minutes. The only minor addition I'd make to John's article is of course
you need to pass the ``captcha_error`` variable from your view to the
template::

  return render_to_response('edit.html', {'form': form, 'captcha_error':captcha_error})

So give reCAPTCHA a try for your next project. It was so easy to do I
might even convert my Blosxom blogs to use it via Lars Engel's
`recaptcha plugin`_.

.. _ReCAPTCHA: http://recaptcha.net/
.. _this article in Wired magazine: http://www.wired.com/techbiz/it/magazine/15-07/ff_humancomp?currentPage=all
.. _FIGLet based ASCII CAPTCHA: /comment-spam-and-wbcaptcha-plugin-enhancement-1.html
.. _Blosxom: http://blosxom.sourceforge.net/
.. _Googility: http://googility.com/
.. _Django: http://www.djangoproject.com/
.. _John DeRosa: http://seeknuance.com/
.. _writing up the steps with a clear example: http://seeknuance.com/2008/03/18/integrating-recaptcha-with-django/
.. _recaptcha plugin: http://blog.berlund.de/public/other/recaptcha

.. |recaptchalogo| image:: /static/images/2009/11/5014940-media_httpdataagilitynerdcomimagesrecaptchalogogif_IkgnpackrkjkaCy.gif
