# 7-4
flag = True

while flag:
    topping = input("Please enter the toppings you want. ")
    if topping.lower() == 'quit':
        flag = False
    else:
        print("We'll add " + topping + " to your pizza.")

# 7-5
while True:
    age = input("How old are you? ")
    if age.lower() == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("You don't need to buy the ticket.")
        elif age <= 12:
            print("10$ for a ticket.")
        elif age > 12:
            print("15$ for a ticket.")