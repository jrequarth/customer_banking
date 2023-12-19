# customer_banking

This program determines the account balances and interest earned for 2 different types of account: savings and certificate of deposit (cd)

The Account class is created in the Accounts.py file
The Accounts.py file is used by both accounts to get and return the balance and the accrued interest.
Variables:
    balance
    interest = interest accrued not interest rate

The customer_banking.py file prompts the user to enter balance, interest rate, and months to maturity for the savings and for the cd accounts. These data are collected by a create_savings_account function and create_cd_account function, respectively. 
These data are passed to their respective files.
Variables input by the user:
    savings_balance
    savings_interest_rate
    savings_maturity
    cd_balance
    cd_interest
    cd_maturity
Variables returned from the savings and cd files:
    new_balance
    new_interest
    new_cd_balance
    accrued_cd_interest

In the savings_account.py program takes in the create_savings_account function with initial balance, interest rate, and months to maturity. These data are used to determine the new balance and the interest earned. The Account class is then called from the Accounts file. The new balance and interest earned parameters are passed, updated, and called. The new balance and interest earned is printed out.
Function: create_savings_account(balance, interest_rate, months)
Variables:
    Balance
    interest_rate
    months
    current_data = calls the Account class
    int_accrued = the amount of interest earned during the time period
    new_balance = old balance + int_accrued

In the cd_account.py program takes in the create_cd_account function with initial balance, interest rate, and months to maturity. These data are used to determine the new balance and the interest earned. 
The Account class is then called from the Accounts file. The new balance and interest earned parameters are passed, updated, and called. The new balance and interest earned is printed out.
Function: create_cd_account(balance, interest_rate, months)
Variables:
    Balance
    interest_rate
    months
    current_cd_data = calls the Account class
    cd_int_accrued = the amount of interest earned during the time period
    new_cd_balance = old balance + int_accrued

