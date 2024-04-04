#!/usr/bin/env bash
set -e

FILE=".env"
if [ -f "$FILE" ]; then
    echo ".env file does exist, continuing."
else
    echo ".env file does not exist and will be created from .env.local"
    cp .env.local .env
fi

# export env variables
export $(grep -v '^#' .env | xargs)

./build.sh
docker compose up -d

echo -e "\033[1m-------------------------------\033[0m"
echo -e "\033[1mApplication started successfully and is running at\033[0m $SERVER_HOST"
echo -e "\033[1mTo stop the application run: docker compose down\033[0m"
echo -e "\033[1mTo view logs run:\033[0m docker logs -f maciej_szok_projects_api_backend"
echo -e "\033[1mTo run tests run:\033[0m ./test.sh"
echo -e "\033[1mFor a simple test run:\033[0m curl -L --request GET --url http://0.0.0.0:$PORT/api/v1/projects "
echo -e "\033[1mFor OpenAPI docs visit:\033[0m http://0.0.0.0:$PORT/docs"
