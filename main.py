import csv


class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity:int =0):
        # validate parameters/arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

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

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"

phone1 = Item("jscPhonev10", 500, 5)
phone2 = Item("jscPhonev20", 700, 5)

# Test change
