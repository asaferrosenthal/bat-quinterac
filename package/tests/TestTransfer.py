import tempfile
from importlib import reload
import os
import io
import sys
import package
from package.app import app

path = os.path.dirname(os.path.abspath(__file__))


class TestTransferR1:
    def testAtmValidateTransfer(self, capsys):
        """Testing R1T1. 
        Purpose:
            Checks if money was transferred between accounts in ATM mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '1234567',
                '0000000',
                '500',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Please provide an account number you wish to transfer to.\n>",
                "Please provide an account number you wish to transfer from.\n>",
                # fix ^ message
                "What is your transfer amount?: ",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                'XFR 0000000 50000 1234567 ***'
            ]
        )

    def testAgentValidateTransfer(self, capsys):
        """Testing R1T2. 
        Purpose:
            Checks if money was successfully transferred between accounts
            in Agent mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '1234567',
                '0000000',
                '500',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Please provide an account number you wish to transfer to.\n>",
                "Please provide an account number you wish to transfer from.\n>",
                # fix ^ message
                "What is your withdrawal amount?: ",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            # need to fix menu for agent!!
            expected_output_transactions=[
                'WDR 0000000 50000 1234567 ***'
            ]
        )


class TestTransferR2:
    def testAtmValidFirstAccountTransfer(self, capsys):
        """Testing R2T1. 
        Purpose:
            Checks if the first (to) account is valid
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '0',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Please provide an account number you wish to transfer to.\n>",
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )

    def testAtmValidSecondAccountTransfer(self, capsys):
        """Testing R2T2. 
        Purpose:
            Checks if the second account is valid
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '1234567',
                '0',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Please provide an account number you wish to transfer to.\n>",
                "Please provide an account number you wish to transfer from.\n>",
                # fix ^ message
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )

    def testAgentValidFirstAccountTransfer(self, capsys):
        """Testing R2T3. 
        Purpose:
            Checks if the first (to) account is valid
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '0',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                # fix agent menu
                "Please provide an account number you wish to transfer to.\n>",
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )

    def testAtmValidSecondAccountTransfer(self, capsys):
        """Testing R2T4. 
        Purpose:
            Checks if the second account is valid
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '1234567',
                '0',
                'exit',
                'exit',
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                # fix agent menu
                "Please provide an account number you wish to transfer to.\n>",
                "Please provide an account number you wish to transfer from.\n>",
                # fix ^ message
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )


class TestTransferR3:
    def testAtmTransferLimit(self, capsys):
        """Testing R3T1. 
        Purpose:
            Checks if transfer amount exceeds $10000 in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '1234567',
                '0000000',
                '10001',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Please provide an account number you wish to transfer to.\n>",
                "What is your withdrawal amount?: ",
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )


class TestTransferR4:
    def testAtmDailyTransferLimit(self, capsys):
        """Testing R4T1.
        Purpose:
            Checks if transfer amount exceeds $999999.99 in Agent Mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '1234567',
                '0000000',
                '1000000',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                "Enter 'login' to begin. Or 'exit' to exit program.",
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                # finish agent menu
                "Please provide an account number you wish to transfer to.\n>",
                "What is your withdrawal amount?: ",
                # error message
                "Enter: 'wdr' to Withdraw\n\
                Enter: 'dep' to Deposit\n\
                Enter: 'xfr' to Transfer\n\
                Enter: 'exit' to Exit\n\
                >",
                "Enter 'login' to begin. Or 'exit' to exit program."
            ],
            expected_output_transactions=[
                None
            ]
        )


class TestTransferR5:
    def testAgentTransferLimit(self, capsys):
        """Testing R5T1. 
        Purpose:
            Checks if daily transfer amount exceeds $10000 in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """

        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '1234567',
                '0000000',
                '9000',
                'xfr',
                '1234567',
                '0000000',
                '1001',
                'exit',
                'exit'
            ],
            intput_valid_accounts=[
                '1234567',
                '0000000'
            ],
            expected_tail_of_terminal_output=[
                # just doing tail here, since it's not worth adding so many transactions
                # fix error message
            ],
            expected_output_transactions=[
                "XFR 0000000 900000 1234567 ***"
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
