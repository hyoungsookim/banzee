"""
"""

from sqlalchemy import Column, String, DateTime, DECIMAL
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class Transaction(db.Model):
    __tablename__ = 'mtt_tx_transactions'

    trx_no      = db.Column(INTEGER(11), primary_key=True, autoincrement=True)
    trx_id      = db.Column(String(50), nullable=False, index=True)
    account_no  = db.Column(INTEGER(11), nullable=False, index=True)
    trx_type    = db.Column(SMALLINT(6), nullable=False)
    trx_status  = db.Column(SMALLINT(6), nullable=False)
    created_at  = db.Column(DateTime, nullable=False)
    updated_at  = db.Column(DateTime, nullable=False)
    trx_amount  = db.Column(DECIMAL(12, 2), nullable=False)
    trx_note    = db.Column(String(50), nullable=True)

    def __init__(self, trx_id, account_no, trx_type, trx_status, trx_amount, trx_note=None):
        self.trx_id = trx_id
        self.account_no = account_no
        self.trx_type = trx_type
        self.trx_status = trx_status
        self.trx_amount = trx_amount
        self.trx_note = trx_note
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
