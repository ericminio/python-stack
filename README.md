
```
docker-compose up -d database nginx
```

## Run the tests

assuming database and nginx ar up

```
docker-compose run --rm builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
pytest tests/internal
pytest tests/external
```

btw, my favorite prompt: PS1='\n\[\e[32m\]\u \[\e[33m\]in \w\[\e[0m\] \n> '

## Run the app

assuming database and nginx ar up

```
docker-compose run --rm --service-ports builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
gunicorn -w 1 -b 0.0.0.0:5000 backend:app

open http://localhost:8080
```
