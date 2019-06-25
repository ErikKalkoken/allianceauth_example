# allianceauth_example
This is an example app for Alliance Auth, an auth system for EVE Online to help in-game organizations manage online service access.
You can find Alliance Auth [here](https://gitlab.com/allianceauth/allianceauth).

The purpose of this app is to provide developers who want to add new apps the Auth with a simple and easy to understand template as a good starting point.

## Features
Here is a list of the features of this app:
- Standalone django app that lives in its own folder
- Has its own menu item in the auth site
- Uses same layout as other apps (e.g. corpstats)
- Access is protected by app specific permission (`example.example_view`)

## Installation

1. Copy main folder with all sub directory on the top level (next to auth)

2. Add your app to installed apps in `/myauth/settings/local.py`:
```
# Add any additional apps to this list.
INSTALLED_APPS += [  
   'example.apps.ExampleConfig'
]
```

3. Integrate the app with
```
$ python manage.py makemigrations example
$ python manage.py migrate
```
Now you are ready to run the example app.
Obviously you many want to rename it to something else.

