===================================
 ReactJS SVG Path Player Component
===================================
:date: 2016-01-24 12:00
:author: Steve Schwarz
:category: javascript
:tags: reactjs, javascript, SVG

I've been a big fan of `SVG <https://en.wikipedia.org/wiki/Scalable_Vector_Graphics>`_ images for many years for their light weight and resolution independence. I started playing with them back when most browsers needed a plugin to render them; which kept me from using them in web sites. Within the past few years SVG has become natively supported by almost all browsers and mobile devices so I could finally use them on my `agilitycourses.com <http://agilitycourses.com/>`_ website to display dog agility obstacles and the sequences through them.

My next enhancement to the site was to animate the shortest/fastest paths dogs could take through the obstacles. I had found the `Snap.svg <http://snapsvg.io/>`_ JavaScript library which is light weight, resonably well supported and, to make it even easier, I found a `great example of animating a path and a marker along the path <http://icanbecreative.com/article/animate-element-along-svg-path/>`_ using it.

I decided to make a "media player component" that I could instantiate in multiple places in the site and realized if I generalized the component a little it might be useful for others.

I also decided to use React to create it. React has a well defined component approach and I thought this would be a good learning experience with the library and the tooling/packaging required to share it.

Here's what the SVG Path Player component looks like in action:

.. class:: thumbnail
.. figure:: {static}/images/ac-dog-path-animation.gif
   :alt: Animated SVG Path Player in Action
   :align: center

Here's an article from my dog agility blog `explaining how dog agility handlers can use this player <http://agilitynerd.com/blog/agility/handling/multiple-dog-paths-challenge-handling.html>`_.

Some Things I Learned
=====================

I won't walk through the code, `it's all on GitHub <http://saschwarz.github.io/react-svgpathplayer/>`_, but I'll give you some pointers and links to articles/videos I found useful.

The ``SVGPathPlayer`` component itself renders the UI and provides the button's callback methods that call to a Snap.svg element that "owns" the SVG image it controls. The ``componentDidMount`` method uses Snap.svg to load the SVG image and select the path(s), and optional marker within it. Within the ``render`` method the element into which the SVG image is rendered is a React `ref <https://facebook.github.io/react/docs/more-about-refs.html#the-ref-callback-attribute>`_ child element:

.. code:: javascript

   <div className="svg-container svg-container-box" ref={(ref) => this.svgImage = ref}></div>

I chose to store the ``ref`` on ``this`` and not in the state of the component since it doesn't impact the component state; it is a data member used only by Snap.

Once loaded the ``render`` method uses a ``Controls`` component to show the animation status and allow the user to start, stop and step forward/backward within the animation. The ``Controls`` component is a "stateless" or `"dumb" compone t <https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.qqffkj3iv>`_; it's buttons invoke callbacks provided via it's ``props`` by it's parent "smart component": ``SVGPathPlayer``.

Making ``Controls`` and ``Spinner`` dumb components made writing tests for them really easy. I might never reuse these components, but they made reasoning about responsibilities easier and helped me simplify the interfaces (props) passed in to each component. Going through the refactoring into components I also deleted some internal state I didn't really need in the original monolithic component.

Writing the React code was straight forward and I found using ES6 syntax made it even easier. The big challenges with this project were packaging it as a reusable component that could be used in both "script" and "npm" installations, generating GitHub hosted pages, and automating the testing/packaging/deployment as part of the Travis-CI automation.

There are a lot of boilerplate React application projects out there but not too many for reusable React components. I found `survivejs/react-component-boilerplate <https://github.com/survivejs/react-component-boilerplate>`_ to be very well supported and included most of the functionality I wanted. I also bought the ebook `SurviveJS - Webpack and React - From apprentice to master <http://survivejs.com/>`_ which has been continuously updated to incorporate all the recent changes in the Webpack/Babel tools (I still need to migrate my tooling to the latest Babel release).

So checkout my project's ``package.json npm`` `scripts <https://github.com/saschwarz/react-svgpathplayer/blob/master/package.json#L6>`_ and the ``webpack.config.babel.js`` `distribution configurations <https://github.com/saschwarz/react-svgpathplayer/blob/master/webpack.config.babel.js#L164>`_ for the scripts/configurations to create all the pieces. Getting all of this to work is still a little complex and I should document how I got it working as well as creating my own boilerplate project. I know I would have benefitted from an annotated versions of those files.

Another very helpful resource was `Kent C. Dodds <http://kentcdodds.com/>`_ egghead.io videos on `How to Write an Open Source JavaScript Library <https://egghead.io/series/how-to-write-an-open-source-javascript-library>`_ particularly for Travis-CI integration and using semantic-release.

If you are looking to make your own redistributable React components I strongly recommend reviewing both of those resources and looking through the configuration of my component. I hope to write up the details after I find some time to migrate the webpack tooling to the latest versions.
