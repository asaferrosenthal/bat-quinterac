from package.app.DailyLimits import *


class SessionHandler:
    isAtm = False

    @staticmethod
    def validateNewAccount(accountNumber, accountName):
        if DailyLimits.getAccountFor(accountNumber):
            return "That account number already exits. Please Choose a different one."

        valid = SessionHandler.validateAccountNumberFormat(accountNumber)
        return valid

    @staticmethod
    def validateAccountNumberFormat(accountNumber):
        if str(accountNumber)[:1] == '0':
            return "Cant start with zero"
        if len(accountNumber) != 7:
            return "Must be exactly 7 digits"
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            return "Must be digits."
        return True

        
    @staticmethod
    def validateAccountNameFormat(accountName):
        if str(accountName)[:1] == " ":
            return "Name cant start with space"
        if len(accountName) < 3 or len(accountName) > 30:
            return "Account name must be between 3 and 30 characters in length."
        accountName = accountName.replace(" ", "")
        if not accountName.isalnum():
            return "Can only be alphanumber characters"
        return True

    @staticmethod
    def validateOldAccount(accountNumber):
        account = DailyLimits.getAccountFor(accountNumber)
        if account:
            DailyLimits.accounts.remove(account)
            return True
        
        return "That account does not exist."

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
