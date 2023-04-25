
# Google Sheets Database Setup

Follow the [Google APIs Setup](/setup/GOOGLE_APIS.md) guide to ensure the Google Sheets API has been enabled, and there is a service account credentials file called "google-credentials.json" in the root directory of your local repository.

### Google Sheets Database Setup

Create a new Google Sheet document, or copy this [starter sheet](https://docs.google.com/spreadsheets/d/1tkVK0dgDRgPsr8iU5FhNYt-AaTUYc118ahYJbAi-DSU).

Modify the document's sharing settings to grant "edit" privileges to the "client email" address specified in the service account credentials file.

Note the document's identifier from its URL (i.e. `https://docs.google.com/spreadsheets/d/____________`), and set as an environment variable called `GOOGLE_SHEETS_DOCUMENT_ID` (see README).

### Schema Setup

If you copied the starter sheet, feel free to skip this schema setup step. Otherwise, here are some instructions for how to configure the sheets from scratch.

> NOTE: the app will be looking for these specific sheet names and column names below

**Products Sheet**

Create a new sheet called "products", and add an initial row of column headers:
  + `id`
  + `name`
  + `description`
  + `price`
  + `url`
  + `created_at`


**Orders Sheet**

Create a new sheet called "orders", and add an initial row of column headers:

  + `id`
  + `user_email`
  + `product_id`
  + `product_name`
  + `product_price`
  + `created_at`

### Seeding the Database

Seed the database to automatically populate it with example product records:

```sh
python -m web_app.services.sheets
```

> NOTE: if this produces a 403 error, remember to share editor privileges on your sheets document with the email address associated with your service account credentials JSON file (see above)


If successful, you should see these default product records added to the "products" sheet:

name | description | price | url
--- | --- | --- | ---
Strawberries | Juicy organic strawberries. | 4.99 | https://picsum.photos/id/1080/360/200
Cup of Tea | An individually-prepared tea or coffee of choice. | 3.49 | https://picsum.photos/id/225/360/200
Textbook | It has all the answers. | 129.99 | https://picsum.photos/id/24/360/200
