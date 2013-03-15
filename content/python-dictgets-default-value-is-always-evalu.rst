Python dict.get's Default Value is Always Evaluated
###################################################
:date: 2011-04-05 17:16
:author: Steve Schwarz
:category: programming
:tags: python
:slug: python-dictgets-default-value-is-always-evalu

This is a gotcha I ran across in some production code that is obvious in
retrospect. I was profiling the code to find places where we were
calling ``an_expensive_database_function`` and came across code like
this:

.. code:: python

  def doit(*args, **kwargs):
       value = kwargs.get('key', an_expensive_database_function())

The original author probably assumed that if 'key' was present in the
``kwargs`` dictionary ``an_expensive_database_function`` wouldn't be called;
that it would be short circuited in the same manner as Boolean
expressions. But since get is a function the arguments are always
evaluated on the way into the function. So in this case even if the
value of ``an_expensive_database_function`` was already present in the
``kwargs`` dictionary the database function would be called again.

Here is a "look before you leap" solution:

.. code:: python

    def doit(*args, **kwargs):
        value = kwargs.get('key')
        if value is None:
             # assuming default value None isn't a valid value
             value = an_expensive_database_function()``

Here is the "easier to ask forgiveness than permission" solution:

.. code:: python

    def doit(*args, **kwargs):
        try:
            value = kwargs['key']
        except KeyError:
            value = an_expensive_database_function()``
