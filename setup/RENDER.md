# Deploying to Render

Follow this guide if you would like to deploy your host your application on a free server provided by the Render platform.

References:
  + https://render.com/docs/deploy-flask

## Render Setup

Login to [Render](https://dashboard.render.com) and visit the dashboard.

Create a New "Web Service". Choose your own repository by specifying its public URL.

Specify start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Under the "Advanced" options, set the following environment variable (specifying your own API Key value):


```sh
GOOGLE_CLIENT_ID="______.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="______"
GOOGLE_CREDENTIALS_FILEPATH="/etc/secrets/google-credentials.json"
GOOGLE_SHEETS_DOCUMENT_ID="___________"
SECRET_KEY="your secret key here"
```

Also set a [secret configuration file](https://community.render.com/t/using-google-application-credentials-json/6885) called "google-credentials.json", and paste the contents from your google service account credentials file. The render web service will then have access to the file as "/etc/secrets/google-credentials.json" (as referenced by the `GOOGLE_CREDENTIALS_FILEPATH` variable above).



Finally, click to "Create" the web service.


## Render Deploys

Whenever you push new code to the desingated branch in your GitHub repository, it will trigger a new deployment to update your hosted site.

You can also trigger builds manually.



## Google Cloud Setup, Revisited

For the Google Login to work on the production server, return to the Google API console, and under [credentials](https://console.cloud.google.com/apis/credentials/) for your web client, configure a redirect url pointing to the render server: "https://YOUR_RENDER_APP.onrender.com/auth/google/callback" and save.

While the web client is in test mode, only tests users can use in production, in which case you may need to add your email address as a "Test User" in the OAuth consent screen. Otherwise publish the app.
