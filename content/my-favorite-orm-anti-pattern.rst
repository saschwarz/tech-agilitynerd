My Favorite ORM and Python Anti-Patterns
########################################

:date: 2012-05-12 23:57
:author: Steve Schwarz
:category: python
:tags: antipattern, development, orm, python
:slug: my-favorite-orm-anti-pattern

At work I was looking at improving the performance of one of our slower
web pages. It can be rewarding to find a little piece of code that can
be easily optimized. This time there were several functions that were
adding 10+ sec to the page in worst case. It wasn't a problem for most
clients, but when clients with who are related to many other clients hit
the page they'd experience terrible performance. Here's pseudo code for
the combination of anti-patterns that caused the problem::

  # Projects have users and users are in different organizations 
  # (project can contain multiple organization's users)
  activeOrganizationProjectUsers = [x for x in project.users 
          if x.active and x.organization == organization]
  if activeOrganizationProjectUsers:
      # do something *NOT* using activeOrganizationProjectUsers

There are two main problems with this code:

#. It ignores the fact the project, users, and organization are backed
   by an ORM
#. The list comprehension is being used to find all matching elements
   when only a single element is needed.

Ignoring the ORM
@@@@@@@@@@@@@@@@

The code above wouldn't be too bad if these were just lists of objects
in memory. But being objects that are instantiated by an ORM a number of
database queries will be issued. In this particular case (w/o eager
loading across user to the organization table) the following queries
where executed:

#. Join project to user and get all users for the project's id
#. For each user load their organization (one by one) if the user is
   active

So in the case where there were hundreds of users on a project there
were hundreds of queries executed and hundreds of User and Organization
instances were instantiated. Depending on the size of the objects (and
the ORM's behavior) it can take "real time" to fetch and instantiate all
these large objects.

This code base has this kind of code sprinkled through out it. At one
time during it's development the developers were encouraged to treat ORM
backed objects as though they were Plain Old Python Objects (POPOs). The
developer wouldn't necessarily see the performance degradation using
small data sets either. This is one of the reasons why I like to tail
the database log (or use `django-debug-toolbar`_ if I''m using Django)
to see the queries go by.

Using List Comprehensions When a Single Value is Needed
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

To make this situation worse, the activeOrganizationProjectUsers list
wasn't actually used. This is a combination of a Python anti-pattern and
the ORM anti-pattern. What was required was to determine if a single
active organization user existed.

I believe the original developer(s) used the list comprehension solution
in a combination of ignorance and syntactic sugar. They didn't want to
write a new function to do the query and put it in the User class so
they used the existing class's API. The syntactic sugar was using the
list comprehension to get more values than the one that was needed. If
this wasn't a (potentially) expensive ORM backed operation the original
code could have been::

  activeOrganizationProjectUsers = False
  for x in project.users:
      if x.active and x.organization == organization:
          activeOrganizationProjectUsers = True
          break
  if activeOrganizationProjectUsers:
      # do something

But this solution could still query all possible user/organization
combinations. The other question would be: which set is larger the
organization users or the project users? It is likely looping over the
organization's users looking for active ones would be more efficient
anyway.

Remember the Underlying Representation
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

When performance matters remembering the objects are ORM backed is
important. So in this case a single query was all that was required
(SqlObject pseudo syntax)::

  activeOrganizationProjectUsers = Users.selectBy(project=project,
                                                  active=True,
                                                  organization=organization).count() > 0

If abstracting out the ORM's methods is important this new function
could be added to the appropriate class as a method. In my case making a
change to use a query resulted in cutting the page load time by two
orders of magnitude.

.. _django-debug-toolbar: http://github.com/robhudson/django-debug-toolbar
