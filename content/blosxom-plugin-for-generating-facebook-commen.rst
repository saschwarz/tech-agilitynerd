Blosxom Plugin for Generating Facebook Comment xids
###################################################
:date: 2010-11-23 05:00
:author: Steve Schwarz
:category: webdev
:tags: blosxom, comments, facebook, perl
:slug: blosxom-plugin-for-generating-facebook-commen

I've been using `Blosxom`_ to power my dog agility blog for over 6
years. In the past year or so I've enabled `Facebook comments`_ in
addition to my site's own comment plugin. I ran into a problem using
Facebook's comments: if the user enters a comment on a page and the URL
has any additional URL parameters then the comment is only associated
with the page when accessed with those parameters, others hitting the
page w/o parameters won't see the comments.

This behavior is `documented by Facebook`_ when the ``xid`` attribute
isn't set in ``fb:comments`` HTML element. I didn't think I'd encounter this
situation since my blog post URLs don't contain any parameters. However,
when people link to one of my articles within Facebook, Facebook appends
various parameters to the base URL.

The solution is to specify an ``xid`` attribute in the ``fb:comments`` element
containing the URL encoded URL of the page (Facebook's default ``xid``).
This causes existing comments to show up and causes comments created
when the page is loaded with URL parameters to use the same encoded URL.

So I created a simple Blosxom plugin to perform the encoding so the
encoded URL can be placed in the story.html template:

.. code:: perl

  # Blosxom Plugin: urlencode -*- perl -*-
  # Author: Steve Schwarz <http://agilitynerd.com/>
  # 2010-NOV-22    0.1 initial version.package urlencode;
  # puts the urlencoded string of the URL for this page
  # into $urlencode::url without any params# use this in fb.comments xid to give the same xid
  # even when query params are provided
  # -------------------
  use CGI qw/:standard/;
  use URI::Escape;

  sub start {
      return 1;
  }
  $url = '';

  sub story {
      my ($pkg, $path, $filename, $story_ref, $title_ref, $body_ref) = @_;
      $urlencode::url = uri_escape("$blosxom::url/${blosxom::path_info}");
      return 1;
  }
  1;

Then it is used in the story template::

  <fb:comments width="550" numposts="5" xid="$urlencode::url"></fb:comments>

Now my readers won't have to worry that their comments won't show up.

.. _Blosxom: http://www.blosxom.com/
.. _Facebook comments: http://developers.facebook.com/docs/reference/plugins/comments
.. _documented by Facebook: http://developers.facebook.com/docs/reference/fbml/comments_%28XFBML%29
