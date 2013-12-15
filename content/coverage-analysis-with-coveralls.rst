Integrated Coverage Analysis with Coveralls
###########################################
:date: 2013-12-15 17:00
:author: Steve Schwarz
:category: webdev
:tags: coverage, webdevelopment, github, django
:slug: coverage-analysis-with-coveralls
:description: Coveralls made it so simple to add coverage testing to my Travis-CI configuration for django-periodicals. I found that it pushed me to take coverage testing all the way.


When I converted `django-periodicals <https://github.com/saschwarz/django-periodicals>`_ to use `cookiecutter-djangopackage <|filename|cookiecutter-djangopackage-do-the-right-thing.rst>`_ I was running `coverage.py <https://pypi.python.org/pypi/coverage>`_ in my `Travis-CI <https://travis-ci.org>`_ ``.travis.yml`` to report the coverage results to the command line log. The coverage results were interesting but didn't really alter my development practice much.

Over the years I've had differing options about coverage testing/analysis. Like any programming metric you can "cook the books" and pump up the metric while not actually improving the quality or maintainability of the code being measured.  Minimally coverage testing can uncover unexercised corners of the code, especially error handling code. Nothing is worse than crashing an application with faulty error handling code.

``coverage.py`` is trivial to run and it generates reports in various formats to make finding unexercised code simple. It is so easy there is no reason not to run it.

So my local coverage testing showed 7% of my code wasn't exercised - "good enough" right?

Then I discovered `Coveralls <https://coveralls.io/>`_. Coveralls integrates with Travis and collects coverage data for each buid and displays it on their website. It was `trivial to setup <https://github.com/coagulant/coveralls-python#usage-travis-ci>`_:

* Create a login on Coverall and enable your Travis-CI project.

* Add ``coveralls`` to the project's test ``requirements.txt``.

* Then add ``after_success: coveralls`` to ``.travis.yml``.

The next time the project is tested on Travis-CI the coverage results appear on coveralls.io. You can view the untested code in each file and Coveralls will track the increase/decrease of coverage in each file each time you check-in/test.

They also have badges showing the percent coverage that you can embed in your reStructuredText documentation on GitHub and ReadTheDocs. And that's the insidious part of integrated open source development...

The ``cookiecutter-djangoproject`` produces an application GitHub page that shows the Travis-CI test status and the PyPi package version. With the addition of the Coveralls badge it can now show the coverage percentage. That turned out to be a little bit of programming peer group pressure that made 93% coverge no longer "good enough"!

So a few minutes and a few tests later I had tests that did exercise the full code base including error handling. That gave me a happy little green badge that displayed "coverage 100%".

So not only is Coveralls fully integrated with the GitHub - CI - Open Source infrastructure, and dead simple to use, it got this developer to push into all the corners of his code before releasing. And I now have the peace of mind that Travis *and* Coveralls will be watching my back.

.. image:: https://badge.fury.io/py/django-periodicals.png
    :target: http://badge.fury.io/py/django-periodicals
    
.. image:: https://travis-ci.org/saschwarz/django-periodicals.png?branch=master
        :target: https://travis-ci.org/saschwarz/django-periodicals

.. image:: https://coveralls.io/repos/saschwarz/django-periodicals/badge.png?branch=master 
        :target: https://coveralls.io/r/saschwarz/django-periodicals?branch=master

