Refererblock Version 0.2
########################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin, referrer, spam
:slug: refererblock-version-02-1

I came up with two improvements to the first release of my `refererblock
plugin`_:

-  If the referer string matches the site's URL it passed immediately
   and isn't checked against the blacklist.
-  The blacklist.txt file was being read even if the referer string was
   empty. Now it is only read if the referer string is not empty and it
   isn't for the site's URL.

These optimizations do improve the performance of the plugin. My testing
on a PIII 800MHz running Fedora Core 3 Linux with Apache 2.0 showed the
following average latencies:

-  1.5 ms - Empty referer string or current domain.
-  2.0 ms - Referer string matching the first regex of the example
   blacklist file.
-  3.0 ms - Referer string matching the final regex of the example
   blacklist file.

I was kind of surprised at how little additional time was required to
load the blacklist file and process the regular expressions. This is
probably due to the file remaining in the disk cache for subsequent
requests. Of course your mileage may vary.

Download version 0.2 of the plugin `here`_.

See my `original plugin description`_ for installation, configuration,
and testing information. Please let me know if you use this plugin or if
you have comments or suggestions for improving it.

.. _refererblock plugin: http://agilitynerd.posterous.com/blosxom-plugin-to-block-referer-spam-1
.. _here: http://data.agilitynerd.com/downloads/refererblock_0.2.tar
.. _original plugin description: /blosxom-plugin-to-block-referer-spam-1
