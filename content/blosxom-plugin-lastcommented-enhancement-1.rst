Blosxom Plugin lastcommented Enhancement
########################################
:date: 2008-02-29 18:50
:author: Steve Schwarz
:category: webdev
:tags: blosxom, plugin
:slug: blosxom-plugin-lastcommented-enhancement-1

I had a comment entered on my `dog agility blog <http://agilitynerd.com/blog>`_ that I
subsequently deleted and of course my ``lastcommented`` plugin recorded
the comment as the most recent comment. Since the plugin uses
``Storable`` to store the data I couldn't manually edit the file to
remove the entry.

So I modified my ``lastcommented`` plugin to allow you to specify the,
base zero, index of the entry on the URL and delete the entry. For
example to delete the second entry in the list (index 1):

    ``http://example.com/blog/?lastcommentremove=1``

To keep mischief makers from deleting all your comments the plugin has a
variable in its configuration section called ``lastcommentremove`` that
you set to a non zero value to enable this feature. Since this is
probably a relatively infrequent activity (if you have blacklisting or
wbcaptcha comment spam protection enabled) I figured this was a
sufficient mechanism.

You can `download the latest version of this plugin here`_.

.. raw:: html

   </p>

.. _download the latest version of this plugin here: http://data.agilitynerd.com/downloads/lastcommented
