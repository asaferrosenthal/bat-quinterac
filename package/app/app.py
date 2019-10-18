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

    def __init__(self, val_file, trans_act_sum):
        """ Default Constructor """
        print("here")
        f = open("session.txt", "w+")   # Creates the session file.
        self.curr_session = f.name      # Saves file name as a class attribute
        self.agent_mode = False         # False in atm mode, true in agent mode
        self.validAccountListFile = str(val_file)
        self.transactionSummaryFile = str(trans_act_sum)
        self.login()
        self.display()                  # Displays transaction options based on mode

    """
    Purpose:
        Set the menu with the availible transactions for the respective mode.
    Args:
        Class instance.
    """
    def menuOptions(self):
        if self.agent_mode: # Menu options for agent mode.
            menu = OrderedDict([
                ('new', self.create_acct),
                ('del', self.delete_acct),
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
        self.menu = menu

    """
    Purpose:
        Display the availible transactions the user has.
    Args:
        Class instance.
    """
    def display(self):
        choice = None
        while choice != 'end':                      # User logs out
            for key, value in self.menu.items():    # Goes through every key and value in the ordered dictionary menu
                print(f"Enter: '{key}' to {value.__doc__}")
            choice = input("> ").lower().strip()

            if choice in self.menu:
                self.menu[choice]()     # If the choice exists in the menu, call the value at the key, from the ordered dictionary as a function

    """
    Purpose:
        Write a line to the session file.
    Args:
        Class instance.
        The line being written to the session file.
    """
    def session_write(self, line_content):
        f = open(self.curr_session, "a+")
        f.write(line_content + "\n")

    def checkForExistingAccount(self):
        f = open(self.validAccountListFile, "r")
        allAccounts = f.readlines()
        return allAccounts

    def addNewValidAccount(self, account):
        pass

    def deleteValidAccount(self, account):
        pass

        
    """
    Purpose:
        User logs into the front-end. Session file is updated. Asks user for
        which mode.
    Args:
        Class instance.
    """
    def login(self):
        self.session_write("Login")
        print("Please choose a mode.\n '1' for agent\n '2' for atm.")
        choice = input("> ").lower().strip()
        if choice == '1':
            self.agent_mode = True
            self.session_write("Agent")
            self.menuOptions()      # Sets agent mode to true, agent menu is displayed
        elif choice == '2':
            self.session_write("ATM")
            self.menuOptions()        # self.agentMode remains false, atm menu is displayed
        else:
            print("that is an invalid option.")


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
        Session file is updated with the new information.
    Args:
        Class instance.
    """
    def create_acct(self):
        """Create Account"""
        accountNumber = input("Please provide an account number for the new account.\n> ")
        allValidAccounts = self.checkForExistingAccount
        if accountNumber not in allValidAccounts:
            name = input("Please enter a name for the account.\n> ")

            #adds new account number to the valid accounts file
            self.session_write("createacct")
            self.session_write(accountNumber)
            self.session_write(name)
        else:
            print("That number already exists please try again.")
            self.create_acct()

    """
    Purpose:
        Delete account feature. Prompts user for a number and name for the account they wish to delete.

    Args:
        Class instance.
    """
    def delete_acct(self):
        """Delete Account"""
        acct_number = input("Please provide an account number you wish to delete.\n> ") # Assume that the number is within the constraints
        name = input("Please enter a name for the account.\n> ")
        #updates the valid accounts list after the format is valid?
        self.session_write("deleteacct")
        self.session_write(acct_number)
        self.session_write(name)


    def deposit(self):
        """Deposit"""
        acct_number = input("Please provide an account number you wish to deposit into.\n> ") # Assume that the number is within the constraints
        amount = input("What is your deposit amount?: ")
        self.session_write("deposit")
        self.session_write(acct_number)
        self.session_write(amount)


    def withdraw(self):
        """Withdraw"""
        acct_number = input("Please provide an account number you wish to withdraw from.\n> ") # Assume that the number is within the constraints
        amount = input("What is your withdrawal amount?: ")
        self.session_write("withdraw")
        self.session_write(acct_number)
        self.session_write(amount)


    """
    Purpose:
        To transfer actions.
    Args:
        Class instance.
    """
    def transfer(self):
        """Transfer"""
        from_acct_number = input("Please provide the account number you wish to transfer from.\n> ")
        to_acct_number = input("Please provide the account number you wish to transfer to.\n> ")
        amount = input("What is your transfer amount?: ")
        self.session_write("transfer")
        self.session_write(from_acct_number)
        self.session_write(to_acct_number)
        self.session_write(amount)
