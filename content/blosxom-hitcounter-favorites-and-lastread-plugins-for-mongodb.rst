Blosxom hitcounter, favorites and lastread plugins for MongoDB
##############################################################
:date: 2010-05-17 10:48
:author: Steve Schwarz
:category: webdev
:tags: blosxom, mongodb, perl, webdevelopment
:slug: blosxom-hitcounter-favorites-and-lastread-plugins-for-mongodb

When I wrote my plugins for tracking the visits to each page
(``hitcounter``), presenting the counts by popularity (``favorites``), and
displaying the most recently read posts (``lastread``) I used Perl's
``Storable`` module as a simple way to serialize the data structure to and
from disk. At the time I wasn't too concerned with performance, my blog
`agilitynerd.com <http://agilitynerd.com>`_ didn't suffer under the load of the disk reads/writes.

But periodically I get DOS'd and my website becomes unresponsive. Not
too suprising since Blosxom has to run as a plain CGI script; but I'm
certain the disk writes of these plugins weren't helping. Occasionally
the Storable on disk would become corrupted which would take down the
site (not enough exception handling in the plugins).

I decided to go with `Mongo`_ as the backing data store to remove the
disk reads/write from the cgi script. It supports an increment operation
(ala memcached) so multiple threads can update the hit count and MongoDB
will "do the right thing". It also has a query API that made rewriting
favorites and lastread trivial.

.. raw:: html

   <div style="float:right;padding 20px;">

|Poweredmongodbgreen75|

.. raw:: html

   </div>

I haven't tested the performance but my website, especially the
favorites page, seems faster. Once I write a JavaScript client to update
the hitcounts I'll be able to move the website to a fully cached
deployment while still tracking hits which should make the load of
running the agilitynerd blog very low.

I've hosted the plugins on github:
http://github.com/saschwarz/blosxom-mongodb-plugins The mongohitcounter
plugin can be configured to automatically import existing count data
from the hitcounter plugin's Storable. So conversion to the new plugins
just requires updating the template's variables to the new plugin names.

.. _Mongo: http://mongodb.org

.. |Poweredmongodbgreen75| image:: /static/images/2010/05/9077760-PoweredMongoDBgreen75.png
