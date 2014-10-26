#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Steve Schwarz'
SITENAME = u'tech.agilitynerd'
SITESUBTITLE = u'scratching that itch'
SITEURL = 'http://tech.agilitynerd.com'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('agilitynerd.com', 'http://agilitynerd.com/blog/'),
          ('agilitycourses.com', 'http://agilitycourses.com/'),
          ('googility.com', 'http://googility.com/'),
          )

# Social widget
SOCIAL = (('Linked in', 'http://www.linkedin.com/profile/view?id=10135443'),
          ('GitHub', 'https://github.com/saschwarz'),
          )


DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

THEME = './themes/pelican-bootstrap-responsive-theme'

SUMMARY_MAX_LENGTH = 50

AUTHOR_ABOUT = """<p class="about">I'm Steve Schwarz a Chicago software developer and dog agility enthusiast. <a href="/pages/about.html">more</a></p>"""

COPYRIGHT_DATE = "2014"

#TEMPLATE_PAGES = {"/Users/saschwarz/dev/tech-agilitynerd/content/about.html": "/Users/saschwarz/dev/tech-agilitynerd/output/about.html",                  }

FEED_DOMAIN = SITEURL
#FEED_ALL_RSS = 'feeds/all.rss' # input to feedburner
FEED_ALL_ATOM = 'TechAgilityNerd' # output from feedburner
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
#TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'

# GOOGLE_SEARCH = '001042720131993941673:rqdekl8sewe'
GOOGLE_SEARCH = '001042720131993941673:szhtogqckem'
