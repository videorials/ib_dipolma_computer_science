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
        # We will count out the floats that are point zero
        # For i.e. 5.0, 10.0
        if isinstance(num, float):
            # Count the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    all = []
    def __init__(self, name:str, price:float, quantity:int =0, broken_phones=0):

        super().__init__(name, price, quantity)

        # validate parameters/arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # instance attributes
        self.broken_phones = broken_phones

        # actions to execute
        Phone.all.append(self)

phone1 = Phone("jsvPhonev10", 500, 5, 1)