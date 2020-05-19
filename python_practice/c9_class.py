# 9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name.title() + ".")
        print("It has food of " + self.cuisine_type + ".")

    def set_number_served(self, n_customers):
        self.number_served = n_customers

    def increment_number_served(self, new_customer):
        if new_customer >= 0:
            self.number_served += new_customer
        else:
            print("You can't roll back this number.")

    def open_restaurant(self):
        print("The restaurant is opened.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']

    def show_flavors(self):
        print("We have ice creams of following flavors:")
        for flavor in self.flavors:
            print(" -" + flavor)


my_restaurant = Restaurant('da long yi', 'hotpot')
super_ice = IceCreamStand('Kuka', 'icecream')
super_ice.show_flavors()


# 9-3
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("This person is " + full_name.title() + '.')
        print("He/She is " + str(self.age) + " years old.")
        print("He/She lives in " + self.city.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print("Hello, " + self.first_name.title() + "!")


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super(Admin, self).__init__(first_name, last_name, age, city)
        self.privileges = Privilege()


class Privilege:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileages(self):
        print("The admin has following rights:")
        for privileage in self.privileges:
            print(" -" + privileage)


admin = Admin('hao', 'lang', 22, 'chengdu')
admin.describe_user()
admin.privileges.show_privileages()


# 9-
