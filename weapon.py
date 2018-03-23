from random import randint
from observable import Observable

#### Austin Van Kempen and Lanndon Rose ####



#### Weapon Class ####
class Weapon(Observable):
  def __init__(self, weapon):
      super().__init__()

#### HersheyKiss weapon and properties ####
      if weapon == 0:
        self.name = "HersheyKiss"
        self.weapon = weapon
        self.uses = 1000
        
#### SourStraws weapon and properties ####
      if weapon == 1:
        self.name = "SourStraws"
        self.weapon = weapon
        self.uses = 2
        
#### ChocolateBars weapon and properties ####
      if weapon == 2:
          self.name = "ChocolateBars"
          self.weapon = weapon
          self.uses = 4
          
#### NerdBOMB weapon and properties ####
      if weapon == 3:
          self.name = "NerdBOMB"
          self.weapon = weapon
          self.uses = 1

#### Icecream weapon and properties ####          
      if weapon == 4:
          self.name = "IceCream"
          self.weapon = weapon
          self.uses = 1


#### https://codereview.stackexchange.com/questions/138085/text-based-rpg-using-oop ####
#### Went on the website above and it gave a lot of useful info ####

#### Damage for each weapon ####
  def wear(self):
      if self.weapon == 0:
        self.uses = self.uses - 1
        if self.uses == 0:
            self.update(self)
      return randint(100,175)/100.0

      if self.weapon == 1:
        self.uses = self.uses - 1
        if self.uses == 0:
            self.update(self)
      return randint(200,250)/100.0

      if self.weapon == 2:
        self.uses = self.uses - 1
        if self.uses == 0:
            self.update(self)
      return randint(350,501)/100.0

      if self.weapon == 3:
          self.uses = self.uses - 1
          if self.uses == 0:
              self.update(self)
          return 1

      #if self.weapon == 4 and monster == "Ira"
        #self.uses -=1
          #if self.uses == 0
           # self.update(self)
      #return 1000





  def getName(self):
    return self.name

  def getWeapon(self):
    return self.weapon

  def getUses(self):
    return self.uses
