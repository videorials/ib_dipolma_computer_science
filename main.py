import csv

class Item:
    # >> --------------- << class attribute/variables >>
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    
    # >> --------------- << constructor method >>
    def __init__(self, name: str, price: float, quantity=0):

        # >> ----------- << validate recieved arguments >>
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # >> ----------- << instance variables >>
        self.name = name
        self.price = price
        self.quantity = quantity

        # >> ----------- << actions to execute >>       
        Item.all.append(self)


    # >> --------------- << mutator methods >>
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    # >> --------------- << class methods >>
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )


    # >> --------------- << accessor methods >>
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)