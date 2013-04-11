#!/bin/bash

rm ./recommend_db
python manage.py syncdb
./run.sh