Modifications to Blosxom moreenties PluginLinks to a Configurable Number of Index Pages
#######################################################################################
:date: 2004-10-21 19:00
:author: Steve Schwarz
:category: webdev
:slug: modifications-to-blosxom-moreenties-pluginlin-1

Jason Clark created the `moreentries`_ plugin for `Blosxom`_ to allow
adding links to the previous and next group of articles/entries in the
head or foot of a Blosxom weblog. He solved a problem that most weblogs
have; it can be difficult for visitors to browse older articles.
Although he calls the solution a hack, he nicely solved an important
problem.

I had been using the morentries plugin but found the text links didn't
make it obvious to some visitors that there were more pages of entries.
So I added images to the links to make them stand out. But I decided it
might be more intuitive to use the same model used by search sites;
create a graphical and textual link for each page of articles along with
previous and next links.

So I decided to modify Jason's plugin to provide this feature. If you
take a look at the bottom of my `AgilityNerd`_ home page page with more
than $blosxom::num_entries entries and scroll to the bottom) you'll see
grey dots, arrows, and page numbers each linking to a page of articles.

You can download the modified plugin `here`_. The prolog of the file
describes the configuration options. I've included the public domain
icons I use on my site in the zip file for your experimentation. Since
there are a few configuration options I've put some examples below so
you can see how the new parameters control the html stored in
$moreentries::pagelinks.

With these settings::

    $numpagelinks = 10;$textlinks = 1;                # set to 1 to enable text links 0 to disable
    $imagelinks = 0;        # set to 1 to enable image links 0 to disable

A screenshot of the HTML generated when the fifth page is selected:

.. raw:: html

   <div class="thumbnail">

|image0|

.. raw:: html

   </div>

 

With these settings::

    $numpagelinks = 10;
    $textlinks = 0;                # set to 1 to enable text links 0 to disable
    $imagelinks = 1;        # set to 1 to enable image links 0 to disable
    $prevlinkimage = "/images/left.gif";
    $nextlinkimage = "/images/right.gif";
    $currentpageimage = "/images/ball.red.gif";@pageimages = qw( /images/ball.gray.gif );

.. raw:: html

   </div>

A screenshot of the HTML generated when the fifth page is selected:

.. raw:: html

   <div class="thumbnail">

|image1|

.. raw:: html

   </div>

 

With these settings::

    $numpagelinks = 10;
    $textlinks = 1;                # set to 1 to enable text links 0 to disable
    $imagelinks = 1;        # set to 1 to enable image links 0 to disable
    $prevlinkimage = "/images/left.gif";
    $nextlinkimage = "/images/right.gif";
    $currentpageimage = "/images/text.gif";@pageimages = qw( /images/ball.gray.gif /images/ball.red.gif );

A screenshot of the HTML generated when the fifth page is selected:

.. raw:: html

   <div class="thumbnail">

|image2|

.. raw:: html

   </div>

Thanks again to Jason for creating this plugin. It was fun to modify and
I hope it is useful for other Blosxom webloggers.

.. _moreentries: http://jclark.org/weblog/WebDev/Blosxom/plugins/moreentries
.. _Blosxom: http://blosxom.sourceforge.net/
.. _AgilityNerd: http://agilitynerd.com/blog/
.. _here: http://data.agilitynerd.com/downloads/moreentries.zip

.. |image0| image:: https://data.agilitynerd.com/images/moreentries_pagelink_1.jpg
.. |image1| image:: https://data.agilitynerd.com//images/moreentries_pagelink_6.jpg
.. |image2| image:: https://data.agilitynerd.com//images/moreentries_pagelink_4.jpg
