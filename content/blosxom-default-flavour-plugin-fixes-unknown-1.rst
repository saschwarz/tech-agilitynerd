Blosxom - Default Flavour Plugin - Fixes Unknown Flavour Error
##############################################################
:date: 2007-12-29 23:16
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: blosxom-default-flavour-plugin-fixes-unknown-1

I previously `blogged a solution`_ for the Unknown Flavour error that
involved modifying the blosxom.cgi script itself. I recently found my
modification caused requests for the RSS 0.91 feed and atom feeds to
return the default flavour instead of the desired feed. I suspect any
plugin using a flavour that inserted itself into the Blosxom template
hash table without corresponding flavour file(s) probably didn't work
correctly after my modification.

While investigating a fix for that bug I noticed that a better solution
would be to override the `Blosxom`_ template subroutine. So I created
the defaultflavour plugin. This plugin fixes the bug by first applying
any registered flavour templates if the requested template files are not
found. If that registered flavour templates don't exist the plugin
finally applies the default flavour template files.

Download version 0.1 of the defaultflavour plugin `here`_.

No configuration of the plugin is required. Just copy it into the plugin
directory.

.. _blogged a solution: /blosxom-removing-the-unknown-flavour-error-1.html
.. _Blosxom: http://blosxom.sourceforge.net/
.. _here: http://data.agilitynerd.com/downloads/defaultflavour_0.1.tar
