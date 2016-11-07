=========================
 LiveReload with Pelican
=========================
:date: 2016-11-06
:author: Steve Schwarz
:category: webdev
:tags: python, webdev, pelican

I was looking to use `LiveReload <http://livereload.com/>`_ while developing using  `Pelican <http://getpelican.com>`_ and I came across this `nice simple solution <https://merlijn.vandeen.nl/2015/pelican-livereload.html>`_ by `Merlijn van Deen <https://merlijn.vandeen.nl/>`_.

In my use case I also wanted to watch the ``pelicanconf.py`` file and ``themes`` directory for changes and then regenerate the output and reload the browser. Lastly I wanted to use the host/port defined in my ``pelicanconf.py``. So I made some small edits to his script named ``pelican-livereload.py``:

.. raw:: html

  <script src="https://gist.github.com/saschwarz/8eff30f5ea5d468f0b86bd0bb149a186.js"></script>

Just copy it into your Pelican top level directory and execute it::

  python ./pelican-livereload.py

The LiveReload server automatically injects the livereload JavaScript script tag into the HTML so you don't need to install the LiveReload browser extension.

So all you need to do is visit the ``SITEURL`` you've specified in your ``pelicanconf.py`` otherwise it defaults to ``http://localhost:5500``. Then any edit you make causes Pelican to regenerate the files and the browser immediately refreshes. The only downside to the regular Pelican watcher feature is all files are regenerated instead of just the modified file. But for me having the browser automatically reload is is worth the extra brief delay.
