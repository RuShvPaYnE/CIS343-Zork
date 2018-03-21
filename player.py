from random import randint
from observer import Observer
from weapon import Weapon

class Player(Observer):

	def __init__ (self):
		self.health = 100000#randint(100,125)
		self.inventory = []
		self.inventory.append(Weapon(0))
		for x in range (9):
			self.inventory.append(Weapon(randint(1,4)))
			self.inventory[x+1].add_observer(self)

	def get_health(self):
		return self.health

	def get_inventory(self):
		return self.inventory

	def set_health(self, num):
		self.health += num

	def set_inventory(self, update):
		self.inventory = update

	def update(self, obj):
		self.inventory.remove(obj)
		print("Learn to count cause you're out of ammo!")
		self.weapon_held = 0
