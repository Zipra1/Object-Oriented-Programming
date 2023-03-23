from random import choice # Importing method 'choice' from the random module.

class Cat:
    def __init__(self, name, breed, colour): #First argument always self, references the current class to access attributes & methods.
        self.name = name # Left side is attribute, right side is function argument
        self.breed = breed
        self.colour = colour
        self.is_hungry = choice([True,False])
        self.want_to_scratch = choice([True,False])
    def eat(self, food_name):
        if self.is_hungry:
            print(f'{self.name} ate {food_name}')
            self.is_hungry = False
        else:
            print(f'{self.name} is not hungry.')
    def scratch(self, post):
        if self.want_to_scratch:
            if post.use():
                self.wants_to_scratch = False
                print(f'{self.name} scratched {post}.')
            else:
                print(f'{post} is dead.')
        else:
            print(f'{self.name} does not want to scratch.')

class ScratchPost:
    def __init__(self):
        self.hp = 10
    
    def use(self):
        if self.hp <= 0:
            return False
        else:
            self.hp -= 1
            return True