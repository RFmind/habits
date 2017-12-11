# Habits Project [![Travis-ci Build Status](https://travis-ci.org/RFmind/habits.svg?branch=master)](https://travis-ci.org/RFmind/habits) [![wercker status](https://app.wercker.com/status/c052797d601f12279620faf7d6ced6ea/m/master "wercker status")](https://app.wercker.com/project/byKey/c052797d601f12279620faf7d6ced6ea) [![BCH compliance](https://bettercodehub.com/edge/badge/RFmind/habits?branch=master)](https://bettercodehub.com/)

## Server

### Install Dependencies

`pip install -r requirements.txt`

### Run Tests

##### Locally

Make sure to set the `SETTINGS_MODE` environment variable to `TEST`, `DEV` or `PROD`.
Then run the tests:

`python habits/server/tests.py`

##### In a docker container

`docker-compose up test`

### Run Application

##### Locally

Make sure to set the `SETTINGS_MODE` to `TEST`, `DEV` or `PROD`.
Then run the application:

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
cd /habits/static/
npm run build
```

### Run Tests

```
cd /habits/static/
npm run tests
```

