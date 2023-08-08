import csv

# We create the class of an Item
class Item:
    # We create a *class* attribute, different than normal attributes (global)
    pay_rate = 0.8 #to set discount

    # We want to see all the instnaces created
    all = []

    def __init__(self, name: str, price: float, quantity = 0): #price float also accepts integers
        # Run validations to the received arguments
        assert price >= 0, f"ERROR -> price {price} is not >= 0"
        assert quantity >= 0, f"ERROR -> quantity {quantity} is not >= 0"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property #this decorator sets the properties to attributes of instances of being inmutable after definition
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("The name given is too long")
        else:
            self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self): #second method, apply discount to total price
        self.__price = self.__price * self.pay_rate
        return

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price*increment_value

    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def __repr__(self): #to represent
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})" # With self.__class__.__name__ we ddo not hardcode the class name for inheritance calling
    
    def calculate_total_price(self): #first method, compute total price
        return self.quantity * self.__price
    
    @classmethod #to make it a class method (not sending self-instance as first argument but the whole class)
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
            name = item.get('name'),
            price = float(item.get('price')),
            quantity = int(item.get('quantity'))
            )
    
    @staticmethod #to make it static method (not sending any special first argument, just as a normal function)
    def is_integer(num):
        if isinstance(num, float):
            # To count .0 floats as integers
            return num.is_integer() #careful this is an in built function, not the static method
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __write_email(self):
        pass

    def send_email(self):
        self.__write_email()
        print("Email sent")






if __name__ == "__main__":
    # We assign *instance* attributes (unique per instance) to two instances of the class
    item1 = Item("Phone", 100.0, 3)
    item1.apply_discount()
    print(item1.calculate_total_price())

    item2 = Item("Laptop", 1000.0, 1)
    item2.pay_rate = 0.7 #locally change the class attribute
    item2.apply_discount()
    print(item2.calculate_total_price())

    # We access the *class* attribute
    print(Item.pay_rate, item1.pay_rate)