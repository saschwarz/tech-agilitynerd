===========================================
 Pelican For Fast Site/Project Development
===========================================
:date: 2016-11-08 13:00
:author: Steve Schwarz
:category: webdev
:tags: python, webdev, webops, pelican, CSS, JavaScript


I was working on a simple single page website for `calculating dog agility jump heights <http://www.agilitynerd.com/jumpheights/>`_ and was really missing the tool chain I normally use in Flask and Django web sites for bundling, compressing, and versioning CSS and JS files and a mechanism for putting the bundled/versioned file names in the HTML files. I was searching for what I needed and was about to write a little script to do it and then it occurred to me that `Pelican <http://getpelican.com>`_ already has just what I needed!

Pelican is known for making static generation of blogs easy. But it also has a lot of powerful features that can be easily leveraged to create small web sites and web sites for projects:

* `webassets <https://webassets.readthedocs.io/en/latest/>`_ integration to SASS/LESS, minify, bundle, and version CSS and JavaScript. It automatically inserts versioned bundled names in the HTML.
* Dozens of `themes <https://github.com/getpelican/pelican-themes>`_.
* Themes are implemented using `Jinja2 templates <http://jinja.pocoo.org/>`_ and allow sharing page layouts across your project's pages. You can also have custom templates per page.
* Theme templates already contain useful integrations which can be used in you templates:

  * Navigation
  * Analytics
  * Disqus

* Dozens of `Pelican plugins <https://github.com/getpelican/pelican-plugins>`_ can be installed to add new features.
* During development regeneration of files is automatic when you save files.
* Many deployment options are also available:

  * GitHub pages
  * FTP/SSH to your own server
  * Dropbox
  * S3
  * Rackspace Cloud Files


Overview
========

I've written a lot of detail on every step but it is actually very easy use Pelican for non-blog web sites. Here's how it works:

#. Create a virtualenv and install Pelican and webassets Python packages (I use the same venv for all my Pelican projects).

#. Checkout pelican-plugins.

#. Edit the Pelican theme's ``base.html`` Jinja template to include the CSS and JavaScript files you need.

#. Create your pages' body content in files in ``content/pages`` in HTML, Markdown or reStructuredText.

#. Run ``make devserver`` and refresh your browser to see your changes or use this `LiveReload script <|filename|pelican-livereload.rst>`_ to automatically reload your browser.

#. Repeat steps 3 and 4 until you are done.

#. Deploy to GitHub Pages: ``make github``. Or deploy to your own server.


Setup the Environment
=====================

Install and configure Pelican for creating non-blog web sites:

#. Create a virtualenv and install pelican, webassets, cssmin, and jsmin (or any other `CSS/JS filters supported by webassets <http://webassets.readthedocs.io/en/latest/builtin_filters.html>`_)::

    virtualenv ~/virtualenvs/pelican
    source ~/virtualenvs/pelican/bin/activate
    pip install pelican webassets cssmin jsmin

#. Check out the pelican plugins repository outside of your project (plugins are only used during the build process)::

    git checkout https://github.com/getpelican/pelican-plugins.git

#. Create your project directory, run ``pelican-quickstart`` and answer the questions just like for a blog site::

    mkdir myproject && cd $_
    pelican-quickstart

    Welcome to pelican-quickstart v3.6.3.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.

    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Dog Agility Jump Height Calculator
    > Who will be the author of this web site? Steve Schwarz
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
    > /agility-jump-heights           <-- enter the name of your GitHub repository
    > Do you want to enable article pagination? (Y/n) n
    > What is your time zone? [Europe/Paris] America/Chicago
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N) n
    > Do you want to upload your website using Dropbox? (y/N) n
    > Do you want to upload your website using S3? (y/N) n
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    > Do you want to upload your website using GitHub Pages? (y/N) y
    > Is this your personal page (username.github.io)? (y/N) n
    Done. Your new project is available at /home/dev/agility-jump-heights

