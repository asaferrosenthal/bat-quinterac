"""
app.py runs all of the transactions, login, logout, create and delete account, withdrawal, deposit and transfer.
When the file is run, a session.txt file is created. After every transaction the session file is updated.
After the user logs out, the session file is passed on to (tamirs file), and its converted into the transaction
summary file.

Please note that constraints to check for valid account numbers as well as formatting for both numbers, and amounts
is assumed to be true. This we be implemented when we create test code for our function. This just demonstrates the
functionality of the front-end.
""" 

from collections import OrderedDict
from package.app.formats import *
from package.app.SessionHandler import SessionHandler
from package.app.DailyLimits import *

import os

class App:

    def __init__(self, validAccountsFileName, transactionSummaryFileName, pathToSessionFile):
        sessionFile = open(pathToSessionFile, "w+")   # Creates the session file.
        sessionFile.close()
        self.currentSession = sessionFile.name      # Saves session file name as a class attribute for later writes

        self.validAccountsListFile = str(validAccountsFileName)
        self.transactionSummaryFile = str(transactionSummaryFileName)
        self.isAgent = False

        self.setup()

    def setup(self):
        """Start"""

        isValid = False

        while not isValid:
            choice = input("Enter 'login' to begin. Or 'exit' to exit program.\n> ").lower().strip()
            if choice == 'login':
                DailyLimits.loadAccounts(self.validAccountsListFile)
                self.login()
            if choice == 'exit':
                print("Exiting program")
                isValid = True
            else: 
                print("Invalid input. Try again.")

       

    def restartProgram(self):
        """Exit"""
        self.login()

    """
        Purpose:
            Writes a line to the session file.
        Args:
            Class instance.
            The line being written to the session file.
    """
    def sessionWrite(self, lineContent, isEOS=False):
        file = open(self.currentSession, "a+")
        file.write(lineContent + "\n")
        if isEOS:
            file.write(TransactionCode.EOS.name)
            file.close()
            Formatter.formatSession(self.currentSession, self.transactionSummaryFile)

    # MARK: Agent Only Transactions

    """
        Purpose:
            Create account feature. Prompts user for an account number and a name for the new account.
            Session file is updated with the new information. Function assumes the account number is valid.
        Args:
            Class instance.
        """
    def createAccount(self):
        """Create Account"""
        accountNumber = input("Please provide an account number for the new account.\n> ")


        accountName = input("Please enter a name for the account.\n> ")

        accountNumberError = SessionHandler.validateNewAccount(accountNumber, accountName)
        accountNameError = SessionHandler.validateAccountNameFormat(accountName)
        if type(accountNumberError) is bool and type(accountNameError) is bool:
            newAccount = Account(accountNumber, accountName, True)
            DailyLimits.addAccount(newAccount)
            self.sessionWrite(Transaction.createAccount.name, False)
            self.sessionWrite(accountNumber, False)
            self.sessionWrite(accountName, False)
            tempFile = self.validAccountsListFile
            with open(tempFile, "r") as inFile:
                with open("package/resources/validAccountsListFile1.txt", "w+") as outFile:
                    for line in inFile:
                        if line.strip("\n") != "0000000":
                            outFile.write(line)

                    outFile.write(accountNumber+"\n")
                    outFile.write("0000000")
            os.rename("package/resources/validAccountsListFile1.txt", "package/resources/validAccountsListFile.txt")


        else:
            if type(accountNumberError) is not bool:
                print(accountNumberError + " Please try again.")
            if type(accountNameError) is not bool:
                print(accountNameError + " Please try again.")

            self.createAccount()


    """
    Purpose:
        Delete account feature. Prompts user for a number and name for the account they wish to delete.
        Session file is updated with the new information. Function assumes the account number is valid.
    Args:
        Class instance.
    """
    def deleteAccount(self):
        """Delete Account"""
        accountNumber = input("Please provide an account number you wish to delete.\n> ")
        accountName = input("Please enter a name for the account.\n> ")
        accountNumberError = SessionHandler.validateOldAccount(accountNumber)
        accountNameError = SessionHandler.validateAccountNameFormat(accountName)
        if type(accountNumberError) is bool and type(accountNameError) is bool:
            tempFile = self.validAccountsListFile
            with open(tempFile, "r") as inFile:
                with open("package/resources/validAccountsListFile1.txt", "w+") as outFile:
                    for line in inFile:
                        if line.strip("\n") != accountNumber:
                            outFile.write(line)

            os.rename("package/resources/validAccountsListFile1.txt", "package/resources/validAccountsListFile.txt")
            self.sessionWrite(Transaction.deleteAccount.name, False)
            self.sessionWrite(accountNumber, False)
            self.sessionWrite(accountName, False)
        else:
            if type(accountNumberError) is not bool:
                print(accountNumberError + " Please try again.")
            if type(accountNameError) is not bool:
                print(accountNameError + " Please try again.")
            self.deleteAccount()

    # MARK: ATM & Agent Transactions

    """
    Purpose:
        Deposit feature. Prompts user for an account number to deposit into and the amount they wish to deposit.
        Session file is updated with the new information. Function assumes the account number and amount is valid.
    Args:
        Class instance.
    """
    def deposit(self):
        """Deposit"""
        accountNumber = input("Please provide an account number you wish to deposit into.\n> ")
        depositAmount = input("What is your deposit amount?: ")

        errorMessage = SessionHandler.deposit(accountNumber, depositAmount)
        if type(errorMessage) is bool:
            self.sessionWrite(Transaction.deposit.name, False)
            self.sessionWrite(accountNumber, False)
            self.sessionWrite(depositAmount, False)
        else:
            print(errorMessage + " Please try again.")
            self.deposit()
    """
    Purpose:
        Withdrawal feature. Prompts user for an account number to withdraw from and the amount they wish to withdraw.
        Session file is updated with the new information. Function assumes the account number and amount is valid.
    Args:
        Class instance.
    """
    def withdraw(self):
        """Withdraw"""
        
        accountNumber = input("Please provide an account number you wish to withdraw from.\n> ")
        withdrawalAmount = input("What is your withdrawal amount?: ")
        errorMessage = SessionHandler.withdraw(accountNumber, withdrawalAmount)

        if type(errorMessage) is bool:
            self.sessionWrite(Transaction.withdraw.name, False)
            self.sessionWrite(accountNumber, False)
            self.sessionWrite(withdrawalAmount, False)
        else:
            print(errorMessage + " Please try again.")
            self.withdraw()

        

    """
    Purpose:
        Transfer feature. Prompts user for an account number to transfer from, an account number to transfer to, and the
        amount they wish to transfer. Session file is updated with the new information. Function assumes the account 
        numbers and amount is valid.
    Args:
        Class instance.
    """
    def transfer(self):
        """Transfer"""

        toAccountNumber = input("Please provide the account number you wish to transfer to.\n> ")
        fromAccountNumber = input("Please provide the account number you wish to transfer from.\n> ")
        transferAmount = input("What is your transfer amount?: ")

        errorMessage = SessionHandler.transfer(toAccountNumber, fromAccountNumber, transferAmount)

        if type(errorMessage) is bool:
            self.sessionWrite(Transaction.transfer.name, False)
            self.sessionWrite(fromAccountNumber, False)
            self.sessionWrite(toAccountNumber, False)
            self.sessionWrite(transferAmount, False)
        else:
            print(errorMessage + " Please try again.")
            self.transfer()

        

    # MARK: Admin Functions

    """
    Purpose:
        User logs into the front-end. Session file is updated. Asks user for
        which mode.
    Args:
        Class instance.
    Returns:
        Display menu according to chosen mode.
    """
    def login(self):
        isValid = False

        while not isValid:
            choice = input("Please choose a mode.\n '1' for agent\n '2' for machine.\n 'logout' to quit.\n> ").lower().strip()
            if choice == 'logout':
                isValid = True
            elif choice == '1' or choice == '2':
                self.setupEnvironment(choice == '1')
            else:
                print("Invalid input. Try again.\n")

        self.logout()

    def setupEnvironment(self, isAgent):
        self.sessionWrite(Transaction.login.name, False)
        self.isAgent = isAgent
        SessionHandler.isAtm = not isAgent
        if isAgent:
            self.sessionWrite(SessionMode.agent.name, False)
        else:
            self.sessionWrite(SessionMode.atm.name, False)

        self.displayOptions()

    """
    Purpose:
        Log out of the front-end. Updates the session file, the writes to the transaction summary file.
    Args:
        Class instance.
    """
    def logout(self):
        """Logout"""
        self.sessionWrite(Transaction.logout.name, True)
        # update the transaction summary file
        # empty the session file

    # MARK: Display Menus

    """
    Purpose:
        Sets the menu with the available transactions for the respective mode.
    Args:
        Class instance.
    Returns:
        Menu as an ordered dictionary.
    """
    def getMenuOptions(self):
        if self.isAgent:  # Menu options for agent mode.
            menu = OrderedDict([
                ('new', self.createAccount),
                ('del', self.deleteAccount),
                ('wdr', self.withdraw),
                ('dep', self.deposit),
                ('xfr', self.transfer),
                ('exit', self.restartProgram)
            ])
        else:   # Menu options for atm mode.
            menu = OrderedDict([
                ('wdr', self.withdraw),
                ('dep', self.deposit),
                ('xfr', self.transfer),
                ('exit', self.restartProgram)
            ])
        return menu

    """
    Purpose:
        Display the available transactions the user has.
    Args:
        Class instance.
    """
    def displayOptions(self):
        menuOptions = self.getMenuOptions()
        choice = None
        while choice != 'end':                      # User logs out
            for key, value in menuOptions.items():    # Goes through every key and value in the ordered dictionary menu
                print(f"Enter: '{key}' to {value.__doc__}")
            choice = input("> ").lower().strip()

            if choice in menuOptions:     # If the choice exists in the menu.
                menuOptions[choice]()     # Call the value at the key, from the ordered dictionary as a function.
