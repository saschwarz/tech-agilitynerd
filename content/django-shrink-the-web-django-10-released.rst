Django Shrink The Web django-stw 1.0 Released
#############################################
:date: 2017-01-10 13:00
:author: Steve Schwarz
:category: webdev
:tags: django, shrinktheweb, python, images, bootstrap
:slug: django-shrink-the-web-10-released

It has been several years since I've worked on my `Django`_ driven website that uses `Shrink The Web`_ (STW) screen shots.
During that time STW has simplified their feature set and their API.

As I upgraded my site (`Googility.com`_) I took
some time to modernize the ``django-stw`` template tag and support API changes for the latest Django and Python versions.

I also tested the package when deployed using HTTP and HTTPS.

Here are the changes (from the `CHANGELOG.txt`_)::

    1.0.1 Use https for all requests to shrinktheweb.com
    - Stops browser warnings when used on https websites while not interferring with sites running on http.

    1.0.0 Updates for Django 1.9/1.10 and Python 2.7/3.5
    - Old versions of Django/Python are no longer supported.
    - Removed ``shrinkthewebimage`` template tag since there is no longer an API distinction between free and Pro accounts.

You can the template tag in action on this `demo page`_ in a nicer `"Bootstrap-ified"`_ UI:

.. class:: thumbnail
.. figure:: {filename}/images/DjangoSTWDemoScreenshot.png
    :alt: Screenshot of first slide of my presentation

The latest package is `available on PyPi`_:

.. code:: python

    pip install django-stw

Or as a `source download on github`_, or via `git clone`_.

.. _Django: https://www.djangoproject.com/
.. _Googility.com: https://www.googility.com/
.. _Shrink The Web: http://www.shrinktheweb.com/
.. _CHANGELOG.txt: https://github.com/saschwarz/django-stw/blob/master/CHANGELOG.txt
.. _demo page: https://www.googility.com/django-stw/
.. _available on PyPi: http://pypi.python.org/pypi?:action=display&name=django-stw
.. _source download on github: https://github.com/saschwarz/django-stw/releases
.. _git clone: https://github.com/saschwarz/django-stw
.. _"Bootstrap-ified": http://getbootstrap.com/