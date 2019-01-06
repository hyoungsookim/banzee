"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class Cart(db.Model):
    __tablename__ = 'mtt_tx_carts'

    user_no             = db.Column(INTEGER, primary_key=True)
    product_no          = db.Column(INTEGER, primary_key=True)
    product_quantity    = db.Column(INTEGER, nullable=False)
    created_at          = db.Column(DateTime, nullable=False)
    updated_at          = db.Column(DateTime, nullable=False)

    def __init__(self, user_no, product_no, product_quantity):
        self.user_no = user_no
        self.product_no = product_no
        self.product_quantity = product_quantity
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()

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
