cookiecutter-djangopackage - Do the Right Thing
###############################################
:date: 2013-12-09 20:02
:author: Steve Schwarz
:category: webdev
:tags: python, django, googility, development, testing, travis, rtd, pypi, tox, virtualenv, webdevelopment, github
:slug: cookiecutter-django-do-the-right-thing

In preparation for upgrading and enhancing `Googility.com <http://googility.com>`_ I've started breaking out reusable applications, upgrading them, and open sourcing the code on GitHub. I wanted to follow development best practices and create high quality applications including these features:

* A full set of tests.

* Near 100% code coverage.

* Continuous Integration running on each check-in via `Travis CI <https://travis-ci.org/>`_.

* Documentation in Sphinx on `Read the Docs (RTD) <https://readthedocs.org/>`_.

* Packaging/versioning compatible with `PyPi <https://pypi.python.org/pypi>`_.

* Packaging building/testing on multiple python versions using virtualenvs via `tox <http://tox.readthedocs.org/en/latest/>`_.

I had started researching each aspect and was getting a little frustrated that there wasn't a best practice for tying everthing together. Then I came across `Audrey Roy's <https://twitter.com/audreyr>`_ `cookiecutter <https://github.com/audreyr/cookiecutter>`_ and `Daniel Greenfeld's <http://pydanny.com/>`_ `cookiecutter-djangopackage <https://github.com/pydanny/cookiecutter-djangopackage>`_. ``cookiecutter`` is a utility to create project directory structures and files from the command line. ``cookiecutter-djangopackage`` is a template for creating a reusable Django application.

Yes there are other similar projects, and Django provides ``startproject`` and ``startapp`` commands that can take template arguments. But since I've never used Travis, RTD or tox I really wanted to leverage more experienced developers' knowledge so I could set them up in a "smart" way. 

That's what I liked about ``cookiecutter-djangopackage`` it came with sane defaults that worked out of the box [#]_ and did smart stuff like wiring the version from the package's ``__init__.py`` in to the documentation and ``setup.py``. The ``requirements.txt`` used by ``pip`` is wired in to ``tox`` and the ``README.rst`` is used in the ``setup.py`` and included in the Spinx docs.

And there are other integrations that make it easy to release a professional Django application. In fact that's my long winded point - it makes it hard to not do the right thing! I might have skipped using one or more of these support technologies, but ``cookiecutter-djangopackage`` made it easy for me to use them and focus on writing code, tests and documentation. 

So that is what I want to stress: with ``cookiecutter-djangopackage`` you *can* create a packaged application, whose code is tested on multiple python/Django versions, tested for installation, installable via PyPi and nicely documented without much additional effort.

So take look at my nearly released ``django-periodicals`` application to see how it all works on `GitHub <https://github.com/saschwarz/django-periodicals>`_, `RTD <http://django-periodicals.readthedocs.org/en/latest/>`_ and `Travis <https://travis-ci.org/saschwarz/django-periodicals>`_.

.. rubric: Footnotes

.. [#] I did submit a `pull request <https://github.com/pydanny/cookiecutter-djangopackage/pull/13>`_ and found another resolved issue with application names that don't match their imported package name. (i.e. ``django-periodicals`` is the application name and ``periodicals`` is the package that is imported).
