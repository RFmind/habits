# Habits Project

## Server

### Install Dependencies

`pip install -r requirements.txt`

### Run Tests

##### Locally

`python habits/server/tests.py`

##### In a docker container

`docker-compose up test`

### Run Application

##### Locally

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

