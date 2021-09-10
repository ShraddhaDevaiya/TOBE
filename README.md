# Task-Oriented Bug Report Summarizer (TOBE)

TOBE annotates sentences in bug reports automatically so that users can select which sentences that they are interested to see.

TOBE is developed using Python 3.8 and Flask 1.1.1. To run TOBE in your local machine you need Python >=3.6. 

#### TOBE setup instructions
1. Clone the repository to a preferred location in your local machine.
2. Create the files `.env` and `config.py` in the project root (in the same level of `app.py`). Contents are as follows.

`.env`
```
APP_SETTINGS = "config.DevelopmentConfig"
```

`config.py`
```
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'add a key later'

class ProductionConfig(object):
    DEBUG = False

class StagingConfig(object):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(object):
    DEVELOPMENT = True
    DEBUG = True
    
class TestingConfig(object):
    TESTING = True
```

3. Install the requirements using the following command.
```buildoutcfg
pip install -r requirements.txt
```

4. Run the app using the following command.
```buildoutcfg
python -m flask run
```

5. Go to your browser and use the localhost:port given in the terminal. The default given by the flask debugging server is `127.0.0.1:5000`.
It will take some to load the first bug report or to load a new bug report when selected from the dropdown menu.

