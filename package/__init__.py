import sys
from frontend import app





if __name__ == '__main__':
    try:
        valid_acct_file = sys.argv[1]
        trans_sum_file = sys.argv[2]
    except IndexError:
        print("must have valid arguments")

    a = app.App(str(valid_acct_file), str(trans_sum_file))
