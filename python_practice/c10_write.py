while True:
    name = input("Please enter your name: ")
    if name == 'q':
        break
    print("Hello, " + name + "!")

    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name.title() + " has visited.\n")