from enum import Enum
import os

pathToDir = os.path.dirname(os.path.abspath(__file__))

class TransactionCode(Enum):
    WDR = "withdraw"
    DEP = "deposit"
    XFR = "transfer"
    NEW = "createAccount"
    DEL = "deleteAccount"
    EOS = "EOS"
    

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
    def formatSession(sessionFileD, sessionFileName, transSumFileName):
        sessionFile = open(sessionFileName, "r")
        transSumFile = open(transSumFileName, "w+")

        # Read temporary file content
        lines = sessionFile.read().splitlines()
        # Check that the user was logged in, and its a valid session file
        line = getLine(lines)
        if line != Transaction.login.name:
            return

        # Check for the session mode, agent or ATM
        if getLine(lines) == Transaction.logout.name:
            lines.insert(0, Transaction.logout.name)

        while len(lines) != 0:
            line = getLine(lines).strip()

            curLine = ""
            if line == Transaction.logout.name:
                line = getLine(lines).strip()
                if line == TransactionCode.EOS.name:
                    curLine = Formatter.formatLine(TransactionCode.EOS.name, "0000000", "000", "0000000", "***")
            else:
                transCode = TransactionCode(line)
                if transCode == TransactionCode.WDR or transCode == TransactionCode.DEP:
                    accountNum = getLine(lines).strip()
                    amount = getLine(lines).strip()
                    curLine = Formatter.formatLine(transCode.name, "0000000", amount, accountNum, "***")
                elif transCode == TransactionCode.NEW or transCode == TransactionCode.DEL:
                    accountNum = getLine(lines).strip()
                    accountName = getLine(lines).strip()
                    curLine = Formatter.formatLine(transCode.name, "0000000", "000", accountNum, accountName)
                elif transCode == TransactionCode.XFR:
                    fromAccountNUm = getLine(lines).strip()
                    toAccountNum = getLine(lines).strip()
                    amount = getLine(lines).strip()
                    curLine = Formatter.formatLine(transCode.name, toAccountNum, amount, fromAccountNUm, "***")

            transSumFile.write(curLine)

        transSumFile.close()
        sessionFile.close()
        os.close(sessionFileD)
        os.remove(sessionFileName)
        Formatter.mergeTransaction(transSumFileName)

    @staticmethod
    def mergeTransaction(transSumFileName):
        EOSLine = "EOS 0000000 000 0000000 ***"

        # Clean merged file for all EOS lines
        mergedTransactionSummaryFile = os.path.join(pathToDir, "mergedTransactionSummaryFile.txt")
        mergedTransFile = open(mergedTransactionSummaryFile, "r+")
        lines = mergedTransFile.read().splitlines()
        if EOSLine in lines:
            lines.remove(EOSLine)

        # Close before reopening to append
        mergedTransFile.close()

        # Open merged transaction summary file for appending
        mergedTransFile = open(mergedTransactionSummaryFile, "w+")
        # Open transaction summary file for reading
        transSumFile = open(transSumFileName, "r")

        newLines = lines + transSumFile.read().splitlines()
        # Write new transactions to merged transaction file
        for line in newLines:
            if line != EOSLine:
                mergedTransFile.write(line + "\n")

        mergedTransFile.write(EOSLine + "\n")
        mergedTransFile.close()
        transSumFile.close()

    @staticmethod
    def formatLine(transCode, toAcc, amount, fromAcc, accName):
        return "{} {} {} {} {}\n".format(transCode, toAcc, amount, fromAcc, accName)


def getLine(lines=None):
    if lines is None:
        return []

    line = lines[0]
    lines.pop(0)
    return line
