from observable import Observable
from random import randint
#Monster Class that stores the monsters and notifies the house class
#when they die, also stores monsters attack rates and HP
class NPC(Observable):

	#Constructor for Monster class
	def __init__ (self, randNum):
		super().__init__()
		if randNum == 0:
			self.name = "Person"
			self.health = 100
			self.npcT = randNum
		if randNum == 1:
			self.name = "Zombie"
			self.health = randint(50,100)
			self.npcT = randNum
		if randNum == 2:
			self.name = "Vampire"
			self.health = randint(100, 200)
			self.npcT = randNum
		if randNum == 3:
			self.name = "Ghoul"
			self.health = randint(40,80)
			self.npcT = randNum
		if randNum == 4:
			self.name = "Werewolf"
			self.health = 200
			self.npcT = randNum
	#Getter methods
	def get_name(self):
		return self.name
	def get_health(self):
		return self.health
	def get_npcT(self):
		return self.npcT

	#Attack method that deals damage to the player
	def attack(self):
		if self.npcT == 0:
			return -1
		if self.npcT == 1:
			return randint(0,10)
		if self.npcT == 2:
			return randint(10,20)
		if self.npcT == 3:
			return randint(15,30)
		if self.npcT == 4:
			return randint(0,40)

	#Hit method that hits the monsters and notifies the House when
	#their HP reaches 0
	def hit(self, atk, weapon):
		if self.npcT == 1:
			if weapon == 1:
				self.health -= atk*2
			else:
				self.health -= atk
			if self.health < 1:
				self.update(self)
		if self.npcT == 2:
			if weapon == 2:
				pass
			else:
				self.health -= atk
			if self.health < 1:
				self.update(self)
		if self.npcT == 3:
			if weapon == 3:
				self.health -= atk*5
			else:
				self.health -= atk
			if self.health < 1:
				self.update(self)
		if self.npcT == 4:
			if weapon == 1 or weapon == 2:
				pass
			else:
				self.health -= atk
			if self.health < 1:
				self.update(self)
