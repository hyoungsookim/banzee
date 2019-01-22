"""
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from server.config import Config



app = Flask(__name__, static_folder=os.path.join('server', 'static'))

app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://banzee:banzee!$@localhost/db_microtransaction"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False


from server.api.v1.system_resource import system_resource
from server.api.v1.partner_resource import partner_resource
from server.api.v1.payment_method_resource import payment_method_resource
from server.api.v1.product_resource import product_resource
from server.api.v1.account_type_resource import account_type_resource
from server.api.v1.transaction_type_resource import transaction_type_resource
from server.api.v1.transaction_resource import transaction_resource
from server.api.v1.order_resource import order_resource
from server.api.v1.user_resource import user_resource

app.register_blueprint(system_resource)
app.register_blueprint(partner_resource)
app.register_blueprint(payment_method_resource)
app.register_blueprint(product_resource)
app.register_blueprint(account_type_resource)
app.register_blueprint(transaction_type_resource)
app.register_blueprint(transaction_resource)
app.register_blueprint(order_resource)
app.register_blueprint(user_resource)

#db = SQLAlchemy(app)

