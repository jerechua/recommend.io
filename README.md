Recommend.io
=============

Community driven recommendation for anything and everything!!!


###recommend_api###

The recommend api endpoints

###recommend_core###

where we put all our frontend files

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
