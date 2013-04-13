#!/bin/bash

rm ./recommend_db
python manage.py syncdb --no-input
./run.sh
