import sys
import os
from package.app import app

path = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    try:
        '''
        extension = ".txt"
        if sys.argv[1] and sys.argv[2]:

            validAccountsListFile = os.path.join("package/resources", str(sys.argv[1] + extension)) #sys.argv[1]
            transactionSummaryFile = os.path.join("package/resources", str(sys.argv[2] + extension)) #sys.argv[2]
            a = app.App(validAccountsListFile, transactionSummaryFile)
        '''
        aFile = "validAccountsListFile.txt"
        tFile = "transactionSummaryFile.txt"

        if sys.argv[1] and sys.argv[2]:
            aFile = sys.argv[1]
            tFile = sys.argv[2]

        validAccountsListFile = os.path.join("package/resources", aFile)
        transactionSummaryFile = os.path.join("package/resources", tFile)
        a = app.App(validAccountsListFile, transactionSummaryFile)
    except IndexError:
        print("Front-end must have two arguments")
