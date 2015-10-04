Notes on Configuring Postfix on Ubuntu Gutsy to Send Email via Google Apps
##########################################################################
:date: 2008-01-05 23:53
:author: Steve Schwarz
:category: devops
:tags: postfix, slicehost, ubuntu
:slug: notes-on-configuring-postfix-on-ubuntu-gutsy-1

Here are some notes I took on configuring my `Slicehost`_ Ubuntu Gutsy
installation to use Postfix to send emails via Google Apps. I am far
from an expert on postfix configuration but maybe these notes will be
helpful to others needing this configuration.

These sites contain the key information:

-  `Behind My Screen - Configuring[Ubuntu] Postfix and Gmail in 10+1
   Easy Steps`_
-  `The Prancing Tarantula - Getting Postfix to work on Ubuntu with
   Gmail`_
-  `Mike Chirico - Gmail on Home Linux Box using Postfix and Fetchmail`_

I basically followed the Behind My Screen tutorial (read the comments
too) with the updates from The Prancing Tarantula and the following
changes.

My Ubuntu server install didn't have the Thawte certificates installed
by default so I installed them::

    sudo aptitude install ca-certificates

Then you can append that file to your /etc/postfix/cacert.pem If you
"sudo su" before doing the append to the file you won't get messed up by
the shell::

    $ sudo su
    # cat /etc/ssl/certs/Thawte_Premium_Server_CA.pem >>
    /etc/postfix/cacert.pem

Since I have Google Apps setup for my domain I don't just want to relay
email as "user@gmail.com\ ", I want the email to be sent as though it
came from my domain ("me@agilitynerd.com\ "). This requires some simple
changes to the config files.

In my transport file I have::

    agilitynerd.com smtp:[smtp.gmail.com]:587

In my generic file I have::

    demo@myservername.agilitynerd.com me@agilitynerd.com

Where "demo" is the login name and "myservername" is my slicename. In my
sasl_passwd file I have::

    [smtp.gmail.com]:587 me@agilitynerd.com:me_gmail_account_password

After restarting postix you can test sending email from your server::

    $ sudo aptitude install mailx
    $ mailx -s "test email" someotheraccount@gmail.com <
    ~/sometestfile_to_send

Check your logfiles for errors/warnings::

    sudo tail /var/log/mail.\*

I hope these notes might help folks "get over the hump" if they are
setting up the same configuration.

.. _Slicehost: http://www.slicehost.com/
.. _Behind My Screen - Configuring[Ubuntu] Postfix and Gmail in 10+1 Easy Steps: http://behindmyscreen.newsvine.com/_news/2006/12/31/501615-configuringubuntu-postfix-and-gmail-in-101-easy-steps
.. _The Prancing Tarantula - Getting Postfix to work on Ubuntu with Gmail: http://prantran.blogspot.com/2007/01/getting-postfix-to-work-on-ubuntu-with.html
.. _Mike Chirico - Gmail on Home Linux Box using Postfix and Fetchmail: http://souptonuts.sourceforge.net/postfix_tutorial.html
