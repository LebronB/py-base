sandwich_orders = ['tokyo', 'berlin', 'moscow']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

# 7-9
print("Sorry! Pastrami has been sold out.")
sandwich_orders = ['tokyo', 'pastrami', 'berlin', 'pastrami', 'moscow', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

# 7-10 梦想的度假圣地
dream_place = {}

polling_flag = True

while polling_flag:
    name = input("What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    dream_place[name] = response

    repeat = input("Is there anyone want to talk about it? (yes/no)")
    if repeat.lower() == 'no':
        polling_flag = False

for name, response in dream_place.items():
    print(name.title() + " want to travel to " + response.title() + ".")