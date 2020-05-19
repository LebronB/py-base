while True:
    num_1 = input("Please enter the first number: ")
    if num_1 == 'q':
        break
    num_2 = input("Please enter the second number: ")
    if num_2 == 'q':
        break

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        print("You can't enter strings!")
    else:
        add = num_1 + num_2
        print("The sum is " + str(add) + ".")