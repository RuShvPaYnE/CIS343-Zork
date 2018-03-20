from observable import Observable
from observer import Observer
from random import randint
from home import Home
from npc import NPC

class Neighborhood(Observer):
    def __init__(self):
        self.neighborhood = []
        self.size = randint(2,5)
        for r in range(self.size):
            self.neighborhood.append([])
            for c in range(self.size):
                self.neighborhood[r].append(Home(randint(1,10)))
                self.neighborhood[r][c].add_observer(self)
    def get_neighborhood(self):
        return self.neighborhood
    def update(self, house):
        print("Yay no more monsters!")
