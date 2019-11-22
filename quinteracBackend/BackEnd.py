import logging
import os

from quinterac.Account import *
from quinterac.Formatter import TransactionCode

pathToDir = os.path.dirname(os.path.abspath(__file__))
pathToFront = pathToDir.replace("quinteracBackend", "quinterac")

class BackEnd:

    # take transaction summary file from frontend session and update Master Accounts list
    def __init__(self, masterAccountsFileName, mergedTransactionFileName):
        self.masterFileName = os.path.join(pathToDir, masterAccountsFileName)
        self.masterAccountsFile = open(self.masterFileName, 'r')
        # Current list of accounts from master account file
        self.accounts = self.loadAccounts()

        self.mergedTransactionFileName = os.path.join(pathToFront, mergedTransactionFileName)
        self.mergedTransactionFile = open(self.mergedTransactionFileName, "r+")
        self.update(self.mergedTransactionFile)

    def update(self, transactionSummaryFile):
        for line in transactionSummaryFile:
            trans = line.split()
            transCode = trans[0]

            if transCode == TransactionCode.DEL.name:
                self.deleteAccount(trans[3], trans[4])
            elif transCode == TransactionCode.NEW.name:
                self.createAccount(trans[3], trans[4])
            elif transCode == TransactionCode.DEP.name:
                self.depositAccount(trans[3], int(trans[2]))
            elif transCode == TransactionCode.WDR.name:
                self.withdrawAccount(trans[3], int(trans[2]))
            elif transCode == TransactionCode.XFR.name:
                # withdraw from account
                self.withdrawAccount(trans[3], int(trans[2]))
                # deposit into other account
                self.depositAccount(trans[1], int(trans[2]))
            elif transCode == TransactionCode.EOS.name:
                print("Done reading")
            else:
                print("Error reading transactions")

        self.accounts.sort(key=lambda x: x.accountNumber, reverse=True)
        self.writeMaster()

    def writeMaster(self):
        self.masterAccountsFile = open(self.masterFileName, "w")

        for account in self.accounts:
            curLine = self.formatLine(account.accountNumber, account.balance, account.accountName)
            self.masterAccountsFile.write(curLine)

        self.masterAccountsFile.close()
        self.generateNewAccountsFile()

    def generateNewAccountsFile(self):
        validAccountsListFileName = os.path.join(pathToFront, "validAccountsListFile.txt")
        accountsFile = open(validAccountsListFileName, "w")
        for account in self.accounts:
            accountsFile.write(account.accountNumber + "\n")

        accountsFile.write("0000000\n")
        accountsFile.close()

        open(self.mergedTransactionFileName, "w").close()

    def depositAccount(self, number, amount):
        if len(self.accounts) == 0:
            logging.error(Error.noAccounts.value)

        for account in self.accounts:
            if account.accountNumber == number:
                account.updateBalance(amount)
                break

    def withdrawAccount(self, number, amount):
        if len(self.accounts) == 0:
            logging.error(Error.noAccounts.value)

        for account in self.accounts:
            if account.accountNumber == number:
                if account.updateBalance(-amount) == Error.negativeBalance:
                    logging.error(Error.negativeBalance.value + "- for account: " + account.accountNumber)
                break

    def createAccount(self, number, name):
        accountExists = False
        for account in self.accounts:
            if account.accountNumber == number:
                accountExists = True
                logging.error(Error.accountExists.value + "- for account: " + account.accountNumber)
                break

        if not accountExists:
            self.accounts.append(Account(number, name, True))

    def deleteAccount(self, number, name):
        acc = None

        for account in self.accounts:
            if account.accountName == name and account.accountNumber == number:
                if account.balance != 0:
                    logging.error(Error.accountHasBalance.value + "- for account: " + account.accountNumber)
                else:
                    acc = account
                break

        if acc:
            self.accounts.remove(acc)

    """ Load current accounts from old master accounts file."""
    def loadAccounts(self):
        tempAccountsList = []
        for line in self.masterAccountsFile:
            accInfo = line.split()
            account = Account(accInfo[0], accInfo[2], False, accInfo[1])

            tempAccountsList.append(account)

        return tempAccountsList

    @staticmethod
    def formatLine(accountNumber, balance, accountName):
        return "{} {} {}\n".format(accountNumber, balance, accountName)

