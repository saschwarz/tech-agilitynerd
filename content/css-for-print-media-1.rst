CSS for Print Media
###################
:date: 2004-08-14 23:16
:author: Steve Schwarz
:category: webdev
:slug: css-for-print-media-1

In keeping with my desire to have this site's layout be easy to read,I
wanted it to look good in print too. The layout uses `CSS`_ instead
of HTML tables. This lets me position the divscontaining various text for
the screen and it allows me to positionand hide text differently for the
printed media.

Any CSS book covers the basics of changing the display,
position, margins, and padding along with the use of separate style
sheets forprint and screen media. But I ran into problems with printing
mysite's pages with the Mozilla/Netscape browsers. Only
the first page of my main div would print. Alittle Googling turned up
this excellent `article`_ on `A ListApart`_. ALA is a great resource for
web developers.

The only clarification I have is that since both the screen and the print
CSS files are included, the print CSS file's elements may needto set
additional properties as well as reseting properties that existin the
screen media file. Otherwise the definitions for the screen will be used.
I had to set some div's position properties to static to get them back
into the document flow.

.. _CSS: http://www.w3.org/Style/CSS/
.. _article: http://www.alistapart.com/articles/goingtoprint/
.. _A ListApart: http://www.alistapart.com
