from item import Item

class Mouse(Item):
    def __init__(self, name: str, price: float, quantity = 0):
        # Call to super function to have access to Item (parent) attributes and methods
        super().__init__(
            name, price, quantity
        )