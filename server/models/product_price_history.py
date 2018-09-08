"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric, SmallInteger, DateTime

Base = declarative_base()


class ProductPriceHistory(Base):
    __tablename__ = 'mtt_md_product_price_history'

    change_no       = Column(Integer, primary_key=True)
    product_no      = Column(Integer)
    account_type    = Column(SmallInteger)
    unit_price      = Column(Numeric(12, 2))
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, product_no, account_type, unit_price):
        self.product_no = product_no
        self.account_type = account_type
        self.unit_price = unit_price
