====================================================
 Leverage Pelican For Fast Site/Project Development
====================================================
:date: 2016-11-05
:author: Steve Schwarz
:category: webdev
:tags: python, webdev, webops, pelican, CSS, JavaScript
:status: draft

I was working on a simple single page website for `calculating dog agility jump heights <http://www.agilitynerd.com/jumpheights/>`_ and was really missing the tool chain I normally use in Flask and Django web sites for bundling, compressing, and versioning CSS and JS files and a mechanism for replacing the file names in the HTML files. Then it occurred to me that `Pelican <http://getpelican.com>`_ has just what I needed.

Pelican is known for making static generation of blogs easy. But it also has a lot of powerful features that can be easily leveraged to create small web sites and web sites for projects:

* Use `webassets <https://webassets.readthedocs.io/en/latest/>`_ integration to SASS/LESS, minify, bundle, and version CSS and JavaScript. Then insert versioned bundled names in the HTML.
* Dozens of `themes <https://github.com/getpelican/pelican-themes>`_.
* Themes are implemented using `Jinja2 templates <http://jinja.pocoo.org/>`_ and allow sharing page layouts across your project's pages.
* Theme templates contain useful integrations which can be used in you templates:
  * Navigation
  * Analytics
  * Disqus
* Dozens of `Pelican plugins <https://github.com/getpelican/pelican-plugins>`_ can be installed to add new features.
* During development automatic regeneration of files is available upon edit.
* Many deployment options are also available:
  * GitHub pages
  * FTP
  * SSH
  * Dropbox
  * S3
  * Rackspace Cloud Files
* I've added `Live Reload of the browser <https://gist.github.com/saschwarz/8eff30f5ea5d468f0b86bd0bb149a186>`_ after page regeneration.


 It's So Easy

  * Create virtualenv and install:

    * pelican

    * webassets

  * `pelican-project???`

  * Edit `pelican.conf` as follows:

  * Copy any theme from pelican-themes into .theme

Now to create you web site! It's easy:

  * Edit base.html and delete/add any sections, stylesheets and javascript you like. Your page's will only define content that goes in the `content` block of the Jinja templates. Similarly you can define your own templates and use the full power of Jinja templating.

I put my files in `content/pages`. Within each file I set the `url_for` attribute to define the output URL.

For a non-blog site I found it easy to write my page content directly in HTML. Though you can use any input representation supported by Pelican e.g. ReStructuredText, Markdown, or even write a Reader class for your own custom input file format.

I used webassets to combine JS/CSS files into bundles, minify and version them. In the base.html I just did:


DIRECT_TEMPLATES setting EXTRA_TEMPLATE_PATHS
