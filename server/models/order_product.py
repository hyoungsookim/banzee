"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class OrderProduct(db.Model):
    __tablename__ = "mtt_tx_order_products"

    order_no                = db.Column(INTEGER, primary_key=True)
    product_no              = db.Column(INTEGER, primary_key=True)
    account_type            = db.Column(SMALLINT, primary_key=True)
    unit_price              = db.Column(DECIMAL(12, 2), nullable=False)
    order_quantity          = db.Column(INTEGER, nullable=False)
    total_product_amount    = db.Column(DECIMAL(12, 2), nullable=False)

    def __init__(self, order_no, product_no, account_type, 
                unit_price, order_quantity, total_product_amount):
        self.order_no = order_no
        self.product_no = product_no
        self.account_type = account_type
        self.unit_price = unit_price
        self.order_quantity = order_quantity
        self.total_product_amount = total_product_amount

    def to_dict(self, output_attrs=None):
        """Returns the model attributes as a dict
        :output_attrs: list that includes attributes to convert
        """
        if output_attrs:
            return {col.name: getattr(self, col.name) 
                        for col in self.__table__.columns 
                            if col.name in output_attrs}

        return {col.name: getattr(self, col.name) 
                    for col in self.__table__.columns}
