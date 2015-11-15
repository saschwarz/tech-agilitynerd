Django Migrating Models from an Abstract Base Class to a Concrete Base Class
############################################################################
:date: 2015-11-15 05:00
:author: Steve Schwarz
:category: webdev
:tags: python, agilitycourses, django, database, migration
:slug: django-migrate-abstract-concrete-base-class


On my `agilitycourses.com <http://agilitycourses.com>`_ I had been modeling three types of dog agility courses using an abstract base class ``Course`` with three child classes: ``Box``, ``StarBox``, and ``DoubleBox``. This created three tables in the database prepended with the `Django <http://djangoproject.com>`_ application name ``box``: ``box_box``, ``box_starbox``, and ``box_doublebox``. I needed to add a relationship to all three classes from a new table and, rather than creating three separate tables relating to each child table, I decided to convert the ``Course`` class to a concrete class/table and relate the new class/table to it instead of each child class. For my purposes the extra join to the child class won't impact performance significantly (if it does I'd move the identity of the type of subclass into a column in the parent ``Course`` table and delete the child tables/models).

I didn't find any examples of this type of migration online so I thought I write down my notes in case they are useful to others.

This ends up being a schema migration to put columns in place for inserting data into the parent table, a data migration to populate that table and the new many-to-many table(s), and then another schema migration to remove the temporary columns.

After playing around with a few approaches I found it was easiest to put temporary join ids on the parent class that I could use during the migration and then remove them when I was done. I added these fields to the parent in the ``models.py``:

.. code:: python

    subclass = models.IntegerField(default=-1)
    subclassid = models.IntegerField(default=-1)

and removed the ``abstract = True`` Meta class attribute from ``Course``.

I struggled for a while when I found I couldn't control the ``OneToOneField`` Django automatically creates from the child classes to the parent. I then saw this `StackOverflow answer on a table inheritance question <http://stackoverflow.com/a/32997081/457935>`_ which gave the null/blank field attribute that you'll see I use below.


Backup Your Database
====================

It took me a few attempts to get this right so backups are wise...

First Schema Migration
======================

