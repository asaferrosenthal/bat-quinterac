import os
from quinterac import app

curPath = os.path.dirname(__file__)

if __name__ == '__main__':
    try:
        aFile = "validAccountsListFile.txt"
        tFile = "transactionSummaryFile.txt"

        # if sys.argv[1] and sys.argv[2]:
        #     aFile = sys.argv[1]
        #     tFile = sys.argv[2]

        validAccountsListFile = os.path.join(curPath, aFile)
        transactionSummaryFile = os.path.join(curPath, tFile)
        a = app.App(validAccountsListFile, transactionSummaryFile)
    except IndexError:
        print("Front-end must have two arguments")
