# Django Rest Framework + Nuxt3 template

This repo is a template for all the boilerplate involved in getting a DRF+Nuxt dev environment running.

## How to start a project ?

Run the following command (you will need to have django installed in your current `$PYTHONPATH`) :

```bash
django-admin startproject --template https://git.pierre-couy.fr/pcouy/drf-nuxt-template/archive/main.zip -e py,yaml,yml,toml,sh my_awesome_project
cd startproject
```

This will download the latest version from the repository, unpack it and render the templates.
Once this is done, you can launch either a dev environment or a production build by running one of the following commands :

```bash
docker compose up -d
docker compose -f docker-compose.deploy.yml up -d
```

You can optionally opt-in to the pre-commit python formatting with `black` :

```bash
poetry install --with dev # Will install the project's dependencies outside docker, including `black` and `pylint`
pre-commit install # Will configure your local git repo to run the hook before each commit
```

Most management commads will require you to run the python interpreter from the poetry environment inside the docker container :

```bash
docker compose exec django poetry run python manage.py [...your management command...]
```

This is quite verbose, you should probably create an alias.

The development front-end will be available at `http://localhost:50080` and all Django URLs will be available under `http://localhost:50080/api`. You can get a PostgreSQL shell by running `docker compose exec -u postgres postgres psql {{your_project_name}}db` or using the database name, user and password from `settings_constants.py` with `localhost:55432`. The dev servers (both front-end and back-end) will auto-detect changes in the working directory, but you may ocasionally need to run `docker compose restart` after installing new dependencies.

When using the `docker-compose.deploy.yml` file, the web server will be available at `http://localhost:50090`. Values in `settings_constants.py` are intended make the dev environment run "out of the box", you will want to edit this file when deploying publicly.

## What's included ?

### Python/back-end side

- Django + Django Rest Framework
- Some boilerplate for using DRF's router in `urls.py`
- Logging that is more advanced than Django's default settings
- Dependency management with [`poetry`](https://python-poetry.org/)
- [`black` code formatter](https://github.com/psf/black) + `pylint` + `pylint-django` + base config for these tools in `pyproject.toml`
- Pre-commit hook to auto-format the code with [`pre-commit`](https://pre-commit.com/)
- `settings_constants.py` file for settings that are deployment-specific
- [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/index.html) and [`django-extensions`](https://github.com/django-extensions/django-extensions) pre-configured for dev server, but not production deployments.
- Settings to serve the API under the `/api/` path with a reverse-proxy.
- Pre-configured to use the PostgreSQL database from docker compose

### Nuxt/front-end side

- `npm run lint` & `npm run fix` commands using `prettier` and `eslint` (pre-configured with nuxt/vue rules)
- Bootstrap + icons + CSS boilerplate to use it in the project
- Disabled SSR by default

### General + Docker stuff

- 2 compose files : one for the dev environment, one for deploying the app
- Internal nginx instance(s) that make it easier to serve the whole thing from a single origin
- Plumbing to serve Django's static bundle and Nuxt's build output from nginx
- Sane `.gitignore`
