"""
"""

from sqlalchemy import Column, String, DECIMAL, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class OrderPayment(db.Model):
    __tablename__ = "mtt_tx_order_payments"

    paymet_no           = db.Column(INTEGER, primary_key=True, autoincrement=True)
    order_no            = db.Column(INTEGER, nullable=False)
    method_code         = db.Column(String(10), nullable=False)
    payment_status      = db.Column(SMALLINT, nullable=False)
    created_at          = db.Column(DateTime, nullable=False)
    updated_at          = db.Column(DateTime, nullable=False)
    payment_currency    = db.Column(String(3), nullable=False)
    payment_amount      = db.Column(DECIMAL(12, 2), nullable=False)
    trx_id              = db.Column(String(50), nullable=True)
    ref_id              = db.Column(String(50), nullable=True)
    approval_code       = db.Column(String(50), nullable=True)
    reason_code         = db.Column(String(50), nullable=True)
    avs_result          = db.Column(String(50), nullable=True)
    cvv_result          = db.Column(String(50), nullable=True)

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
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()
