"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class Order(db.Model):
    __tablename__ = "mtt_tx_orders"

    order_no        = db.Column(INTEGER, primary_key=True, autoincrement=True)
    order_id        = db.Column(String(50), nullable=False, unique=True)
    user_no         = db.Column(INTEGER, nullable=False)
    order_status    = db.Column(SMALLINT, nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)
    order_amount    = db.Column(DECIMAL(12, 2), nullable=False)
    tax_amount      = db.Column(DECIMAL(12, 2), nullable=False)
    total_amount    = db.Column(DECIMAL(12, 2), nullable=False)
    platform_type   = db.Column(String(50), nullable=True)
    app_type        = db.Column(String(50), nullable=True)

    def __init__(self, order_id, user_no, order_status, 
                order_amount, tax_amount, total_amount, 
                platform_type=None, app_type=None):
        self.order_id = order_id
        self.user_no = user_no
        self.order_status = order_status
        self.order_amount = order_amount
        self.tax_amount = tax_amount
        self.total_amount = total_amount
        self.platform_type = platform_type
        self.app_type = app_type
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
