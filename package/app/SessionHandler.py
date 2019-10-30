from package.app.DailyLimits import *


class SessionHandler:
    isAtm = False

    @staticmethod
    def validateNewAccount(accountNumber, accountName):
        if DailyLimits.getAccountFor(accountNumber):
            return False

        # TODO: Validate Account Number
        newAccount = Account(accountNumber, accountName, True)
        DailyLimits.addAccount(newAccount)

        return True

    @staticmethod
    def deposit(accountNumber, amount):
        account = DailyLimits.getAccountFor(accountNumber)

        if account:
            if account.deposit(amount, SessionHandler.isAtm):
                print("deposited", amount)
            else:
                print("The new deposit amount will go over your daily limit.\nCurrent amount:", account.totalDeposited)
        else:
            print("No account found with number:", accountNumber)

    @staticmethod
    def withdraw(accountNumber, amount):
        print("withdrawing", amount)

    @staticmethod
    def transfer(toAccountNumber, fromAccountNumber, amount):
        print("depositing", amount)
