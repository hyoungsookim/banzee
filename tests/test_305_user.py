import pytest
# import uuid
# import decimal

from server.models.user import User
from server.models.user_account import UserAccount
from server.controller.user_controller import UserController


class TestUser(object):
    info = User(user_id="USER_ID_TEST", 
                partner_id="VINCLE",
                user_status=200,
                user_type=1,
                user_level=100,
                first_name="TEST_FIRST_NAME",
                last_name="TEST_LAST_NAME")

    account_info = UserAccount()

    controller = UserController()

    def test_get_list(self):
        assert self.controller.get_list(q=None, offset=0, fetch=20) is not None

    def test_get(self):
        assert self.controller.get("TEST_USER_ID") is not None

    def test_create_200_success(self):
        #global account_no

        assert self.controller.create(self.info) is not None
        #account_no = self.accountData.open(self.info.user_id).account_no
        #assert account_no > 0

    def test_update_200_success(self):
        self.info.user_status = 0
        self.info.user_type = 2
        self.info.user_level = 101
        self.info.first_name = "FIRST_NAME_TEST"
        self.info.last_name = "LAST_NAME_TEST"
        assert self.controller.update(self.info) is not None

    def test_get_accounts_200_success(self):
        assert self.controller.get_account_list(self.info.user_id) is not None

    def test_open_account_200_success(self):
        self.account_info.account_id = self.controller.open_account(self.info.user_id, 410) # 410 - KRW
        assert self.account_info.account_id is not None

    def test_get_account_200_success(self):
        user_id = self.info.user_id
        account_id = self.account_info.account_id
        assert self.controller.get_account(user_id, account_id) is not None

    def test_close_account_200_success(self):
        user_id = self.info.user_id
        account_id = self.account_info.account_id
        assert self.controller.close_account(user_id, account_id) == True

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
        assert self.controller.delete('USER_ID_TEST') == True


