"""
Maria Galante
COP2373
Programming Exercise #9

This program makes a BankAcct class that stores a person's name,
account number, balance amount, and interest rate. The class can
deposit money, withdraw money, change the interest rate, give the
current balance, and calculate interest based on a number of days.
There is also a test function at the bottom to show that all the
methods work.

Student: Maria Galante
Date: 2026-03-31
"""


class BankAcct:
    """
    This class represents one bank account.

    Parameters:
        name (str): account holder name
        account_number (str): bank account number
        amount (float): starting balance
        interest_rate (float): yearly interest rate as a decimal

    Variables:
        self.name (str): account holder name
        self.account_number (str): account number
        self.amount (float): current balance
        self.interest_rate (float): yearly interest rate

    Returns:
        None

    Logical Steps:
        1. Receive the starting values for the account.
        2. Store them in instance variables.
        3. Convert amount and interest rate to float just to be safe.
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        This starts the bank account object with the basic account info.

        Parameters:
            name (str): account holder name
            account_number (str): bank account number
            amount (float): starting balance
            interest_rate (float): yearly interest rate as a decimal

        Variables:
            self.name (str): account holder name
            self.account_number (str): account number
            self.amount (float): current balance
            self.interest_rate (float): yearly interest rate

        Returns:
            None

        Logical Steps:
            1. Save the account holder's name.
            2. Save the account number.
            3. Save the starting balance.
            4. Save the interest rate.
        """
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def adjust_interest_rate(self, new_rate):
        """
        This method changes the account's interest rate.

        Parameters:
            new_rate (float): the new yearly interest rate as a decimal

        Variables:
            new_rate (float): new interest rate value

        Returns:
            None

        Logical Steps:
            1. Receive the new interest rate.
            2. Convert it to float.
            3. Store it in the account object.
        """
        self.interest_rate = float(new_rate)

    def deposit(self, deposit_amount):
        """
        This method adds money to the account balance.

        Parameters:
            deposit_amount (float): amount of money being added

        Variables:
            deposit_amount (float): deposit value

        Returns:
            None

        Logical Steps:
            1. Receive the deposit amount.
            2. Check that it is greater than 0.
            3. Add it to the balance if valid.
        """
        if deposit_amount > 0:
            self.amount += float(deposit_amount)
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, withdraw_amount):
        """
        This method takes money out of the account balance.

        Parameters:
            withdraw_amount (float): amount of money being taken out

        Variables:
            withdraw_amount (float): withdrawal value

        Returns:
            None

        Logical Steps:
            1. Receive the withdrawal amount.
            2. Check that it is greater than 0.
            3. Check that the balance has enough money.
            4. Subtract it from the balance if valid.
        """
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif withdraw_amount > self.amount:
            print("Not enough money in the account.")
        else:
            self.amount -= float(withdraw_amount)

    def give_balance(self):
        """
        This method returns the current account balance.

        Parameters:
            None

        Variables:
            self.amount (float): current balance

        Returns:
            float: the current balance

        Logical Steps:
            1. Look at the current balance.
            2. Return that balance.
        """
        return self.amount

    def calculate_interest(self, days):
        """
        This method calculates simple interest based on the number of days.

        Parameters:
            days (int): number of days interest is being calculated for

        Variables:
            days (int): number of days
            interest_amount (float): calculated interest for that time period

        Returns:
            float: calculated interest amount

        Logical Steps:
            1. Receive the number of days.
            2. Use the balance, interest rate, and days in the formula.
            3. Return the interest amount.

        Formula:
            interest = balance * rate * (days / 365)
        """
        interest_amount = self.amount * self.interest_rate * (days / 365)
        return interest_amount

    def __str__(self):
        """
        This method returns the bank account information as a string.

        Parameters:
            None

        Variables:
            None

        Returns:
            str: formatted account information string

        Logical Steps:
            1. Build a readable string with account info.
            2. Format money values to 2 decimal places.
            3. Return the finished string.
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}")


def test_bank_account():
    """
    This function tests all the methods in the BankAcct class.

    Parameters:
        None

    Variables:
        acct1 (BankAcct): test bank account object
        interest_30_days (float): interest for 30 days
        interest_90_days (float): interest for 90 days

    Returns:
        None

    Logical Steps:
        1. Create a bank account object.
        2. Print starting account info.
        3. Test deposit.
        4. Test withdrawal.
        5. Test balance method.
        6. Test changing the interest rate.
        7. Test interest calculation for different days.
        8. Print results to the screen.
    """

    # making a test bank account
    acct1 = BankAcct("Maria Galante", "45891234", 1000.00, 0.05)

    print("Starting Account Info")
    print(acct1)
    print()

    # testing deposit
    print("Depositing $250.00")
    acct1.deposit(250.00)
    print(acct1)
    print()

    # testing withdrawal
    print("Withdrawing $175.00")
    acct1.withdraw(175.00)
    print(acct1)
    print()

    # testing balance method
    print(f"Current balance from give_balance method: ${acct1.give_balance():.2f}")
    print()

    # testing interest rate change
    print("Changing interest rate to 6%")
    acct1.adjust_interest_rate(0.06)
    print(acct1)
    print()

    # testing interest calculation
    interest_30_days = acct1.calculate_interest(30)
    interest_90_days = acct1.calculate_interest(90)

    print(f"Interest for 30 days: ${interest_30_days:.2f}")
    print(f"Interest for 90 days: ${interest_90_days:.2f}")
    print()

    # testing bad withdrawal just to show it works
    print("Trying to withdraw too much money")
    acct1.withdraw(5000.00)
    print()

    # final account info
    print("Final Account Info")
    print(acct1)


def main():
    """
    This function runs the bank account test.

    Parameters:
        None

    Variables:
        None

    Returns:
        None

    Logical Steps:
        1. Call the test function.
        2. End the program.
    """
    test_bank_account()


main()