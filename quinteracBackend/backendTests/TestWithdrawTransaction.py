import pytest
import os
from quinterac.Account import *

pathToDir = os.path.dirname(os.path.abspath(__file__))
pathToTests = pathToDir.replace("backendTests", "backendTests/resourceFiles")

class TestWithdraw:

    @pytest.fixture
    def accounts(self):
        masterFileName = os.path.join(pathToTests, "testMasterAccountsFile.txt")
        masterAccountsFile = open(masterFileName, 'r')
        accounts = loadAccounts(masterAccountsFile)
        masterAccountsFile.close()
        return accounts

    @pytest.fixture
    def noAccounts(self):
        masterFileName = os.path.join(pathToTests, "testEmptyMasterAccountsFile.txt")
        masterAccountsFile = open(masterFileName, 'r')
        accounts = loadAccounts(masterAccountsFile)
        masterAccountsFile.close()
        return accounts

    @pytest.fixture
    def transactions(self):
        transactionSummaryFileName = os.path.join(pathToTests, "testWithdrawTransactionSummaryFile.txt")
        transactionSummaryFile = open(transactionSummaryFileName, 'r')
        lines = transactionSummaryFile.readlines()
        transactionSummaryFile.close()
        return lines

    def testPathOneWithdraw(self, noAccounts):
        assert noAccounts == []

    def testPathTwoWithdraw(self, accounts, transactions):
        transaction = transactions[0].split()
        transCode = transaction[0]
        number = transaction[3]
        amount = transaction[2]

        if accounts[0].accountNumber == number and transCode == 'WDR':
            newAmount = int(accounts[0].balance) - int(amount)
            assert newAmount >= 0

    def testPathThreeWithdraw(self, accounts, transactions):
        transaction = transactions[1].split()
        transCode = transaction[0]
        number = transaction[3]
        amount = transaction[2]
        if accounts[0].accountNumber == number and transCode == 'WDR':
            newAmount = int(accounts[0].balance) - int(amount)
            assert newAmount < 0

    def testPathFourWithdraw(self, accounts, transactions):
        transaction = transactions[2].split()
        transCode = transaction[0]
        number = transaction[3]
        amount = transaction[2]
        for account in accounts:
            if account.accountNumber == number and transCode == 'WDR':
                newAmount = int(account.balance) - int(amount)
                assert newAmount >= 0

    def testPathFiveAccountWithdraw(self, accounts, transactions):
        transaction = transactions[3].split()
        transCode = transaction[0]
        number = transaction[3]
        amount = transaction[2]
        for account in accounts:
            if account.accountNumber == number and transCode == 'WDR':
                newAmount = int(account.balance) - int(amount)
                assert newAmount < 0


def loadAccounts(masterAccountsFile):
    tempAccountsList = []
    for line in masterAccountsFile:
        accInfo = line.split()
        account = Account(accInfo[0], accInfo[2], False, accInfo[1])

        tempAccountsList.append(account)

    return tempAccountsList




