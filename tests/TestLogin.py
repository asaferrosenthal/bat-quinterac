import tempfile
from importlib import reload
import os
import io
import sys
import quinterac
from quinterac import FrontEnd

path = os.path.dirname(os.path.abspath(__file__))


class TestLoginR1:
    def testIdleLogout(self, capsys):
        """Testing R1T1.
        Purpose:
            Can't logout before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'logout',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testIdleCreateAccount(self, capsys):
        """Testing R1T2.
        Purpose:
            Can't create account before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'new',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testIdleDeleteAccount(self, capsys):
        """Testing R1T3.
        Purpose:
            Can't delete account before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'del',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testIdleDeposit(self, capsys):
        """Testing R1T4.
        Purpose:
            Can't deposit before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'dep',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testIdleWithdraw(self, capsys):
        """Testing R1T4.
        Purpose:
            Can't withdraw before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'wdr',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )

    def testIdleTransfer(self, capsys):
        """Testing R1T6.
        Purpose:
            Can't transfer before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'xfr',
                'exit'
            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "> Enter 'login' to begin. Or 'exit' to exit program.",
                "> Exiting program"],
            expected_output_transactions=[
                None
            ]
        )


class TestLoginR2:

    def testAdditionalLoginAttempt(self, capsys):
        """Testing R1T6.
        Purpose:
            Can't transfer before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                'login',
                'logout'

            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                '> Please choose a mode.',
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                '> Already logged in.',
                'Please choose a mode.',
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                '> Exiting program'],
            expected_output_transactions=[
                "EOS 0000000 000 0000000 ***"
            ]
        )


class TestLoginR3:

    def testAtmCreateAccountAfterLogin(self, capsys):
        """Testing R3T1. 
        Purpose:
            Can't transfer before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'new',
                'back',
                'logout'

            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                '> Please choose a mode.',
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                '> Please choose a mode.',
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"],
            expected_output_transactions=[
                "EOS 0000000 000 0000000 ***"
            ]
        )

    def testAtmDeleteAccountAfterLogin(self, capsys):
        """Testing R3T2. 
        Purpose:
            Can't transfer before logging in.
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'del',
                'back',
                'logout'

            ],
            input_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Type 'back' to go back to mode selection.",
                "Enter: 'wdr' to Withdraw",
                "Enter: 'dep' to Deposit",
                "Enter: 'xfr' to Transfer",
                "> Please choose a mode.",
                " '1' for agent",
                " '2' for machine.",
                " 'logout' to quit.",
                "> Exiting program"],
            expected_output_transactions=[
                "EOS 0000000 000 0000000 ***"
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
    FrontEnd.FrontEnd(validAccountsListFile, transactionSummaryFile)

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
