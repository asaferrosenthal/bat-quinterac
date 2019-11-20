import os
from quinteracBackend import BackEnd

curPath = os.path.dirname(__file__)

if __name__ == '__main__':
    try:
        a = BackEnd.BackEnd()
    except IndexError:
        print("Front-end must have two arguments")
