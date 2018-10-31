import urllib.request
import json
import pytest
# import uuid
# import decimal

from server.models.user import User
#from server.models.user_account import UserAccount
#from server.controller.user_controller import UserController


base_url = "http://localhost:5000/v1/users"
headers = {'Content-Type': 'application/json;charset=UTF-8'}

class UserAccount(object):
    user_id = None
    account_id = None


class TestUser(object):
    '''
    info = User(user_id="USER_ID_TEST", 
                partner_id="VINCLE",
                user_status=200,
                user_type=1,
                user_level=100,
                first_name="TEST_FIRST_NAME",
                last_name="TEST_LAST_NAME")

    account_info = UserAccount()
    controller = UserController()
    '''
    account_info = UserAccount()

    def test_get_list(self):
        res = urllib.request.urlopen(base_url)
        data = str(res.read())

        assert "200" in data
        assert "users" in data

    def test_get(self):
        res = urllib.request.urlopen(base_url + '/TEST_USER_ID')
        data = str(res.read())

        assert "200" in data
        assert "user" in data

    def test_create_200_success(self):
        data = '{ \
                    "user_id": "TEST_USER_X", \
                    "partner_id": "VINCLE", \
                    "first_name": "Hyoung Soo", \
                    "last_name": "Kim" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "user" in data

    def test_update_200_success(self):
        data = '{ \
                    "user_status": 0, \
                    "user_type": 99, \
                    "user_level": 2, \
                    "first_name": "Bong Hye", \
                    "last_name": "Kim" \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/TEST_USER_X', 
                                    data=data,
                                    headers=headers,
                                    method='PUT')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data
        assert "user_id" in data

    def test_get_accounts_200_success(self):
        res = urllib.request.urlopen(base_url + '/TEST_USER_X/accounts')
        data = str(res.read())

        assert "200" in data
        assert "accounts" in data

    def test_open_account_200_success(self):
        # 410 - KRW
        data = '{ \
                    "user_id": "TEST_USER_X", \
                    "account_type": 410 \
                }'.encode('utf8')

        req = urllib.request.Request(base_url + '/TEST_USER_X/accounts', 
                                    data=data,
                                    headers=headers,
                                    method='POST')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data

        self.account_info.account_id = json.loads(data).get('account').get('account_id')

    def test_get_account_200_success(self):
        account_id = self.account_info.account_id

        res = urllib.request.urlopen(base_url + '/TEST_USER_X/accounts/' + account_id)
        data = str(res.read())

        assert "200" in data
        assert "user" in data

    def test_close_account_200_success(self):
        account_id = self.account_info.account_id

        req = urllib.request.Request(base_url + '/TEST_USER_X/accounts/' + account_id,
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data


    """
    def test_deposit_200_success(self):
        global account_no
        assert self.accountData.deposit(account_no, self.info.user_id, 1000) == True

    def test_withdraw_200_success(self):
        global account_no
        assert self.accountData.withdraw(account_no, self.info.user_id, 300) == True

    def test_change_account_status_200_success(self):
        global account_no
        assert self.accountData.change_status(account_no, self.info.user_id, 0) == True
    """
    def test_delete_200_success(self):
        req = urllib.request.Request(base_url + '/TEST_USER_X',
                                    headers=headers,
                                    method='DELETE')
        res = urllib.request.urlopen(req)
        data = res.read().decode('utf8')

        assert "200" in data


