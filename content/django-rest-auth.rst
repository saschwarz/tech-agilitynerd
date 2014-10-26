Django REST Registration with django-rest-auth and django-allauth
==================================================================
:date: 2014-10-26 03:02
:author: Steve Schwarz
:category: webdev
:tags: python, REST, API, agilitycourses, django, django-rest-framework, django-allauth, django-rest-auth, mobile
:slug: django-rest-registration-with-django-rest-auth

I'm creating a mobile app for my `agilitycourses website <http://agilitycourses.com>`_ and I'm using `django-rest-api <http://www.django-rest-framework.org/>`_ to provide a REST API for use by the client application. In order to provide authentication and registration I'm using `django-allauth <http://django-allauth.readthedocs.org/en/latest/>`_. Lastly I use `django-rest-auth <https://github.com/Tivix/django-rest-auth/>`_ to provide REST resources for authentication and registration.

I implemented and tested ``django-rest-framework`` and then added in ``django-allauth``. But when I went to integrate ``django-rest-auth`` POSTing to the ``/rest-auth/registration/`` resource was generating a traceback::

    Exception Type: TypeError at /rest-auth/registration/
    Exception Value: add_message() argument must be an HttpRequest object, not 'Request';.

It turns out ``django-allauth``'s ``allauth.account.adapter.DefaultAccountAdapter`` uses Django's messaging middleware to give feedback to users when HTML templates are used. When ``rest-auth`` invokes the view it is is passing in a ``Request``. I took a look at the ``rest-auth`` demo application and saw that it's ``settings.py`` file had ``django.contrib.messages`` disabled. Which keeps this traceback from happening.

Disabling messaging is a reasonable thing to do if the service is only handling REST data. For now I'd like to use the same service for both HTML and REST traffic. So I needed a way to disable messaging in ``django-allauth``.

I found ``django-allauth`` allows configuring/replacing the account adapter so I subclassed ``DefaultAccountAdapter`` and stubbed out the ``add_message`` method. I put it in my "glue" application (called ``main``) in a file called ``adapters.py``::

    class MessageFreeAdapter(DefaultAccountAdapter):
        """
        django-allauth's `allauth.account.adapter.DefaultAccountAdapter` uses Django's messaging middleware to give feedback to users. When using django-rest-auth for registration/login JSON-REST requests a traceback is generated when the `HTTPRequest` is passed into `django.contrib.messages.add_messages` when a `Request` is expected:

        Exception Type: TypeError at /rest-auth/registration/
        Exception Value: add_message() argument must be an HttpRequest object, not &#39;Request&#39;.

        If messaging cannot be disabled (it is used by other applications) using this subclass
        disables messaging for allauth/django-rest-auth.

        In settings.py add ACCOUNT_ADAPTER = 'main.adapters.MessageFreeAdapter'
        """
        def add_message(self, request, level, message_template,
                        message_context={}, extra_tags=''):
            pass

Then I set the ``ACCOUNT_ADAPTER`` variable in ``settings.py`` to use this new adapter::

    ACCOUNT_ADAPTER = 'main.adapters.MessageFreeAdapter'

So now I can continue to use Django messaging and use ``django-allauth`` in the same Django project.
