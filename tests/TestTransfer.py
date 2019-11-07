import tempfile
from importlib import reload
import os
import io
import sys
import quinterac
from quinterac import app

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
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 1234567 50000 0123456 ***'
            ]
        )

    def testAgentValidateTransfer(self, capsys):
        """Testing R1T2.
        Purpose:
            Checks if money was transferred between accounts in Agent mode
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
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 1234567 50000 0123456 ***'
            ]
        )


class TestTransferR2:
    def testAtmValidFirstAccountTransfer(self, capsys):
        """Testing R2T1.
        Purpose:
            Checks if first (to) account is valid in atm mode
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
                '0123456',
                '0',
                '1234567',
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: The to account provided does not exist. Please try again.",
                "Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 1234567 1 0123456 ***'
            ]
        )

    def testAtmValidSecondAccountTransfer(self, capsys):
        """Testing R2T2.
        Purpose:
            Checks if second (from) account is valid in atm mode
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
                '0',
                '1234567',
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: The from account provided does not exist. Please try again.",
                "Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 0123456 1 1234567 ***'
            ]
        )

    def testAgentValidFirstAccountTransfer(self, capsys):
        """Testing R2T3.
        Purpose:
            Checks if first (to) account is valid in agent mode
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
                '0123456',
                '0',
                '1234567',
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: The to account provided does not exist. Please try again.",
                "Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 1234567 1 0123456 ***'
            ]
        )

    def testAgentValidSecondAccountTransfer(self, capsys):
        """Testing R2T4.
        Purpose:
            Checks if second (from) account is valid in agent mode
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
                '0',
                '1234567',
                '0123456',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
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
                "> Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: The from account provided does not exist. Please try again.",
                "Please provide the account number you wish to transfer to.",
                "> Please provide the account number you wish to transfer from.",
                "> What is your transfer amount?: Transferred: 1, from: 0123456, to: 1234567",
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
                'XFR 0123456 1 1234567 ***'
            ]
        )


class TestTransferR3:
    def testAtmTransferLimit(self, capsys):
        """Testing R3T1.
        Purpose:
            Checks if transfer amount exceeds $10,000 in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '1111111',
                '2222222',
                '10001',
                '1111111',
                '2222222',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide the account number you wish to transfer to.',
             '> Please provide the account number you wish to transfer from.',
             '> What is your transfer amount?: Transferred: 10001, from: 2222222, to: 1111111',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             "> Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
             " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                'XFR 2222222 1 1111111 ***'
            ]
        )


class TestTransferR4:
    def testAgentTransferLimit(self, capsys):
        """Testing R4T1.
        Purpose:
            Checks if transfer amount exceeds $999,999 in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '1',
                'xfr',
                '1111111',
                '2222222',
                '1000000',
                '1111111',
                '2222222',
                '1',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide the account number you wish to transfer to.',
             '> Please provide the account number you wish to transfer from.',
             '> What is your transfer amount?: Transferred: 1000000, from: 2222222, to: 1111111',
             "Type 'back' to go back to mode selection.", "Enter: 'new' to Create Account",
             "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", "> Type 'back' to go back to mode selection.",
             "Enter: 'new' to Create Account", "Enter: 'del' to Delete Account", "Enter: 'wdr' to Withdraw",
             "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                'XFR 2222222 1 1111111 ***'
            ]
        )


class TestTransferR5:
    def testAtmDailyTransferLimit(self, capsys):
        """Testing R5T1.
        Purpose:
            Checks if daily total transfer amount exceeds $10,000 in atm mode
        Arguments:
            capsys -- object created by pytest to capture stdout and stderr
        """
        helper(
            capsys=capsys,
            terminal_input=[
                'login',
                '2',
                'xfr',
                '1111111',
                '1234567',
                '100',
                'back',
                'logout'
            ],
            input_valid_accounts=[
                '1234567',
                '0123456',
                '1111111',
                '2222222'
            ],
            expected_tail_of_terminal_output=
            ["Enter 'login' to begin. Or 'exit' to exit program.", '> Please choose a mode.', " '1' for agent",
             " '2' for machine.", " 'logout' to quit.", "> Type 'back' to go back to mode selection.",
             "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit", "Enter: 'xfr' to Transfer",
             '> Please provide the account number you wish to transfer to.',
             '> Please provide the account number you wish to transfer from.',
             '> What is your transfer amount?: Transferred: 100, from: 1234567, to: 1111111',
             "Type 'back' to go back to mode selection.", "Enter: 'wdr' to Withdraw", "Enter: 'dep' to Deposit",
             "Enter: 'xfr' to Transfer", '> Please choose a mode.', " '1' for agent", " '2' for machine.",
             " 'logout' to quit.", '> Exiting program'],
            expected_output_transactions=[
                'XFR 2222222 1 1111111 ***'
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

    # cleanup quinterac
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
