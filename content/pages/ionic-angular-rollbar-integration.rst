Ionic Rollbar Integration
#############################################
:date: 2017-07-14 13:00
:author: Steve Schwarz
:category: webdev
:tags: ionic, rollbar
:status: draft


To use `Ionic Native Rollbar <https://ionicframework.com/docs/v2/native/rollbar/>`_ to integrate Rollbar with the native "side" of your Ionic application.

But you don't want to use the version of the plugin currently recommended on the Ionic Native page::

    ionic plugin add resgrid-cordova-plugins-rollbar --variable ROLLBAR_ACCESS_TOKEN="POST_CLIENT_ACCESS_TOKEN" --variable ROLLBAR_ENVIRONMENT="ENVIRONMENT_NAME" --save

Instead you want to use this fork which allows you to also track::

    ionic plugin add https://github.com/emilyemorehouse/cordova-plugins-rollbar.git--variable ROLLBAR_ACCESS_TOKEN="POST_CLIENT_ACCESS_TOKEN" --variable ROLLBAR_ENVIRONMENT="ENVIRONMENT_NAME" --save


In `app.component.ts`::

    import { Rollbar } from 'ionic-native';

    platformReady() {
        // Call any initial plugins when ready
        this.platform.ready().then(() => {
        Rollbar.init();
        });
    }

Angular/TypeScript Integration


npm install @types/requirejs --save

cd src

From: https://github.com/rollbar/rollbar.js/tree/master/examples/webpack
wget https://raw.githubusercontent.com/rollbar/rollbar.js/master/dist/rollbar.umd.nojson.min.js

Create `rollbar.ts` file::

    import { ErrorHandler } from '@angular/core';

    // You could put this data in a configuration file for each environment that is imported at build time:
    var rollbarConfig = {
        accessToken: 'POST_CLIENT_ACCESS_TOKEN',
        captureUncaught: true,
        payload: {
            environment: 'ENVIRONMENT_NAME',
        }
    };
    export let Rollbar = require('../rollbar.umd.nojson.min.js').init(rollbarConfig);

    export class RollbarErrorHandler implements ErrorHandler {
        handleError(err:any) : void {
            Rollbar.error(err.originalError);
        }
    }

Configure Angular error/exception handler to use the `RollbarErrorHandler`.

This mechanism was taken from the Sentry Raven docs: https://docs.sentry.io/clients/javascript/integrations/angular2/#angular-cli::

    import { RollbarErrorHandler } from '../rollbar';

    @NgModule({
      ...
      providers: [ { provide: ErrorHandler, useClass: RollbarErrorHandler } ]
    });


In Ionic pages you can call Rollbar methods::

    import { Rollbar } from '../../rollbar';
    ...
    Rollbar.error('An Error');
    ...
