from enum import Enum


class Error(Enum):
    newAccount = "Cannot perform a transaction on a new account in the same session."
    overDepositLimit = "The new deposit amount will go over your daily limit."
    overWithdrawalLimit = "The new withdrawal amount will go over your daily limit."
    overTransferLimit = "The new transfer amount will go over your daily limit."
    negativeBalance = "Account balance can not be negative."
    accountExists = "An account already exists with this number."
    accountHasBalance = "Unable to delete account with non-zero balance."
    noAccounts = "No accounts exists"
