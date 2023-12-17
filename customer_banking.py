# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = print(float(input("How much money is in your savings account?")))
    savings_interest_rate = print(float(input("What is the interest rate in %")))
    savings_maturity =  print(float(input("How long to maturity?")))

    # Call the create_savings_account function and pass the variables from the user. ???????
    updated_savings_data(balance, interest) = create_savings_account(savings_balance, 
        savings_interest_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your account balance is $", format(updated_savings_data.balance(), ",.2f"))
    print("You earned $", format(updated_savings_data.interest(), ",.2f, in interest"))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = print(float(input("How much will you add to the Certificate of Deposit?")))
    cd_interest = print(float(input("what is the interest rate?")))
    cd_maturity = print(float(input("How long to maturity?")))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_data(balance, interest) = create_cd_account(cd_balance, cd_interest, 
        cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your new CD balance is $", format(updated_cd_data.balance(), ",.2f"))
    print("You earned $", format(updated_cd_data.interest(), ",.2f, in interest"))

if __name__ == "__main__":
    # Call the main function.