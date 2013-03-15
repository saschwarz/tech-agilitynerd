Centering DIVs in CSS
#####################
:date: 2004-08-15 00:00:00
:author: Steve Schwarz
:category: webdev
:slug: centering-divs-in-css-1
:tags: css, webdevelopment

I took a look at this site on an 800x600 resolution monitor and didn't
like how the original layout looked. Having the menu box on the left hand
side with a ``20px`` margin to the left used up too much screen space. So I
decided to move the menu box to the right of the main body of the page.

I could have hard-coded the box position; but decided that I wanted
to have the main body remain centered regardless of browser size.
That would complicate the positioning of the menu box (which is it's
own div not contained with the main page). Once again `A List Apart`_ had
a good `article`_\ describing how they got their CSS centering to work.

The ALA article had links to these two pages describing the methods
I used: `Auto Width Margins`_\ and `NegativeMargins`_.

The AgilityNerd site has two main divs: #page for the main body
and#sidebar for the box containing the menu. I used the Auto Width
Margins method to center the main body::

    #page { font-size: 13px; background: white; border: 1px solid black;
    top: 0px; width: 640px; margin: 0px auto; margin-bottom: 50px;
    text-align: left;}

The two lines of interest are ``margin: 0px auto;` and ``text-align: left;``.
Thelater is required because I used the IE 5.x workaround of
specifying ``text-align: center;`` in the body element.

So now that the main body of the site was centered, I wanted the menu to
be floating off to the right of the main body. The Negative
Margins method let me horizontally center the divand also offset it
horizontally by any amount. I offset it by half the(fixed) width of the
main body plus a little space. The additionalspace keeps IE 5.x
browser's miscalculation of sizes from causing theborders to not meet
correctly::

    #sidebar { background: white; font-size: 12px; position: fixed;
    width: 140px; height: auto; top: 70px; left: 50%; margin-left:
    330px; text-align: center; border: 1px solid black; }

Unlike the article, I used ``position: fixed`` instead of absolute. This
allows the menubox to float in place during scrolling (but only for CSS
compliant browsers like: Mozilla/Netscape).

.. _A List Apart: http://www.alistapart.com
.. _article: http://www.alistapart.com/articles/journey/
.. _Auto Width Margins: http://bluerobot.com/web/css/center1.html
.. _NegativeMargins: http://bluerobot.com/web/css/center2.html
