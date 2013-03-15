Multiple YouTube Videos per page using VideoLightBox
####################################################
:date: 2010-06-04 22:58
:author: Steve Schwarz
:category: webdev
:tags: css, html, javascript, jquery, video, visuallightbox, webdevelopment, youtube
:slug: multiple-youtube-videos-per-page-using-videol

I decided to stop displaying the default `YouTube`_ video players within
posts on my `AgilityNerd blog`_ and I started looking for a light boxed
player. Their were two main reasons. The smallest video playback window
provided by YouTube for HD videos is too wide for my two column layout
and now that I'm posting more videos the load time of the page is
delayed by the communication with all the off site webservers; serving
the YouTube static image of the video will be much faster/lighter
weight.

I looked around and really liked the lightbox containing the default
YouTube player provided by `VideoLightBox`_ and started playing around
with their demo. VideoLightBox (VLB) has an interesting approach. You
download an application (PC or Mac), configure how you want your
video(s) to look and it generates a directory of files on your local
disk (or uploads files to your website via FTP) along with an index.html
file from which you copy the code to put in the <head> and <body> of
your web page. For YouTube it also downloads a static image for each
selected video which is used as the image link within the HTML page.
Straight forward and works well.

For my purposes there was a problem with their approach, its locates the
image used to launch the light box using an element id. This assumes a
single video or gallery of videos per web page. On my blog's main page
or the category pages there will be multiple videos (possibly multiple
videos within a single post). I figured a little bit of CSS and JQuery
hacking would solve the problem and it did.

I decided to modify their HTML/CSS/JS to use a CSS class instead of an
element id to allow for multiple videos per page. At first I just
modified the generated files. Then I saw that VLB has template files in
their installation. So I started modifying the templates to output the
new code. Two hours later I bailed. Using `procmon`_ it looks like the
client app reads the template files but then doesn't actually use the
files to generate the output files(?). I was only able to modify one of
the three template files that needed to change and have it effect the
generated files.

I'm going to provide my edits to the VLB developers in case they are
interested.

So the solution is to edit one of the template files and then edit two
of the generated files; not ideal but once you put the generated files
on your webserver you'll probably not touch them unless you are changing
CSS styles. The modifications aren't hard but you need to be careful and
typos will definitely break things. You should backup the VLB directory
before your start or be prepared to uninstall and reinstall from their
installation program.

#. Navigate to the VideoLightBox directory (i.e. C:Program Files
   (x86)VideoLightBox)
#. Change the permissions on the templates subdirectory to give your
   user full access to overwrite the files
#. For each directory in the templates subdirectory open the
   videolightbox.js file in an programming editor (a keyboard macro
   makes this trivial):

   #. Globally replace $("#videogallery a[rel]") with
      $(".videogallery a[rel]").each(function(idx){$(this)
   #. Go to the end of the line and add });
   #. Save the file

Then generate the output files using the VLB executable for one or more
videos, saving the results to your local file system

#. Navigate to the output directory
#. Open the index.html file in an programming editor

   #. Globally replace #videogallery with .videogallery
   #. Globally replace id="videogallery" with class="videogallery"
   #. Save the file

#. In the engine/css subdirectory open the videolightbox.css file in an
   programming editor

   #. Globally replace #videogallery with .videogallery
   #. Save the file

Then you can copy the files just as specified by the VLB installation
instructions.

The other change I'll be making for my deployment is to rename the video
images. They are named 0.png, 1.png, etc. I'm going to put them all in a
directory on my resource webserver so I'll rename the files and their
references in the code copied from the index.html to use the YouTube
video id.

I'll be changing my existing web posts over to this new scheme over
time...

.. _YouTube: http://youtube.com
.. _AgilityNerd blog: http://agilitynerd.com/
.. _VideoLightBox: http://videolightbox.com
.. _procmon: http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx
