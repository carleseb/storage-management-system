from item import Item

# We define some instances of Item (now in csv file)
'''
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''

# We call the items from the csv file
Item.instantiate_from_csv()

# We check all of them have been stored
print(Item.all)

# We can also see all the names of the instances created
for instance in Item.all:
    print(instance.name)

# We check the is_integer static method
print(Item.is_integer(7))