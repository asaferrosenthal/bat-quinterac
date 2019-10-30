import sys
import os
from package.app import app

path = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    try:
        validAccountsListFile = os.path.join("package/resources", "validAccountsListFile.txt") #sys.argv[1]
        transactionSummaryFile = os.path.join("package/resources", "transactionSummaryFile.txt") #sys.argv[2]
        a = app.App(validAccountsListFile, transactionSummaryFile)
    except IndexError:
        print("Front-end must have two arguments")
