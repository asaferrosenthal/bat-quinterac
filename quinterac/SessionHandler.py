from quinterac.Account import *
from quinterac.Errors import *


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
            return True
        except ValueError:
            return "Must be digits."

    @staticmethod
    def validateAccountNameFormat(accountName):
        if str(accountName)[:1] == " ":
            return "Name cant start with space"
        if len(accountName) < 3 or len(accountName) > 30:
            return "Account name must be between 3 and 30 characters in length."
        accountName = accountName.replace(" ", "")
        if not accountName.isalnum():
            return "Can only be alphanumeric characters"
        return True

    @staticmethod
    def validateOldAccount(accountNumber):
        account = DailyLimits.getAccountFor(accountNumber)
        if account:
            DailyLimits.accounts.remove(account)
            return True
        
        return "That account does not exist."

    @staticmethod
    def validateAmount(amount):
        if "." in amount:
            return "Please enter the amount in cents."
        try:
            amount = int(amount)
            return True
        except ValueError:
            return "Amount must be an integer."

    @staticmethod
    def deposit(accountNumber, amount):
        account = DailyLimits.getAccountFor(accountNumber)
        validAmount = SessionHandler.validateAmount(amount)
        if type(validAmount) is bool:
            if account:
                result = account.deposit(amount, SessionHandler.isAtm)
                if type(result) is bool:
                    if result:
                        print("Deposited ${} into account number: {}".format(amount, accountNumber))
                        return validAmount
                else:
                    result = Error(result)
                    return result.value + " Current amount: " + str(account.totalDeposited) + "."
            else:
                return "No account found with number: " + str(accountNumber)
        else:
            return validAmount

    @staticmethod
    def withdraw(accountNumber, amount):
        account = DailyLimits.getAccountFor(accountNumber)
        validAmount = SessionHandler.validateAmount(amount)
        if type(validAmount) is bool:
            if account:
                result = account.withdraw(amount, SessionHandler.isAtm)
                if type(result) is bool:
                    if result:
                        print("Withdrew", amount, "from", accountNumber)
                        return validAmount
                else:
                    result = Error(result)
                    return result.value + " Current amount: " + str(account.totalWithdrawn) + "."
            else:
                return "No account found with number: " + str(accountNumber)
        else:
            return validAmount

    @staticmethod
    def transfer(toAccountNumber, fromAccountNumber, amount):
        toAccount = DailyLimits.getAccountFor(toAccountNumber)
        fromAccount = DailyLimits.getAccountFor(fromAccountNumber)
        validAmount = SessionHandler.validateAmount(amount)
        if type(validAmount) is bool:
            if toAccount and fromAccount:
                if toAccountNumber == fromAccountNumber:
                    return "To account number and from account number cannot be the same."

                result = fromAccount.transfer(amount, SessionHandler.isAtm)
                if type(result) is bool:
                    if result:
                        print("Transferred: " + str(amount) + ", from: " + str(fromAccountNumber)+ ", to: " + str(toAccountNumber))
                        return validAmount
                else:
                    result = Error(result)
                    return result.value + " Current amount: " + str(fromAccount.totalTransferred) + "."
            else:
                if not toAccount and not fromAccount:
                    return "Both of your account numbers provided do not exist."
                if toAccount and not fromAccount:
                    return "The from account provided does not exist."
                if not toAccount and fromAccount:
                    return "The to account provided does not exist."
        else:
            return validAmount
