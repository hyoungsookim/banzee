"""
"""

from datetime import datetime

from server.utils import *
from server.models.order import Order
from server.models.order_product import OrderProduct
from server.models.order_payment import OrderPayment
from server.models.payment_method import PaymentMethod
from server.models.product import Product
from server.models.user import User
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db


class OrderData(DataBase):
    """
    Order data class for accssing database
    """
    def __init__(self):
        pass


    def get_list_by_user_id(self, user_id=None, q=None, offset=0, fetch=20):
        if user_id is not None:
            user_no = self._findUserNo(user_id)
            _rows = db.session.query(Order).\
                        filter(Order.user_no == user_no).all()
        else:
            _rows = db.session.query(Order).all()
        rows = [row.to_dict() for row in _rows]
        return rows


    def get(self, order_id):
        row = db.session.query(Order).\
                filter(Order.order_id == order_id).one_or_none()
        return row.to_dict()


    def create(self, user_id, platform_type=None, app_type=None):
        params = { 
            "user_id": user_id, 
            "platform_type": platform_type,
            "app_type": app_type 
        }
        
        try:
            db.session.execute("call mtp_tx_create_order(:user_id, :platform_type, :app_type, @order_no, @order_id, @error_code)", params)
            res = db.session.execute("select @order_no, @order_id, @error_code").fetchone()
            
            error_code = int(res[2])
            if (error_code != 0):
                raise BanzeeException(error_code)

            order_no = res[0]           # int object doesn't have decode method
            order_id = res[1].decode()
            
            db.session.commit()

        except:
            db.session.rollback()
            raise

        return order_id


    def change_status(self, order_id, order_status):
        try:
            db.session.query(Order).\
                filter(Order.order_id == order_id).\
                update({
                    "order_status": order_status,
                    "updated_at": get_current_datetime_str()
                })            
        except:
            raise
    

    def cancel(self, order_id):
        try:
            self.change_status(order_id, -1)
            db.session.commit()
        except:
            db.session.rollback()
            raise


    def get_products(self, order_id):
        _rows = None
        try:
            order_no = self._findOrderNo(order_id)
            _rows = db.session.\
                        query(OrderProduct).\
                        join(Product, Product.product_no == OrderProduct.product_no).\
                        filter(OrderProduct.order_no == order_no).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]
        return rows


    def get_payments(self, order_id):
        _rows = None
        try:
            order_no = self._findOrderNo(order_id)
            _rows = db.session.\
                        query(OrderPayment).\
                        filter(OrderPayment.order_no == order_no).all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]
        return rows


    def create_payment(self, order_id, method_code, payment_currency, payment_amount):
        params = { 
            "order_id": order_id,
            "method_code": method_code, 
            #"payment_status": payment_status, 
            "payment_currency": payment_currency,
            "payment_amount": payment_amount
        }

        try:
            db.session.execute("call mtp_tx_create_order_payment(:order_id, :method_code, :payment_currency, :payment_amount, @payment_no, @error_code)", params)
            res = db.session.execute("select @payment_no, @error_code").fetchone()

            error_code = int(res[1])
            if (error_code != 0):
                raise BanzeeException(error_code)

            payment_no = int(res[0])

            db.session.commit()

        except:
            db.session.rollback()
            raise

        return payment_no


    def _findOrderNo(self, order_id):
        order_no = None

        row = db.session.query(Order.order_no).\
                filter(Order.order_id == order_id).one_or_none()

        if not row:
            raise ResourceNotFoundException
        
        return row.order_no


    def _findUserNo(self, user_id):
        user_no = None

        row = db.session.query(User.user_no).\
                filter(User.user_id == user_id).one_or_none()

        if not row:
            raise ResourceNotFoundException
        
        return row.user_no
