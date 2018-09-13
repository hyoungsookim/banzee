"""
"""

from sqlalchemy import Column, String, DateTime, DECIMAL
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Transaction(Base):
    __tablename__ = 'mtt_tx_transactions'

    trx_no      = Column(INTEGER(11), primary_key=True)
    account_no  = Column(INTEGER(11), nullable=False, index=True)
    trx_type    = Column(SMALLINT(6), nullable=False)
    trx_status  = Column(SMALLINT(6), nullable=False)
    created_at  = Column(DateTime, nullable=False)
    updated_at  = Column(DateTime, nullable=False)
    trx_amount  = Column(DECIMAL(12, 2), nullable=False)
    trx_note    = Column(String(50), nullable=True)

    def __init__(self, account_no, trx_type, trx_status, trx_amount, trx_note=None):
        self.account_no = account_no
        self.trx_type = trx_type
        self.trx_status = trx_status
        self.trx_amount = trx_amount
        self.trx_note = trx_note
