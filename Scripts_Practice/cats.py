# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name: object, age: object) -> object:
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
garfield = Cat("garfield", 7)
plukje = Cat("plukje", 11)
minoes = Cat("minoes", 13)


# 2 Create a function that finds the oldest cat

def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {get_oldest_cat(garfield.age, plukje.age, minoes.age)} years old.")
