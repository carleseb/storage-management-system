from phone import Phone

# Inheritance
# We instantiate a phone
phone1 = Phone("jscPhonev10", 500, 5, 1)

# We see we can still send emails having used class Phone instead of Item because of inheritance
phone1.send_email()

# We can also increment price
phone1.apply_increment(0.3)
print(phone1.price)