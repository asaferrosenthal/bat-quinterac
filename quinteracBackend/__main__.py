import os
import sys
from quinteracBackend import BackEnd

curPath = os.path.dirname(__file__)
otherPath = curPath.replace("quinteracBackend", "quinterac")

if __name__ == '__main__':
    merged = str(otherPath) + "/mergedTransactionSummaryFile.txt"
    a = BackEnd.BackEnd("masterAccountsFile.txt", merged)
    #try:
        #if sys.argv[1] and sys.argv[2]:
            #masterAccountFile = sys.argv[1] # Must be the master account file located in the quinteracBackend package.
            #mergedTransactionSummaryFile = sys.argv[2] # Must be the merged transaction summary file located in the quinterac package.
            #a = BackEnd.BackEnd(masterAccountFile, mergedTransactionSummaryFile)
    #except IndexError:
        #print("Back-end must have two arguments. Master Account file as the first, and the merged transaction summary file as the second.")
