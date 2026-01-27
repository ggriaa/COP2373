def calculate_discount(price, discount_rate):
    # Convert price to float
    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid price: expected a number, got {price!r}")

    # Convert discount_rate to float
    try:
        discount_rate = float(discount_rate)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid discount rate: expected a number, got {discount_rate!r}")

    # Validate discount rate range
    if not (0 <= discount_rate <= 1):
        raise ValueError(f"Invalid discount rate: {discount_rate} (must be between 0 and 1)")

    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    # Convert price to float
    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid price: expected a number, got {price!r}")

    new_price = price - discount_amount
    return new_price


def main():
    products = [
        {"name": "Laptop", "price": 800, "discount_rate": 0.15},
        {"name": "Headphones", "price": 150, "discount_rate": 0.10},
        {"name": "Tablet", "price": "500", "discount_rate": 0.20},
        {"name": "Smartphone", "price": 1000, "discount_rate": 0.05}
    ]

    for product in products:
        name = product["name"]
        price = product["price"]
        discount_rate = product["discount_rate"]

        try:
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"{name}: Original Price = ${float(price):.2f}")
            print(f"Discount Amount = ${discount_amount:.2f}")
            print(f"Final Price = ${final_price:.2f}\n")

        except ValueError as error:
            print(f"Error processing {name}: {error}")
            print("Skipping this product.\n")


if __name__ == "__main__":
    main()
