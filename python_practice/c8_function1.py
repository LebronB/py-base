# 8-9
def show_magicians(magicians_name):
    for magician_name in magicians_name:
        print("This magician is called " + magician_name.title() + ".")


def make_great(magicians_name):
    new_names = []
    for magician_name in magicians_name:
        new_name = 'the Great ' + magician_name
        new_names.append(new_name)
    return new_names


magicians_list = ['langhao', 'gao', 'liu']
n_names = make_great(magicians_list[:])
show_magicians(magicians_list)
show_magicians(n_names)


# 8-12
def make_sandwich(*toppings):
    """描述三明治中加入的食材"""
    print('Making a pizza with following toppings:')
    for topping in toppings:
        print("- " + topping)


make_sandwich('a', 'b', 'c')
make_sandwich('d', 'e')
make_sandwich('g')


# 8-13
def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name

    for k, v in user_info.items():
        profile[k] = v
    return profile


my_profile = build_profile('zeming', 'wang', age='22', city='Taiyuan')
print(my_profile)


# 8-14
def make_car(producer, no, **extra_info):
    car_info = {'Producer': producer, 'No': no}

    for k, v in extra_info.items():
        car_info[k] = v

    return car_info


car = make_car('subaru', 'outback', color='black', two_page='True')
print(car)