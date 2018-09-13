"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime, Text, Index
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OrderPaymentLog(Base):
    __tablename__ = "mtt_tx_order_payment_logs"

    log_no          = Column(INTEGER, primary_key=True)
    payment_no      = Column(INTEGER, nullable=False, Index=True)
    payment_status  = Column(SMALLINT, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    remote_ip       = Column(String(50), nullable=True)
    log_text        = Column(Text, nullable=True)

    def __init__(self, order_no, method_code, 
                payment_status, remote_ip=None, log_text=None):
        self.order_no = order_no
        self.method_code = method_code
        self.payment_status = payment_status
        self.remote_ip = remote_ip
        self.log_text = log_text
