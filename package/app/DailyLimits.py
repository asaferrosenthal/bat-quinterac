import os
curPath = os.path.dirname(os.path.abspath(__file__))


class DailyLimits:
    accounts = []

    @staticmethod
    def loadAccounts(fileName):
        accountsFile = open(fileName, 'r')
 
        lines = accountsFile.readlines()
        for line in lines:
            line = line.strip()
            if line != "0000000":
                account = Account(line, "", False)
                DailyLimits.accounts.append(account)

    @staticmethod
    def addAccount(account):
        DailyLimits.accounts.append(account)

    @staticmethod
    def getDepositLimit(isAtm):
        return 5000 if isAtm else 999999.99

    @staticmethod
    def getWithdrawalLimit(isAtm):
        return 5000 if isAtm else 999999.99

    @staticmethod
    def getTransferLimit(isAtm):
        return 10000 if isAtm else 999999.99

    @staticmethod
    def getAccountFor(accountNumber):
        for account in DailyLimits.accounts:
            if account.accountNumber == accountNumber:
                return account

        return None


class Account:

    def __init__(self, accountNumber, accountName, isNewAccount=None):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.totalDeposited = 0
        self.totalWithdrawn = 0
        self.totalTransferred = 0
        self.isNewAccount = isNewAccount

    def deposit(self, amount, isAtm):
        if self.totalDeposited + int(amount) <= DailyLimits.getDepositLimit(isAtm) and not self.isNewAccount:
            self.totalDeposited += int(amount)
            return True

        return False

    def withdrawal(self, amount, isAtm):
        if self.totalWithdrawn + amount <= DailyLimits.getWithdrawalLimit(isAtm) and not self.isNewAccount:
            self.totalWithdrawn += amount
            return True

        return False

    def transfer(self, amount, isAtm):
        if self.totalTransferred + amount <= DailyLimits.getTransferLimit(isAtm) and not self.isNewAccount:
            self.totalTransferred += amount
            return True

        return False

