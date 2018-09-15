"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ProductPriceHistory(Base):
    __tablename__ = 'mtt_md_product_price_history'

    change_no       = Column(INTEGER, primary_key=True, autoincrement=True)
    product_no      = Column(INTEGER, nullable=False)
    account_type    = Column(SMALLINT, nullable=False)
    updated_at      = Column(DateTime, nullable=False)
    unit_price      = Column(DECIMAL(12, 2), nullable=False)

    def __init__(self, product_no, account_type, unit_price):
        self.product_no = product_no
        self.account_type = account_type
        self.unit_price = unit_price
