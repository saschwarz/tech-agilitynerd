#!/usr/bin/env python

AUTHOR = "Steve Schwarz"
SITENAME = "tech.agilitynerd"
SITESUBTITLE = "scratching that itch"
SITEURL = "http://127.0.0.1:8000"

PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("agilitycoursemaster.com", "https://agilitycoursemaster.com"),
    ("agilitynerd.com", "https://agilitynerd.com/blog/"),
    ("agilitycourses.com", "https://agilitycourses.com/"),
    ("googility.com", "https://googility.com/"),
)

# Social widget
SOCIAL = (
    ("Linked in", "https://www.linkedin.com/profile/view?id=10135443"),
    ("GitHub", "https://github.com/saschwarz"),
    ("Twitter", "https://twitter.com/steveaschwarz"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = "./themes/pelican-bootstrap-responsive-theme"

SUMMARY_MAX_LENGTH = 50

DEFAULT_DATE_FORMAT = "%d %b %Y"

AUTHOR_ABOUT = """<p class="about">I'm Steve Schwarz a Chicago software developer and dog agility enthusiast.
 <a href="/pages/about.html">more</a></p>"""

COPYRIGHT_DATE = "2020"

FEED_DOMAIN = SITEURL
# FEED_ALL_RSS = 'feeds/all.rss' # input to feedburner
FEED_ALL_ATOM = "TechAgilityNerd"  # output from feedburner

GOOGLE_SEARCH = "001042720131993941673:szhtogqckem"

PLUGIN_PATHS = ["/Users/saschwarz/dev/pelican-plugins"]
PLUGINS = ["tag_cloud"]
