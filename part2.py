from item import Item

# Encapsulation of name
# We instantiate an item with a name
item1 = Item("MyItem", 750)
#print(item1.__name) #gives error

# We test the name to be only readable
#item1.name = "OtherName" #gives error
# However, as a new one
item1.__name = "OtherItem"

print(item1.name)
print(item1.__name)

# If we want to set a new name to this property attribute we have to use a setter
item1.name = "OtherItem"
#item1.name = "NewLongNameToItem" # gives error for length
print(item1.name)