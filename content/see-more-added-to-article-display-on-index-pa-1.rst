See More... Added to Article Display on Index Pages
###################################################
:date: 2004-09-26 19:00
:author: Steve Schwarz
:category: webdev
:slug: see-more-added-to-article-display-on-index-pa-1

I know my Agility readers will give me a hard time about this
non-Agility post, but hey I'm "thinking about technology" too. I was
limiting to five the number of articles/posts on my main and index pages
to minimize the download time for non cable/DSL visitors. But I've
noticed some searches hit my site for which an article was moved off my
main page and I'm sure they didn't hunt around for the missing post. So
I wanted to show more articles without increasing the download time.

The `Blosxom`_ plugin `seemore`_ automatically adds a link labeled "See
More..." in place of a special label in each article. Selecting the link
takes you to the full text of the article. This useful plugin was
developed by `Todd Larason`_, a blogger who's developed a number of
powerful Blosxom plugins.

I made a minor modification to seemore, which I've forwarded to Todd, to
allow showing the entire article for a configurable number of articles
on a page. This lets you see the full text and diagrams for the latest
articles and only seeing the first couple paragraphs of the older
articles.

If you are a Blosxom blogger and would like my modifications you can
download my modified version `here`_. Unzip it and put it in your plugin
directory. By default it should work the same as Todd's original
version. A new configuration variable $show_all_of_stories_until can
be set to the number of stories on each index page that you'd like to
show in full.

So I've modified most of my posts to include the seemore label and
increased the number of articles shown on each index page to
$blosxom::num_entries. I like this new site configuration; let me know
if you do too.

.. _Blosxom: http://blosxom.sourceforge.net/
.. _seemore: http://www.blosxom.com/plugins/display/seemore.htm
.. _Todd Larason: http://molelog.molehill.org/blox/Computers/Internet/Web/Blosxom/SeeMore/
.. _here: http://data.agilitynerd.com/downloads/seemore.zip
