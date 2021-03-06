"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.db_factory import db

#Base = declarative_base()
#metadata = Base.metadata


class TransactionType(db.Model):
    __tablename__ = 'mtt_tx_transaction_types'

    trx_type                = db.Column(SMALLINT, primary_key=True)
    trx_type_name           = db.Column(String(50), nullable=False)
    io_type                 = db.Column(TINYINT, nullable=False)
    parent_trx_type         = db.Column(SMALLINT, nullable=True)
    created_at              = db.Column(DateTime, nullable=False)
    updated_at              = db.Column(DateTime, nullable=False)
    trx_type_description    = db.Column(String(250), nullable=True)

    def __init__(self, trx_type, trx_type_name, io_type, parent_trx_type=None, trx_type_description=None):
        self.trx_type = trx_type
        self.trx_type_name = trx_type_name
        self.io_type = io_type
        self.parent_trx_type = parent_trx_type
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
        self.trx_type_description = trx_type_description

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
