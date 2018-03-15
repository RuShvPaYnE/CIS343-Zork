from observable import Observable
from observer import observer
from random import randint

class Home(Observer):
    def __init__(self,NPCNumber)):
        super().__init__()
        self.NPCNumber = NPCNumber
        self.NPCArray = []
        for i in range(0,NPCNumber):
            self.NPCArray.append(NPC(randint(0,4)))
            self.NPCArray[x].add_observer(self)

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
            if self.NPCArray[i].get_NPCT != 0:
                num +=1
        return num

    def update(self,NPC):
        tempNum = self.NPCArray.indec(NPC)
        print(self.NPCArray)
