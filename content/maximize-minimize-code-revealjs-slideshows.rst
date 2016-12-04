==========================================================
Maximize and Minimize Code Blocks in Reveal.js Slide Shows
==========================================================
:date: 2016-12-04 12:00
:author: Steve Schwarz
:category: webdev
:tags: webdev, CSS, JavaScript


I was working on a slideshow about `Using Gestures in Angular 2 Components <https://saschwarz.github.io/angular2-gestures-slides/#/>`_
for a lightning talk at the December `Northwest Chicago JavaScript <https://www.meetup.com/Northwest-Chicago-JavaScript/>`_ meetup and
I found the code sections just weren't large enough. So I threw together a little JavaScript to add "+" and "-"
buttons next to each code section that maximizes/restores the code blocks for easier viewing during the presentation:

.. class:: thumbnail
.. figure:: {filename}/images/max-min-screenshot.png
    :alt: Screenshot of slide showing plus sign to right of code section

Just copy/paste the following into your ``index.html`` file:

.. raw:: html

    <script src="https://gist.github.com/saschwarz/ee02786cd1a64c33611fafd70c0df900.js"></script>

