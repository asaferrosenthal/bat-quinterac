import pytest
import os
from quinterac.Account import *

pathToDir = os.path.dirname(os.path.abspath(__file__))
pathToTests = pathToDir.replace("backendTests", "backendTests/resourceFiles")

class TestCreateAccount:

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

    def testDecisionOne(self, accounts, transactions):
        transaction = transactions[4].split()
        number = transaction[3]
        accountExists = False
        for account in accounts:
            if account.accountNumber == number:
                accountExists = True
                break
        assert not accountExists

    def testDecisionTwo(self, accounts, transactions):
        transaction = transactions[5].split()
        number = transaction[3]
        accountExists = False
        for account in accounts:
            if account.accountNumber == number:
                accountExists = True
                break
        assert accountExists

    def testDecisionThree(self, noAccounts):
        assert noAccounts == []















def loadAccounts(masterAccountsFile):
    tempAccountsList = []
    for line in masterAccountsFile:
        accInfo = line.split()
        account = Account(accInfo[0], accInfo[2], False, accInfo[1])

        tempAccountsList.append(account)

    return tempAccountsList


