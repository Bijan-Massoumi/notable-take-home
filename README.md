# Flask-React-Boilerplate
Boilerplate for a RESTfull React, Flask project.

## To start:

In project root run `make`

Then create a virtualenv and install dependencies. I used 3.7.5 for my development; most minor versions of 3 should work.

```
cd server
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
```

Launch the app with `python run.py` and go to `http://127.0.0.1:5000/`
