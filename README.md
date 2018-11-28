# Taishanese–Middle Chinese correspondence database

TODO:
* Fix notes using old romanisation
* Update to new romanisation

## How do I set this up?

Mostly for personal reference but you might find this useful too!

1. Set up virtualenv

2. Install these packages (you don't actually need all of these)

```
Package         Version
--------------- -------
Django          2.1.1
django-watson   1.5.2
hanziconv       0.3.2
pip             18.0
psycopg2-binary 2.7.5
pytz            2018.5
setuptools      40.4.3
wheel           0.31.1
```

3. Set up database.

This project expects a postgresql setup with role blep (`createuser
--interactive` as postgres user if need be) and a database called taishanese
(`createdb taishanese`).

4. Apply database migrations (`./manage.py migrate`) then `./manage.py
   --exclude=contenttypes --exclude=auth.Permission loaddata [file]` (and pray
   that works...)
