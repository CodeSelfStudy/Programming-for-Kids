"""Creates a cat."""

class Cat():
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def purr(self):
        """Type cat_name.purr() to make the cat purr."""
        print('{} is purring.'.format(self.name))

    def meow(self):
        """Type cat_name.meow() to have the cat meow."""
        print('{} is meowing... meow meow meow.'.format(self.name))

    def eat(self):
        """Type cat_name.eat() to have the cat eat."""
        print('{} is eating... nom nom nom!'.format(self.name))

    def climb_tree(self):
        """Type cat_name.climb_tree() to have the cat climb a tree."""
        print('{} is climing the tree.'.format(self.name))

    def info(self):
        """Shows the attributes for the cat."""
        print(self.__dict__)

    def change_mood(self, new_mood):
        """Changes the mood of the cat."""
        old_mood = self.mood
        self.mood = new_mood
        print("{}'s mood was changed from {} to {}!".format(
                                                        self.name,
                                                        old_mood,
                                                        self.mood))
        self.meow()


def create_cat():
    """Creates a cat."""
    name = input("What is the cat's name? ")
    mood = input("What is the cat's mood? ")
    print("Your {} cat, {}, has been created.".format(mood, name))
    return Cat(name, mood)

def main():
    print("Type something like 'cookie = create_cat()' to begin. (Don't use quotes.)")

if __name__ == '__main__':
    main()
