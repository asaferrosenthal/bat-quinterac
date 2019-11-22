import logging
import os

from quinterac.Account import *
from quinterac.Formatter import TransactionCode

pathToDir = os.path.dirname(os.path.abspath(__file__))              # Gets the path to this dir ~/quinteracBackend
pathToFront = pathToDir.replace("quinteracBackend", "quinterac")    # Get the path to the frontend package ~/quinterac

class BackEnd:

    def __init__(self, masterAccountsFileName, mergedTransactionFileName):
        """
        Purpose:
            Default contructor set the old master accounts file as an attribute. Gets all of the
            existing accounts as a list of Account objects.
        Args:
            masterAccountsFileName - Name of the old master accounts file.
            mergedTransactionFileName - Name of the current merged transaction file.        
        """
        self.masterFileName = os.path.join(pathToDir, masterAccountsFileName)
        self.masterAccountsFile = open(self.masterFileName, 'r')
        self.mergedTransactionFileName = os.path.join(pathToFront, mergedTransactionFileName)
        self.mergedTransactionFile = open(self.mergedTransactionFileName, "r+")
        self.accounts = self.loadAccounts()
        self.update(self.mergedTransactionFile)

    def update(self, transactionSummaryFile):
        """
        Purpose:
            Update method goes through each line of the merged transaction summary file,
            and makes modifications to the accounts accordingly. Once all of the changes
            have been made to the accounts, the Account object list is sorted.
        Args:
            Transaction Summary File - The merged transaction summary file.
        """
        for line in transactionSummaryFile:
            trans = line.split()
            transCode = trans[0]

            if transCode == TransactionCode.DEL.name:
                self.deleteAccount(trans[3], trans[4])
            elif transCode == TransactionCode.NEW.name:
                self.createAccount(trans[3], trans[4])
            elif transCode == TransactionCode.DEP.name:
                self.depositAccount(trans[3], int(trans[2]))
            elif transCode == TransactionCode.WDR.name:
                self.withdrawAccount(trans[3], int(trans[2]))
            elif transCode == TransactionCode.XFR.name:
                # withdraw from account
                self.withdrawAccount(trans[3], int(trans[2]))
                # deposit into other account
                self.depositAccount(trans[1], int(trans[2]))
            elif transCode == TransactionCode.EOS.name:
                print("Done reading")
            else:
                print("Error reading transactions")

        self.accounts.sort(key=lambda x: x.accountNumber, reverse=True)
        self.writeMaster()

    def writeMaster(self):
        """
        Purpose:
            Updates the master accounts file based on the account changes from the merged transaction summary file.
        """
        self.masterAccountsFile = open(self.masterFileName, "w")
        for account in self.accounts:
            curLine = self.formatLine(account.accountNumber, account.balance, account.accountName)
            self.masterAccountsFile.write(curLine)

        self.masterAccountsFile.close()
        self.generateNewAccountsFile()

    def generateNewAccountsFile(self):
        """
        Purpose:
            Uses the updated accounts from the Account objects list and creates a new valid accounts list file to be
            used in the next processing day.
        """
        validAccountsListFileName = os.path.join(pathToFront, "validAccountsListFile.txt")
        accountsFile = open(validAccountsListFileName, "w")
        for account in self.accounts:
            accountsFile.write(account.accountNumber + "\n")

        accountsFile.write("0000000\n")
        accountsFile.close()

        open(self.mergedTransactionFileName, "w").close() # Clears merged transaction file to prevent duplicated transactions.

    def depositAccount(self, number, amount):
        """
        Purpose:
            Deposits money to account.
        Args:
            number - The account number that is getting the deposit.
            amount - The amount being deposited.
        """
        if len(self.accounts) == 0:     # No Accounts
            logging.error(Error.noAccounts.value)

        for account in self.accounts:
            if account.accountNumber == number:
                account.updateBalance(amount)
                break

    def withdrawAccount(self, number, amount):
        """
        Purpose:
            Withdraws money from account.
        Args:
            number - The account number that is getting the withdrawal.
            amount - The amount being withdrawn.
        """
        if len(self.accounts) == 0:     # No Accounts
            logging.error(Error.noAccounts.value)

        for account in self.accounts:
            if account.accountNumber == number:
                if account.updateBalance(-amount) == Error.negativeBalance:
                    logging.error(Error.negativeBalance.value + "- for account: " + account.accountNumber)
                break

    def createAccount(self, number, name):
        """
        Purpose:
            Creates new account.
        Args:
            number - The number of the new account.
            name - The name associated to the new account.
        """
        accountExists = False
        for account in self.accounts:
            if account.accountNumber == number:
                accountExists = True
                logging.error(Error.accountExists.value + "- for account: " + account.accountNumber)
                break

        if not accountExists:   # Valid account number
            self.accounts.append(Account(number, name, True))   # Creates the new Account object

    def deleteAccount(self, number, name):
        """
        Purpose:
            Deletes account.
        Args:
            number - The account number associated with the deleted account.
            name - The name associated with the deleted account.
        """
        acc = None
        for account in self.accounts:
            if account.accountName == name and account.accountNumber == number:
                if account.balance != 0:
                    logging.error(Error.accountHasBalance.value + "- for account: " + account.accountNumber)
                else:
                    acc = account
                break

        if acc:     # Valid account
            self.accounts.remove(acc)   # Deletes account

    def loadAccounts(self):
        """ 
        Purpose:
            Load current accounts from old master accounts file.    
        Returns:
            List of current Account objects.
        """
        tempAccountsList = []
        for line in self.masterAccountsFile:
            accInfo = line.split()
            account = Account(accInfo[0], accInfo[2], False, accInfo[1])
            tempAccountsList.append(account)

        return tempAccountsList

    @staticmethod
    def formatLine(accountNumber, balance, accountName):
        """
        Purpose:
            Format string for the master account file.
        Args:
            accountNumber - The account number.
            balance - The accounts balance (in cents).
            accountName - The name associated to the account.
        Returns:
            The formatted string.
        """
        return f"{accountNumber} {balance} {accountName}\n"

