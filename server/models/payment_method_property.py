"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class PaymentMethodProperty(db.Model):
    __tablename__ = 'mtt_md_payment_method_properties'

    method_code     = db.Column(String(10), primary_key=True)
    property_type   = db.Column(SMALLINT, primary_key=True)
    property_value  = db.Column(String(250), nullable=True)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)

    def __init__(self, method_code, property_type, property_value=None):
        self.method_code = method_code
        self.property_type = property_type
        self.property_value = property_value
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
