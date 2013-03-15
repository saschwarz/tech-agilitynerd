Configuring Runit for Gunicorn and Django Installed in a Virtualenv on Ubuntu
#############################################################################
:date: 2010-09-08 03:08
:author: Steve Schwarz
:category: python
:tags: apache, django, gunicorn, runit, ubuntu, virtualenv
:slug: configuring-runit-for-gunicorn-and-django-ins

I couldn't find any documentation that covered all the pieces for
configuring my latest Django site so I hope this helps someone else out.

I had used mod\_wsgi under Apache for my other Django sites. But now I'm
using different python versions for the sites (until if/when I update
the older sites) and I wasn't getting the correct versions of some
python libraries (even though virtualenv apeared to be putting the
appropriate python packages at the start of the sys.path). So I decided
to configure Apache to ProxyPass to `Gunicorn`_\ so I could run my
Django app in its virtualenv without it getting any other python
modules.

Installing Gunicorn
@@@@@@@@@@@@@@@@@@@

I installed Gunicorn into the virtualenv for my application, which
simplifies using gunicorn from the command line. Assuming
``/home/user/virtualenvs/myapp`` is the location of the virtualenv:

.. code::

  $ source /home/user/virtualenvs/myapp/bin/activate
  $ pip install gunicorn
  
  # or
  $ easy_install gunicorn

This copies gunicorn\_django to the /home/user/virtualenvs/myapp/bin
directory. Test gunicorn with your app, assuming your Django app is
located at /home/user/source/myapp, as follows:

.. code::

  $ source /home/user/virtualenvs/myapp/bin/activate
  (myapp)$ cd /home/user/source/myapp
  (myapp)$ gunicorn_django

Gunicorn starts myapp using the ``settings.py`` file in the current
directory on 127.0.0.1:8000. Ctrl-C to stop the process.

Installing Runit on Ubuntu
@@@@@@@@@@@@@@@@@@@@@@@@@@

There are two `runit`_ packages. You want the one that only runs
services you add to it:

.. code::

  $ sudo apt-get install runit
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  Suggested packages:
    runit-run socklog-run
  The following NEW packages will be installed:
    runit0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
  Need to get 0B/113kB of archives.After this operation, 537kB of additional disk space will be used.
  Selecting previously deselected package runit.
  (Reading database ... 209845 files and directories currently installed.)
  Unpacking runit (from .../runit_2.0.0-1ubuntu2_i386.deb) ...
  Processing triggers for man-db ...
  Setting up runit (2.0.0-1ubuntu2) ...
  runsvdir (start) waiting
  runsvdir (start) startingrunsvdir (start) pre-start
  runsvdir (start) spawned, process 9575
  runsvdir (start) post-start, (main) process 9575
  runsvdir (start) running, process 9575

You'll want to create a directory for the application and a run script
in ``/etc/service:``

.. code::

  $ sudo mkdir /etc/service/myapp
  $ sudo vi /etc/service/myapp/run
  # enter the run script I'll show below
  $ sudo chmod +x /etc/service/myapp/run
  # stop runit from trying to run gunicorn until we are ready
  $ sudo sv stop myappok: down: myapp: 0s, normally up

The example run script checked into Gunicorn had some syntax errors
and wasn't quite what I wanted. Here's my version:

.. code::

  #!/bin/sh
  GUNICORN=/home/user/virtualenvs/myapp/bin/gunicorn_django
  ROOT=/home/user/source/myapp
  PID=/var/run/myapp.pid
  
  if [ -f $PID ] 
      then rm $PID 
  fi

  cd $ROOT
  exec $GUNICORN -c $ROOT/gunicorn.conf.py --pid=$PID

You can create a `configuration file for gunicorn`_\ to use or just
create an empty file for now:

.. code::

  $ touch /home/user/source/myapp/gunicorn.conf.py

If you have multiple appserver you'll need to run gunicorn on
different ports, you can put the configuration in the gunicorn.conf.py
file:: 

  bind = "127.0.0.1:8111"

Putting it Together
@@@@@@@@@@@@@@@@@@@

Now you can test that the run script works when run as root::

  $ sudo /etc/service/myapp/run

Gunicorn should start and start the appserver. If it fails you can
debug the script via::

  $ sudo bash -x /etc/service/myapp/run

Tell runit to start and keep gunicorn running::

  $ sudo sv start myapp
  ok: run: myapp: (pid 7540) 0s
  $ sudo sv status myapp
  run: myapp: (pid 7543) 1s

.. _Gunicorn: http://gunicorn.org/
.. _runit: http://smarden.org/runit/index.html
.. _configuration file for gunicorn: http://gunicorn.org/configure.html
