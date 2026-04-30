class TotalPrice:
    def __init__(self, original_price, item_quantity):
        self.original_price = original_price
        self.item_quantity = item_quantity
    
    def total_amount(self):
        """
        Calculate total price before discount.
        """
        return self.original_price * self.item_quantity

class Discount():
    def __init__(self, discount_per = 0.1):
        self.discount_per = discount_per

    def calculate_discount(self, total_amount):
        discount_price = total_amount * self.discount_per
        return discount_price 

class FinalPrice():
    def show_final_price(self, total_amount, discount):
        print("Total before discount: ", total_amount)
        print("Discount applied:", discount)

        final_amount = total_amount - discount
        print("Final amount:", final_amount)


item1 = TotalPrice(50, 3)
total_amount = item1.total_amount()

discount = Discount()
discount = discount.calculate_discount(total_amount)

final_price = FinalPrice() 
final_price.show_final_price(total_amount, discount)

