"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric, SmallInteger, DateTime

Base = declarative_base()


class OrderPayment(Base):
    __tablename__ = "mtt_order_payments"

    order_no            = Column(Integer, primary_key=True)
    method_code         = Column(String(50), primary_key=True)
    payment_status      = Column(SmallInteger, nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    payment_currency    = Column(String(3), nullable=False)
    payment_amount      = Column(Numeric(12, 2), nullable=False)
    trx_id              = Column(String(50), nullable=True)
    ref_id              = Column(String(50), nullable=True)
    approval_code       = Column(String(50), nullable=True)
    reason_code         = Column(String(50), nullable=True)
    cvv_result          = Column(String(50), nullable=True)

    def __init__(self, order_no, method_code, payment_status, 
                payment_currency, payment_amount,
                trx_id, ref_id, approval_code, reason_code, cvv_result):
        self.order_no = order_no
        self.method_code = method_code
        self.payment_status = payment_status
        self.payment_currency = payment_currency
        self.payment_amount = payment_amount
        self.trx_id = trx_id
        self.ref_id = ref_id
        self.approval_code = approval_code
        self.reason_code = reason_code
        self.cvv_result = cvv_result
