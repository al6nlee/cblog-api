#!/usr/bin/env bash

cd "$(dirname "$0")/.." || exit

cd api || exit

# 开发过程中的脚本，init基本不会执行了，如果远端没有建过数据库，可以执行create-db，migrate更新本地表结构，upgrade同步远端表结构
flask --app app.server.py migrate create-db

#flask --app app.server.py db init
#flask --app app.server.py db migrate
flask --app app.server.py db upgrade   # 项目启动的时候只需要数据投喂即可
flask --app app.server.py migrate init-db