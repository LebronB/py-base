txts = ['cats.txt', 'dogs.txt']
for txt in txts:
    try:
        with open(txt) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


# 10-10
with open('monster.txt') as file_object:
    contents = file_object.read()
    num_word = contents.lower().count('the')
    print("'the' appears " + str(num_word) + " times in this file.")

