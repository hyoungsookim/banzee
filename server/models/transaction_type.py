"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class TransactionType(db.Model):
    __tablename__ = 'mtt_tx_transaction_types'

    trx_type                = db.Column(SMALLINT, primary_key=True)
    trx_type_name           = db.Column(String(50), nullable=False)
    created_at              = db.Column(DateTime, nullable=False)
    updated_at              = db.Column(DateTime, nullable=False)
    trx_type_description    = db.Column(String(250), nullable=True)

    def __init__(self, trx_type, trx_type_name, trx_type_description=None):
        self.trx_type = trx_type
        self.trx_type_name = trx_type_name
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
        self.trx_type_description = trx_type_description
