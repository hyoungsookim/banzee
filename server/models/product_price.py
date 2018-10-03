"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class ProductPrice(db.Model):
    __tablename__ = 'mtt_md_product_prices'

    product_no      = db.Column(INTEGER, primary_key=True)
    account_type    = db.Column(SMALLINT, primary_key=True)
    unit_price      = db.Column(DECIMAL(12, 2), nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)

    def __init__(self, product_no, account_type, unit_price):
        self.product_no = product_no
        self.account_type = account_type
        self.unit_price = unit_price
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
