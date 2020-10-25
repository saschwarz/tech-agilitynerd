title: Lightning Talk: StorybookJS Streamlines UI Component Development
date: 2020-10-24 20:00
author: Steve Schwarz
category: webdev
tags: talks, javascript, video, vuejs

I became interested in [Storybook.js](https://storybook.js.org/) when I was creating a new UI component and wanted a way to quickly iterate on the design and be able to demo the different ways it could be used to my team members.

In the past I would temporarily add a page to our application, add multiple versions of the component, configure them for each variation, and then demo it.
Then repeat as we refined the design.
The temporary page would never be committed to the product's main branch.

Storybook had recently released version 6 so I thought I'd give it a try.
I was _really impressed_ with how easy it was to use for my scenario.

You define your component as you normally would (in [VueJS](https://vuejs.org/) in my case) and import it into a "story file".
A story file is just a JS (or Typescript file) where you define the properties for your component for any variations (use cases) in which you are interested.
Storybook then reads that file and renders pages containing the component for each story.

I was able to quickly modify my component, interact with it, style it, create new stories for different property configurations, and Storybook re-displayed them on each save.
It made for a fast and easy development cycle!

TL;DR: These are the key takeaways for using Storybook when developing web components:

- Installs along side your components/project.
- Watches your component and story files for changes and automatically hot reloads.
- Story files define your components' expected use cases.
- The Storybook UI also allows for interactive modification of properties in the browser.
- The Storybook UI provides basic documentation for users of your components.
- Individual stories can be directly imported into spec files **unit and visual regression tests**. This is a valuable Storybook feature that is often overlooked!

I was so impressed by Storybook I put together a "lightning talk" on using it with VueJS for the [Northwest Chicago JavaScript meetup](https://www.meetup.com/Northwest-Chicago-JavaScript/) September 2020 virtual meeting.
Check it out to see how easy and powerful Storybook is to use.
Here's the video of my presentation (unfortunately, the first few minutes didn't get recorded):

<div class="embed-video">
<iframe src="https://www.youtube.com/embed/ku-62XlU8yk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

If you'd like to see my [slides they are online](https://nwcjs-vue2-storybook.netlify.app/#1). Use arrow keys/spacebar to navigate them.

My [example repo is on GitHub](https://github.com/saschwarz/vue2-storybook).

If you develop web components/controls give Storybook.js a try to simplify component development and test, provide an interactive component browser, and component documentation.
