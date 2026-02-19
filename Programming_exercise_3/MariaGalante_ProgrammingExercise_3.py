"""
Monthly Expense Analyzer (Programming Exercise 3)

Rules:
- Ask the user to enter their monthly expenses
- User must enter the type of expense and the amount
- Continue asking until the user chooses to stop
- Use reduce() to calculate the total expenses
- Use reduce() to find the highest expense
- Use reduce() to find the lowest expense
- Display the total, highest, and lowest expenses clearly

Student: Maria Galante
Date: 2026-02-18
"""

# Import reduce to be able to calculate totals and compare expenses
from functools import reduce


def get_expenses():
    """
    Description:
    This function asks the user to enter their monthly expenses.
    The user enters the expense type and the amount. The function keeps asking
    until the user chooses to stop.

    Parameters:
    None

    Variables:
    expenses (list) - stores all expenses as tuples (expense_type, amount)
    expense_type (str) - the name of the expense
    amount (float) - cost of the expense
    more (str) - controls whether the loop continues
    amount_raw (str) - raw user input before converting to float

    Steps:
    1. Create an empty list to store expenses.
    2. Ask the user for the expense type.
    3. Ask the user for the expense amount and validate it is a number.
    4. Store the expense type and amount as a tuple in the list.
    5. Ask if they want to enter another expense.
    6. Repeat until the user enters 'n'.
    7. Return the list of expenses.

    Returns:
    List of expense tuples.
    """

    expenses = []

    while True:
        # Ask user for expense name
        expense_type = input("Enter expense type: ").strip()

        # Make sure the user enters a valid number for the amount
        while True:
            # Ask user for expense amount
            amount_raw = input("Enter amount: $").strip()

            try:
                amount = float(amount_raw)

                # make sure only numbers above 0 are entered
                if amount < 0:
                    print("Please enter a non-negative amount.")
                    continue

                break
            except ValueError:
                print("Please enter a valid number for the amount.")

        # Store expense as a tuple
        expenses.append((expense_type, amount))

        # Ask user if they want to continue
        more = input("Do you want to add another expense? (y/n): ").strip().lower()

        # Treat anything other than 'y' as no, so the program doesn't crash
        if more != "y":
            break

    # Return the completed list of expenses back to the main program
    return expenses


def calculate_total(expenses):
    """
    Description:
    This function uses reduce() to calculate the total cost of all expenses.

    Parameters:
    expenses (list) - list of expense tuples

    Variables:
    total (float) - total of all expenses

    Steps:
    1. Use reduce() to add all expense amounts together.
    2. Return the total.

    Returns:
    Total expenses as a float.
    """

    # Use reduce to add all expense amounts together to get the total
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Return the total expense amount
    return total


def find_highest(expenses):
    """
    Description:
    This function finds the highest expense using reduce().

    Parameters:
    expenses (list) - list of expense tuples

    Variables:
    highest (tuple) - tuple with the highest expense

    Steps:
    1. Compare each expense amount using reduce().
    2. Keep the one with the larger value.
    3. Return the highest expense.

    Returns:
    Tuple containing highest expense name and amount.
    """

    # Use reduce to compare each expense and keep the one with the highest amount
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Return the highest expense tuple (name and amount)
    return highest


def find_lowest(expenses):
    """
    Description:
    This function finds the lowest expense using reduce().

    Parameters:
    expenses (list) - list of expense tuples

    Variables:
    lowest (tuple) - tuple with the lowest expense

    Steps:
    1. Compare each expense amount using reduce().
    2. Keep the one with the smaller value.
    3. Return the lowest expense.

    Returns:
    Tuple containing lowest expense name and amount.
    """

    # Use reduce to compare each expense and keep the smallest one
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # Return the lowest expense tuple
    return lowest


def main():
    """
    Description:
    This function runs the program. It collects expenses from the user,
    calculates totals, and displays the highest and lowest expenses.

    Parameters:
    None

    Steps:
    1. Call get_expenses() to collect user input.
    2. Calculate total expenses.
    3. Find highest and lowest expenses.
    4. Display results clearly to the user.

    Returns:
    None
    """

    # Display program title
    print("Monthly Expense Tracker")

    # Call function to get all expenses from the user
    expenses = get_expenses()

    # Calculate the total of all expenses entered
    total = calculate_total(expenses)

    # Find the highest expense entered
    highest = find_highest(expenses)

    # Find the lowest expense entered
    lowest = find_lowest(expenses)

    # Display results for the user
    print("\nExpense Summary")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()
