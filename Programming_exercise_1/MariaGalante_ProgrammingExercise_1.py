"""
Cinema Ticket Pre-Sale (Programming Exercise 1)

Rules:
- Maximum total tickets: 20
- Maximum tickets per buyer: 4
- Program repeats until all tickets are sold
- Displays remaining tickets after each valid purchase
- Displays total number of buyers at the end

Student: Maria Galante
Date: 2026-01-21
"""


MAX_TICKETS = 20
MAX_PER_BUYER = 4


def sell_tickets() -> int:
    """
    Controls the ticket selling process until all tickets are sold.

    Parameters:
    None

    Variables:
    total_tickets (int): Tracks how many tickets are still available.
    buyers (int): Accumulator that counts total buyers.
    request_raw (str): Raw user input before conversion to int.
    requested_tickets (int): Number of tickets requested by the current buyer.

    Logic:
    1. Initialize total of tickets to be sold.
    2. Initialize buyer counter to 0.
    3. Loop while tickets remain.
    4. Prompt user for ticket amount.
    5. Validate input using if statements.
    6. Subtract tickets from total tickets.
    7. Increment buyer accumulator.
    8. Repeat until sold out.

    Return:
    buyers (int): Total number of buyers.
    """

    # Set starting inventory of tickets
    total_tickets = MAX_TICKETS

    # Accumulator to count how many buyers purchase tickets
    buyers = 0

    # Continue selling until all tickets are sold
    while total_tickets > 0:
        # Collect user input as a string first
        request_raw = input(
            f"How many tickets would you like to buy (1-{MAX_PER_BUYER})? "
            f"Tickets remaining: {total_tickets}: "
        )

        # Convert input to an integer if possible
        try:
            requested_tickets = int(request_raw)
        except ValueError:
            print("Invalid entry. Please enter a whole number (example: 2).")
            continue

        # Validate per-buyer limit and positive request
        if requested_tickets < 1 or requested_tickets > MAX_PER_BUYER:
            print(
                f"Invalid amount. You can only buy 1 to {MAX_PER_BUYER} tickets."
            )
            continue

        # Prevent selling more than the remaining inventory
        if requested_tickets > total_tickets:
            print(
                f"Not enough tickets remaining. Only {total_tickets} ticket(s) left."
            )
            continue

        # Update remaining total tickets after a valid purchase
        total_tickets -= requested_tickets

        # Increment buyer count after a successful purchase
        buyers += 1

        # Display remaining total tickets after the purchase
        print(f"Tickets remaining after purchase: {total_tickets}")

    return buyers


def display_summary(total_buyers: int) -> None:
    """
    Displays the final results after tickets are sold out.

    Parameters:
    total_buyers (int): Total number of buyers.

    Variables:
    None

    Logic:
    1. Display SOLD OUT message.
    2. Display total buyers.

    Return:
    None
    """
    # Display the final summary once inventory reaches zero
    print("\nSOLD OUT")
    print(f"Total number of buyers: {total_buyers}")


if __name__ == "__main__":
    buyers_total = sell_tickets()
    display_summary(buyers_total)
