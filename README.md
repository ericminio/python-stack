
## Run the tests
```
docker-compose run --rm builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
pytest tests
```

## Run the app
```
docker-compose run --rm --service-ports builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
gunicorn -w 1 -b 0.0.0.0:5000 app:app

open http://localhost:5000
```
