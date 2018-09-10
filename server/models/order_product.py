"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric, SmallInteger, DateTime

Base = declarative_base()


class OrderProduct(Base):
    __tablename__ = "mtt_tx_order_products"

    order_no                = Column(Integer, primary_key=True)
    product_no              = Column(Integer, primary_key=True)
    account_type            = Column(SmallInteger, primary_key=True)
    unit_price              = Column(Numeric(12, 2), nullable=False)
    order_quantity          = Column(Integer, nullable=False)
    total_product_amount    = Column(Numeric(12, 2), nullable=False)

    def __init__(self, order_no, product_no, account_type, 
                unit_price, order_quantity, total_product_amount):
        self.order_no = order_no
        self.product_no = product_no
        self.account_type = account_type
        self.unit_price = unit_price
        self.order_quantity = order_quantity
        self.total_product_amount = total_product_amount
