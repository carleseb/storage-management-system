from phone import Phone
from mouse import Mouse

# Polimorphism
# An example of polimorphism is len():
print(len("Carles"), len(["Carles", "Carles"])) #behaves different for different types of inputs

# We instantiate a phone
phone1 = Phone("jscPhonev10", 1000, 5)

# We apply discount
# However, apply discount would also work for new child classes from Item, like the Mouse class
mouse1 = Mouse("jscMouse", 30, 2)
Mouse.pay_rate = 0.7 #we can even change the discount just for the Mouse class
phone1.apply_discount()
mouse1.apply_discount()
print(phone1.price) #still 0.8 instead of 0.7
print(mouse1.price)