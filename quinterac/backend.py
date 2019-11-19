from quinterac.Account import *
from quinterac.formats import *

class Backend:

    # take transaction summary file from frontend session and update Master Accounts list
    def __init__(self):
        self.masterFileName = "masterAccountsFile.txt"
        self.masterAccountsFile = open(self.masterFileName, 'r')
        # Current list of accounts from master account file
        self.accounts = self.loadAccounts()

    # Process:
    # load old master accounts to array on init
    # on update() - traverse transaction summary file and create/delete accounts, deposit/withdraw/transfer
    #               make changes to account in accounts array accordingly (add or remove in necessary)
    #               when finished, sort using mergesort and write new master accounts file
    # generate valid accounts list for front end

    def update(self, transactionSummaryFile):
        print("updating")
        for line in transactionSummaryFile:
            trans = line.split()
            transCode = TransactionCode(trans[0])

            if transCode == TransactionCode.DEL:
                self.deleteAccount(trans[3], trans[4])
            elif transCode == TransactionCode.NEW:
                self.accounts.append(Account(trans[3], trans[4], True))
            elif transCode == TransactionCode.DEP:
                self.updateAccount(trans[3], trans[4], int(trans[2]))
            elif transCode == TransactionCode.WDR:
                self.updateAccount(trans[3], trans[4], -int(trans[2]))
            elif transCode == TransactionCode.XFR:
                # withdraw from account
                self.updateAccount(trans[3], None, -int(trans[2]))
                # deposit into other account
                self.updateAccount(trans[1], None, int(trans[2]))
            elif transCode == TransactionCode.EOS:
                print("Done reading")
            else:
                print("Error reading transactions")

        sorted(self.accounts, reverse=True)
        # self.sort(self.accounts)

    def writeMaster(self):
        self.masterAccountsFile = open(self.masterFileName, "w")

        for account in self.accounts:
            curLine = self.formatLine(account.accountNumber, account.balance, account.accountName)
            self.masterAccountsFile.write(curLine)

        self.masterAccountsFile.close()

    def updateAccount(self, number, name, amount):
        for account in self.accounts:
            if account.accountNumber == number:
                account.updateBalance(amount)
                break

    def deleteAccount(self, number, name):
        acc = None

        for account in self.accounts:
            if account.accountName == name and account.accountNumber == number:
                acc = account
                break

        self.accounts.remove(acc)

    """ Load current accounts from old master accounts file."""
    def loadAccounts(self):
        tempAccountsList = []
        for line in self.masterAccountsFile:
            accInfo = line.split()
            account = Account(accInfo[0], accInfo[2], False, accInfo[1])

            tempAccountsList.append(account)

        return tempAccountsList

    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

        # The main function that implements QuickSort

    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def sort(self, accountsList):
        length = len(accountsList)
        self.quickSort(accountsList, 0, length)

    @staticmethod
    def formatMasterAccounts(self):
        print("formatting")
        # for line in self.masterAccountsFile:

    @staticmethod
    def formatLine(accountNumber, balance, accountName):
        return "{} {} {}\n".format(accountNumber, balance, accountName)
