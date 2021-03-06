[![Build Status](https://github.com/ericminio/python-stack/actions/workflows/ci.yml/badge.svg)](https://github.com/ericminio/python-stack/actions)

# Working Sofware

https://python-stack.herokuapp.com

# Local development
```
docker-compose up
open http://localhost:8080
```
Should see 
- hello world coming from api
- Alice & Bob coming from api+database

# Run the tests

## features
```
cd features/support
docker-compose run behave
```

## backend
```
docker-compose up
docker-compose exec backend ./backend/tests/support/run.sh
```

# Deployment

## Heroku

- create 2 applications, for example
    - `python-stack`
    - `python-stack-backend`
- access your heroku.com account
    - navigate to `python-stack-backend` Resources
    - add Heroku Postgres add-on
    - navigate to `python-stack` Settings
    - click `Reveal Config Vars`
    - add config var 
        - key `BACKEND_URL`
        - value `https://python-stack-backend.herokuapp.com/` [1]
- run `./deployment/heroku.sh` [2]

[1] trailing slash needed by nginx configuration

[2] adjust script to target your applications.
