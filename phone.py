from item import Item

# We create a subclass of Item specially for the phones to keep trak of the broken ones

class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # Call to super function to have access to Item (parent) attributes and methods
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"ERROR -> quantity {broken_phones} is not >= 0"

        # Assign to self object
        self.broken_phones = broken_phones





if __name__ == "__main__":
    # We call two instances of Phone with the broken ones
    phone1 = Phone("jscPhonev10", 500, 5, 1)
    phone2 = Phone("jscPhonev20", 700, 5, 1)

    # We call the total price
    print(phone1.calculate_total_price())

    # We can see that Phones are still stored in all
    print(Item.all)