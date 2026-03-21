# Journal App

A Django journal application with user authentication and private entry management. Users can sign up, log in, create entries, edit them, review older notes, and delete entries they no longer want to keep.

## Features

- User signup and login using Django's built-in authentication
- Private journal entries scoped to the logged-in user
- Create, view, edit, and delete entry workflows
- Entry list ordered by most recent creation date
- Tailwind-powered UI served from templates
- Production-oriented deployment setup with `gunicorn`, `whitenoise`, and `dj-database-url`

## Tech Stack

- Python
- Django 6
- SQLite or PostgreSQL via `DATABASE_URL`
- Gunicorn
- WhiteNoise
- Tailwind CSS via CDN

## Project Structure

```text
journal-app/
|-- config/              # Django project settings and root URLs
|-- journal/             # Journal app models, views, routes, migrations
|-- templates/           # Base, auth, and journal templates
|-- manage.py
|-- requirements.txt
|-- Procfile
|-- db.sqlite3
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set `DATABASE_URL`.

This project currently requires `DATABASE_URL` to be present at startup. If it is missing, Django raises an exception in [config/settings.py](c:\Users\midhu\OneDrive\Desktop\journal-app\config\settings.py).

Examples:

```powershell
$env:DATABASE_URL="sqlite:///db.sqlite3"
```

```bash
export DATABASE_URL="sqlite:///db.sqlite3"
```

For PostgreSQL:

```bash
export DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/DB_NAME"
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open `http://127.0.0.1:8000/`.

## Main Routes

- `/` - entry list for the logged-in user
- `/entries/new/` - create a new entry
- `/entries/<id>/` - view a single entry
- `/entries/<id>/edit/` - edit an entry
- `/entries/<id>/delete/` - delete an entry
- `/accounts/login/` - login page
- `/signup/` - signup page

## Deployment

The project includes a `Procfile` for running Django with Gunicorn:

```text
web: gunicorn config.wsgi
```

`ALLOWED_HOSTS` is currently set for Render in [config/settings.py](c:\Users\midhu\OneDrive\Desktop\journal-app\config\settings.py).

## Current Limitations

- `SECRET_KEY` is hardcoded in settings and should be moved to an environment variable for real deployments.
- `DEBUG` is currently set to `True`.
- There are no meaningful automated tests yet; [journal/tests.py](c:\Users\midhu\OneDrive\Desktop\journal-app\journal\tests.py) is still the default placeholder.
- The settings file requires `DATABASE_URL` even though `db.sqlite3` is present in the repository.

## License

No license file is currently included in this repository.
