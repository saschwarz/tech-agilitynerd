Disabling Rollbar and Enabling Logging During Vue.js Development
################################################################
:date: 2019-03-30 8:00
:author: Steve Schwarz
:category: webdev
:tags: javascript, vuejs

I was adding `Rollbar <https://rollbar.com>`_ support to a `Vue.js <https://vuejs.org>`_ application and ran into an issue that made it inconvenient for use in development environments:

Captured exceptions and ``rollbar.error|warning|log|...`` calls are always sent and logged in the Rollbar dashboard.

You could configure different a Rollbar ``environment`` for development and filter the dashboard; but I'd rather not even send "developer-induced" errors to Rollbar at all.
After speaking with support they don't yet have a "log locally and don't send to Rollbar" configuration.

So I came up with this simple Vue plugin that is only installed during development builds:

.. code-block:: javascript

    if (process.env.NODE_ENV === 'development') {
      const Rollbar = function () {
        // I only call $rollbar.error in the app
        this.error = console.error
        // define other rollbar API mocks here
      }
      const RollbarMockPlugin = {
        install: function (Vue, options) {
          Vue.rollbar = new Rollbar(options);
          Vue.prototype.$rollbar = Vue.rollbar;
        }
      }
      Vue.use(RollbarMockPlugin)
    } else {
      // Your normal Rollbar configuration
      // I set some env vars in the build script
      Vue.use(Rollbar, {
        accessToken: process.env.VUE_APP_ROLLBAR_POST_CLIENT_ITEM_KEY,
        captureUncaught: true,
        captureUnhandledRejections: true,
        enabled: process.env.NODE_ENV === 'production',
        environment: process.env.DEPLOY_ENV, // dashboard filtering
        verbose: true, // also log to console
        payload: {
          client: {
            javascript: {
              guess_uncaught_frames: true,
              source_map_enabled: true,
              code_version: process.env.VUE_APP_VERSION
            }
          }
        }
      });

So when I have code like this in the app:

.. code-block:: javascript

    async save(value) {
      this.loading = true
      try {
        const payload = { todo: value }
        await this.saveTodo(payload)
      } catch (e) {
        this.$rollbar.error(e)
        this.notifySaveFailed()
      }
      this.loading = false

The call to ``this.$rollbar.error(e)`` now logs **only** to the dev console when running in development.

So I hope this little shim helps you keep your Rollbar dashboard free from development environment clutter.
