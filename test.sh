#!/usr/bin/env bash

export $(grep -v '^#' .env | xargs)

# TODO create and remove a test database locally
pytest app/tests/
