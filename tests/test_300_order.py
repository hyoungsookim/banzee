import urllib.request
import json
import pytest
# import uuid
# import decimal

#from server.models.orders import Order
#from server.data.order_data import OrderData


base_url = "http://localhost:5000/v1/orders"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class OrderInfo(object):
    order_id = None


class TestOrder(object):
    info = OrderInfo()
    #data = OrderData()

    def test_create_200_success(self):
        #self.info.order_id = self.data.create(user_id="VINCLE_ADMIN", platform_type="apple", app_type="iphone") 
        #assert self.info.order_id is not None
        data = '{ \
                    "user_id": "VINCLE_ADMIN", \
                    "platform_type": "apple", \
                    "app_type": "iphone" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        self.info.order_id = json.loads(data).get('order').get('order_id')

        assert "200" in data
        assert "order" in data

    def test_get_list_by_user_id(self):
        #assert self.data.get_list_by_user_id(user_id="VINCLE_ADMIN") is not None
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "orders" in data

    def test_get(self):
        #assert self.data.get(self.info.order_id) is not None
        res = urllib.request.urlopen(base_url + '/' + self.info.order_id)
        data = str(res.read())

        assert "200" in data
        assert "order" in data

    
    #def test_get_products(self):
    #    assert self.data.get_products(self.info.order_id) is not None

    
    #def test_get_payments(self):
    #    assert self.data.get_payments(self.info.order_id) is not None

        
    """def test_cancel_200_success(self):
        assert self.data.cancel(self.info.order_id)
    """