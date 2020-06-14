class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} the Cat is just walking around'


class Dog():
    is_alert = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} the Dog is chasing the cats'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Minoes(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Bob(Dog):
    def sing(self, sounds):
        return f'{sounds}'


class Billy(Dog):
    def sing(self, sounds):
        return f'{sounds}'


class Cash(Dog):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Minoes("Minoes", 9), Sally("Sally", 7), Simon("Simon", 11)]
my_dogs = [Bob("Bob", 12), Billy("Billy", 18), Cash("Cash", 14)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats + my_dogs)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
