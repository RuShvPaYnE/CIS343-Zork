from random import randint

class Player(Observer):

	def __init__ (self):
		self.health = randint(100,125)
		self.inventory = []
		self.inventory.append(Weapon(0))
		for x in range (9):
			self.inventory.append(Weapon(randint(1,3)))
			self.inventory[x+1].add_observer(self)

	def get_health(self):
		return self.health

	def get_locationx(self):
		return self.locationx

	def get_locationy(self):
		return self.locationy

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
