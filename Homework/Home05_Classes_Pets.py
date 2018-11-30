__author__ = 'stanislav-kuhtinski'


class Pets(object):
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:
    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False
        print('{} was hungry, gave him to eat'.format(self.name))
        return True


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    # Child class (inherits from Dog class)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Create instances of dogs
my_dogs = [
    Bulldog("Belka", 2),
    RussellTerrier("Strelka", 5),
    Dog("Rex", 1)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
eat_status = {}
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
    eat_status.update({dog.name: dog.eat()})
if all(value == True for key, value in eat_status.items()):
    print('Dogs are not hungry.')
else:
    print('Some dogs are still hungry')
