"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TransactionType(Base):
    __tablename__ = 'mtt_tx_transaction_types'

    trx_type                = Column(SMALLINT, primary_key=True)
    trx_type_name           = Column(String(50), nullable=False)
    created_at              = Column(DateTime, nullable=False)
    updated_at              = Column(DateTime, nullable=False)
    trx_type_description    = Column(String(250), nullable=True)

    def __init__(self, trx_type, trx_type_name, trx_type_description=None):
        self.trx_type = trx_type
        self.trx_type_name = trx_type_name
        self.trx_type_description = trx_type_description
