=================================================
 Upgrading Pelican and Migrating to GitHub Pages
=================================================
:date: 2015-11-29 15:00
:author: Steve Schwarz
:category: devops
:tags: pelican, github, python
:slug: upgrading-pelican-migrating-gh-pages


I've been using `Pelican <http://blog.getpelican.com/>`_ for this blog for almost three years with source and output stored in a GitHub repository. The output files were then checked out and hosted as static content behind an `NGINX web server <http://www.nginx.com/>`_ on my VPS. Since I set that up GitHub introduced `GitHub Pages <https://pages.github.com/>`_ with support for custom domains and all the "cool kids" started hosting their static web sites right on GitHub.

I had some free time this weekend and decided to see what it would take to upgrade my Pelican version to the latest (3.6.3) and host my files on GitHub Pages. I had four steps to perform:

1. Create a new environment with the latest Pelican

2. Update my content files for the changes in Pelican versions

3. Put output files into GitHub and verify them on GitHub Pages

4. Move my subdomain to point to my GitHub Pages

Create New Environment
======================

I didn't want to screw up my existing/working virtual environment so I created a new one containing Pelican and ``ghp-import`` which does all the work of updating the ``gh-pages`` branch with the output:

.. code:: bash

  # Create a new virtualenv
  mkvirtualenv pelican-new
  # Install pelican and ghp-import:
  pip install pelican ghp-import


Update Content
==============

This was arguably the most painful part as I wasn't using appropriate reStructuredText markup for my images and the location of images required removing ``/static`` from the path. So my markup went from:

.. code::


  .. raw:: html

     <div class="thumbnail">

  <img src="/static/images/myimage.png" />

  .. raw:: html

     </div>

to this (which includes adding a missing ``alt`` tag):

.. code::

  .. class:: thumbnail
  .. figure:: {static}/images/myimage.png
     :alt: Clever alt image text goes here

Those changes were mostly mechanical and using ``figure::`` in place of ``raw::`` also cleaned up the mark up. I tested the changes locally and confirmed all modified pages where displaying correctly.

Convert to GitHub Pages
=======================

This setup is now documented in the Pelican docs on `Publish to GitHub <http://docs.getpelican.com/en/3.6.3/tips.html#publishing-to-github>`_ and is easy.

It looks like the clever setup is to put the source for the blog in the ``master`` branch and then check the output of running ``pelican`` into a branch called ``gh-pages``.  The `ghp-import python package <https://github.com/davisp/ghp-import>`_ does all the work of creating and updating the ``gh-pages`` branch from the ``output`` directory for you!

The first thing I did was to switch to my ``master`` branch and then remove the ``content`` directory and all of it's files:

.. code:: bash

   git checkout master
   rm -rf output

Then I edited the ``.gitignore`` file to exclude the ``output`` directory.

I wanted to keep my existing blog working until I worked out all the kinks in the migration. So I delayed pointing DNS to the GitHub pages. That meant I needed to temporarily change the URL of the blog to match where it will be hosted on GitHub pages. So I edited the ``publishconf.py`` configuration file and changed the ``SITEURL`` temporarily from:

.. code:: python

    SITEURL = 'http://steve.agilitynerd.com'

to it's location on GitHub Pages:

.. code:: python

    SITEURL = 'http://saschwarz.github.io/steve-agilitynerd'

Get the URL by clicking on the Settings tab for the GitHub repository:

.. class:: thumbnail
.. figure:: {static}/images/github-pages-url.png
   :alt: Screenshot of GitHub settings showing URL for GitHub pages

Now that the ``master`` branch is set up I checked in and commited the changes:

.. code:: bash

  git commit -a -m"Migration to GitHub Pages"

Now I followed the instructions in the Pelican docs to generate the output and add it to the ``gh-pages`` branch via ``ghp-import`` (except they show using ``pelicanconf.py`` which I use for local development)

.. code:: bash

  pelican content -o output -s publishconf.py
  ghp-import output

or, since I opted to have Pelican automation setup, I did:

.. code:: bash

  make github

``ghp-import`` committed and pushed the output to GitHub and I tested that files/images were correctly being served by going to the GitHub Pages URL in my browser.

Move Subdomain to GitHub Pages
==============================

This step is well documented in the GitHub help page: `About custom domains for GitHub Pages sites <https://help.github.com/articles/about-custom-domains-for-github-pages-sites/>`_. In my case I was already using a subdomain for my Pelican blogs so I just followed their instructions.

On my VPS's DNS configuration screen I deleted my subdomain's ``A`` record pointing to my VPS and added a ``CNAME`` record pointing to my GitHub `.io` account.

Then **don't followed these instructions:** `Adding a CNAME file to your repository <https://help.github.com/articles/adding-a-cname-file-to-your-repository/>`_ to setup a ``CNAME`` file in the ``gh-pages`` branch. The instructions work but ``ghp-import`` deletes the content of the ``gh-pages`` branch before re-adding files and that deletes the ``CNAME`` file you just added!

After some googling I found Tip #2 in the `Pelican Tips <http://docs.getpelican.com/en/latest/tips.html#extra-tips>`_ and followed their instructions. I added the following to my ``publishconf.py``:

.. code:: python

  STATIC_PATHS = ['images', 'extra/CNAME']
  EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

Then I created the ``CNAME`` file in the new ``content/extra`` directory with the name of my subdomain in it:

``steve.agilitynerd.com``.

Undo the edit to ``publishconf.py`` so it uses the subdomain name:

.. code:: python

    SITEURL = 'http://steve.agilitynerd.com'

Commit that edit to the ``master`` branch and then regenerate the output and commit it to ``gh-pages`` branches:

.. code:: bash

  git commit -a -m"Done with migration to sub domain"
  git push
  make github

Opened the browser to my subdomain and verified that images and links within the site were working correctly. I went back to my VPS and disabled the subdomains from NGINX and deleted the blog check outs to free some resources.  Two fewer websites to maintain on my VPS!
