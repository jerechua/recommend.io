#!/bin/bash

rm ./recommend_db
python manage.py syncdb --noinput
python manage.py load_anime_data ../../anime-lists/
