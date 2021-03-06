# Habits Project

## Badges

[![wercker status](https://app.wercker.com/status/c052797d601f12279620faf7d6ced6ea/m/master "wercker status")](https://app.wercker.com/project/byKey/c052797d601f12279620faf7d6ced6ea) [![BCH compliance](https://bettercodehub.com/edge/badge/RFmind/habits?branch=master)](https://bettercodehub.com/)

## Introduction

This is a fullstack application. A React + Redux based frontend is integrated with
a REST-style Python-based backend.

You can find the latest builds on Docker Hub @ hub.docker.com/r/rfmind/habits

To run the container the following environment variables should be set:
* `SETTINGS_MODE` should be one of `TEST`, `DEV` or `PROD`
* `DATABASE_URL` (e.g. `postgresql://user:pass@host:port/databasename`)

Additionally you can set a custom port using the `PORT` variable.

You can also clone this repository and follow the instructions below to test/run
the application.

## Server

### Install Dependencies

`pip install -r requirements.txt`

### Run Tests

##### Locally

Make sure to set the `SETTINGS_MODE` environment variable to `TEST`.

Then run the tests:

`python habits/server/tests.py`

##### In a docker container

`docker-compose up test`

### Run Application

##### Locally

Make sure to set the `SETTINGS_MODE` to `DEV` or `PROD`.
In case of `PROD` the `DATABASE_URL` should also be set.

Now run the application:

`python habits/server/run.py`

##### In a docker container

`docker-compose up web`

## Front-end

### Install Dependencies

```
cd habits/static/
npm install
```

### Build Application

```
cd habits/static/
npm run build
```

### Run Tests

```
cd habits/static/
npm run tests
```

