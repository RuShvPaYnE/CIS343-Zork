from observable import Observable
from observer import Observer
from random import randint
from npc import NPC

#### Home Observer Class #####
class Home(Observer):
    def __init__(self,NPCNumber):
        super().__init__()
        self.NPCNumber = NPCNumber
        self.NPCArray = []
#### Adds the NPC's to each House ####
        for i in range(0,NPCNumber):
            self.NPCArray.append(NPC(randint(0,4)))
            self.NPCArray[i].add_observer(self)
    def add_NPC(self,NPC):
        self.NPCArray.append(NPC)
#### If statement for Showing if there are Monsters are inside or not ####
    def get_NPC(self):
        if self.NPCNumber == 0:
            print("Home has no one inside")
        for i in self.NPCArray:
            print(i.get_name(), "Health:", round(i.get_health()))
#### Function get_NPCNumber ####
    def get_NPCNumber(self):
        total = 0
        for i in range(self.NPCNumber):
            if self.NPCArray[i].get_npcT != 0:
                num = num +1
        return num
#### updates the house after the player attacks each turn ####
    def update(self,npc):
        tempNum = self.NPCArray.index(npc)
        print(self.NPCArray[tempNum].get_name(), "has been slain!")
        self.NPCArray.remove(npc)
        self.NPCArray.insert(tempNum, NPC(0))
        self.NPCArray[tempNum].add_observer(self)
        if all( x.get_npcT() is 0 for x in self.NPCArray):
            print("THE MONSTERS ARE DEAD!!!")
            print("Leave and head to another house!")
            super().update(self)
        #print(self.NPCArray)


    def getNPC(self):
        return self.NPCArray
#### checks to see if the house is empty ####
    def isEmpty(self):
        if all( x.get_npcT() is 0 for x in self.NPCArray):
            return 0
        else:
            return 1
