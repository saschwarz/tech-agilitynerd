Django Shrink The Web django-stw 0.2.0 Released
###############################################
:date: 2011-04-23 13:32
:author: Steve Schwarz
:category: webdev
:tags: django, shrinktheweb
:slug: django-shrink-the-web-django-stw-020-released

`Shrink The Web`_ has announced a new API for free users using their new
`preview verification`_ feature. This change required changes to my
django-stw package.

The changes (lifted from the `CHANGELOG.txt`_):

Changes to the ``shrinkthewebimage`` template tag:

-  The ``shrinkthewebimage`` template tag is NOT backward compatible with
   version 0.0.1. The alt argument is no longer accepted.

-  The ``shrinkthewebimage`` template tag is now intended for use by free
   accounts, it adds the required preview feature. It can also be used
   by PRO account users wanting the preview functionality.

-  The ``shrinkthewebimage`` template tag now accepts PRO key-value
   arguments in the same manner as the stwimage tag. This functionality
   is shown in theexample template but may not yet be fully implemented
   by the STW web service.

Changes to the ``stwimage`` template tag:

-  The ``stwimage`` can now only be used for PRO features.

Common changes:

-  Template tags now throw exceptions in their constructors instead of
   in the render function so configuration errors are visible during
   development.
-  django-stw defines a key 'lang' for the SHRINK_THE_WEB dictionary
   that can be passed along as a default to the preview tag. Alternately
   a 'lang' keyword can be supplied in each template tag invocation.
   django-stw defaults it to 'en'. This functionality is not yet
   implemented by the STW web service.

The v 0.2.0 package is `available on PyPi`_, as a `source download on
github`_, or via `git clone`_.

.. _Shrink The Web: http://www.shrinktheweb.com/
.. _preview verification: http://www.shrinktheweb.com/content/what-stw-preview-verification.html
.. _CHANGELOG.txt: https://github.com/saschwarz/django-stw/blob/master/CHANGELOG.txt
.. _available on PyPi: http://pypi.python.org/pypi?:action=display&name=django-stw&version=0.2.0
.. _source download on github: https://github.com/saschwarz/django-stw/archives/v0.2.0
.. _git clone: https://github.com/saschwarz/django-stw
