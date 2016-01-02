"""Creates a cat."""

class Cat():
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def purr(self):
        """Type c.purr() to make the cat purr."""
        print('{} is purring.'.format(self.name))

    def eat(self):
        """Type c.eat() to have the cat eat."""
        print('{} is eating... nom nom nom!'.format(self.name))

    def climb_tree(self):
        """Type c.climb_tree() to have the cat climb a tree."""
        print('{} is climing the tree.'.format(self.name))

def create_cat():
    name = input("What is the cat's name? ")
    mood = input("What is the cat's mood? ")
    print("Your {} cat, {}, has been created.".format(mood, name))
    return Cat(name, mood)

print("Type something like 'name_of_cat = create_cat()' to begin. (Don't use quotes.)")
