#!/bin/bash

rm ./recommend_db
./manage.py syncdb
./run.sh