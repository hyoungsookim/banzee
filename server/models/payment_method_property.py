"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class PaymentMethodProperty(Base):
    __tablename__ = 'mtt_md_payment_method_properties'

    method_code     = Column(String(10), primary_key=True)
    property_type   = Column(SmallInteger, primary_key=True)
    property_value  = Column(String(250), nullable=True)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, method_code, property_type, property_value=None):
        self.method_code = method_code
        self.property_type = property_type
        self.property_value = property_value
