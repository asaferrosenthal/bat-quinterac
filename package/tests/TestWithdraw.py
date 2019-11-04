import tempfile
from importlib import reload
import os
import io
import sys
import package
from package.app import app

path = os.path.dirname(os.path.abspath(__file__))

class TestDepositR1:
    def testAtmValidateWithdraw(self, capsys):
        """Testing R1T1. 
        Purpose:
            Checks if money was successfully withdrawn in ATM mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'wdr',
                '1234567',
                '500',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 500",
                "Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 1234567 50000 1234567 ***'
            ]
        )

    def testAgentValidateDeposit(self, capsys):
        """Testing R1T2. 
        Purpose:
            Checks if money was successfully withdrawn in Agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'wdr',
                '1234567',
                '500',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 500",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 1234567 50000 1234567 ***'
            ]
        )

class TestWithdrawR2:   
    def testAtmDailyWithdrawalLimit(self, capsys):
        """Testing R2T1. 
        Purpose:
            Checks if daily amount withdrawn exceeds $5000
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'wdr',
                '0123456',
                '4900',
                'back',
                '2',
                'wdr',
                '0123456',
                '200',
                '0123456',
                '1',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 4900",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: The new withdrawl amount will go over your daily limit.",
                "Current amount:4900 Please try again.",
                "Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 1",
                "Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 1234567 0 1234567 ***'
            ]
        )

class TestWithdrawR3:
    def testAtmValidWithdrawAmount(self, capsys):
        """Testing R3T1. 
        Purpose:
            Checks if the withdrawal amount in ATM mode exceeds $1000
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'wdr',
                '0012345',
                '100100',
                '0012345',
                '0',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: The new withdrawl amount will go over your daily limit.",
                "Current amount:0 Please try again.",
                "Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 0",
                "Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 0012345 0 0012345 ***'
            ]
        )


class TestWithdrawR4:   
    def testAtmDailyWithdrawLimit(self, capsys):
        """Testing R4T1. 
        Purpose:
            Checks if same account has withdrawn more that $999,999.99 in Agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'wdr',
                '0012345',
                '999998',
                'wdr',
                '0012345',
                '2',
                '0012345',
                '1',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 999998",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: The new withdrawl amount will go over your daily limit.",
                "Current amount:999998 Please try again.",
                "Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 1",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 0012345 999999800 0012345 ***'
                'WDR 0012345 100 0012345 ***'
            ]
        )

class TestWithdrawR5:   
    def testAtmValidWithdrawAccount(self, capsys):
        """Testing R5T1. 
        Purpose:
            Checks if the account is valid in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'wdr',
                '0',
                '0',
                '1234567',
                '0',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: No account found with number: 0 Please try again.",
                "Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 0",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 1234567 0 1234567 ***'
            ]
        )

    def testAgentValidWithdrawAccount(self, capsys):
        """Testing R5T2. 
        Purpose:
            Checks if the account is valid in agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'wdr',
                '0',
                '0',
                '1234567',
                '0',
                'back',
                'logout'
            ],
            intput_valid_accounts=[
                '1234567',
                '0123456',
                '0012345'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: No account found with number: 0 Please try again.",
                "Please provide an account number you wish to withdraw from.",
                "> What is your withdrawal amount?: withdrew 0",
                "Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"
            ],
            expected_output_transactions=[
                'WDR 1234567 0 1234567 ***'
            ]
        )

def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
    ):
    """Helper function for testing
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(package)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transactionSummaryFile = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    validAccountsListFile = temp_file2
    sessionFile = temp_fd2
    with open(validAccountsListFile, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'package',
        validAccountsListFile,
        transactionSummaryFile,
        sessionFile]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.App(validAccountsListFile, transactionSummaryFile, sessionFile)

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a 
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output) + 1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    with open(transactionSummaryFile, 'r') as of:
        content = of.read().splitlines()

        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)

        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
