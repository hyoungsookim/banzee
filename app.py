"""
Main entry point of Banzee API application

Usages:
    python app.py
"""

#import os
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

#from server.config import Config
from server import app

"""
from server.api.v1.system_resource import system_resource
from server.api.v1.partner_resource import partner_resource
 

app = Flask(__name__, static_folder=os.path.join('server', 'static'))

app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://banzee:banzee!$@localhost/db_microtransaction"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.register_blueprint(system_resource)
app.register_blueprint(partner_resource)
"""
#db = SQLAlchemy(app)


if __name__ == '__main__':
    #app.run(debug=Config.DEBUG)
    app.run(debug=True)
