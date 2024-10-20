#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.." || exit

echo '##################################### create database #####################################'
python3 -m flask --app api.app.server.py create-db

echo '################################# run migrations  upgrade #################################'
python3 -m flask --app api.app.server.py db upgrade -d api/migrations

echo '#################################### init project data ####################################'
python3 -m flask --app api.app.server.py init-db

echo '####################################### start server ######################################'
