## Local development
```
docker-compose up
```

Open http://localhost

Should see 
- hello world coming from api
- Alice & Bob coming from api+database

## Run the tests

Assuming containers are running
```
docker-compose exec backend bash

./tests/install-internal.sh
pytest tests/internal

./tests/install-external.sh
source ./tests/install-geckodriver.txt
pytest tests/external
```
