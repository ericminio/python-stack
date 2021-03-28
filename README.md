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

## features
```
docker-compose up
docker-compose exec backend bash

./features/install.sh
source ./features/install-geckodriver.txt
behave
```

## backend
```
docker-compose up
docker-compose exec backend bash

./backend/requirements.sh
pytest backend/tests
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
