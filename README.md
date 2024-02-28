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
poetry install --with dev # Will install the project's dependencies outside docker
pre-commit install # Will configure your local git repo to run the hook before each commit
```

Most management commads will require you to run the python interpreter from the poetry environment inside the docker container :

```bash
docker compose exec django poetry run python manage.py [...your management command...]
```

This is quite verbose, you should probably create an alias.

## What's included ?

### Python/back-end side

- Django + Django Rest Framework
- Some boilerplate for using DRF's router in `urls.py`
- Logging that is more advanced than Django's default settings
- Dependency management with [`poetry`](https://python-poetry.org/)
- [`black` code formatter](https://github.com/psf/black) + `pylint` + `pylint-django` + base config for these tools
- Pre-commit hook to auto-format the code with [`pre-commit`](https://pre-commit.com/)
- `settings_constants.py` file for settings that are deployment-specific
- [`django-debug-toolbar`](https://django-debug-toolbar.readthedocs.io/en/latest/index.html) and [`django-extensions`](https://github.com/django-extensions/django-extensions) pre-configured for dev server, but not production deployments.
- Settings to serve the API under the `/api/` path with a reverse-proxy.
- Pre-configured to use the PostgreSQL database from docker compose

### Nuxt/front-end side

- `npm run lint` & `npm run fix` commands using `prettier` and `eslint` (pre-configured with nuxt/vue rules)
- Bootstrap + icons + CSS boilerplate to use it in the project
- Disabled SSR by default

### Docker stuff

- 2 compose files : one for the dev environment, one for deploying the app
- Internal nginx instance(s) that make it easier to serve the whole thing from a single origin
- Plumbing to serve Django's static bundle and Nuxt's build output from nginx
