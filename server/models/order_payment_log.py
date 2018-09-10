"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric, SmallInteger, DateTime, Text

Base = declarative_base()


class OrderPaymentLog(Base):
    __tablename__ = "mtt_tx_order_payment_logs"

    log_no          = Column(Integer, primary_key=True)
    order_no        = Column(Integer, nullable=False)
    method_code     = Column(String(10), nullable=False)
    payment_status  = Column(SmallInteger, nullable=False)
    created_at      = Column(DateTime, nullable=False)
    remote_ip       = Column(String(50), nullable=True)
    log_text        = Column(Text, nullable=True)

    def __init__(self, order_no, method_code, 
                payment_status, remote_ip, log_text):
        self.order_no = order_no
        self.method_code = method_code
        self.payment_status = payment_status
        self.remote_ip = remote_ip
        self.log_text = log_text
