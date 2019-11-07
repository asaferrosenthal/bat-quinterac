import tempfile
from importlib import reload
import os
import io
import sys
import quinterac
from quinterac import app

path = os.path.dirname(os.path.abspath(__file__))


class TestCreateAccountR1:
    """
    Purpose:
        Only accepted in Agent mode.
    """
    def testValidCreateAccountTransaction(self, capsys):
        """
        Test is the same as R2T1.
        This is written to maintain consistency with assignment 1 table.
        """
        assert True


class TestCreateAccountR2:
    """
    Purpose:
        New account number is 7 decimal digits not beginning with 0.
    """

    def testValidAccountDigit(self, capsys):
        """Testing R2T1.
        Purpose:
            Check if the account number are digits and has a length of 7
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '1122334',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 1122334 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testValidAccountStartingDigit(self, capsys):
        """Testing R2T2.
        Purpose:
            Check if the account number starts with a zero.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '0122334',
                'ben',
                '7654328',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> Cant start with zero Please try again.",
                "Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 7654328 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )


class TestCreateAccountR3:
    """
    Purpose:
        New account number must be different from all other account numbers.
    """
    def testValidAccountNumber(self, capsys):
        """Testing R3T1.
        Purpose:
            Checks if account number already exits.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '1234567',
                'ben',
                '7624328',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567\n',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> That account number already exits. Please Choose a different one. Please try again.",
                "Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 7624328 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )


class TestCreateAccountR4:
    """
    Purpose:
       New account name is between 3 and 30 alphanumeric characters not starting or ending with a space.
    """

    def testAccountNameLength(self, capsys):
        """Testing R4T1.
        Purpose:
            Checks if the account name is between 3 and 30 characters.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '1034567',
                'b',
                '1034567',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567\n',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> Account name must be between 3 and 30 characters in length. Please try again.",
                "Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 1034567 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testAlphanumericCharacters(self, capsys):
        """Testing R4T2.
        Purpose:
            Checks if the account name only consists of alphanumeric characters (except a space).
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '1004567',
                '---',
                '1004567',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567\n',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> Can only be alphanumeric characters Please try again.",
                "Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 1004567 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testValidSpaceCharacter(self, capsys):
        """Testing R4T3.
        Purpose:
            Checks if a space character is not at the end or beginning of an account name.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '1024567',
                ' ben',
                '1024567',
                'ben',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567\n',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> Name cant start with space Please try again.",
                "Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                '> Created new account: 1024567 – ben',
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )


class TestCreateAccountR5:
    """
    Purpose:
        No Transactions on new account accepted.
    """
    def testTransactionsOnNewAccount(self, capsys):
        """Testing R5T1.
        Purpose:
            Checks if a transaction was attempted on the new account.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'new',
                '7777777',
                'ben',
                'dep',
                '7777777',
                '10',
                '1234567',
                '10',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
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
                "> Please provide an account number for the new account.",
                "> Please enter a name for the account.",
                "> Created new account: 7777777 – ben",
                "Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please provide an account number you wish to deposit into.",
                "> What is your deposit amount?: Cannot perform a transaction on a new account in the same session. Current amount: 0. Please try again.",
                "Please provide an account number you wish to deposit into.",
                "> What is your deposit amount?: Deposited $10 into account number: 1234567",
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
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        input_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing
    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        input_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(quinterac)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transactionSummaryFile = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    validAccountsListFile = temp_file2

    temp_fd3, temp_file3 = tempfile.mkstemp()
    sessionFile = temp_file3

    with open(validAccountsListFile, 'w') as wf:
        wf.write('\n'.join(input_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'quinterac',
        validAccountsListFile,
        transactionSummaryFile,
        sessionFile]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.App(validAccountsListFile, transactionSummaryFile)

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', input_valid_accounts)
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
    os.close(temp_fd2)
    os.close(temp_fd3)

    os.remove(temp_file)
    os.remove(temp_file2)
    os.remove(temp_file3)
