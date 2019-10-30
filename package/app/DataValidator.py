"""
Demonstrates the constraints behind the 3 transactions:
    - Deposit
    - Withdrawal
    - Transfer
As well as writing completed transactions to the daily transactions file

Input files: Daily transaction file (valid account list in completed version)
Output files: Updated daily transaction file
"""a


# Used in place of a real account number validator
def AccountValid(account_number):
    return True


# Validates a deposit amount
# Inputs: deposit amount, account number and atm/agent mode
# Output: True for valid amount, False for invalid
def DepositAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 2000 and dailyAmountValid(amount, account_number, "DEP"):
            return True
    elif amount < 999999.99:
        return True
    return False


# Validates a withdrawal amount
# Inputs: withdrawal amount, account number and atm/agent mode
# Output: True for valid amount, False for invalid
def WithdrawalAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 1000 and dailyAmountValid(amount, account_number, "WDR"):
            return True
    elif amount < 999999.99:
        return True
    return False


# Validates a transfer amount
# Inputs: transfer amount, both account numbers and atm/agent mode
# Output: True for valid amount, False for invalid
def TransferAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 10000 and dailyAmountValid(amount, account_number, "XFR"):
            return True
    elif amount < 999999.99:
        return True
    return False


# Validates a transaction amount based on daily total limits
# Inputs: transaction amount, account number, and transaction type
# Output: True for valid amount, False for invalid
def dailyAmountValid(amount, account_number, transCode):
    dailyAmount = amount
    TransactionList = getTransList()
    for transaction in TransactionList:
        if transaction[0] == transCode and transaction[1] == account_number:
            dailyAmount += (int(transaction[2]) / 100)
    print("daily withdrawal amount:", dailyAmount)  # flag
    if ((transCode == "DEP" or transCode == "WDR") and dailyAmount < 5000) or \
            (transCode == "XFR" and dailyAmount < 10000):
        return True
    dailyAmount -= amount
    return False


# Reads the daily transaction list and
#   makes a list of current daily transactions
# Inputs: aaily transactions file
# Output: a list of current daily transactions
def getTransList():
    TransactionList = []
    f = open("dailyTransactionFile.txt", "r")
    data = f.readlines()
    for line in data:
        line = line.split()
        TransactionList.append(line)
    # print(TransactionList) #flag
    return TransactionList


# Takes an account number from the user
# Inputs: User inputed account number
# Output: a (valid) account number
#   (False if account number is invalid)
def getAccountNumber():
    account_number = input("What is your account number?: ")
    if AccountValid(account_number):
        return account_number
    return False


# Updates the daily transaction file with completed transaction
# Inputs: transaction type, amount, account number(s)
# Output: updated daily transaction file
def updateTransactionFile(transCode, amount, account_number1, account_number2):
    f = open("dailyTransactionFile.txt", "a")
    newLine = transCode + " " + account_number1 + " " + str(amount * 100) + " " + account_number2 + " Aaron\n"
    print("Transaction Summary:", newLine)  # flag
    f.write(newLine)
    f.close()


# Drives the deposit transaction
# Inputs: atm/agent mode
# Outputs: updated daily transaction file for a valid transaction
#   Error message for invalid transaction
def deposit(atm_mode):
    account_number = getAccountNumber()
    if account_number:
        amount = int(input("What is your deposit amount?: "))
        if DepositAmountValid(amount, account_number, atm_mode):
            updateTransactionFile("DEP", amount, account_number, account_number)
        else:
            print("not valid")


# Drives the withdrawal transaction
# Inputs: atm/agent mode
# Outputs: updated daily transaction file for a valid transaction
#   Error message for invalid transaction
def withdrawal(atm_mode):
    account_number = getAccountNumber()
    if account_number:
        amount = int(input("What is your withdrawal amount?: "))
        if WithdrawalAmountValid(amount, account_number, atm_mode):
            updateTransactionFile("WDR", amount, account_number, account_number)
        else:
            print("not valid")


# Drives the transfer transaction
# Inputs: atm/agent mode
# Outputs: updated daily transaction file for a valid transaction
#   Error message for invalid transaction
def transfer(atm_mode):
    account_number1 = getAccountNumber()
    account_number2 = getAccountNumber()
    if account_number1 and account_number2:
        amount = int(input("What is your transfer amount?: "))
        if TransferAmountValid(amount, account_number1, atm_mode):
            updateTransactionFile("XFR", amount, account_number1, account_number2)
        else:
            print("not valid")


# Changes mode to atm or agent
# Input: user input for atm/agent mode
# Output: user selected mode
def checkMode():
    mode = input("<atm> | <agent> - ")
    print("")
    if mode == "atm":
        return True
    return False


# Chooses transaction type
# Input: atm/agent mode, user input for transaction type, daily transaction file
# Output: completed daily transaction file
def checkTrans(atm_mode):
    trans = input("<DEP> | <WDR> | <XFR> | <empty> for done - ")
    if trans.lower() == "dep":
        deposit(atm_mode)
    elif trans.lower() == "wdr":
        withdrawal(atm_mode)
    elif trans.lower() == "xfr":
        transfer(atm_mode)
    else:
        f = open("dailyTransactionFile.txt", "a")
        f.write("END OF SUMMARY")
        f.close()
        return True


# Main function which drives the program
# Demonstrates the constraints behind the 3 transactions:
#   Deposit, Withdrawal and Transfer
# As well as writing completed transactions to the daily transactions file
def main():
    f = open("dailyTransactionFile.txt", "w")
    f.close()
    done = False
    atm_mode = checkMode()
    while not done:
        done = checkTrans(atm_mode)


main()
