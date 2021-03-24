
## Working software

Start with 
```
docker-compose up -d database
```

Wait for the database to be started, then

```
docker-compose up -d frontend backend
```

open http://localhost:8080

Should see hellow world, and Alice & Bob listed

## Run the tests

assuming database and frontend ar up

```
docker-compose run --rm --service-ports builder

./backend/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
pytest tests/internal
pytest tests/external
```

See the app running locally
```
gunicorn -w 1 -b 0.0.0.0:5000 backend:app
```
open http://localhost:8080

btw, my favorite prompt: PS1='\n\[\e[32m\]\u \[\e[33m\]in \w\[\e[0m\] \n> '

