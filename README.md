Recommend.io
=============

Community driven recommendation for anything and everything!!!

###plan###
https://trello.com/board/recommend/5169f1222cc31afe7a00133d

###Setup###
* Might wanna use virtualenv, only needs to be done once:

    `virtualenv env`

* Activate the new virtual environment

    `source env/bin/activate`

* Install any (new) requirements as needed

    `pip install -r reqs.txt`

* Any db changes?

    * Update db:
        `./manage.py syncdb`

    * reset db:
        `./reset_db.sh`

* Load the anime data, anime data comes from https://github.com/ScudLee/anime-lists or http://anidb.net/api/anime-titles.xml.gz. Clone the repo or download the xml file first.

    `./manage.py load_anime_data ../../anime-list/animetitles.xml`


* Start server and start clicking away:
        `./run.sh`


### Anime Data ###

Anime data comes from:

http://anidb.net/api/anime-titles.xml.gz
https://github.com/ScudLee/anime-lists


