#!/usr/bin/env bash

set -e
export $(grep -v '^#' .env | xargs)

pytest app/tests/
