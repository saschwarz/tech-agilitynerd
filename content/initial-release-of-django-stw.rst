Initial Release of django-stw
#############################
:date: 2010-07-11 15:47
:author: Steve Schwarz
:category: python
:tags: django, github, googility, pypi, python, shrinktheweb, webdevelopment
:slug: initial-release-of-django-stw

I have been using the free website thumbnail service from `Shrink The
Web`_ on my dog agility search website `Googility`_ since I launched it.
It is quick and easy to use and it adds a lot to the look of the pages.

I had created a simple `Django`_ template tag for inserting the little
snippet of HTML needed by their service.

Recently they asked me to add support for their advanced features to my
template tag. I used this opportunity to convert my templatetag to a
Django application. This mostly makes it a lot easier to install but it
also let me to bundle tests and an example template with the template
tag.

I kept the existing ``shrinkthewebimage`` template tag and added a new
tag called ``stwimage`` to enable the new features.

I'm hosting the example page included in the package `here`_ so you can
see how the template tags work.

I've hosted the `project source on github`_ and uploaded the `initial
release to the CheeseShop`_ for easy installation.

.. _Shrink The Web: http://www.shrinktheweb.com?a=988
.. _Googility: http://googility.com
.. _Django: http://djangoproject.com/
.. _here: http://googility.com/django-stw/
.. _project source on github: http://github.com/saschwarz/django-stw
.. _initial release to the CheeseShop: http://pypi.python.org/pypi/django-stw/
