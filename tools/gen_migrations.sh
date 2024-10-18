#!/usr/bin/env bash

cd "$(dirname "$0")/.." || exit

cd api || exit
flask --app app.server.py db init