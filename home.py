from observable import Observable
from observer import Observer
from random import randint
from npc import NPC
from observable import Observable

class Home(Observer,Observable):
    def __init__(self,NPCNumber):
        super().__init__()
        self.NPCNumber = NPCNumber
        self.NPCArray = []
        for i in range(0,NPCNumber):
            self.NPCArray.append(NPC(randint(0,4)))
            self.NPCArray[i].add_observer(self)

    def add_NPC(self,NPC):
        self.NPCArray.append(NPC)

    def get_NPC(self):
        if self.NPCNumber == 0:
            print("Home has no one inside")
        for i in self.NPCArray:
            print(i.get_name(), "Health:", i.get_health())

    def get_NPCNumber(self):
        total = 0
        for i in range(self.NPCNumber):
            if self.NPCArray[i].get_npcT != 0:
                num = num +1
        return num

    def update(self,NPC):
        tempNum = self.NPCArray.index(NPC)
        print(self.Array[tempNum].get_name(), "has been slain!")
        self.NPCArray.remove(NPC)
        self.NPCArray.insert(tempNum, Monster(0))
        self.NPCArray[tempNum].add_observer(self)
        if all( x.get_npcT() is 0 for x in self.NPCArray):
            print("THE MONSTERS ARE DEAD!!! savage!")
            super().update(self)
        print(self.NPCArray)


    def getNPC(self):
        return self.NPCArray
