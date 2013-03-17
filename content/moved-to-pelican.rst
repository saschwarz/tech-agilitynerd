Moved To Pelican
################
:date: 2013-03-17 12:00
:author: Steve Schwarz
:category: webdev
:tags: posterous, pelican, blosxom
:slug: moved-to-pelican

Way back in 2004, when the content in this blog was a category in the main `AglityNerd blog <http://agilitynerd.com>`_, I used the Perl `Blosxom <http://blosxom.sourceforge.net/>`_ application to serve the blog. When my dog agility readers complained/were confused by the sprinkling of tech postings I split off tech.agilitynerd in another Blosxom instance. 

Once modern web hosted blogs came in to existence I wanted to see how they worked and moved the tech content to `posterous <http://posterous.com>`_. That was only OK, the source code formatting was painful but it did support email and web based content creation. I was reasonably content, not bugged enough to move again.

Then posterous announced `it is closing on April 30 <http://blog.posterous.com/thanks-from-posterous>`_ so I finally had to do something. This site really only needs a few features:

- easy format in which to write content

- source code formatting

- Atom/RSS feeds

- comments

I use Disqus for comments on my other sites so that meant I could go with a statically generated site. Also since I primarily code in Python I wanted a platform to which I could contribute. I came across `Pelican <http://blog.getpelican.com/>`_ and it fit the bill nicely.

I exported the posterous posts, imported them through a temporary wordpress.com site and re-exported them in wordpress format. After a quick bug fix to the pelican wordpress importer I was able to generate reStructured Text files for each post. After a few days of editing the embeded source code in the content files and fixing long broken links, I had the blog running and not looking bad at all.

I wanted a Twitter Boostrap based responsive layout and I found `azizmb's pelican-bootstrap-responsive-them <https://github.com/azizmb/pelican-bootstrap-responsive-theme>`_ which had a very pleasing layout. I tweaked it to have category and tag feeds and some other enhancements to get what you see today. I will see if Aziz is interested in pulling any of my changes back.

So far I like using Pelican and I've made the `content of the blog <https://github.com/saschwarz/tech-agilitynerd>`_ and my `edits to the theme <https://github.com/saschwarz/pelican-bootstrap-responsive-theme>`_ available on github in case anyone is interested.
