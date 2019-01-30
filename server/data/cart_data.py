"""
"""

from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

from server.utils import *
from server.models.cart import Cart
from server.models.product import Product
from server.models.product_price import ProductPrice
from server.models.user import User
from server.data import DataBase
from server.data.helper import ConnectionHelper
from server.db_factory import db
from server.exceptions import *


class CartData(DataBase):
    """
    Cart data class for accssing database
    """
    def __init__(self):
        pass


    def get_list(self, user_id):
        _rows = None
        try:
            # account_type 840 is Cash(USD), 0 is reward
            _rows = db.session.\
                        query(Cart.product_quantity, Product.product_id, Product.product_name, ProductPrice.unit_price).\
                        join(User, Cart.user_no == User.user_no).\
                        join(Product, Product.product_no == Cart.product_no).\
                        join(ProductPrice, ProductPrice.product_no == Product.product_no).\
                        filter(User.user_id == user_id).\
                        filter(ProductPrice.account_type == 840).\
                        all()

        except OperationalError as ex:
            raise InternalServerError(ex)

        rows = [row.to_dict() for row in _rows]

        return rows

    
    def add(self, user_id, product_id):
        """
        Add a product to cart
        """
        return_value = False

        try:
            sql_stmt = text(
                        "insert into mtt_tx_carts " + \
                            "(user_no, product_no, product_quantity, created_at, updated_at) " + \
                        "select user_no, product_no, 1, now(), now() " + \
                        "from mtt_uw_users u " + \
                        "join mtt_md_products p " + \
                        "where u.user_id = :user_id " + \
                        "and p.product_id = :product_id " + \
                        "on duplicate key update product_quantity = product_quantity + 1;")
            
            sql_stmt = sql_stmt.bindparams(user_id=user_id, product_id=product_id)

            db.session.execute(sql_stmt)
            db.session.commit()

            return_value = True

        except OperationalError as ex:
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return return_value
    

    def update_quantity(self, user_id, product_id, product_quantity=1):
        """
        Update quantity of a selected product in cart
        """
        return_value = False

        try:
            product_no = self._findProductNo(product_id)
            user_no = self._findUserNo(user_id)

            db.session.\
                query(Cart).\
                filter(Cart.user_no == user_no).\
                filter(Cart.product_no == product_no).\
                update({
                    "product_quantity": product_quantity,
                    "updated_at": get_current_datetime_str()
                })

            db.session.commit()
            return_value = True

        except OperationalError as ex:
            print(ex)
            raise InternalServerError(ex)

        except:
            db.session.rollback()
            raise

        return return_value
    

    def delete(self, user_id, product_id):
        """
        Delete a selected product in cart
        """
        return_value = False

        try:
            product_no = self._findProductNo(product_id)
            user_no = self._findUserNo(user_id)

            db.session.query(Cart).\
                filter(Cart.user_no == user_no).\
                filter(Cart.product_no == product_no).\
                delete()

            db.session.commit()
            return_value = True

        except:
            db.session.rollback()

        return return_value


    def clear(self, user_id):
        """
        Delete all product in cart of a user
        """
        return_value = False

        try:
            user_no = self._findUserNo(user_id)

            db.session.query(Cart).\
                filter(Cart.product_no == product_no).\
                delete()

            db.session.commit()
            return_value = True

        except:
            db.session.rollback()

        return return_value


    def _findUserNo(self, user_id):
        user_no = None

        row = db.session.query(User.user_no).\
                filter(User.user_id == user_id).one_or_none()

        if not row:
            raise ResourceNotFoundException
        
        return row.user_no
    

    def _findProductNo(self, product_id):
        product_no = None

        row = db.session.query(Product.product_no).\
                filter(Product.product_id == product_id).one_or_none()

        if not row:
            raise ResourceNotFoundException
        
        return row.product_no
