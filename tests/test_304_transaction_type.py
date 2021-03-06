import urllib.request
import json
import pytest
# import uuid
# import decimal

from server.models.transaction_type import TransactionType


base_url = "http://localhost:5000/v1/transaction_types"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class TestTransactionType(object):

    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "transaction_types" in data

    def test_create_200(self):
        data = '{ \
                    "trx_type": 999, \
                    "trx_type_name": "TEST TRANSACTION TYPE", \
                    "io_type": 1, \
                    "parent_trx_type": null, \
                    "trx_type_description": "TEST TRANSACTION TYPE DESCRIPTION" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "transaction_type" in data

    def test_get_200(self):
        res = urllib.request.urlopen(base_url + '/999')
        data = str(res.read())

        assert "200" in data
        assert "transaction_type" in data

    def test_update_200(self):
        data = '{ \
                    "trx_type_name": "TEST TRANSACTION TYPE", \
                    "io_type": 1, \
                    "parent_trx_type": null, \
                    "trx_type_description": "TEST TRANSACTION TYPE DESCRIPTION" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/999', 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "transaction_type" in data

    def test_delete_200(self):
        req = urllib.request.Request(base_url + '/999',
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data

