from quinterac.Errors import *


class Account:

    def __init__(self, accountNumber, accountName, isNewAccount=None, balance=0):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = int(balance)
        self.totalDeposited = 0
        self.totalWithdrawn = 0
        self.totalTransferred = 0
        self.isNewAccount = isNewAccount

    def deposit(self, amount, isAtm):
        if self.isNewAccount:
            return Error.newAccount

        if self.totalDeposited + int(amount) <= DailyLimits.getDepositLimit(isAtm):
            self.totalDeposited += int(amount)
            self.updateBalance(int(amount))
            return True

        return Error.overDepositLimit

    def withdraw(self, amount, isAtm):
        if self.isNewAccount:
            return Error.newAccount

        if self.totalWithdrawn + int(amount) <= DailyLimits.getWithdrawalLimit(isAtm):
            self.totalWithdrawn += int(amount)
            self.updateBalance(-int(amount))
            return True

        return Error.overWithdrawalLimit

    def transfer(self, amount, isAtm):
        if self.isNewAccount:
            return Error.newAccount

        if self.totalTransferred + int(amount) <= DailyLimits.getTransferLimit(isAtm):
            self.totalTransferred += int(amount)
            self.updateBalance(-int(amount))
            return True

        return Error.overTransferLimit

    def updateBalance(self, newValue):
        if (int(self.balance) + int(newValue)) < 0:
            return Error.negativeBalance

        self.balance += int(newValue)
        return None

    def __lt__(self, other):
        return self.accountNumber < other.accountNumber

    def __gt__(self, other):
        return self.accountNumber > other.accountNumber

class DailyLimits:
    accounts = []

    @staticmethod
    def loadAccounts(fileName):
        try:
            accountsFile = open(fileName, 'r')
            if accountsFile:
                lines = accountsFile.readlines()
                for line in lines:
                    line = line.strip()
                    if line != "0000000":
                        account = Account(line, "", False)
                        DailyLimits.accounts.append(account)
            else:
                accountsFile = open(fileName, 'w+')
                accountsFile.close()

        except FileNotFoundError:
            DailyLimits.accounts = []

    @staticmethod
    def addAccount(account):

        DailyLimits.accounts.append(account)

    @staticmethod
    def getDepositLimit(isAtm):
        return 500000 if isAtm else 99999999

    @staticmethod
    def getWithdrawalLimit(isAtm):
        return 500000 if isAtm else 99999999

    @staticmethod
    def getTransferLimit(isAtm):
        return 1000000 if isAtm else 99999999

    @staticmethod
    def getAccountFor(accountNumber):
        for account in DailyLimits.accounts:
            if account.accountNumber == accountNumber:
                return account

        return None
