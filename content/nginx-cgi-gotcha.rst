============================
 NGINX CGI Parameter Gotcha
============================
:date: 2016-07-31 12:02
:author: Steve Schwarz
:category: devops
:tags: nginx, cgi, fcgiwrap, ubuntu, apache
:slug:

When I first started the `agilitynerd <http://agilitynerd.com>`_  blog in 2004 I had my `Blosxom <http://blosxom.sourceforge.net/>`_ blogging CGI script running via `Apache <http://httpd.apache.org/>`_. Later on I moved all my sites to `nginx <https://nginx.org/en/>`_ or took advantage of nginx's caching features to have it act as a proxy in front of Apache. I finally decided to remove Apache entirely and that meant solving running CGI scripts using nginx.

After some googling I found FastCGI and `fcgiwrap  <https://www.nginx.com/resources/wiki/start/topics/examples/fcgiwrap/>`_

I'm on Ubuntu so installation was as easy as::

  sudo apt-get install fcgiwrap

That setup the init script that starts the fcgi daemon. To run the cgi script(s) nginx has to be configured to parse apart the incoming URL, execute the appropriate script and pass along any arguments needed by the CGI script. Sounds easy.

I only want to support running a single CGI script: ``index.cgi`` and pass along the path after the root of URL as the argument to the script. Most examples are more generic and parse out any cgi script and any arguments.

The key built-in to nginx to do the splitting is ``fastcgi_split_path_info`` which takes a regex with two captured groups to parse out the script name and the arguments. These are stored in the ``$fastcgi_script_name`` and the ``$fastcgi_path_info`` variables respectively. This `Digital Ocean article <https://www.digitalocean.com/community/tutorials/understanding-and-implementing-fastcgi-proxying-in-nginx>`_ discusses FastCGI and has an excellent discussion of the variables available and also used by ``fcgiwrap``.

So I created this configuration file that matches ``http://agilitynerd.com/blog/foo.html`` and invokes ``/home/agilitynerd/cgi-bin/index.cgi foo.html``::

    location /blog/ {
        root /home/agilitynerd/cgi-bin/;

        fastcgi_split_path_info ^(/blog)(.*)$;
        include /etc/nginx/fastcgi_params;
        fastcgi_param DOCUMENT_ROOT /home/agilitynerd/cgi-bin/;
        fastcgi_param SCRIPT_NAME index.cgi$fastcgi_path_info;

        # Fastcgi socket
        fastcgi_pass  unix:/var/run/fcgiwrap.socket;
    }

You'll notice: ``include /etc/nginx/fastcgi_params`` is used to get default values for the ``fastcgi_param`` variables.

And it didn't work. I kept getting errors::

  Cannot get script name, are DOCUMENT_ROOT and SCRIPT_NAME (or SCRIPT_FILENAME) set and is the script executable?"

Clearly I'm setting ``DOCUMENT_ROOT`` and ``SCRIPT_NAME``. After almost a day of googling and testing (during which I found this helpful article on `nginx debugging <https://blog.martinfjordvald.com/2013/06/debugging-nginx-errors/>`_) I temporarily commented out ``fastcgi_pass``, and returned the variables.

I found that they were being set as I expected... Strange!

Then I came across this `Digital Ocean article <https://www.digitalocean.com/community/tutorials/understanding-and-implementing-fastcgi-proxying-in-nginx>`_ where they have a critical discussion on overriding variables in which they state:

  This inconsistency and unpredictability means that you cannot and should not rely on the backend to correctly interpret your intentions when setting the same parameter more than one time. The only safe solution is to only declare each parameter once. This also means that there is no such thing as safely overriding a default value with the fastcgi_param directive.

So in my case I commented out ``DOCUMENT_ROOT`` and ``SCRIPT_FILENAME`` in the ``/etc/nginx/fastcgi_params`` file, reloaded nginx, and voila! Everything worked. Hope this helps you if you run in to the same problem.
