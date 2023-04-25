

# Google APIs Setup

To interface with Google APIs, the app will need access to a local "service account" credentials file.

## Enabling APIs

From the [Google APIs Dashboard](https://console.cloud.google.com/apis/dashboard) page, search for and "enable" any API(s) of interest, in this case the Google Sheets API.

## Service Account Credentials

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account as necessary.

For the chosen service account, create new JSON credentials file as necessary from the "Keys" menu, then download the resulting JSON file.

Move the service account credentials JSON file into the root directory of this repo, and rename it as "google-credentials.json".

> NOTE: the "google-credentials.json" file has been ignored from version control via the ".gitignore" file, to avoid seeing / exposing these credentials on GitHub
