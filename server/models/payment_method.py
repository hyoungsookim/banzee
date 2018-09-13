"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PaymentMethod(Base):
    __tablename__ = 'mtt_md_payment_methods'

    method_code     = Column(String(10), primary_key=True)
    method_status   = Column(SMALLINT, nullable=True)
    method_name     = Column(String(50), nullable=False)
    method_type     = Column(String(10), nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, method_code, method_status, method_name, method_type):
        self.method_code = method_code
        self.method_status = method_status
        self.method_name = method_name
        self.method_type = method_type
