
"""
This script calculates the total price of items and applies a discount
to determine the final price.

"""

# Constants
DISCOUNT_PERCENT = 10.0

#calculate total
def calculate_total_price(prices, quantity):
    """
     Calculate the total price before discount.

    args:
        prices : price of item (float)
        quantity : number of items of brought (int).

    return:
        total prices returned (float) 
    
    """

    # type validation 
    if not isinstance(prices , (int , float)):
        raise TypeError("Prices must be a number. ")

    if not isinstance(prices, int):
        raise TypeError("Quantity must be a whole number. ")

    # value validation
    if prices < 0:
        raise ValueError("Price cannot be negative. ")
    
    if quantity < 0 :
        raise ValueError("Quantity cannot be negative. ")

    return prices * quantity

#discount
def discount_calculator(total_price_amount):
    """
     Calculate the final price after discount. Global discount 

    args:
        total_price_amount : total prices of item before discount (float)
        
    return:
        final_discounted_price returned (float) 
    
    """

    # Dicount Validation 
    if not 0 <= total_price_amount <= 100:
        raise ValueError("Discount percent must be between 0 and 100.")
    
    discount_amount = total_price_amount * DISCOUNT_PERCENT / 100
    final_discounted_price = total_price_amount - discount_amount

    return final_discounted_price

#main
def main():

    price = 20
    quantity = 5

    total_price =  calculate_total_price(price, quantity)
    final_price =  discount_calculator(total_price)

    print("Total price before discount:", total_price)
    print(f"Discount applied: {DISCOUNT_PERCENT} %")
    print("Final price after discount:", final_price)

if __name__ == "__main__":
    main()