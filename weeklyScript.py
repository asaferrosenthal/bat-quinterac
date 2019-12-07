import os
from time import sleep
from dailyScript import Daily

class Weekly:

    def __init__(self):
        validAccounts = open('quinterac/validAccountsListFile.txt', 'r')
        self.inputValidAccounts = validAccounts.readlines()  
        self.runWeek()

    def runWeek(self):
        """
        This method runs the daily script 5 times. Each time with three different transaction sets.
        """
        day = 1
        while day <= 5:
            transactionInputs1 = self.transactionSetOne(day)
            transactionInputs2 = self.transactionSetTwo(day)
            transactionInputs3 = self.transactionSetThree(day)
            a = Daily(transactionInputs1, transactionInputs2, transactionInputs3, self.inputValidAccounts)
            os.system("python3 -m quinteracBackend")    # Command runs the backend after the day is done.
            day = day + 1

    def transactionSetOne(self, day):
        """ 5 Days of one transaction set"""
        if day == 1:     # Valid accounts list is empty, so new accounts must be made on the first day.
            transactionInputs = [
                'login',
                '1',
                'new',
                '7777776',
                'Ben',
                'back',
                'logout'
            ]

        elif day == 2:
            transactionInputs = [
                'login',
                '1',
                'dep',
                '7777776',
                '7777',
                'back',
                'logout'
            ]

        elif day == 3:
            transactionInputs = [
                'login',
                '2',
                'wdr',
                '7777776',
                '500',
                'back',
                'logout'
            ]

        elif day == 4:
            transactionInputs = [
                'login',
                '2',
                'xfr',
                '7777776',
                '4444444',
                '10',
                'back',
                'logout'
            ]
        else:
            transactionInputs = [
                'login',
                '1',
                'del',
                '7777776',
                'Ben',
                'back',
                'logout'
            ]

        return transactionInputs

    def transactionSetTwo(self, day):
        """ 5 Days of another transaction set"""
        if day == 1:     # Valid accounts list is empty, so new accounts must be made on the first day.
            transactionInputs = [
                'login',
                '1',
                'new',
                '4444444',
                "Aaron",
                'back',
                'logout'
            ]

        elif day == 2:
            transactionInputs = [
                'login',
                '1',
                'dep',
                '4444444',
                '69420',
                'back',
                'logout'
            ]

        elif day == 3:
            transactionInputs = [
                'login',
                '2',
                'wdr',
                '4444444',
                '500',
                'back',
                'logout'
            ]

        elif day == 4:
            transactionInputs = [
                'login',
                '2',
                'xfr',
                '1122334',
                '4444444',
                '10',
                'back',
                'logout'
            ]
        else:
            transactionInputs = [
                'login',
                '1',
                'del',
                '4444444',
                'Aaron',
                'back',
                'logout'
            ]

        return transactionInputs

    def transactionSetThree(self, day):
        """ 5 Days of the last transaction set"""
        if day == 1:    # Valid accounts list is empty, so new accounts must be made on the first day.
            transactionInputs = [
                'login',
                '1',
                'new',
                '1122334',
                "Tamir",
                'back',
                'logout'
            ]

        elif day == 2:
            transactionInputs = [
                'login',
                '1',
                'dep',
                '1122334',
                '200',
                'back',
                'logout'
            ]

        elif day == 3:
            transactionInputs = [
                'login',
                '2',
                'wdr',
                '1122334',
                '100',
                'back',
                'logout'
            ]
        
        elif day == 4:
            transactionInputs = [
                'login',
                '2',
                'xfr',
                '7777776',
                '1122334',
                '10',
                'back',
                'logout'
            ]

        else:
            transactionInputs = [
                'login',
                '1',
                'del',
                '1122334',
                'Tamir',
                'back',
                'logout'
            ]

        return transactionInputs
        

if __name__ == "__main__":
    a = Weekly()