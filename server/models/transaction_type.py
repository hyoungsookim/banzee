"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class TransactionType(Base):
    __tablename__ = 'mtt_tx_transaction_types'
