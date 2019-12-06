import tempfile
from importlib import reload
import os
import io
import sys
import quinterac
from quinterac import FrontEnd

path = os.path.dirname(os.path.abspath(__file__))


def helper(terminal_input, input_valid_accounts):

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
    FrontEnd.FrontEnd(validAccountsListFile, transactionSummaryFile)

    os.close(temp_fd)
    os.close(temp_fd2)
    os.close(temp_fd3)

    os.remove(temp_file)
    os.remove(temp_file2)
    os.remove(temp_file3)


def main():
    terminal_input=[
                'login',
                '2',
                'dep',
                '7777776',
                '1000',
                'back',
                'logout'
            ]
    valid_accounts = open('quinterac/validAccountsListFile.txt', 'r')
    input_valid_accounts = valid_accounts.readlines()
    helper(terminal_input, input_valid_accounts)

main()

    