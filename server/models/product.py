"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TEXT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class Product(db.Model):
    __tablename__ = 'mtt_md_products'

    product_no          = db.Column(INTEGER, primary_key=True, autoincrement=True)
    product_id          = db.Column(String(50), nullable=False, unique=True)
    product_status      = db.Column(SMALLINT, nullable=False)
    product_name        = db.Column(String(50), nullable=False)
    product_type        = db.Column(String(20), nullable=False)
    created_at          = db.Column(DateTime, nullable=False)
    updated_at          = db.Column(DateTime, nullable=False)
    product_description = db.Column(TEXT, nullable=True)

    def __init__(self, product_id, product_status, product_name, product_type, 
                product_description=None):
        self.product_id = product_id
        self.product_status = product_status
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
