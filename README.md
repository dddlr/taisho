# Taishanese–Middle Chinese correspondence database

An online dictionary and database for a Chinese dialect called Taishanese. Uses
Django and Postgres.

## How do I set this up?

This is a personal project, which means that running this on your own machine
is not supported. However, you might find these instructions helpful.

1. On a Python 3-only system, set up virtualenv.

2. Install the packages in `requirements.txt` (you don't actually need all of these)
then update them to latest version

3. Set up database.

This project expects a postgresql setup. Useful commands:

- `createuser --interactive` as postgres user
- `createdb taishanese`

4. Set environment variables in `.env` (for Heroku). This is for a dev
environment:

```sh
DJANGO_SETTINGS_MODULE=taishanese.settings.dev
SECRET_KEY='secret key here'
DATABASE_URL='postgresql://username@domain:port/database_name'
DATABASE_NO_SSL=true
```

For a production environment, replace `taishanese.settings.dev` with
`taishanese.settings.prod`, and remove the `DATABASE_NO_SSL` line.

5. Apply database migrations (`./manage.py migrate`) then load data, praying
everything works out:

```sh
$ ./manage.py --exclude=contenttypes --exclude=auth.Permission loaddata [file]
```

## Helpful commands

Mainly for my own purposes.

Running previous version of PostgreSQL database (in this case, 11):

```sh
$ /opt/pgsql-11/bin/pg_ctl -D data start
```

Running local instance:

```sh
$ . ./env/bin/activate
$ export $(cat .env | xargs)
$ heroku local
```
