import sys
from package.app import app

if __name__ == '__main__':
    try:
        validAccountsListFile = sys.argv[1]
        transactionSummaryFile = sys.argv[2]
    except IndexError:
        print("Front-end must have to arguments")

    a = app.App(str(validAccountsListFile), str(transactionSummaryFile))