Now that the models are prepared I created the first database migration adding a default of ``-1`` for the foreign key from the existing child tables to their new concrete parent (which I'll remove manually):

.. code:: bash

    $ python ./manage.py makemigrations box --settings=dev_settings
    You are trying to add a non-nullable field 'course_ptr' to box without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    You are trying to add a non-nullable field 'course_ptr' to doublebox without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    You are trying to add a non-nullable field 'course_ptr' to starbox without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    Migrations for 'box':
      0004_auto_20151114_1255.py:
        - Create model Course
        - Remove field created from box
        - Remove field generator from box
        - Remove field id from box
        - Remove field sequence from box
        - Remove field short_url from box
        - Remove field skills from box
        - Remove field created from doublebox
        - Remove field generator from doublebox
        - Remove field id from doublebox
        - Remove field sequence from doublebox
        - Remove field short_url from doublebox
        - Remove field skills from doublebox
        - Remove field created from starbox
        - Remove field generator from starbox
        - Remove field id from starbox
        - Remove field sequence from starbox
        - Remove field short_url from starbox
        - Remove field skills from starbox
        - Add field course_id to box
        - Add field course_ptr to box
        - Add field course_id to doublebox
        - Add field course_ptr to doublebox
        - Add field course_id to starbox
        - Add field course_ptr to starbox

This automatic migration drops the columns in the subclass tables and with them all the existing data (including keys used in foreign key tables) is lost. But at least I can modify the migration to do what I need for the first migration. The steps will be:

1. Keep the ``CreateModel`` of the parent class, ``Course``, table.

2. Manually edit the ``AddField`` of the ``OneToOneField`` from the child classes to the parent from this:

.. code:: python

        migrations.AddField(
            model_name='box',
            name='course_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=-1, serialize=False, to='box.Course'),
            preserve_default=False,
        ),

to remove the default and add null/blank parameters (which allows leaving subclass data in place during the data migrations):

.. code:: python

        migrations.AddField(
            model_name='box',
            name='course_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, null=True, blank=True, serialize=False, to='box.Course'),
            preserve_default=False,
        ),

If you want to see/validate/test the SQL that will be run you can use the ``sqlmigrate`` management command (just give it your app name and the number of the migration):

.. code:: bash

    $ python ./manage.py sqlmigrate box 0004
    BEGIN;
    CREATE TABLE "box_course" ("id" serial NOT NULL PRIMARY KEY, "sequence" varchar(64) NOT NULL, "short_url" varchar(64) NOT NULL, "created" timestamp with time zone NOT NULL, "generator" varchar(2) NOT NULL, "subclass" integer NOT NULL, "subclassid" integer NOT NULL);
    CREATE TABLE "box_course_skills" ("id" serial NOT NULL PRIMARY KEY, "course_id" integer NOT NULL, "skill_id" integer NOT NULL, UNIQUE ("course_id", "skill_id"));
    ALTER TABLE "box_box" ADD COLUMN "course_ptr_id" integer NULL UNIQUE;
    ALTER TABLE "box_box" ALTER COLUMN "course_ptr_id" DROP DEFAULT;
    ALTER TABLE "box_doublebox" ADD COLUMN "course_ptr_id" integer NULL UNIQUE;
    ALTER TABLE "box_doublebox" ALTER COLUMN "course_ptr_id" DROP DEFAULT;
    ALTER TABLE "box_starbox" ADD COLUMN "course_ptr_id" integer NULL UNIQUE;
    ALTER TABLE "box_starbox" ALTER COLUMN "course_ptr_id" DROP DEFAULT;
    ALTER TABLE "box_course_skills" ADD CONSTRAINT "box_course_skills_course_id_4bbae33e06b494d4_fk_box_course_id" FOREIGN KEY ("course_id") REFERENCES "box_course" ("id") DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE "box_course_skills" ADD CONSTRAINT "box_course_skills_skill_id_35b3dcfd6d387281_fk_box_skill_id" FOREIGN KEY ("skill_id") REFERENCES "box_skill" ("id") DEFERRABLE INITIALLY DEFERRED;
    CREATE INDEX "box_course_skills_ea134da7" ON "box_course_skills" ("course_id");
    CREATE INDEX "box_course_skills_d38d4c39" ON "box_course_skills" ("skill_id");
    ALTER TABLE "box_box" ADD CONSTRAINT "box_box_course_ptr_id_9f73cfe60a5d542_fk_box_course_id" FOREIGN KEY ("course_ptr_id") REFERENCES "box_course" ("id") DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE "box_doublebox" ADD CONSTRAINT "box_doublebox_course_ptr_id_6b112382d489a445_fk_box_course_id" FOREIGN KEY ("course_ptr_id") REFERENCES "box_course" ("id") DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE "box_starbox" ADD CONSTRAINT "box_starbox_course_ptr_id_25fd8909f85eb93a_fk_box_course_id" FOREIGN KEY ("course_ptr_id") REFERENCES "box_course" ("id") DEFERRABLE INITIALLY DEFERRED;

    COMMIT;

If you are happy then save and run the migration:

.. code:: bash

    $ python ./manage.py python migrate box


Data Migration
==============

I decided to use SQL (via `RunSQL <https://docs.djangoproject.com/en/1.8/ref/migration-operations/#runsql>`_ ) for the data migration since it was easier/faster than instantiating each Django model instance as part of the migration. I didn't write reverse migrations since I won't be needing them.

Here's my approach:

1. Copy subclass rows into parent ``course`` table with the ``subclass`` column set to a unique value for the subclass (just used a number for each subclass: 1, 2 & 3) and ``subclassid`` set to each the child table's ``id`` (primary key) value. Together they are a composite key that will be used to tie the parent records back to the child records and their many-to-many relationships.

2. Update the subclass ``course_ptr`` foreign key column with the primary key id of the ``course`` table rows having the subclass's id and subclass number value.

3. Insert subclass's many-to-many table data into the corresponding many-to-many parent table.

Create an empty migration:

.. code:: bash

   $ python manage.py makemigrations --empty box

Then add the migration queries to it (repeat the following for each of the subclasses giving each a different number):

.. code:: python

    operations = [
        # insert data from subclass into parent class with subclass 'number' and primary key/id
        migrations.RunSQL("""INSERT INTO box_course (sequence, short_url, created, generator, subclass, subclassid)
                          SELECT sequence, short_url, created, generator, 1, id
                          FROM box_box;"""

        ),
        # update subclass primary key to point to parent class (notice composite key values):
        migrations.RunSQL("UPDATE box_box box SET course_ptr_id=course.id FROM box_course course WHERE course.subclassid=box.id AND course.subclass=1;"
        ),
        # insert child's many-to-many foreign key references into it's parent's many-to-many table
        migrations.RunSQL("""INSERT INTO box_course_skills (course_id, skill_id)
                          SELECT box.course_ptr_id, skills.id
                          FROM box_box box JOIN box_box_skills skills
                          ON box.id = skills.box_id"""
        ),
    ]


Final Schema Migration
======================

Then it is time to edit the ``models.py`` file and remove the temporary members/fields in the parent class: ``subclass`` and ``subclassid``. Then create the schema migration which will drop those columns and the migrated columns from the child tables:

.. code:: bash

  $ python manage.py makemigrations box
    You are trying to add a non-nullable field 'course_ptr' to doublebox without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    You are trying to add a non-nullable field 'course_ptr' to starbox without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    You are trying to change the nullable field 'course_ptr' on box to non-nullable without a default; we can't do that (the database needs something to populate existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows)
     2) Ignore for now, and let me handle existing rows with NULL myself (e.g. adding a RunPython or RunSQL operation in the new migration file before the AlterField operation)
     3) Quit, and let me add a default in models.py
    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
    >>> -1
    Migrations for 'box':
      0006_auto_20151114_1708.py:
        - Remove field created from box
        - Remove field generator from box
        - Remove field id from box
        - Remove field sequence from box
        - Remove field short_url from box
        - Remove field skills from box
        - Remove field subclass from course
        - Remove field subclassid from course
        - Remove field created from doublebox
        - Remove field generator from doublebox
        - Remove field id from doublebox
        - Remove field sequence from doublebox
        - Remove field short_url from doublebox
        - Remove field skills from doublebox
        - Remove field created from starbox
        - Remove field generator from starbox
        - Remove field id from starbox
        - Remove field sequence from starbox
        - Remove field short_url from starbox
        - Remove field skills from starbox
        - Alter field course_ptr to doublebox
        - Alter field course_ptr to starbox
        - Alter field course_ptr on box

You see management command detects that the child fields still haven't been deleted and that the default value for inserts of the children's parent reference still doesn't exist. Running this final migration completes the migration:

.. code:: bash

  $ python ./manage.py migrate box

Wrap Up
=======

I hope this helps if you need this type of migration. It may look a little complicated at first, but all it amounts to is:

Step 1. Remove abstract inheritance and add temporary fields to the parent class for identifying each subclass's records in the parent table when migrating the data.

Step 2. Migrate the child data to the parent class with the subclass composite keys. Use new parent primary keys to migrate tables with foreign key that have moved to the parent class.

Step 3. Drop columns used in migration on the parent and child tables.

Let me know if you've found other/better solutions!
