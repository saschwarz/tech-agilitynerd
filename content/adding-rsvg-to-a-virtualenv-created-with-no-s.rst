Adding pyrsvg to a virtualenv created with --no-site-packages
#############################################################
:date: 2010-10-12 03:02
:author: Steve Schwarz
:category: python
:tags: python, rsvg, virtualenv
:slug: adding-rsvg-to-a-virtualenv-created-with-no-s

I set up my development and deployment environments on Ubuntu with
`virtualenv`_ with the ``--no-site-packages`` option to isolate them from
packages in the system installation. My application uses `pyrsvg`_ and
it is installed by default as a system package. Consequently I had to
link the shared libraries it installs (w/in gtk) into my virtualenv.

Here are the links I created (``workon`` and ``cdsitepackages`` are
`virtualenvwrapper`_ shell aliases)::

  $ workon project
  $ cdsitepackages
  $ ln -s /var/lib/python-support/python2.6/gtk-2.0/rsvg.so .
  $ ln -s /var/lib/python-support/python2.6/gtk-2.0/gobject .
  $ ln -s /var/lib/python-support/python2.6/gtk-2.0/glib .

.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _pyrsvg: http://cairographics.org/pyrsvg/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
