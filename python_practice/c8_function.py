# 8-1
def display_message():
    print("This chapter is about the function.")


display_message()


# 8-2
def favorite_book(book_name):
    print("My favorite book is " + book_name.title() + ".")


favorite_book('The great gatsby')


# 8-3
def make_shirt(size='big', pattern='i love python'):
    print("This shirt's size is " + size.upper() + ".")
    print('"' + pattern.title() + '" is written on it.\n')


make_shirt()
make_shirt('m')
make_shirt(pattern='i love go')


# 8-5
def describe_city(city, country='germany'):
    print(city.title() + " is in " + country.title() + ".")


describe_city('chongqing', 'china')
describe_city('berlin')


# 8-6
def city_country(city, country):
    message = city.title() + ", " + country.title()
    return message


print(city_country('chongqing', 'china'))
print(city_country('new york', 'usa'))
print(city_country('london', 'uk'))


# 8-7
def make_album(s_name, a_name, s_num=''):
    if s_num:
        albums = {"singer name": s_name, "album name": a_name, 'singer number': s_num}
    else:
        albums = {"singer name": s_name, "album name": a_name}
    return albums


while True:
    singer_name = input("Singer's name is: ")
    if singer_name == 'q':
        break
    album_name = input("Album's name is: ")
    if album_name == 'q':
        break

    info_album = make_album(singer_name, album_name)
    print(info_album)


