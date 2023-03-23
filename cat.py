from random import choice # Importing method 'choice' from the random module.

class Cat:
    def __init__(self, name, breed, colour): #First argument always self, references the current class to access attributes & methods.
        self.name = name # Left side is attribute, right side is function argument
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True,False])
        self.want_to_scratch = choice([True,False])
        