Obtain Short URLs and QR-Codes for Django Apps
##############################################
:date: 2010-10-22 04:00
:author: Steve Schwarz
:category: webdev
:tags: django, googl, python, qrcode
:slug: obtain-short-urls-and-their-qr-codes-for-djan

Lately I've been interested in improving the interaction of my
`agilitycourses <http://agilitycourses.com>`_ website for mobile users. One such improvement is to add
`QR Codes`_ (aka 2D barcodes) representing the page URLs to the printed
representations of pages served as PDFs.

I found that developers have reverse engineered the "api" of the
`goo.gl`_ URL shortening web site. In my brief testing it is very fast.
What makes that service extra useful is by adding ".qr" to a shortened
URL it returns a PNG image of the QR Code for the shortened URL. That
made it perfect for providing both short text and QR Code URL
representations for my printed documents.

I threw together a few functions and put them in a module to make it
easy to shorten a long URL, obtain the QR Code PNG and store it using
`Django's Storage functionality`_:

.. code:: python

  import osimport urllib
  from django.utils import simplejson

  def googl_shorten_url(long_url):
      """
      Returns goo.gl shortened url for the provided long_url.
      Code taken from: http://djangosnippets.org/snippets/2220/
      Parameters:
      - `long_url`: the url to supply to goo.gl to be shortened.
      """
      params = urllib.urlencode({'security_token': None, 'url': long_url})
      f = urllib.urlopen('http://goo.gl/api/shorten', params)
      return simplejson.loads(f.read())['short_url']

  def googl_qrcode(googl_url):
      """
      Return file containing qr code image file for the given goo.gl url.
      Parameters:
      - `googl_url`: url from which to obtain the qr code.
      """
      return urllib.urlopen(googl_url + '.qr')

  def get_url_qr_code_image(long_url, storage, storage_image_file_path=''):
      """
      Return goo.gl shortened url and storage name of qr code corresponding to
      the shortened url for the supplied full url. Contacts goo.gl to shorten
      the supplied long url then downloads and stores the qr code image file
      in the storage instance using the file path and the shortened url name
      as the storage name.
      Parameters:
      - `long_url`: the url to shorten.
      - `storage': a Django storage instance into which to store the qr code
      image.
      - `storage_image_file_path`: file system path to prepend to shortened
      url. This path must exist prior to calling this function.
      """
      try:
          googl_url = googl_shorten_url(long_url)
          qr_file_name = googl_url.split('/')[-1] + '.qr'
          qr_code_name = os.path.join(storage_image_file_path, qr_file_name)
          if not storage.exists(qr_code_name):
              qr_buffer = storage.open(qr_code_name, 'wb')
              qr_buffer.write(googl_qrcode(googl_url).read())
              qr_buffer.close()
      except:
          googl_url = None
          qr_code_name = None
      return googl_url, qr_code_name

Yes, it has a nasty bare try/except. For my uses this is optional
functionality so I never want a failure to stop the main functionality
of the views that use it. Add exception handling appropriate for your
needs.

The main entry point is ``get_url_qr_code_image()``. Here is an example
of its use (assuming you save the code in googl.py):

.. code:: python

  >>> import googl
  >>> from django.core.files.storage import default_storage
  >>> short_url, qr_code_storage_name = googl.get_url_qr_code_image('http://google.com', default_storage)>>> short_urlu'http://goo.gl/mR2d'
  >>> qr_code_storage_nameu'mR2d.qr'
  >>> default_storage.path(qr_code_storage_name)u'/home/dev/agilitycourses/static/mR2d.qr'
  >>> default_storage.url(qr_code_storage_name)u'mR2d.qr'
  >>>

Hope you find this useful.

.. _QR Codes: http://en.wikipedia.org/wiki/QR_Code
.. _goo.gl: http://goo.gl
.. _Django's Storage functionality: http://docs.djangoproject.com/en/dev/topics/files/
