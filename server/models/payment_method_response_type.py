"""
"""

from sqlalchemy import Column, String , DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PaymentMethodResponseType(Base):
    __tablename__ = 'mtt_md_payment_method_response_types'

    method_code         = Column(String(10), primary_key=True)
    paymenet_response   = Column(String(50), primary_key=True)
    payment_status      = Column(SMALLINT, primary_key=True)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    type_description    = Column(TEXT, nullable=True)

    def __init__(self, method_code, payment_response, payment_status, type_description=None):
        self.method_code = method_code
        self.paymenet_response = payment_response
        self.payment_status = payment_status
        self.type_description = type_description
