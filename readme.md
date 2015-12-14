# INSTALLATION AND CONFIGURATION

### Pull down the repository to your local machine

### Install Postgres if it is not already installed
* Using the postgres admin tool, create the database user account to use with the project database
* Using the postgres admin tool, create the database for this project and assign the user you created above as the owner

### Prepare the python virtualenv for the project
* How to install virtualenv - http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Create the virtualenv for your project

### Install the project requirements
* Navigate to the folder containing the repository (lets assume this is /Work/portal)
* Using the fully qualified path to the virtualenv pip, install the requirements
    * Example: /Work/portal/.virtual/portal/bin/pip install -r requirements.txt

### Create a settings.override file for your local machine (note: this will not be included in source control)
* Add a new json file to your /.config/ folder, named settings.override.json , add teh following block:
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "builder-portal",
            "USER": "123",
            "PASSWORD": "1111",
            "HOST": "127.0.0.1",
            "PORT": "5432"
        }
    }

### Prepare the database
* Update the data /.config/settings.override.json file

python manage.py syncdb # prepare the database