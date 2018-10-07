import urllib.request
import json
import pytest
# import uuid
# import decimal

from server.models.product import Product
#from server.controller.product_controller import ProductController


base_url = "http://localhost:5000/v1/products"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class ProductInfo:
    product_id = None


class TestProduct(object):
    #info = Product(product_id="PRODUCT_ID_TEST", 
    #               product_status=200,
    #               product_name="PRODUCT_NAME_TEST",
    #               product_type="SERVICE",
    #               product_description=None)

    #controller = ProductController()
    info = ProductInfo()

    def test_create_200(self):
        data = '{ \
                    "product_name": "TEST PRODUCT NAME", \
                    "product_status": 200, \
                    "product_type": "ITEM", \
                    "product_description": "TEST PRODUCT DESCRIPTION" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "product" in data

        self.info.product_id = json.loads(data).get('product').get('product_id')
        
    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "products" in data

    def test_get_200(self):
        res = urllib.request.urlopen(base_url + '/' + self.info.product_id)
        data = str(res.read())

        assert "200" in data
        assert "product" in data

    def test_update_200(self):
        data = '{ \
                    "product_name": "TEST PRODUCT NAME", \
                    "product_status": 200, \
                    "product_type": "ITEM", \
                    "product_description": "TEST PRODUCT DESCRIPTION" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/' + self.info.product_id, 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "product_id" in data

    def test_delete_200(self):
        req = urllib.request.Request(base_url + '/' + self.info.product_id,
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data

    

