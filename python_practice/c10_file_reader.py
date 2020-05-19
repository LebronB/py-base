with open('pi_digits.txt') as file_object:
    # for line in file_object:
    #     print(line.strip())

    lines = file_object.readlines()

for line in lines:
    if 'Python' in line:
        print(line.replace('Python', 'Java').strip())
    else:
        print(line.strip())

