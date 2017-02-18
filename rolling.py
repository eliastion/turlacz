import random


class RandProvider(object):
    def __init__(self):
        pass

    def rand(self):
        return random.randint(1, 6)


class Die(object):
    def __init__(self, randProvider):
        self.randomizer = randProvider

    def roll(self):
        return self.randomizer.rand()
