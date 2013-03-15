Embedding JSON Within Generated HTML
####################################
:date: 2010-07-08 21:03
:author: Steve Schwarz
:category: webdev
:tags: html, javascript, json, python, webdevelopment
:slug: embedding-json-within-generated-html

Ran into an interesting problem at work this past week that had a simple
and pleasing resolution. We have an in house developed JavaScript grid
on some of our pages and when users entered some text strings we'd
generate invalid `JSON`_ payloads that would give the user an error
page. If they entered strings that looked like an HTML Entity i.e. &#13
which (with the addition of a trailing ; ) is a non-visible HTML
character (carriage return) the text wasn't displayed in the widget. To
further complicate things some of the content displayed in the grid is
HTML which is inserted into the grid as is and can contain escaped HTML
characters.

The grid gets its content as a JSON payload from within a hidden div in
the HTML which is generated via a template mechanism. Heres a portion of
the template where <%= and %> stringifying of the value of the Python
variable(s)/code they surround::

  <div style="display:none;" id="grid-init-args-<%= count %>">
    <textarea>
    <!-- this is the JSON payload loaded via the grid JavaScript -->
    <%= [ columnsIndex, indexColumns, columns, rowBuffer, footerRows, formulas] %>
    </textarea>
  </div>

This approach has a number of problems:

#. By using the template mechanism to create the JSON payload this
   template was relying on the similarity of the string representation
   of Python objects to JSON. After some testing I found the following
   scenarios: If a string contained a single quote character the string
   representation was a double quoted string around the text and the
   single quote; a valid JSON string. If the string contained a double
   quote character the string representation was a single quoted string
   around the text and the double quote; `an invalid JSON string`_. If
   the string contained both a single and a double quote the string
   representation would be a single quoted string containing a slash
   escaped single quote and the double quote; an invalid JSON string.
   Depending on the browser (of course) the JSON string would fail to
   parse correctly when the double quote was encountered within the
   single quoted string.
#. The JSON payload had to be HTML encoded (converting <, >, ", and &)
   since it was parsed by the browser as HTML.
#. The HTML encoding would encode or double encode HTML to be inserted
   directly into the grid's DOM.

The variation in single/double quoting was an easy fix, I changed to
`simplejson`_.dumps() which correctly double quotes key/values in dicts
and escapes embedded double quotes (single quotes don't need to be
escaped). I didn't time it but with the C extension it may be faster
than the template engine for our larger datasets.

I played around with (not) encoding various portions of the payload and
then it hit me that I should change the grid to get its payload from a
non HTML element so that only HTML destined for insertion into the DOM
would be HTML encoded (which is as you'd expect for normal HTML
handling). I started changing the payload to be stored in JavaScript
generated in the template but didn't like the impact the change would
have on all the existing templates. So I started Googling and found `Ben
Nadel's blog post on using script tags as data containers`_.

So here's my solution::

  <div style="display:none;" id="grid-init-args-<%= count %>">
  <script type="application/json">  
  <%= simplejson.dumps([ columnsIndex, indexColumns, columns, rowBuffer, footerRows, formulas]) %>
  </script>
  </div>

There were two changes:

#. Used ``simplejson.dumps`` to correctly double quote and escape double
   quotes within the variables in the payload.
#. Change the textarea to a script element.

By converting to a script tag within the hidden div the HTML parser no
longer parsed the content of the JSON payload. so the JSON payload only
needed to HTML encode HTML elements that were being inserted into the
DOM created by the grid.

This change also meant I was able to delete the unnecessary HTML
encoding of non-HTML JSON payload data. Got to love solutions that
involve deleting code.

Ultimately, we'll convert to loading the JSON payload as a separate AJAX
request from the page to the server, but for now this simplifies the
markup and handles all types of user input and HTML encoded characters
correctly.

.. _JSON: http://www.json.org/js.html
.. _an invalid JSON string: http://www.bennadel.com/blog/388-People-Please-Stop-Using-Single-Quotes-.htm
.. _simplejson: http://pypi.python.org/pypi/simplejson/
.. _Ben Nadel's blog post on using script tags as data containers: http://www.bennadel.com/blog/1603-jQuery-And-Script-Tags-As-Data-Containers.htm
