#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://tech.agilitynerd.com'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss'

DISQUS_SITENAME = "techagilitynerd"
GOOGLE_ANALYTICS = "UA-1127677-3"

