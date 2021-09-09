__version__ = '0.1'

from flask import Flask
from flask_debutoolbar import DebugToolbarExtension
app = Flask('flask_bug_summary')
app.config['SECRET_KEY'] = 'random'
app.debug = True
toolbar = DebugToolbarExtension(app)