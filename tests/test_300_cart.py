import urllib.request
import json
import pytest
# import uuid
# import decimal

#from server.models.partner import Partner


base_url = "http://localhost:5000/v1/users/11e9-11a6-a983d12c-a44b-54ee75488a22/cart"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class TestCart(object):

    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        #assert "products" in data


    def test_add_200(self):
        data = '{ \
                    "product_id": "TEST_PRODUCT_A" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        #partner_id = json.loads(data).get('partner').get('partner_id')

        assert "200" in data
        assert "products" in data


    def test_update_200(self):
        data = '{ \
                    "product_quantity": 2 \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/TEST_PRODUCT_A', 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "products" in data


    def test_delete_200(self):
        req = urllib.request.Request(base_url + '/TEST_PRODUCT_A',
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data

