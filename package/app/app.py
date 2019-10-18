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
from package.app.formats import Formatter


class App:

    """
    Purpose:
        Default constructor. Sets class attributes.
    Args:
        Class instance.
        Valid accounts list file.
        Transaction summary file.
    """
    def __init__(self, validAccountsListFile, transactionSummaryFile):
        """ Default Constructor """
        sessionFile = open("session.txt", "w+")   # Creates the session file.
        self.currentSession = sessionFile.name      # Saves session file name as a class attribute for later writes

        self.validAccountListFile = str(validAccountsListFile)
        self.transactionSummaryFile = str(transactionSummaryFile)
        self.agentMode = False  # False in atm mode, true in agent mode
        displayMenu = self.login()
        self.menu = displayMenu
        self.display()                  # Displays transaction options based on mode
    """
    Purpose:
        Sets the menu with the available transactions for the respective mode.
    Args:
        Class instance.
    Returns:
        Menu as an ordered dictionary.
    """
    def menuOptions(self):
        if self.agentMode:  # Menu options for agent mode.
            menu = OrderedDict([
                ('new', self.createAccount),
                ('del', self.deleteAccount),
                ('wdr', self.withdraw),
                ('dep', self.deposit),
                ('xfr', self.transfer),
                ('end', self.logout)
            ])
        else:   # Menu options for atm mode.
            menu = OrderedDict([
                ('wdr', self.withdraw),
                ('dep', self.deposit),
                ('xfr', self.transfer),
                ('end', self.logout)
            ])
        return menu

    """
    Purpose:
        Display the available transactions the user has.
    Args:
        Class instance.
    """
    def display(self):
        choice = None
        while choice != 'end':                      # User logs out
            for key, value in self.menu.items():    # Goes through every key and value in the ordered dictionary menu
                print(f"Enter: '{key}' to {value.__doc__}")
            choice = input("> ").lower().strip()

            if choice in self.menu:     # If the choice exists in the menu.
                self.menu[choice]()     # Call the value at the key, from the ordered dictionary as a function.

    """
    Purpose:
        Writes a line to the session file.
    Args:
        Class instance.
        The line being written to the session file.
    """
    def sessionWrite(self, lineContent):
        file = open(self.currentSession, "a+")
        file.write(lineContent + "\n")

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
        choice = input("Please choose a mode.\n '1' for agent\n '2' for atm.\n> ").lower().strip()
        if choice == '1':
            self.sessionWrite("Login")
            self.agentMode = True
            self.sessionWrite("Agent")
            displayMenu = self.menuOptions()      # Sets agent mode to true, agent menu is displayed
        elif choice == '2':
            self.sessionWrite("Login")
            self.sessionWrite("ATM")
            displayMenu = self.menuOptions()        # self.agentMode remains false, atm menu is displayed
        else:
            print("That is an invalid option. Please try again.")
            return self.login()
        return displayMenu

    """
    Purpose:
        Log out of the front-end. Updates the session file, the writes to the transaction summary file.
    Args:
        Class instance.
    """
    def logout(self):
        """Logout"""
        self.session_write("Logout")
        Formatter.formatSession(self.curr_session, self.transactionSummaryFile)
        #update the transaction summary file
        #empty the session file

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
        self.sessionWrite("createacct")
        self.sessionWrite(accountNumber)
        self.sessionWrite(accountName)

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
        self.sessionWrite("deleteacct")
        self.sessionWrite(accountNumber)
        self.sessionWrite(accountName)

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
        self.sessionWrite("deposit")
        self.sessionWrite(accountNumber)
        self.sessionWrite(depositAmount)

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
        self.sessionWrite("withdraw")
        self.sessionWrite(accountNumber)
        self.sessionWrite(withdrawalAmount)

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
        fromAccountNumber = input("Please provide the account number you wish to transfer from.\n> ")
        toAccountNumber = input("Please provide the account number you wish to transfer to.\n> ")
        transferAmount = input("What is your transfer amount?: ")
        self.sessionWrite("transfer")
        self.sessionWrite(fromAccountNumber)
        self.sessionWrite(toAccountNumber)
        self.sessionWrite(transferAmount)
