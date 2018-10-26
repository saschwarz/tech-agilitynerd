# -*- coding: utf-8 -*- #

AUTHOR = u'Steve Schwarz'
SITENAME = u'tech.agilitynerd'
SITESUBTITLE = u'scratching that itch'
SITEURL = 'http://127.0.0.1:8000'  # 'http://127.0.0.1:5500'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (('agilitynerd.com', 'https://agilitynerd.com/blog/'),
         ('agilitycourses.com', 'https://agilitycourses.com/'),
         ('googility.com', 'https://googility.com/'),
         )

# Social widget
SOCIAL = (('Linked in', 'https://www.linkedin.com/profile/view?id=10135443'),
          ('GitHub', 'https://github.com/saschwarz'),
          ('Twitter', 'https://twitter.com/steveaschwarz'),
          )

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

THEME = './themes/pelican-bootstrap-responsive-theme'

SUMMARY_MAX_LENGTH = 50

AUTHOR_ABOUT = """<p class="about">I'm Steve Schwarz a Chicago software developer and dog agility enthusiast.
 <a href="/pages/about.html">more</a></p>"""

COPYRIGHT_DATE = "2017"

# TEMPLATE_PAGES = {"/Users/saschwarz/dev/tech-agilitynerd/content/about.html":
#                   "/Users/saschwarz/dev/tech-agilitynerd/output/about.html", }

FEED_DOMAIN = SITEURL
# FEED_ALL_RSS = 'feeds/all.rss' # input to feedburner
FEED_ALL_ATOM = 'TechAgilityNerd'  # output from feedburner
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
#TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'

# GOOGLE_SEARCH = '001042720131993941673:rqdekl8sewe'
GOOGLE_SEARCH = '001042720131993941673:szhtogqckem'

PLUGIN_PATHS = ['/Users/saschwarz/dev/pelican-plugins']
PLUGINS = ['tag_cloud']
