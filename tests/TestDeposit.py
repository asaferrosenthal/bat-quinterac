import tempfile
from importlib import reload
import os
import io
import sys
import quinterac
from quinterac import app

path = os.path.dirname(os.path.abspath(__file__))


class TestDepositR1:
    def testAtmValidateDeposit(self, capsys):
        """Testing R1T1.
        Purpose:
            Checks if money was successfully deposited in ATM mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'dep',
                '1234567',
                '500',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
                " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
                '> Please provide an account number you wish to deposit into.',
                '> What is your deposit amount?: Deposited $500 into account number: 1234567',
                "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
                " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                'DEP 1234567 50000 1234567 ***'
            ]
        )

    def testAgentValidateDeposit(self, capsys):
        """Testing R1T2.
        Purpose:
            Checks if money was successfully deposited in Agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'dep',
                '1234567',
                '500',
                'back',
                'logout',
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
                " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
                '> Please provide an account number you wish to deposit into.',
                '> What is your deposit amount?: Deposited $500 into account number: 1234567',
                "Type 'back' to go back to mode selection.", "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
                " 'logout' to quit.", '> Exiting program']
            ,
            expected_output_transactions=[
                'DEP 1234567 50000 1234567 ***'
            ]
        )


class TestDepositR2:
    def testAtmValidDepositAmount(self, capsys):
        """Testing R2T1.
        Purpose:
            Checks if the deposit in ATM mode is under $2000
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'dep',
                '1234567',
                '2001',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $2001 into account number: 1234567',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
             " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                None
            ]
        )


class TestDepositR3:
    def testAtmDailyDepositLimit(self, capsys):
        """Testing R3T1.
        Purpose:
            Checks if same account has deposited more than $5000 per day
            in ATM mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """

        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'dep',
                '1234567',
                '2000',
                'dep',
                '1234567',
                '2000',
                'dep',
                '1234567',
                '1001',
                '1234567',
                '1001',
                'back',
                'logout',
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $2000 into account number: 1234567',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $2000 into account number: 1234567',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $1001 into account number: 1234567',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please choose a mode.', " '1' for agent", " '2' for machine.", " 'logout' to quit.",
             '> Exiting program'],
            expected_output_transactions=[
                'DEP 1234567 200000 1234567 ***',
                'DEP 1234567 200000 1234567 ***'
            ]
        )


class TestDepositR4:
    def testAgentDailyDepositLimit(self, capsys):
        """Testing R4T1.
        Purpose:
            Checks if same account has deposited more than $999,999.99 per day
            in Agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """

        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'dep',
                '1234567',
                '1000000',
                '1234567',
                '100000',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $1000000 into account number: 1234567',
             "Type 'back' to go back to mode selection.", "Enter: 'new' to Create Account",
             "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                None
            ]
        )


class TestDepositR5:
    def testAtmValidDepositAccount(self, capsys):
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
                '2',
                'dep',
                '1111111',
                '10',
                'back',
                'logout',
            ],
            input_valid_accounts=[
                '1111111',
                '0000000'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide an account number you wish to deposit into.',
             '> What is your deposit amount?: Deposited $10 into account number: 1111111',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
             " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                None
            ]
        )

    def testAgentValidDepositAccount(self, capsys):
        """Testing R5T2.
        Purpose:
            Checks if account is valid in agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'dep',
                '1234567',
                '0',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
                " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
                "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
                '> Please provide an account number you wish to deposit into.',
                '> What is your deposit amount?: Deposited $0 into account number: 1234567',
                "Type 'back' to go back to mode selection.", "Enter: 'new' to Create Account",
                "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
                " 'logout' to quit.", '> Exiting program'],
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
        'package',
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
