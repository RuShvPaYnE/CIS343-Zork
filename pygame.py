from observer import Observer
from observable import Observable
from home import Home
from npc import NPC
from weapon import Weapon
from player import Player
from neighborhood import Neighborhood



if __name__ == "__main__":
    print("Zork, A Text Based RPG")
    print("The goal is to go to every home in the neighborhood and remove")
    print("all of the monsters inside. Once this is done you win!")


    n = Neighborhood()
    hood = n.get_neighborhood()

    hero = Player()
    candyBucket = hero.get_inventory()
