
## start the database
```
docker-compose up -d database
```

## start nginx
```
docker-compose up -d nginx
```

## Run the tests
```
docker-compose run --rm builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
pytest tests/internal
pytest tests/external
```

## Run the app
```
docker-compose run --rm --service-ports builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
gunicorn -w 1 -b 0.0.0.0:5000 app:app

open http://localhost:8080
```
