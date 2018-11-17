import urllib.request
import json
import pytest
# import uuid
# import decimal

from server.models.transaction import Transaction


base_url = "http://localhost:5000/v1/transactions"
headers = {'Content-Type': 'application/json;charset=UTF-8'}


class Transaction(object):
    trx_id = None


class TestTransaction(object):
    transacion_info = Transaction()

    def test_get_list_200(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "transactions" in data


    def test_deposit_200(self):
        data = '{ \
                    "sender_id": "NEWUSERID001", \
                    "recipient_account_id": "c73bb94c-d82a-11e8-863b-024607912c40", \
                    "deposit_type": 1200, \
                    "deposit_amount": 10.30, \
                    "reason": "test reason" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "transaction" in data

        self.transacion_info.trx_id = json.loads(data).get('transaction').get('trx_id')


    def test_withdraw_200(self):
        data = '{ \
                    "account_id": "c73bb94c-d82a-11e8-863b-024607912c40", \
                    "withdrawal_amount": 1.03, \
                    "source_transaction_id": "TEST_SOURCE_TRX_ID", \
                    "reason": "test reason" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data


    def test_withdraw_406(self):
        data = '{ \
                    "account_id": "c73bb94c-d82a-11e8-863b-024607912c40", \
                    "withdrawal_amount": 1000.03, \
                    "source_transaction_id": "TEST_SOURCE_TRX_ID", \
                    "reason": "test reason" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "406" in data


    def test_get_200(self):
        res = urllib.request.urlopen(base_url + '/' + self.transacion_info.trx_id)
        data = str(res.read())

        assert "200" in data
        assert "transaction" in data

