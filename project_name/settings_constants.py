"""
This file gathers all settings that need attention when deploying {{ project_name }} to a new host/server.
All constants in this file are deployment-specific. Some of them are secrets that should not
be committed to version-control.

Some of these secrets can be commited to version control for convenience, on the condition that
they only grant access to resources running inside local dev envs (not publicly accessible).
These secrets MUST be changed for production deployments.

Add `# SECURITY WARNING:` comment lines where appropriate
Use `EDIT-THIS` as a placeholder for anything that should not be commited to version control

See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:50080",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "{{ project_name }}db",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "postgres",
        "PORT": "5432",
    },
}

# SECURITY WARNING: ANYTHING BELOW THIS LINE IS A SECRET. THE VALUE USED IN PRODUCTION SHOULD NOT
# BE COMITTED TO VERSION CONTROL. THE VALUES FROM VERSION CONTROL ARE PROVIDED FOR CONVENIENCE
SECRET_KEY = "EDIT-THIS-django-not-really-a-secret-{{ secret_key }}"
