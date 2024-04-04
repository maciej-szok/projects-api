#!/usr/bin/env bash

# Simplified script for testing the application.
# Usually, the CI/CD pipeline would run the tests and check if they passed,
# but this provides a quick and easy way to run the tests in the container.

# Ideally, a new database would be created for the tests when running locally, but again, for the sake of
# simplicity, the tests are run against the local db.


# make sure the app is not running before we start
docker-compose down

export $(grep -v '^#' .env | xargs)
INSTALL_DEV=true

# build including dev dependencies
./build.sh --build-arg INSTALL_DEV=true

# start the server and the database
docker compose up -d

# run migrations and tests
docker exec -it maciej_szok_projects_api_backend bash -c "alembic upgrade head"
docker exec -it maciej_szok_projects_api_backend bash -c "pytest app/tests/"

docker compose down
