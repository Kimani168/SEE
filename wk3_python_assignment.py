def calculate_discount(price, discount_percent):
    """ 
    A Function that calculates the final price after applying a discount.
    If the discount is 20% or more, apply the discount; otherwise, return the original price. 
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example use
original_price = input("Enter the original price: ")
discount = input("Enter the discount percentage: ")

try:
    original_price = float(original_price)
    discount = float(discount)
    final_price = calculate_discount(original_price, discount)
    print(f"The price after discount is: {final_price}")
except ValueError:
    print("Please enter valid numerical values for price and discount.")
