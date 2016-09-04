=======================================
NGINX, HTTPS, Let's Encrypt, and Django
=======================================
:date: 2016-09-04 12:02
:author: Steve Schwarz
:category: devops
:tags: nginx, ubuntu, https, ssl, django, gunicorn, letsencrypt
:slug:

My `agilitycourses.com <https://agilitycourses.com>`_ website is served by `nginx <https://nginx.org/en/>`_ proxying to `gunicorn <http://gunicorn.org/>`_ running my `Django <https://www.djangoproject.com/>`_ application. I'll be adding user accounts soon so I wanted to convert the site to be more secure by using HTTPS encryption. Also `Google has announced it will likely prefer sites using HTTPS <https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html>`_.

The site is running on Ubuntu 14.04 LTS. I won't recount the whole process, I followed some great resources and made a couple adjustments that might be helpful to others.

#. I basically followed the instructions in this excellent Digital Ocean tutorial: `How To Secure Nginx with Let's Encrypt on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-14-04>`_.

#. I confirmed via the `SSL Labs SSL Server Test <https://www.ssllabs.com/ssltest/analyze.html>`_ that my IPv4 and IPv6 server configurations had "A+" ratings.

#. While looking for other SSL testing sites I came across `securityheaders.io <https://securityheaders.io/>`_ developed by `Scott Helme <https://scotthelme.co.uk/>`_. My initial score was a sad "D". The site has snippets for NGINX and Apache configuration changes and in depth articles describing the how and the why.

#. While investigating the changes to the HTTP Headers to improve my test score I came across this `nginx-conf GitHub repository <https://github.com/jonnybarnes/nginx-conf>`_. Specifically the idea of putting the header settings into an `NGINX include file <https://github.com/jonnybarnes/nginx-conf/blob/master/conf/includes/security-headers.conf>`_. I have several other domains on the same server and will also be converting them. I used that idea to include ssl and header configurations into any virtual host.

Here's my `/etc/nginx/ssl.conf` file::

      # From https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-14-04
      ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
      ssl_prefer_server_ciphers on;
      ssl_dhparam /etc/ssl/certs/dhparam.pem;
      ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
      ssl_session_timeout 1d;
      ssl_session_cache shared:SSL:50m;
      ssl_stapling on;
      ssl_stapling_verify on;


And my `/etc/nginx/security_headers.conf` file::

      # See https://github.com/jonnybarnes/nginx-conf/blob/master/conf/includes/security-headers.conf
      add_header X-Xss-Protection "1; mode=block";
      add_header X-Content-Type-Options "nosniff";
      add_header Content-Security-Policy "default-src https: data: 'unsafe-inline' 'unsafe-eval'";
      add_header Strict-Transport-Security max-age=15768000;


So my server blocks with all these edits are now::

    # redirect http://tld to https://www.tld
    server {
        listen 80;
        listen [::]:80;
        server_name agilitycourses.com;
        return 301 https://www.agilitycourses.com$request_uri;
    }
    # redirect http://www.tld to https://www.tld
    server {
        listen 80;
        listen [::]:80;
        server_name www.agilitycourses.com;
        return 301 https://www.agilitycourses.com$request_uri;
    }

    server {
        listen 443 ssl;
        listen [::]:443 ipv6only=on ssl;

        server_name www.agilitycourses.com;
        root /home/agilitycourses/production/current/;

        ssl_certificate /etc/letsencrypt/live/agilitycourses.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/agilitycourses.com/privkey.pem;

        include /etc/nginx/ssl.conf;
        include /etc/nginx/security_headers.conf;

        # letsencrypt location
        location ^~ /.well-known/ {
            allow all;
            root /usr/share/nginx/html/;
        }
        ...
    }

So now I have an "A" score from `securityheaders.io`

5. The Digital Ocean tutorial sets up a root crontab entry to automatically update the SSL Certificate. I decided to also update the letsencrypt client software automatically::

     # m h  dom mon dow   command
     20 2 * * 1 cd /opt/letsencrypt && git pull
     30 2 * * 1 /opt/letsencrypt/letsencrypt-auto renew >> /var/log/le-renew.log
     35 2 * * 1 /etc/init.d/nginx reload


#. The last change I made was to pass along the presence/absence of HTTPS from NGINX to Gunicorn/Django via the `X-Forwarded-Proto` header as `described in the Django SSL/HTTPS docs <https://docs.djangoproject.com/en/1.10/topics/security/#ssl-https>`_ ::

    location @proxy-to-app {
        proxy_pass http://agilitycourses-production-gunicorn;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Accept-Encoding "";
        proxy_read_timeout 120;
        proxy_send_timeout 120;
        ...
    }

#. Based on the Django recommendations I also made these changes in my `settings.py`::

     # SSL settings
     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
     SECURE_BROWSER_XSS_FILTER = True
     SESSION_COOKIE_SECURE = True
     CSRF_COOKIE_SECURE = True

Even with a lot of web browsing to learn about these settings the whole process only took a couple hours.
Now that I've done it once (and updated my Fabric fabfile.py) it will be easier to convert my other domains.
