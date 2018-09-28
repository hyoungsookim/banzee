"""
Main entry point of Banzee API application

Usages:
    python app.py
"""

import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config


app = Flask(__name__, static_folder=os.path.join('server', 'static'))

app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://banzee:banzee!$@localhost/db_microtransaction"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
    #app.run(debug=True)
