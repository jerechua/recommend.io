#!/bin/bash

rm ./recommend_db
python manage.py syncdb --noinput --settings=recommend.my_settings
python manage.py load_anime_data ../../anime-lists/ --settings=recommend.my_settings
