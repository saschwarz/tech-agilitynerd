Comment Spam and wbcaptcha Plugin Enhancements
##############################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:slug: comment-spam-and-wbcaptcha-plugin-enhancement-1

I have been fighting automated comment spam robots (see also
`refererblock update`_, and `hit counter changes`_) with my modified
writeback plugin that uses a blacklist of spam words and URLs. However,
I'm getting tired of updating the blacklist and removing spam comments
that get through the filter. So I decided to install the `wbcaptcha
plugin`_ written by `Pasi Savolainen`_. His plugin uses the `FIGlet`_
program to generate an ASCII "image" of random letters:

.. raw:: html

   <div class="centered"><pre>
                _            
    ___  _ __  | |__    __ _ 
   / _ \| '_ \ | '_ \  / _` |
  |  __/| | | || | | || (_| |
   \___||_| |_||_| |_| \__,_|
   </pre></div>

A person leaving a comment then enters the letters (enha for the image
above) as a "key" along with their comments. The plugin then validates
that the key matches the generated image before it allows the comment to
be posted. This is similar to the approach used by other blog software
to distinguish humans from automated spam programs.

Pasi's plugin worked by executing figlet in a subshell whenever someone
wanted to post a comment. I wanted to change this approach since I don't
have the ability to install figlet on my web host and I didn't want to
pay the performance cost of calling a program through the shell.

So I found the `Text::FIGlet`_ Perl package on `CPAN`_ and made a few
small edits to Pasi's plugin to allow it to invoke the FIGlet Perl code
without the shell. This simplified the plugin and sped up it's
performance. I've sent my changes to Pasi in case he wants to
incorporate them in a future release of his plugin.

I've decided to leave my blacklist in place, since I'm sure I'll still
be facing human comment spammers looking to promote their websites. The
last change I can think to make to further discourage spammers will be
to change all <a> elements in comments to include the `rel="nofollow"`_
attribute supported by most portal/search websites.

I also took this opportunity to add some name anchors to my foot.htm and
foot.html files so clicking on the "Comments" link on my index pages now
takes you directly to the comments section of the individual article.
Similarly, selecting "Add Your Comment" and Posting a comment also show
the writeback for and the last added comment respectively. This makes
for less scrolling on long articles and multiple comments.

Unfortunately, I don't think this will actually reduce the spammer hits
on my site since these are due to automated "bots". I doubt the spammers
actually check if their comments get posted, they are just hoping for a
comment to "get through" occaisionally so their sites can can get some
`"Google Juice"`_. So they'll keep pounding on my site although
hopefully fewer spam comments will get through.

Please email me at the address shown in the right hand menu bar if you
have any problems posting comments.

.. _refererblock update: http://agilitynerd.posterous.com/refererblock-version-02-1
.. _hit counter changes: http://agilitynerd.posterous.com/blosxom-hit-counter-and-favorites-plugins-1
.. _wbcaptcha plugin: http://varg.dyndns.org/psi/pub/code/misc/wbcaptcha.html
.. _Pasi Savolainen: http://varg.dyndns.org/psi/pub/index.html
.. _FIGlet: http://www.figlet.org
.. _`Text::FIGlet`: http://search.cpan.org/~jpierce/Text-FIGlet-1.06/FIGlet.pm
.. _CPAN: http://cpan.org/
.. _rel="nofollow": http://googleblog.blogspot.com/2005/01/preventing-comment-spam.html
.. _"Google Juice": http://search.cpan.org/~jpierce/Text-FIGlet-1.06/FIGlet.pm
