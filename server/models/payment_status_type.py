"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class PaymentStatusType(db.Model):
    __tablename__ = 'mtt_md_payment_status_types'

    payment_status              = db.Column(SMALLINT, primary_key=True)
    payment_status_name         = db.Column(String(50), nullable=False)
    created_at                  = db.Column(DateTime, nullable=False)
    updated_at                  = db.Column(DateTime, nullable=False)
    payment_status_description  = db.Column(String(250), nullable=True)

    def __init__(self, payment_status, payment_status_name, payment_status_description):
        self.payment_status = payment_status
        self.payment_status_name = payment_status_name
        self.payment_status_description = payment_status_description
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
