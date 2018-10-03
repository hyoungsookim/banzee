"""
"""

from flask_sqlalchemy import SQLAlchemy

from server import app

db = SQLAlchemy(app)

