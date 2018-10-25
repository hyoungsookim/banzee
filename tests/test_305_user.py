import pytest
# import uuid
# import decimal

from server.models.user import User
from server.models.user_account import UserAccount
from server.data.user_data import UserData
from server.data.user_account_data import UserAccountData

global account_no

class TestUser(object):
    info = User(user_id="USER_ID_TEST", 
                partner_id="VINCLE",
                user_status=200,
                user_type=1,
                user_level=100,
                first_name="TEST_FIRST_NAME",
                last_name="TEST_LAST_NAME")

    data = UserData()
    accountData = UserAccountData()

    def test_get_list(self):
        assert self.data.get_list() is not None

    def test_get(self):
        assert self.data.get("TEST_USER_ID") is not None

    def test_create_200_success(self):
        #global account_no

        assert self.data.create(self.info) is not None
        #account_no = self.accountData.open(self.info.user_id).account_no
        #assert account_no > 0

    def test_update_200_success(self):
        self.info.user_status = 0
        self.info.user_type = 2
        self.info.user_level = 101
        self.info.first_name = "FIRST_NAME_TEST"
        self.info.last_name = "LAST_NAME_TEST"
        assert self.data.update(self.info) is not None

    """
    def test_get_account_200_success(self):
        global account_no
        assert self.accountData.get(account_no, self.info.user_id)

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
        assert self.data.delete('USER_ID_TEST') == True


