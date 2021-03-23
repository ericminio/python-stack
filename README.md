
## Run the tests
```
docker-compose run --rm builder

./app/requirements.sh
./tests/install-firefox.sh
source ./tests/adjust-path.sh
pytest tests
```