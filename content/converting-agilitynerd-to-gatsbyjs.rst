Moving the AgilityNerd.com Blog to GatsbyJS
##########################################################
:date: 2019-11-28 8:00
:author: Steve Schwarz
:category: webdev
:tags: talks, javascript, video, sideprojects, gatsbyjs

As a software developer, one of the ways I learn about new web technology is by attending the monthly `Northwest Chicago JavaScript meetup <https://www.meetup.com/Northwest-Chicago-JavaScript/>`_.
It's a supportive and enthusiastic group of folks interested in continuing to learn more about software development in JavaScript.
Every month there are one or more informal presentations by members of the group with questions and discussions.

This past week I gave a talk titled: "Moving the AgilityNerd Blog to GatsbyJS".
I started my dog agility blog `AgilityNerd <https://agilitynerd.com>`_ in 2004 using the now defunct, Perl-based, flat file CGI site generator, `blosxom <http://blosxom.sourceforge.net/>`_.
Over the years I wrote, enhanced, and fixed a number of plugins to the Blosxom project.
Though it worked well, technology has long since moved passed Blosxom's humble beginnings.

The costly hosting requirements for Blosxom at the AgilityNerd's site size (with over 800 source pages generating 1,500 pages dynamically), authoring in HTML, lack of preview, and enhancing a nearly 20 year old code base became so onerous that I decided to extract the content and move to a more modern static site generator.

This site, tech.agilitynerd.com, uses the Python powered `Pelican static generator <https://blog.getpelican.com/>`_ and deploys to GitHub pages.
It is simple to author, deploy, and free to host.
But I was looking for a static site generator that would make it easy to integrate custom web components, provide image processing, dynamic image/content loading, and integrate 3rd party plugins like: `Google Analytics <https://analytics.google.com/>`_, `Rollbar <https://rollbar.com/>`_ error tracking, and advanced search (`Algolia <https://www.algolia.com/>`_).

My search boiled down to React-based `GatsbyJS <https://www.gatsbyjs.org/>`_ and Vue-based `Gridsome <https://gridsome.org/>`_.
I've been using Vue daily at work for almost two years, but Gridssome isn't as far along in its development as Gatsby.
It has been a while since I did any serious React development so I decided to go with the more popular GatsbyJS as a reason to get my skills on React more up to date.

Gatsby's offering an easy "GitOps" continuous deployment model hosted (for free) on `Netlify <https://www.netlify.com/>`_ was just icing on the cake.

Here's `a link to my slides <https://nwcjs-gatsby.netlify.com/>`_.
Interestingly, the slides are written using `MDX Deck <https://mdx-deck.jxnblk.com/>`_ which is itself built on top of Gatsby.
Of course I used that functionality to deploy the slide deck to Netlify too.

Here's the video of my presentation which goes into a lot more detail on my reasoning for choosing Gatsby, setting it up, how it works, how plugins work, and deploying a Gatsby site:

.. raw:: html

    <div class="embed-video">
    <iframe src="https://www.youtube.com/embed/bL_QNj_AdWE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

Since this presentation, I've started using Gatsby Cloud's build service to get faster builds and then have it upload the assets to Netlify for hosting.