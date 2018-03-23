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

#### Start of the game, gives a little background text ####
## Created by Austin Van Kempen and Lanndon Rose ####
if __name__ == "__main__":
    print("Zork, A Text Based RPG")
    print("The goal is to go to every home in the neighborhood and remove")
    print("all of the monsters inside. Once this is done, choose the option check. \n")
    print("if all of the monsters are dead, you win. If they aren't. Too bad punk, you lose.")

#### Setting neighborhood() to n ####
    n = Neighborhood()
    
#### Setting n.get_neighborhood() to hood ####    
    hood = n.get_neighborhood()

#### Setting player() to hero ####    
    hero = Player()
    
#### Setting hero.get_inventory() to candyBucket ####    
    candyBucket = hero.get_inventory()

#### Spacing ####
    print()
    print()
#### Spacing ####

#### Lets user know how many houses need to be cleared ####
    print("there are", len(hood), "houses that need to be cleared")
    
#### Gives them an option of what house they would like to go to first ####
    houseNum = int(input("Which house would you like to hit? "))
    if houseNum  <= len(hood):
        int(houseNum)
        houseNum += -1
        hood[houseNum].get_NPC()
        
#### Spacing ####   
        print()
        print()
#### Spacing ####

#### If they pick a house that doesn't exist, they lose (We are harsh) ####
    else:
        print("You picked something that doesn't exsist. You're a dummy. \n \n GAME OVER")
        sys.exit()

#### Gives player an option of what they would like to do ####
    while(len(hood)!= 0):
        option = input("Do you want to 'attack', 'leave','inventory','sugar coma'?")
        while(option is None):
            option = input("Do you want to 'attack', 'leave','inventory','sugar coma'?")
#Attack Command Options
        if option == "attack":
            npc = hood[houseNum].getNPC()
            hood[houseNum].get_NPC()
            print()
            print()
            for x in range(len(candyBucket)):
                print(x ,candyBucket[x].getName())
                print()
            wpnOption = input("Which weapon would you like to use?")
            int(wpnOption)
            wpnNum = candyBucket[int(wpnOption)].getWeapon()
            for n in range(len(npc)):
                npc[n].hit(randint(10,20)* candyBucket[int(wpnOption)].wear(), wpnNum)
            HPlost = 0
            for n in range(len(npc)):
                hero.set_health(-npc[n].attack())
                HPlost += npc[n].attack()
            print()
            print()
            print("You lost ",HPlost, "health. \n remaining health: ", hero.get_health())


#### If hero health falls below zero, they lose. ####
            if hero.get_health() < 1:
                print("dude you died :( ")
                sys.exit()
                print()
                break


#How to end the game without dying
        if option == "sugar coma":
            sys.exit()
#Leave the house
        if option == "leave":
            print()
            print()
            print("There are", len(hood), "houses that need to be cleared.")
            houseNum = int(input("Which house would you like to hit? "))
            int(houseNum)
            houseNum += -1
            hood[houseNum].get_NPC()


#Check your inventory
        if option == "inventory":
            for x in range(len(candyBucket)):
                print()
                print()
                print(x ,candyBucket[x].getName(),candyBucket[x].getUses(), "uses left")

        if hood[houseNum].isEmpty() == 0:
            hood.remove(hood[houseNum])

        else:
            print()
            print()
            print("Please pick a command from the list.")
print()
print()
print()
#### Winning message once you beat the game ####
print("Congrats you little turd, you actually did it")
print("You saved the neighborhood from the monsters!")
