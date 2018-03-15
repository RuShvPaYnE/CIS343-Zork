from observable import Observable
from observer import observer
from random import randint
from home import Home

class neighborhood(Observer):
    def __init__(self):
		self.neighborhood = []
		self.size = randint(2,5)
		for r in range(self.nsize):
			self.neighborhood.append([])
			for c in range(self.size):
				self.neighborhood[r].append(Home(randint(1,10)))
				self.neighborhood[r][c].add_observer(self)
	def get_neighborhood(self):
		return self.neighborhood
	def update(self, house):
		print("Yay no more monsters!")
