# Working Sofware

https://python-stack.herokuapp.com

# Local development
```
docker-compose up
```

Open http://localhost:8080

Should see 
- hello world coming from api
- Alice & Bob coming from api+database

# Run the tests

Assuming containers are running
```
docker-compose exec backend bash

./tests/install-internal.sh
pytest tests/internal

./tests/install-external.sh
source ./tests/install-geckodriver.txt
pytest tests/external
```

# Deployment

## Heroku

- create 2 applications, say `app-nginx` and ```app-backend```
- add config var `BACKEND_URL` in application `nginx`
- deploy `backend`
    - `cd backend`
    - `heroku container:push web --app app-backend`
    - `heroku container:release web --app app-backend`
- deploy `nginx`
    - `cd nginx`
    - `heroku container:push web --app app-nginx`
    - `heroku container:release web --app app-nginx`
