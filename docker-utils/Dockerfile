FROM python:3.13-slim AS django_dev
WORKDIR /django_app
ENV PATH="${PATH}:/home/djangouser/.local/bin"
COPY docker-utils/docker-install.sh /
RUN bash /docker-install.sh
ENV RUNNING_DEVSERVER=1

FROM django_dev AS django_staging
COPY pyproject.toml /django_app
COPY poetry.lock /django_app
RUN sudo -u djangouser /home/djangouser/.local/bin/poetry install --without dev
ENV RUNNING_DEVSERVER=0
