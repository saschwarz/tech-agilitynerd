Blog Spammers Using URL Encoding
################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: spam
:slug: blog-spammers-using-url-encoding-1

I was getting hit by comment spammers in the last week who were using
`URL-encoding`_ of their addresses to get around the comment
blacklisting filter I use. By replacing regular characters with the
multi-character encoded representation of those characters within the
URL the spammers were able to post comment spam with links to casino and
porn websites to my blog.

This type of spam is a reversal of the same method for hiding your own
email address in a web page so it won't be harvested by email spammers
(see for example `Chip Rosenthal's Blog entry`_).

I just added a regular expressions in my blacklist file to block the use
of URL encoded characters in all links. If your blog comment software
supports this approach you might want to do the same thing.

.. _URL-encoding: http://www.w3schools.com/tags/ref_urlencode.asp
.. _Chip Rosenthal's Blog entry: http://www.unicom.com/chrome/a/000388.html
