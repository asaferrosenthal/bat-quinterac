import pytest
from collections import OrderedDict

from package.app.app import App


class TestLogin:

    @pytest.fixture
    def beginFrontend(self):
        a = App("valid-accounts-list-file", "transaction-summary-file")
        return a

    def testIdleLogout(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'logout')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."

    def testIdleCreateAccount(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'create account')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."

    def testIdleDeleteAccount(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'delete account')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."

    def testIdleWithdraw(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'withdraw')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."

    def testIdleDeposit(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'deposit')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."

    def testIdleTransfer(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: 'transfer')
        output = App.login(self)
        assert output == "That is an invalid option. Please try again."


    """
    def testAdditionalLoginAttempt(self, beginFrontend, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda i: '1')
        output = beginFrontend.login(self)
    """





'''
class TestLogout:



    pass


class TestCreateAccount:


    pass


class TestDeleteAccount:


    pass
    
'''