from item import Item

# Encapsulation of price
# We instantiate an item with a price
item1 = Item("MyItem", 750)
print(item1.price)

# We apply discount
item1.apply_discount()
print(item1.price)

# We apply increment
item1.apply_increment(0.2)
print(item1.price)