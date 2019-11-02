from enum import Enum

class TransactionCode(Enum):
    WDR = "withdraw"
    DEP = "deposit"
    XFR = "transfer"
    NEW = "createAccount"
    DEL = "deleteAccount"
    EOS = "eos"


class Transaction(Enum):
    login = "login"
    logout = "logout"
    withdraw = "withdraw"
    deposit = "deposit"
    transfer = "transfer"
    deleteAccount = "deleteacct"
    createAccount = "createacct"


class SessionMode(Enum):
    agent = "agent"
    atm = "atm"


class Formatter:

    @staticmethod
    def formatSession(sessionFileName, transSumFileName):
        sessionFile = open(sessionFileName, "r")
        transSumFile = open(transSumFileName, "a")

        # Check that the user was logged in, and its a valid session file
        line = sessionFile.readline().strip()
        if line != Transaction.login.name:
            exit(1)

        # Check for the session mode, agent or ATM
        sessionFile.readline().strip()

        for line in sessionFile:
            line = line.strip()

            curLine = ""
            if line == Transaction.logout.name:
                line = sessionFile.readline()
                if line == TransactionCode.EOS.name:
                    curLine = Formatter.formatLine(TransactionCode.EOS.name, "0000000", "000", "0000000", "***")
            else:
                transCode = TransactionCode(line)
                if transCode == TransactionCode.WDR or transCode == TransactionCode.DEP:
                    accountNum = sessionFile.readline().strip()
                    amount = sessionFile.readline().strip()
                    curLine = Formatter.formatLine(transCode.name, "0000000", amount, accountNum, "***")
                elif transCode == TransactionCode.NEW or transCode == TransactionCode.DEL:
                    accountNum = sessionFile.readline().strip()
                    accountName = sessionFile.readline().strip()
                    curLine = Formatter.formatLine(transCode.name, "0000000", "000", accountNum, accountName)
                elif transCode == TransactionCode.XFR:
                    fromAccountNUm = sessionFile.readline().strip()
                    toAccountNum = sessionFile.readline().strip()
                    amount = sessionFile.readline().strip()
                    curLine = Formatter.formatLine(transCode.name, toAccountNum, amount, fromAccountNUm, "***")

            transSumFile.write(curLine)

        transSumFile.close()
        exit(0)

    @staticmethod
    def formatLine(transCode, toAcc, amount, fromAcc, accName):
        return "{} {} {} {} {}\n".format(transCode, toAcc, amount, fromAcc, accName)
