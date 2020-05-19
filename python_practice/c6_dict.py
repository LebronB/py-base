# 6-1
wang = {
    'first_name': 'zeming',
    'last_name': 'wang',
    'age': '22',
    'city': 'taiyuan',
}
lang = {
    'first_name': 'shaobo',
    'last_name': 'lang',
    'age': '22',
    'city': "xi'an",
}
hao = {
    'first_name': 'daheng',
    'last_name': 'hao',
    'age': '22',
    'city': 'dai county',
}
people = [wang, lang, hao]

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    print("His full name is " + full_name + ".")
    print("He is " + str(person['age']) + " years old.")
    print("He lives in " + person['city'].title() + ".\n")
# 6-5
famous_river = {
    'nile': 'egypt',
    'yellow river': 'china',
    'yangtzi river': 'china'
}
for river in famous_river.keys():
    print(river.title())
for country in famous_river.values():
    print(country.title())

# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

check_list = ['tom', 'jen', 'jackson', 'phil']

for checked in check_list:
    if checked in favorite_languages.keys():
        print("Thank you!" + checked.title() + ".")
    else:
        print("Would you like to accept it?" + checked.title() + ".")

# 6-8
pony = {
    'kind': 'dog',
    'owner': 'Kevin'
}
mary = {
    'kind': 'cat',
    'owner': 'Jack'
}
berry = {
    'kind': 'alaska',
    'owner': 'Irving'
}
pets = [pony, mary, berry]

for pet in pets:
    print("It is a/an " + pet['kind'] + ".")
    print("It is " + pet['owner'] + "'s pet.\n")

# 6-9
favorite_places = {
    'kevin': ['paris', 'berlin', 'tokyo'],
    'mary': ['nairobi'],
    'tom': ['beijing', 'kunming']
}

for person, places in favorite_places.items():
    print("\n" + person.title() + " likes these places.")
    for place in places:
        print("\t" + place.title())

# 6-11
cities = {
    'paris': {
        'country': 'france',
        'population': '100 million',
        'fact': 'good'
    },

    'berlin': {
        'country': 'germany',
        'population': '10 billion',
        'fact': 'nice'
    },

    'nairobi': {
        'country': 'kennia',
        'population': '1 billion',
        'fact': 'poor'
    }
}

for city_name, city_info in cities.items():
    print("\nCity name:" + city_name)
    print("\tIt belongs to " + city_info['country'].title() + ".")
    print("\tIt has a population of " + city_info['population'] + ".")
    print("\tIt is " + city_info['fact'] + ".")