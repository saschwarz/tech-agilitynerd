Image Theft Ranting And Blocking
################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: apache, sysadmin
:slug: image-theft-ranting-and-blocking-1

I was really disappointed yesterday when I checked my blog's statistics
and found that someone from a Hungarian Agility discussion board had
directly linked course images from my website. Direct linking of an
image is placing the URL of the image directly in a webpage hosted on
another server. Each time a browser loads that page the direct link
causes the other server to send the image to the client's browser. So
each time the forum is viewed my server has to send the images to the
forum's viewer.

I purposely try to make my image sizes small to make it possible for
dial up visitors to view my site without too much delay. So direct
linking doesn't impact my bandwidth costs too much; so far it is about
1Mb a day. The additional burden it puts on the webserver should be
small too, but since I don't own the shared server I don't really know.

Ranting
-------

The aspect of this that most irritates me is that someone would copy my
work without attribution. That is the only thing I ask of visitors to my
site who wish to reuse my content. The `license link`_ at the bottom of
each page should make this clear. I really don't think this is it too
much to ask.

I take copyright infringement very seriously. To me it isn't just the
legal requirements of using other's material in accordance with their
wishes that is important, taking credit, explicitly or implicitly, for
another's work is just wrong. This is one of those `All I Really Need To
Know I Learned In Kindergarten`_ concepts: `Don't take things that
aren't yours`_. As a friend of Nancy's says "Some people don't have good
home training".

Lastly, the Agility community is still a small community and the online
Agility community even more so. I guess I am naive, but I hoped that the
members of our community wouldn't do things like this.

Blocking
--------

My first step was emailing the webmaster of the site. The site was
entirely in Hungarian so it is possible the webmaster may not have
understood my English request. In any event, after 24 hours they hadn't
removed the links.

So I went to look for a technical solution. There are a few well known
technical solutions for this problem. A search of Google for `blocking
direct linking`_ or `blocking hotlinking`_ will turn them all up. The
most useful solutions include:

  -  Rename the direct linked images
  
    This mean updating all posts one your site to match the new name.
    But if you only have a few images and/or posts to them you can do this on a per direct link basis.
    
  - Randomly generate image file names that change over time
  
    This is usually used for photo galleries where there is no text referring to each image.
    
  - Serve images through a script

    This script would reject requests for images based on information in
    the request. This can be a compute intensive approach since it causes
    requests even from your own site to go through the script. For sites
    where you don't have control over the webserver this may be required.

  - Use a Rewrite rule to serve a different image to non-local referers

    This is the technique I used.

Based on this `altlab.com article`_ I originally added these rules to my
.htaccess file on my server::

   RewriteEngine on
   RewriteCond %{HTTP\_REFERER} !^$
   RewriteCond %{HTTP\_REFERER} !^http://(www.)?agilitynerd.com/.\* [NC]
   RewriteRule .\*.(jpg\|jpeg\|gif\|png\|bmp)$ /images/nodirectlink.g [L,NC]

I then created an image called nodirectlink.g shown below.


Redirected Image
----------------

.. raw:: html

   <div class="p_embed p_image_embed">

|image0|

.. raw:: html

   </div>

Don't use the same filename suffix as one of the real image filenames
you use or you'll loop the rewrite engine.

I had forgotten about images direct linked by RSS feed readers that
access the root. Rather than rewrite those requests I moved my Rewrite
rules into the .htaccess file in the images directory. I also decided to
not send the image after all, I'll just fail the request. There is no
sense in even wasting the bandwidth, the clients will now get the broken
image icon from their browser. The official `Apache URL Rewriting
Guide`_ describes this in the Blocked Inline-Images section. So here is
my final solution::

  RewriteEngine on
  RewriteCond %{HTTP\_REFERER} !^$
  RewriteCond %{HTTP\_REFERER} !^http://(www.)?agilitynerd.com/.\*$ [NC]
  RewriteRule .\*.(jpg\|jpeg\|gif\|png\|bmp)$ - [F]

I took this opportunity to modify some of my very first articles and
move their images into the /images directory. Those images were being
served by the Blosxom binary plugin back when I thought it was a
good idea. Now I won't pay any extra processing cost for those images.

Conclusion
----------

So now I have a technical solution to a human problem. There is a chance
that this change may cause some viewers of this site to not see images
on this site. But hopefully that should be a very, very small number of
people. But if you think you are getting my blocking image incorrectly
Please email me: steve at agilitynerd.com.

I'm still disappointed I was forced to resort to this change.

.. _license link: http://creativecommons.org/licenses/by-nc-sa/2.0/
.. _All I Really Need To Know I Learned In Kindergarten: http://www.robertfulghum.com/books.php#book1
.. _Don't take things that aren't yours: http://www.peace.ca/kindergarten.htm
.. _blocking direct linking: http://www.google.com/search?q=blocking+direct+linking
.. _blocking hotlinking: http://www.google.com/search?q=blocking+hotlinking
.. _altlab.com article: http://altlab.com/htaccess_tutorial.html
.. _Apache URL Rewriting Guide: http://httpd.apache.org/docs/1.3/misc/rewriteguide.html

.. |image0| image:: http://data.agilitynerd.com/images/nodirectlink.g
