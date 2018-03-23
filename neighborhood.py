from observable import Observable
from observer import Observer
from random import randint
from home import Home
from npc import NPC

#### Creates the Neighborhood with a size of between 2 and 5 Houses ####
class Neighborhood(Observer):
    def __init__(self):
        self.neighborhood = []
        self.size = randint(2,5)
        for r in range(self.size):
            #self.neighborhood.append([])
            temp = Home(randint(1,10))
            self.neighborhood.append(temp)

            #for c in range(self.size):
            #    self.neighborhood[r][c].add_observer(self)
#### Returns the Neighborhood ####
    def get_neighborhood(self):
        return self.neighborhood
#### Updates the house when there are no more monsters ####    
    def update(self, house):
        print("Yay no more monsters!")
#### Removes the house from the neighborhood ####
    def remove(self,home):
        self.neighborhood.remove(home)
