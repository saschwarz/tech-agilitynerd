Backup Your Data Lately?
########################
:date: 2004-08-20 19:00
:author: Steve Schwarz
:category: devops
:tags: sysadmin
:slug: backup-your-data-lately-1

A few weeks ago I bought a `Ximeta NetDisk`_ 120 GB external hard drive
to back up the data on my home computers. There are a number of vendors
making hard drives that support USB connections; this model is unique in
that it also supports direct ethernet connections. Unlike more expensive
Network Attached Storage devices (more than $ 1000) this unit only cost
a little more than the hard drive itself; about $ 150. The only downside
is that it uses it's own proprietary network protocol which requires
installation of a driver on any computers using the drive.

My goal was to put this drive on my network switch and back up data from
my XP, WinME, RedHat 8.0, and Win95 machines. It turns out this was a
little trickier than I expected. So I spent the better part of the
morning on a cool, grey Chicago day making this all work.

The disk comes formatted for NTFS but in order for it to be shared on
the older Windows platforms and my Linux machine it needs to be
reformatted to use a FAT32 file system. Windows XP doesn't support
formatting drives for FAT32 so I had to install the Ximeta driver
software on my WinME machine and install the NetDisk on my network.

Running fdisk and reformatting the hard drive is the only "scary" aspect
of the installation. Choosing the wrong drive or partition would be a
*bad* thing. This `document`_ gives a good step by step description.

I was skeptical that running fdisk over the network would work
correctly, but it did. At this point I was able to view the drive on
both my WinME and XP systems and copy data to the drive as if it was
locally connected.

I was pretty sure making the drive work for Linux would be difficult.
Unfortunately, the PDF documents from the Ximeta website are unreadable
as they require installing the Korean Acrobat extensions... thankfully
Google has its "View has HTML" facility which let me read the RedHat
instructions. The docs on the install CDROM are viewable (but don't
include the RedHat docs).

I'll spare you all the trial and error but after downloading the `driver
RPM`_ from the website and installing it I couldn't configure and
connect to the drive on the network. It could be that ports required for
their protocol aren't opened on my Linux machine, but Ximeta doesn't
give any information on what ports are used by their driver. The admin
tool gives some cryptic error messages that Googling and the docs didn't
explain (the docs recommend reinstalling the drivers for any errors...).
I ended up connecting the drive directly via USB and was able to mount
the drive and backup my user and system accounts to the disk.

So it looks like my goal of leaving the drive on the network and copying
to it from any computer will only work for Windows machines. But at
least I have a mechanism for backing up all my machines, that is easy
enough that I'll use it all the time. My next step is looking into
configuring `rsync`_ or a similar mechanism to only backup the changed
files to the NetDisk.

In summary, I'd recommend this drive for anyone who is using Windows XP;
it is plug and play for that operating system. If you are computer savvy
you can make this hard drive play with other systems too.

However you do it, **backup your computer!**

.. _Ximeta NetDisk: http://www.ximeta.com/products/network_drives/netdisk/index.php
.. _document: http://www.ximeta.com/support/guides/netdisk/ndas/98seme/05.php
.. _driver RPM: http://www.ximeta.com/support/downloads/red_hat_8/index.php
.. _rsync: http://rsync.samba.org
