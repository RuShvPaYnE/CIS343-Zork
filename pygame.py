from observer import Observer
from observable import Observable
from home import Home
from npc import NPC
from weapon import Weapon
from player import Player
from neighborhood import Neighborhood
import sys
from random import randint
import math


if __name__ == "__main__":
    print("Zork, A Text Based RPG")
    print("The goal is to go to every home in the neighborhood and remove")
    print("all of the monsters inside. Once this is done you win!")


    n = Neighborhood()
    hood = n.get_neighborhood()

    hero = Player()
    candyBucket = hero.get_inventory()
    
    #spacing
    print()
    print()
    print("there are", len(hood), "houses that need to be cleared")
    houseNum = int(input("Which house would you like to hit? "))
    if houseNum  <= len(hood):
        int(houseNum)
        houseNum += -1
        hood[houseNum].get_NPC()
    else:
        print("You picked something that doesn't exsist. You're a dummy. \n \n GAME OVER")
        sys.exit()


    while(houseNum != -1):

        option = input("Do you want to 'attack', 'leave','inventory','sugar coma', 'check'? ")
#Attack Command Options
        if option == "attack":
            npc = hood[houseNum].getNPC()
            hood[houseNum].get_NPC()
            print()
            print()
            for x in range(len(candyBucket)):
                print(x ,candyBucket[x].getName(),candyBucket[x].wear(), "uses left")
            wpnOption = input("which weapon?")
            int(wpnOption)
            wpnNum = candyBucket[int(wpnOption)].getWeapon()
            for n in range(len(npc)):
                npc[n].hit(randint(10,20)* candyBucket[int(wpnOption)].getUses(), wpnNum)
            HPlost = 0
            for n in range(len(npc)):
                hero.set_health(-npc[n].attack())
                HPlost += npc[n].attack()
            print("you lost ",HPlost, "health. \n remaining health: ", hero.get_health())
           
            

            if hero.get_health() < 1:
                print("dude you died")
                break
          
            
#How to end the game
        if option == "sugar coma":
            sys.exit()
#Leave the house      
        if option == "leave":
            print("there are", len(hood), "houses that need to be cleared")
            houseNum = int(input("Which house would you like to hit? "))
            int(houseNum)
            houseNum += -1
            hood[houseNum].get_NPC()
        

#Check your inventory
        if option == "inventory":
            for x in range(len(candyBucket)):
                print(x ,candyBucket[x].getName(),candyBucket[x].getUses(), "uses left")

        else:
            print("Please pick a command from the list.")