#. Paste the following at the end of your ``pelican.conf``::

     STATIC_PATHS = ['images']  # put page specific assets here
     PLUGIN_PATHS = ['../pelican-plugins']  # set this to the location of your plugins checkout
     PLUGINS = ['assets']
     THEME = './theme'          # All CSS/JS files go in directories under here
     # I only want to generate Pages so I disable all "blog-like" pages see Note in:
     # http://docs.getpelican.com/en/stable/settings.html?highlight=url_for#url-settings
     TAGS_SAVE_AS = ''          # Don't generate Tags pages
     TAG_SAVE_AS = ''
     CATEGORY_SAVE_AS = ''      # Don't generate Category pages
     AUTHOR_SAVE_AS = ''        # Don't generate Author pages
     DIRECT_TEMPLATES = ['index']  # Don't generate tag, category, or author output for some themes
     # In the generated output directory move files to the root and adjust their URLs to match:
     PAGE_URL = '{slug}.html'
     PAGE_SAVE_AS = '{slug}.html'
     INDEX_SAVE_AS = "/ignore/index.html"  # don't create normal index.html which lists all articles and pages

#. Copy any theme from ``pelican-themes`` into ``.theme`` or I just copy the ``notmyidea`` theme installed with Pelican from the virtualenv::

    cp -pR $VIRTUAL_ENV/lib/python*/site-packages/pelican/themes/notmyidea/ theme

#. Have Git ignore the output directory::

     echo "/output" >> .gitignore


Create Your Project Web Site
============================

Setup Templates
---------------

Edit ``./templates/base.html`` and delete/add any sections, stylesheets and javascript you like. Your pages only need to define content that goes in the `content` block of the Jinja templates. Of course you can define your own templates and use the full power of Jinja templating `even for individual pages <http://docs.getpelican.com/en/stable/settings.html?highlight=url_for#template-pages>`_.

For small projects it is easiest to serve the same JS/CSS on all pages so I put them in the ``base.html`` file. Using Jinja template inheritance you can also create and serve separate bundles for individual pages.

I use ``webassets`` right in the template to define how to combine JS/CSS files into bundles, minify and version them. For CSS files in the ``head`` of my ``base.html``::

        {% assets filters="cssmin", output="css/style.%(version)s.min.css", "css/normalize.css", "css/skeleton.css", "css/style.css" %}
       <link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
        {% endassets %}

For JavaScript the bundled, versioned, compressed ``script`` tag(s) is defined similarly just before the end of the HTML ``body`` tag::

        {% assets filters="jsmin", output="js/main.%(version)s.min.js", "js/main.js" %}
        <script src="{{ SITEURL }}/{{ ASSET_URL }}"></script>
        {% endassets %}

For more options `see the webassets README <https://github.com/getpelican/pelican-plugins/blob/master/assets/Readme.rst>`_.

Edit ``theme/templates/page.html`` to suite your needs. I just put in a wrapper ``div`` around the content::

    {% extends "base.html" %}
    {% block title %}{{ page.title }}{% endblock %}

    {% block content %}
    <div class="container">
    {{ page.content }}
    </div>
    {% endblock %}

You can also delete any CSS, JS, images, and unused Jinja templates from your copied theme.

Write the Pages
---------------

Create the ``pages`` directory::

  mkdir content/pages

Lastly put each page's body content in a file in the ``content/pages`` directory. I like to write the body content in HTML. You put the Pelican metadata in ``meta`` elements in the ``head`` element as `shown the Pelican docs <http://docs.getpelican.com/en/stable/content.html#file-metadata>`_. Here's ``index.html`` and I recommend specifying the ``title`` and ``save_as``::

    <html>
        <head>
            <!-- By default used to create the URL slug -->
            <title>Dog Agility Jump Height Calculator</title>
            <!-- Override the default URL made up of the slug; needed for the index.html -->
            <meta name="save_as" content="index.html"/>
            <!-- any other metadata attributes as meta tags; none normally needed -->
        </head>
        <body>
            <!-- all  markup goes here. e.g. -->
            <h1>Hello World!</h1>
        </body>
    </html>

You can use any input syntax supported by Pelican e.g. ReStructuredText, Markdown, or even write a Reader class for your own custom input file format.

Start up the Pelican development server to watch for file changes and regenerate changed files::

  make devserver

Point your browser to ``http://localhost:8000/``.

I recommend using this `LiveReload script <|filename|pelican-livereload.rst>`_ as it also watches for changes to the ``themes`` directory and automatically reloads your browser on ``http://localhost:5500``.

Once you are setup just edit your templates, JS, and CSS under the ``theme`` directory and add/edit pages in your ``content/pages`` directory.


Deploy
------

I like to deploy small projects to GitHub Pages and it's this easy::

    make github

Then on GitHub enable GitHub Pages in your project's settings.

To see this whole setup in action take a look at this `single page calculator application with one JS and HTML file <https://github.com/saschwarz/agility-jump-heights>`_.

The next step to make this even easier would be to use `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ to make setting this up via one command.
