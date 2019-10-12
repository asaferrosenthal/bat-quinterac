def AccountValid(account_number):
    return True

def DepositAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 2000 and dailyAmountValid(amount, account_number, "DEP"):
            return True
    elif amount < 999999.99:
        return True
    return False

def WithdrawalAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 1000 and dailyAmountValid(amount, account_number, "WDR"):
            return True
    elif amount < 999999.99:
        return True
    return False

def TransferAmountValid(amount, account_number, atm_mode):
    if atm_mode:
        if amount < 10000 and dailyAmountValid(amount, account_number, "XFR"):
            return True
    elif amount < 999999.99:
        return True
    return False

def dailyAmountValid(amount, account_number, transCode):
    dailyAmount = amount
    TransactionList = getTransList()
    for transaction in TransactionList:
        if transaction[0] == transCode and transaction[1] == account_number:
            dailyAmount += (int(transaction[2])/100)
    print("daily withdrawal amount:", dailyAmount) #flag
    if ((transCode == "DEP"  or transCode == "WDR") and dailyAmount < 5000) or \
       (transCode == "XFR" and dailyAmount < 10000):
        return True
    dailyAmount -= amount
    return False
    
def getTransList():
    TransactionList = []
    f = open("dailyTransactionFile.txt", "r")
    data = f.readlines()
    for line in data:
        line = line.split()
        TransactionList.append(line)
    #print(TransactionList) #flag
    return TransactionList

def getAccountNumber():
    account_number = input("What is your account number?: ")
    if AccountValid(account_number):
        return account_number
    return False

def updateTransactionFile(trans, amount, account_number1, account_number2):
    f = open("dailyTransactionFile.txt", "a")
    newLine = trans + " " + account_number1 + " " + str(amount*100) + " " + account_number2 + " Aaron\n"
    print("Transaction Summary:", newLine) #flag
    f.write(newLine)
    f.close()

def deposit(atm_mode):
    account_number = getAccountNumber()
    if account_number:
        amount = int(input("What is your deposit amount?: "))
        if DepositAmountValid(amount, account_number, atm_mode):
            updateTransactionFile("DEP", amount, account_number, account_number)
        else:
            print("not valid")

def withdrawal(atm_mode):
    account_number = getAccountNumber()
    if account_number:
        amount = int(input("What is your withdrawal amount?: "))
        if WithdrawalAmountValid(amount, account_number, atm_mode):
            updateTransactionFile("WDR", amount, account_number, account_number)
        else:
            print("not valid")

def transfer(atm_mode):
    account_number1 = getAccountNumber()
    account_number2 = getAccountNumber()
    if account_number1 and account_number2:
        amount = int(input("What is your transfer amount?: "))
        if TransferAmountValid(amount, account_number1, atm_mode):
            updateTransactionFile("XFR", amount, account_number1, account_number2)
        else:
            print("not valid")

def checkMode():
    mode = input("<atm> | <agent> - ")
    print("")
    if mode == "atm":
        return True
    return False

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
    
def main():
    f = open("dailyTransactionFile.txt", "w")
    f.close()
    done = False
    atm_mode = checkMode()
    while not done:
        done = checkTrans(atm_mode)

main()
