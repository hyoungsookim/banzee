"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime, Text, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class OrderPaymentLog(db.Model):
    __tablename__ = "mtt_tx_order_payment_logs"

    log_no          = db.Column(INTEGER, primary_key=True, autoincrement=True)
    payment_no      = db.Column(INTEGER, nullable=False, Index=True)
    payment_status  = db.Column(SMALLINT, nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    remote_ip       = db.Column(String(50), nullable=True)
    log_text        = db.Column(Text, nullable=True)

    def __init__(self, order_no, method_code, 
                payment_status, remote_ip=None, log_text=None):
        self.order_no = order_no
        self.method_code = method_code
        self.payment_status = payment_status
        self.remote_ip = remote_ip
        self.log_text = log_text
        self.created_at = get_current_datetime_str()

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
