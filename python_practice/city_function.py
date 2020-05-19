def cities_in_countries(city, country, population=''):
    if population:
        city_in_country = city + ", " + country + " - population " + str(population)
    else:
        city_in_country = city + ", " + country

    return city_in_country.title()

