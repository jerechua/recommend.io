#!/bin/bash

rm ./recommend_db
python manage.py syncdb --noinput
./run.sh
