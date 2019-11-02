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
        validAccountsListFile = os.path.join("package/resources", "validAccountsListFile.txt")
        transactionSummaryFile = os.path.join("package/resources", "transactionSummaryFile.txt")
        a = app.App(validAccountsListFile, transactionSummaryFile, 'package/resources/session.txt')
    except IndexError:
        print("Front-end must have two arguments")

