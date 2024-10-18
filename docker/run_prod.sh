#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.." || exit

echo '################################ run migrations  create-db ################################'
python3 -m flask --app api.app.server.py create-db

echo '################################# run migrations  upgrade #################################'
python3 -m flask --app api.app.server.py db upgrade -d api/migrations

echo '####################################### start server ######################################'
