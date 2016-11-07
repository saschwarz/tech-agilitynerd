=============================
 Architecting for the Future
=============================
:date: 2015-11-04 03:02
:author: Steve Schwarz
:category: webdev
:tags: python, webpack, flask, reactjs, angularjs
:slug:
:status: draft

At `work`_ I've been developing a migration path from our traditional server side rendering (via Python, Jinja2, SQLAlchemy) to a more flexible platform communicating internally and externally via APIs (REST and durable message queues).


This that will let us serve a wider range of client devices, continue updating server technologies, share data between server


While there are front end developers who extole the virtues of client side rendering to create rich web "applications" the motivation here is actually driven by a desire to decouple the server side into cooperative services communicating via well defined APIs. This well proven approach supports scaling and sharing data/combining services into more powerful products. Another benefit of communicating through APIs is to support native mobile apps. Hybrid mobile apps are also popular


hybrid model mixing server side rendering with client side JavaScript rendering communicating with REST APIs. In our case (a large B2B SaaS application) we'll be using existing Python templated pages to render some data and, as we roll out more JSON REST end points, we'll progressively add client side rendering for components accessing those endpoints.

Another aspect of our front end development process is moving from custom JS and jQuery UI components to third party components using popular AngularJS framework and ReactJS/Flux libraries. Most examples/discussions of Angular/React assume client-side rendering and routing to create a Single Page Application (SPA). SPAs put multiple "pages"/views in a single web application that routes between those pages without server page refreshes. SPAs may load all presentation templates at server load or incrementally as routes are changed on the client.

While SPAs are likely in our future, initially we are creating JS components (and components of components) to replace server side generated tables/widgets. In our first step all URL changes will invoke a server page request to generate HTML with appropriate JS/CSS bundles for the JS components on that page.

As more and more of the content of server templates are removed they become just an HTML "shell" into which the JS libraries and their component's render. The groups of URL can be handled much more like Multi-Page Applications (MPA)

We'd been using Makefiles to manage our simple front end processing for deployment. Each URL will build a "bundle", a concatenated group of files with a hash of file content in the file name, for the manually specified JS/CSS needed by each URL/page. Moving forward we want to move to generally available tooling and in our analysis `webpack`_ seems to combine the best of both Gulp and Grunt.

More importantly is we want to automatically build the bundles based on the components (and their associated CSS) used on each page. We will extract the shared vendor libraries's JS/CSS into their own bundles and put page specific JS/CSS into their own bundle. All bundles are ES7/ES6 and SASS preprocessed, map files generated, concatenated, minified, PostCSS processed as appropriate and named with hashs of their content to support far future expires of resources.

This means we'll have something like four assets loaded for each URL/MPA:

  * vendor.hash.js
  * vendor.hash.css
  * page.hash.js
  * page.hash.css

.. _work: http://www.texturacorp.com
.. _webpack: https://webpack.github.io/
