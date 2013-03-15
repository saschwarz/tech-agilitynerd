Create Posterous Posts from Google Forms
########################################
:date: 2012-05-12 23:57
:author: Steve Schwarz
:category: webdev
:tags: email, google, posterous
:slug: create-posterous-posts-from-google-forms

I've been organizing dog agility bloggers for \ `Dog Agility Blog Action
Days`_ and wanted to automate updating our group's blog when each
blogger posted their article on the event/action days. For past events I
had the bloggers email me with the information and manually created each
entry in the blog.

Since `posterous`_ supports posting via email I knew I could create a
form on one of my web servers and have the page format the data so
posterous could turn it into a post. Here are the details for formatting
emails for posterous: `how to get the most out of posting by email`_.

Instead I stumbled upon an article on using Google Forms to send emails
via the Google infrastructure: \ `Get Form Data from Google Docs in an
Email Message [Video Tutorial]`_.

So all I had to do was create a form for my bloggers to fill out and
then have the script run by their submission format and send an email to
posterous to post.

Here's my modified version of the form script:

.. code:: javascript

  function sendFormByEmail(e) {
    // create a draft post - posterous will send you an email
    // when the draft is created.  var email = "draft@YOURBLOGNAMEHERE.posterous.com";
    // e.namedValues is a dictionary where the keys
    // are the names of your form's questions. So you can pick
    // them out and combine them as you wish.
    //
    // My form contained five questions:
    // 1. 'Title of your blog as you want it to appear'
    // 2. 'The URL of your blog as you type it in your browser'
    // 3. 'Title of your article' 
    // 4. 'The URL of your article copied from your browser' 
    // 5. 'Short description/teaser about your article'
    var v = e.namedValues; 
    var subject = v['Title of your article'].toString(); 
    subject += "((tag: attitude))"; // add tags as you wish
    var message = '<a href="' + v['The URL of your blog as you type it in your browser'].toString() + '">'; 
    message += v['Title of your blog as you want it to appear'].toString(); 
    message += '</a > wrote:'; 
    message += "nn"; 
    message += v['Short description/teaser about your article'].toString(); 
    message += '< a href="' + v['The URL of your article copied from your browser'].toString(); 
    message += '"> Read the full article < /a >nn'; 
    message += "n#end"; // so your email signature won't cause a problem  
    // This is the MailApp service of Google Apps Script 
    // that sends the email. You can also use GmailApp here. 
    MailApp.sendEmail(email, subject, message); 
    // Watch the following video for details   // http://youtu.be/z6klwUxRwQI
    // By Amit Agarwal - www.labnol.org 
  }

In the script you can see how I've accessed the form fields by the full
name and woven them into an email with links embedded - just have to
watch the use of double quotes within single quotes. Which produces blog
entries similar `to this one I created manually`_.

So now I can just send the link to the Google form to participants and
they'll create drafts that I can tweak and/or just submit. It took
longer to write this post than it took to modify and test the script!

.. _Dog Agility Blog Action Days: http://dog-agility-blog-events.posterous.com/
.. _posterous: http://posterous.com
.. _how to get the most out of posting by email: http://howdoi.posterous.com/how-to-get-the-most-out-of-posting-by-email
.. _Get Form Data from Google Docs in an Email Message [Video Tutorial]: http://www.labnol.org/internet/google-docs-email-form/20884/
.. _to this one I created manually: http://dogagilityblogevents.wordpress.com/if-i-knew-then-proactive-handling
