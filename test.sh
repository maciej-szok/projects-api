#!/usr/bin/env bash

set -e
export $(grep -v '^#' .env | xargs)

# TODO create and remove a test database locally
pytest app/tests/
