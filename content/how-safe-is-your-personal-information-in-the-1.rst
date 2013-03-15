How Safe is Your Personal Information in the Hands of Website Developers?
#########################################################################
:date: 2005-06-23 19:00
:author: Steve Schwarz
:category: webdev
:tags: development, privacy
:slug: how-safe-is-your-personal-information-in-the-1

I was going through the webserver statistics for this site to see if any
new sites had linked to any of my articles (it is always nice to see
that what I have to say is useful to someone). Anyway, I ran across
someone who had come to my site through a Google query (I won't mention
what the query was for reasons you'll soon see). I ran the same query on
Google to see what else came up since it was a rather unique query.
Another Google link was for a site that looked like it had raw data -
not your usual HTML pages.

When I went to the site I found what looked like a website developer's
development directory wide open to the internet. There were at least
three company's websites sitting in subdirectories. The file referred to
in the Google result page was a backup of an SQL database dump file. Not
just any database file - a backup of all the customer information for
running one site's shopping cart database. It included names, addresses,
email addresses, and phone numbers! (I didn't poke around to see if it
had any more sensitive data).

I was able to figure out the original data owner's domain name from some
info in the header of the file. So I just sent them an email letting
them know that their customer information is posted for all to see on
someone else's website. It will be interesting to see if they respond. I
hope it is just their website developer who has a test server running
and accidentally left this SQL dump in a publicly accessible area of
their webserver. I'd hate to think this data was stolen from the real
website and being used for spamming purposes.

As a software developer I've read numerous cautionary tales of
accidental (and malicious) data theft occurring when real customer data
is used in test systems. I just never imagined I'd stumble across such
an egregious privacy violation. So this experience makes me wonder about
all the online systems into which we type our personal information. All
it takes is one careless developer (not even a malicious one) to expose
our private information to a much wider audience...
