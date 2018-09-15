"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class OrderPayment(Base):
    __tablename__ = "mtt_tx_order_payments"

    paymet_no           = Column(INTEGER, primary_key=True, autoincrement=True)
    order_no            = Column(INTEGER, nullable=False)
    method_code         = Column(String(10), nullable=False)
    payment_status      = Column(SMALLINT, nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    payment_currency    = Column(String(3), nullable=False)
    payment_amount      = Column(DECIMAL(12, 2), nullable=False)
    trx_id              = Column(String(50), nullable=True)
    ref_id              = Column(String(50), nullable=True)
    approval_code       = Column(String(50), nullable=True)
    reason_code         = Column(String(50), nullable=True)
    avs_result          = Column(String(50), nullable=True)
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
