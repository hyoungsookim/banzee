"""
"""

from sqlalchemy import Column, String , DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TEXT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class PaymentMethodResponseType(db.Model):
    __tablename__ = 'mtt_md_payment_method_response_types'

    method_code         = db.Column(String(10), primary_key=True)
    paymenet_response   = db.Column(String(50), primary_key=True)
    payment_status      = db.Column(SMALLINT, primary_key=True)
    created_at          = db.Column(DateTime, nullable=False)
    updated_at          = db.Column(DateTime, nullable=False)
    type_description    = db.Column(TEXT, nullable=True)

    def __init__(self, method_code, payment_response, payment_status, type_description=None):
        self.method_code = method_code
        self.paymenet_response = payment_response
        self.payment_status = payment_status
        self.type_description = type_description
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
