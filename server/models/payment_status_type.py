"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class PaymentStatusType(Base):
    __tablename__ = 'mtt_md_payment_status_types'