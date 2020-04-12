# Marketplace

Unified Django application for the marketplace project.

# Install

- Create a virtual environment: `virtualenv venv -p python3`
- Activate the virtual environment: `source venv/bin/activate`
- Install the project requirements: `pip install -r requirements.txt`
- Migrate the database: `python manage.py migrate`
- Create an admin user: `python manage.py createsuperuser`
- Run the development site: `python manage.py runserver`

# Adding a new application

- To add a new application, run: `python manage.py startapp <app_name>`
- Add your `<app_name>` to `INSTALLED_APPS` in `marketplace/base.py` file.
- After adding/changing your model in `<app_name>/models.py` file, prepare database: `python manage.py makemigrations`
- To apply the migration to the database: `python manage.py migrate`

# Templates

# Static files

# User relation
This project is using a customizable user model.
- If you will need to use the user model: `from user.models import User`

# Custom settings
- To use custom settings, create the local settings file: `cp local_settings.py.template local_settings.py`
- Modify its contents and overwrite your needs.
- This file is only for local usage, it is not committed to the project repository.
