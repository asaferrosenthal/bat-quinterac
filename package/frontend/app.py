"""
desc of project
"""
from collections import OrderedDict



class App:

    def __init__(self, val_file, tsl_file):
        """ Default Constructor """
        f = open("session.txt", "w+")
        self.curr_session = f.name
        self.val_file = val_file
        self.tsl_file = tsl_file
        self.agent_mode = False
        self.login()
        self.display()
       

    def agent_mode_menu(self):
        frontend_menu = OrderedDict([
            ('new', self.create_acct),
            ('del', self.delete_acct),
            ('wdr', self.withdraw),
            ('dep', self.deposit),
            ('xfr', self.transfer),
            ('end', self.logout)
        ])
        self.menu = frontend_menu

    def atm_mode_menu(self):
        frontend_menu = OrderedDict([
            ('wdr', self.withdraw),
            ('dep', self.deposit),
            ('xfr', self.transfer),
            ('end', self.logout)
        ])
        self.menu = frontend_menu

    
    def first_check(self):
        f = open(self.curr_session, "r")
        lines = f.readlines()
        return lines == []
    

    def display(self):
        choice = None
        while choice != 'l':
            for key, value in self.menu.items():
                print(f"{key}, {value.__doc__}")
            choice = input("> ").lower().strip()

            if choice in self.menu:
                self.menu[choice]()
    
    def session_write(self, line_content):
        f = open(self.curr_session, "a+")
        f.write(line_content + "\n")

    def login(self):
        self.session_write("Login")
        print("Please choose a mode.\n '1' for agent\n '2' for atm.")
        choice = input("> ").lower().strip()
        if choice == '1':
            self.agent_mode = True
            self.session_write("Agent")
            self.agent_mode_menu()
        else:   
            self.session_write("ATM")   
            self.atm_mode_menu() 

        
    def logout(self):
        """Logout"""
        self.session_write("Logout")
        #update the transaction summary file
        #empty the session file

           
    def create_acct(self):
        """Create Account"""
        acct_number = input("Please provide an account number for the new account.\n> ") # Assume that the number is within the constraints
        name = input("Please enter a name for the account.\n> ")
        # make function that checks acct_number and name for valid formats and if the account number exists
        #updates the valid accounts list after the format is valid?
        self.session_write("createacct")
        self.session_write(acct_number)
        self.session_write(name)
        

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


    def transfer(self):
        """Transfer"""
        from_acct_number = input("Please provide the account number you wish to transfer from.\n> ")
        to_acct_number = input("Please provide the account number you wish to transfer to.\n> ")
        amount = input("What is your transfer amount?: ")
        self.session_write("transfer")
        self.session_write(from_acct_number)
        self.session_write(to_acct_number)
        self.session_write(amount)
'''
if __name__ == '__main__':
    a = App("valid_acct_file.txt", "trans_sum_file.txt")
'''