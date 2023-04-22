FROM python:3.9-alpine3.13

MAINTAINER "farhansaeed"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8003

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/python -m pip --default-timeout=100 install --upgrade pip && \
    /py/bin/pip --default-timeout=100 install -r /tmp/requirements.txt && \
    if [ $DEV == true ]; \
        then /py/bin/pip --default-timeout=100 install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user