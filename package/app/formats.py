from enum import Enum

class TransactionCode(Enum):
    WDR = "withdrawal"
    DEP = "deposit"
    XFR = "transfer"
    NEW = "createacct"
    DEL = "deleteacct"
    EOS = "eos"


class Formatter:

    @staticmethod
    def formatSession(sessionFileName, transSumFileName):
        print("formatting session")

        sessionFile = open(sessionFileName, "r")
        transSumFile = open(transSumFileName, "a")

        print(TransactionCode("withdrawal").name)

        if sessionFile.readline() != "login":
            exit(1)

        # for line in sessionFile:
        #     transCode = TransactionCode(line).name
        #
        #     if transCode == TransactionCode.WDR:
        #         curLine = Formatter.formatLine(transCode, )
        #     curLine = Formatter.formatLine(transCode,)
        #     transSumFile.write()

    def formatLine(self, transCode, toAcc, amount, fromAcc, accName):
        return "{} {} {} {} {}".format(transCode, toAcc, amount, fromAcc, accName)
