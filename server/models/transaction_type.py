"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class TransactionType(Base):
    __tablename__ = 'mtt_tx_transaction_types'

    trx_type                = Column(SmallInteger, primary_key=True)
    trx_type_name           = Column(String(50), nullable=False)
    created_at              = Column(DateTime, nullable=False)
    updated_at              = Column(DateTime, nullable=False)
    trx_type_description    = Column(String(250), nullable=True)

    def __init__(self, trx_type, trx_type_name, trx_type_description):
        self.trx_type = trx_type
        self.trx_type_name = trx_type_name
        self.trx_type_description = trx_type_description
