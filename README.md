# flask-sheets-starter-2023

This is an example full stack web application built in Python with the Flask framework. This application implements Google Login and interfaces with a Google Sheets datastore.

<img width="750" alt="Screenshot 2023-04-19 at 8 10 15 PM" src="https://user-images.githubusercontent.com/1328807/233225795-2bac1806-37de-4981-a635-bfef72506ad5.png">

## Setup

### Prerequisites

To run this app, you'll need to have Anaconda, Python, and Pip installed (specifically Python version 3.10+).

### Installation

Make a copy of the template repository from GitHub, as necessary. Clone your copy of the repo onto your local computer, for example onto your Desktop.

Navigate to the local repository from the command line, for example if on the Desktop:

```sh
cd ~/Desktop/flask-sheets-starter-2023
```

> NOTE: it is important to navigate to the root directory before running many of the commands below.


Create new virtual environment (first time only):

```sh
conda create -n flask-sheets-starter python=3.10
```

Activate the virtual environment (first time, or whenever you return to the project):

```sh
conda activate flask-sheets-starter
```

> NOTE: it is important to activate the virual environment before running any of the commands below.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
```

### Services

Follow these guides to setup the various cloud services required by this application:

  + [Google Cloud](/setup/GOOGLE_CLOUD.md):
    + [Google Login](/setup/GOOGLE_LOGIN.md)
    + [Google APIs](/setup/GOOGLE_APIS.md)
    + [Google Sheets Datastore](/setup/GOOGLE_SHEETS.md)

## Configuration

Create a new file called ".env" in the root directory of this local repository, and place inside contents like the following:

```sh
# this is the ".env" file...

# for flask:
FLASK_APP="web_app"

# for google analytics (optional):
# GA_TRACKER_ID="G-____________"

# for google login:
GOOGLE_CLIENT_ID="___________"
GOOGLE_CLIENT_SECRET="___________"

# for google sheets:
GOOGLE_SHEETS_DOCUMENT_ID="___________"
```

> NOTE: when you push your repository to GitHub, the ".env" file does not show up - this is desired behavior, as designated by the ".gitignore" file, to prevent our secret credentials stored in the ".env" file from being uploaded or exposed on GitHub.

## Usage

Run the web application (then view in the browser at localhost:5000):

```sh
flask run
```


## [Deploying](/setup/RENDER.md)
