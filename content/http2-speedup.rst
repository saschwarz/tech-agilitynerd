=========================================
HTTP/2: A Quick and Easy Website Speed Up
=========================================
:date: 2016-09-23 18:00
:author: Steve Schwarz
:category: devops
:tags: nginx, ubuntu, https, ssl, http2, performance
:slug:


I always want my websites to be secure and fast. `HTTP/2 <https://http2.github.io/>`_ is the latest enhancement to the HTTP protocol that can provide significant performance improvements:

.. epigraph::

    The primary goals for HTTP/2 are to reduce latency by enabling full request and response multiplexing, minimize protocol overhead via efficient compression of HTTP header fields, and add support for request prioritization and server push.

    -- `High Performance Browser Networking - O'Reilly <https://hpbn.co/http2/>`_:

It turns out all browsers that support HTTP/2 `also require TLS (HTTPS) <http://caniuse.com/#feat=http2>`_. So my first step was `adding HTTPS support to agilitycourses.com <{static}/nginx-django-https.rst>`_ which also provides a backbone on which I'll implement secure user profiles. Then I wanted to enable HTTP/2 to see if it improved the speed of pages served to end users.


But First an OS Upgrade
=======================

After a little research I found that recent releases of `NGINX <https://nginx.org/en/>`_ support HTTP/2 and those versions are packaged with Ubuntu 16.04 LTS. That made upgrading to this latest long term support OS version a better approach than just upgrading NGINX on my older OS. I basically went through the `standard upgrade process <https://www.digitalocean.com/community/tutorials/how-to-upgrade-to-ubuntu-16-04-lts>`_.

While I had to work through a number of small issues upgrading my older websites; the biggest change was converting my upstart scripts to systemd scripts. But the beauty of hosting with virtual servers is it was trivial to create an image of my existing server, spin up a temporary server using that image, and then practice the ugprade/migration on the temporary server. I was able to move some configuration changes back to my live server and test out the changes to my sites' `Fabric <http://www.fabfile.org/>`_ deployment scripts.

Once everything was working I configured my websites that contain user modifiable data into maintenance mode on my temporary server. Then I pointed the DNS for all my domains to the temporary server. After DNS propagated I shutdown Postgres and the webserver on my original server and created a backup image. Then I went through the upgrade process. Once I validated the migration was successful I switched the DNS back to my original server and shutdown the temporary server. After a couple days I deleted the temporary server and the pre-migration backup image.


Enabling HTTP/2
===============

Once I was on NGINX version 1.10 the change to the website to enable HTTP/2 was as simple as changing the virtual server from::

    server {
        listen 443 ssl;
        listen [::]:443 ssl;
    ...
    }

to::

    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;
    ...
    }

Then I just reloaded the Nginx configuration: ``sudo systemctl reload nginx``. That was it!


Testing
=======

Here's the network view of the timing of requests for a page using HTTP/1.1 over HTTPS in Chrome:

.. image:: /images/agilitycourses-http1.png
           :alt: Diagram of HTTP requests for a page showing requests being delayed by previous requests for the same domain.
           :class: thumbnail

Here's the same page using HTTP/2 over HTTPS:

.. image:: /images/agilitycourses-http2.png
           :alt: Diagram of HTTP requests for a page showing requests being multiplexed with previous requests for the same domain.
           :class: thumbnail

The obvious difference is in the *Timeline - Start Time* column. In the first diagram you can see the "waterfall" queueing up of requests for images as all the open sockets to the domain were in use. In the second diagram you can see them all interleaved as they are multiplexed across the same connection.

Also the bottom line is the page is fully loaded in 1.73 sec using HTTP/1.1 and in 1.16 sec using HTTP/2 for a **33% end user page load improvement!**


Next Steps
==========

So that was a nice free speed up and there are plenty of areas I can still investigate to further improve the performance of this web site:

- Bring 3rd party resources back to my domain to save DNS lookups and see how that affects overall performance. This may hurt performance for HTTP/1.1 clients who are limited to the number of connections per domain.
- Change multiple SVG files (which are all steps in a progression) into a single file and use CSS to hide/show appropriate steps using a single image. This will greatly reduce the number of individual files downloaded and save some duplicated data within those files.
- Move Google Analytics locally. GA has a number of problems (short cache times and multiple files downloaded) so at the cost of periodically updating the files I could host them all locally and save some time.
- Disqus is even worse than GA when it comes to many file downloads, redirects, short cache times etc. I might change to have Disqus data loaded on user demand.
- Experiment with other HTTP/2 features:
    - `preconnect <https://www.igvita.com/2015/08/17/eliminating-roundtrips-with-preconnect/>`_ might help reduce the cost of DNS look ups that result from redirects like those used by Google Analytics, Google Fonts, and Disqus resources.
    - `preload <https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/>`_ to load resources before they are accessed by JS during ``onload`` or via user actions.
    - `prefetch <https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ>`_ to load JS/images for future pages. There are some common workflows on this site that could benefit from prefetching the JS for subsequent pages.
