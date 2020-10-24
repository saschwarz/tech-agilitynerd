#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://tech.agilitynerd.com"
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all-en.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "techagilitynerd"
GOOGLE_ANALYTICS = "UA-1127677-3"
