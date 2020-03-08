# Taishanese–Middle Chinese correspondence database

## How do I set this up?

Mostly for personal reference but you might find this useful too!

1. Set up virtualenv

2. Install the packages in `requirements.txt` (you don't actually need all of these)
then update them to latest version

3. Set up database.

This project expects a postgresql setup with role blep (`createuser
--interactive` as postgres user if need be) and a database called taishanese
(`createdb taishanese`).

4. Apply database migrations (`./manage.py migrate`) then `./manage.py
   --exclude=contenttypes --exclude=auth.Permission loaddata [file]` (and pray
   that works...)

## Helpful commands

Mainly for my own purposes.

Running PostgreSQL database (before I upgrade to version 12):

```
$ /opt/pgsql-11/bin/pg_ctl -D data start
```

```
$ . ./env/bin/activate
$ export $(cat .env | xargs)
$ heroku local
```
