Blosxom - Removing the Unknown Flavour Error
############################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: blosxom-removing-the-unknown-flavour-error-1

After my `recent Referer Spam attacks`_ I've been checking my logs and
`AWStats`_ reports daily. I noticed that occasionally I'd get people
requesting pages with incorrect suffixes. i.e. foo.ht or bar.\|id\|
(some of these are probably spammers too). A "feature" of `Blosxom`_ is
that it will still serve the page with the default layout or flavour.
This feature causes a not too helpful and ugly error message to be
displayed on the top of the page::

  Error: I'm afraid this is the first I've heard of an "ht" flavoured
  Blosxom. Try dropping the "/+ht" bit from the end of the URL.

Of course removing the suffix from the URL doesn't usually work; the
client is served with an empty (but flavoured) page. So I though a
better solution would be to have Blosxom serve my default\_flavour
whenever the flavour couldn't be identified. A little Googling later
turned up `this Blosxom mod by James Vasille`_. James explicitly loads a
flavour file named "default" whenever the requested flavour can't be
found.

For my site it is more appropriate to serve the $default\_flavour when
the requested flavour can't be found. That way I didn't have copy/create
head.default, foot.default, etc files. So my code change is almost the
same as James'::

  $template =   sub {
    my ($path, $chunk, $flavour) = @_;
    do {
      return join '', <$fh> if $fh->open("< $datadir/$path/$chunk.$flavour");
    } while ($path =~ s/(/*[^/]*)$// and $1);
    # Begin added code    
    do {
      return join '', <$fh> if $fh->open("< $datadir/$path/$chunk.$default_flavour");
    } while ($path =~ s/(/*[^/]*)$// and $1);
    # End added code
    return join '', ($template{$flavour}{$chunk} || $template{error}{$chunk} || '');
  };

So now a less ugly page will be provided when an unknown suffix/flavour
is requested.

Update 19-Apr-2005 - this algorithm has a bug that has been fixed by the `defaultflavour plugin`_.
--------------------------------------------------------------------------------------------------

.. _recent Referer Spam attacks: /blosxom-plugin-to-block-referer-spam-1.html
.. _AWStats: http://awstats.sourceforge.net
.. _Blosxom: http://blosxom.sourceforge.net/
.. _this Blosxom mod by James Vasille: http://brutalhugs.com/flavours/#mod_default_template
.. _defaultflavour plugin: http://data.agilitynerd.com/downloads/defaultflavour_0.1.tar
