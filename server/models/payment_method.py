"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class PaymentMethod(db.Model):
    __tablename__ = 'mtt_md_payment_methods'

    method_code     = db.Column(String(10), primary_key=True)
    method_status   = db.Column(SMALLINT, nullable=True)
    method_name     = db.Column(String(50), nullable=False)
    method_type     = db.Column(String(10), nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)

    def __init__(self, method_code, method_status, method_name, method_type):
        self.method_code = method_code
        self.method_status = method_status
        self.method_name = method_name
        self.method_type = method_type
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
