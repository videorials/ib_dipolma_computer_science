class Item:
    # >> --------------- << class attribute/variables >>
    pay_rate = 0.8 # the pay rate after 20% discount
    
    # >> --------------- << constructor method >>
    def __init__(self, name: str, price: float, quantity=0):

        # >> ----------- << validate recieved argumants >>
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # >> ----------- << instance variables >>
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Phone', 100, 5)
item1 = Item('Mobile', 1000, 3)

print(Item.pay_rate)