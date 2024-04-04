#!/bin/bash
set -e

# Script that runs the application with live reload.
# ONLY for local development.
# Would be nice if the workspace was mounted to the container,
#  but according to the "lean startup" principles, that can be done later.

if [ -f /app/app/main.py ]; then
    DEFAULT_MODULE_NAME=app.main
elif [ -f /app/main.py ]; then
    DEFAULT_MODULE_NAME=main
fi

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}

export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-3000}
LOG_LEVEL=${LOG_LEVEL:-info}


# Start Uvicorn with live reload
export $(grep -v '^#' .env | xargs)
uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL app.main:app
