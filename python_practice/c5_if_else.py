alien_color = 'red'
if alien_color == 'green':
    print("You've got 5 points for shooting it.")
elif alien_color == 'yellow':
    print("You've got 10 points.")
elif alien_color == 'red':
    print("You've got 15 points.")

favorite_fruits = ['banana', 'orange', 'watermelon']
if 'banana' in favorite_fruits:
    print("You really like banana.")
if 'apple' in favorite_fruits:
    print("You really like apples.")
if 'orange' in favorite_fruits:
    print("You really like oranges.")

# 5-8,9
user_list = ['admin', 'Jack', 'Mary', 'Eric', 'Marshal']
if user_list:
    for user in user_list:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users.")

# 5-10
current_users = ['admin', 'Jack', 'Mary', 'Eric', 'Marshal', 'Robert']
new_users = ['Tom', 'Jerry', 'JACK', 'Robert', 'Harrison']
for new_user in new_users:
    if new_user.title() in current_users:
        print("Oops, this name has been used, please change it.")
    else:
        print("It can be used as your user name.")

# 5-11
# 数字与字符串拼接需要str()转换
num_list = list(range(1, 10))
for num in num_list:
    print(num)
    if num == 1:
        print(str(num) + "st\n")
    elif num == 2:
        print(str(num) + "nd\n")
    elif num == 3:
        print(str(num) + "rd\n")
    else:
        print(str(num) + "th\n")


