"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Order(Base):
    __tablename__ = "mtt_tx_orders"

    order_no        = Column(INTEGER, primary_key=True)
    order_id        = Column(String(50), nullable=False, unique=True)
    user_no         = Column(INTEGER, nullable=False, Index=True)
    order_status    = Column(SMALLINT, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)
    order_amount    = Column(DECIMAL(12, 2), nullable=False)
    tax_amount      = Column(DECIMAL(12, 2), nullable=False)
    total_amount    = Column(DECIMAL(12, 2), nullable=False)
    platform_type   = Column(String(50), nullable=True)
    app_type        = Column(String(50), nullable=True)

    def __init__(self, order_id, user_no, order_status, 
                order_amount, tax_amount, total_amount, 
                platform_type, app_type):
        self.order_id = order_id
        self.user_no = user_no
        self.order_status = order_status
        self.order_amount = order_amount
        self.tax_amount = tax_amount
        self.total_amount = total_amount
        self.platform_type = platform_type
        self.app_type = app_type
