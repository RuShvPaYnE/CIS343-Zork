from random import randint
from observer import Observer
from weapon import Weapon

class Player(Observer):

#### Gives the player heatlh between 100-125 and gives them one of each weapon ####	
	def __init__ (self):
		self.health = randint(100,125)
		self.inventory = []
		self.inventory.append(Weapon(0))
		for x in range (3):
			self.inventory.append(Weapon(x))
			self.inventory[x+1].add_observer(self)
#### Function to return health of player ####
	def get_health(self):
		return self.health
#### Function to return inventory ####
	def get_inventory(self):
		return self.inventory
#### Function to set Health ####
	def set_health(self, num):
		self.health += num
#### Function to set Inventory
	def set_inventory(self, update):
		self.inventory = update
#### Updates if you run out of ammo ####
	def update(self, obj):
		self.inventory.remove(obj)
		print("Learn to count cause you're out of ammo!")
		self.weapon_held = 0
