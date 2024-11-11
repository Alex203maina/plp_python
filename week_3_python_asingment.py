def calculate_discount(price, discount_percent):
    """
    Calculate the discount amount based on the given price and discount percentage.
    """
    # Convert input to float for calculations
    price = float(price)
    discount_percent = float(discount_percent)

    # Apply discount if the discount percentage is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Get user input
price = input("Enter the price: ")
discount_percent = input("Enter the discount percentage: ")

# Calculate and display the final price after discount
final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: ${final_price}")
