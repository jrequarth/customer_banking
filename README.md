# customer_banking

This program determines the account balances and interest earned for 2 different types of account: savings and certificate of deposit (cd)

The Accounts.py file is used by both accounts to get and return the balance and the accrued interest.

The customer_banking.py file prompts the used to enter balance, interest rate, and months to maturity for the savings and for the cd accounts. These data are collected by a create_savings_account function and create_cd_account function, respectively. 
These data are passed to their respective files. 

In the savings_account.py program takes in the create_savings_account function with initial balance, interest rate, and months to maturity. These data are used to determine the new balance and the interest earned. 

The Account class is then called from the Accounts file. The new balance and interest earned parameters are passed, updated, and called. The new balance and interest earned is printed out.

In the cd_account.py program takes in the create_cd_account function with initial balance, interest rate, and months to maturity. These data are used to determine the new balance and the interest earned. 

The Account class is then called from the Accounts file. The new balance and interest earned parameters are passed, updated, and called. The new balance and interest earned is printed out.

