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


* Start server and start clicking away:
        `./run.sh`


### Anime Data ###

Anime data comes from:
https://github.com/ScudLee/anime-lists


