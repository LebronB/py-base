# 7-1
car = input("Which kind of car do you want to hire? ")
print("Let me see if I can find you a " + car.title() + ".")

# 7-2
num_dining = input("How many people are going to dining here? ")
num_dining = int(num_dining)

if num_dining > 8:
    print("We don't have more tables.")
else:
    print("You can sit down there.")

# 7-3
num = input("Please give me a number. ")
num = int(num)

if num % 10 == 0:
    print("It is integer times of 10.")
else:
    print("It can't be divided by 10.")

