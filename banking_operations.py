from database import accounts
def check_balance(acc_num):
    if acc_num in accounts:
        return accounts[acc_num][1]
    return None

def withdraw_money(acc_num, amount):
    if acc_num not in accounts:
        return False, "Account not found"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    if amount > accounts[acc_num][1]:
        return False, "Insufficient balance"
    
    accounts[acc_num][1] -= amount
    return True, accounts[acc_num][1]

def deposit_money(acc_num, amount):
    if acc_num not in accounts:
        return False, "Account not found"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    
    accounts[acc_num][1] += amount
    return True, accounts[acc_num][1]

def authenticate_user(acc_num, pin):
    if acc_num in accounts:
        if accounts[acc_num][0] == pin:
            return True, accounts[acc_num][2]
        return False, "Incorrect PIN"
    return False, "Account not found"
