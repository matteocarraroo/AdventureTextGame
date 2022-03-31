#import classes
from room import Room
from info import RPGInfo
from item import Item
from character import Character, Enemy, Friend
import time

# Set title
spooky_castle = RPGInfo("The spooky castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Matteo Carraro"

# Creating all objects (rooms and inventory)
inventory = []
kitchen= Room()
ballroom= Room()
dining_hall= Room()

# Naming rooms and setting description
print(f"There are {Room.number_of_rooms} rooms to explore.")

kitchen.set_name('\033[1m' + 'Kitchen' + '\033[0m')
kitchen.set_description("A dank and dirty place, buzzing with flies.")

ballroom.set_name('\033[1m' + 'Ballroom' + '\033[0m')
ballroom.set_description("A well-lit majestic room, with paintings, armors and crystal chandeliers decorating it.")

dining_hall.set_name('\033[1m' + 'Dining Hall' + '\033[0m')
dining_hall.set_description("Old, mostly empty room with only a large table in the center of it.")

# Linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")

# Current room
current_room= kitchen

# Items and linking items to rooms
sword = Item()
sword.set_name("sword")
sword.set_description("A very sharp sword.")

cheese = Item()
cheese.set_name("cheese")
cheese.set_description("An eerily large block of cheese...")

dining_hall.set_item(cheese)
kitchen.set_item(sword)

# Characters
matt = Enemy("Matt", "An evil knight")
matt.set_conversation("What are you doing in here, adventurer?")
matt.set_weakness("cheese")
dining_hall.set_character(matt)

lily = Friend("Lily", "A friendly fairy")
lily.set_conversation("Hey there!")
ballroom.set_character(lily)

# Variable for while loop
dead = False

# Game loop
while dead == False:
  print("\n")
  #print(inventory) #testing the array updating
  current_room.get_details()
  item = current_room.get_item()
  
# List characters in the room
  inhabitant= current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
# List items in the room
  if item is not None:
    item.describe()
# Ask for user input and check if it's correct
  command= input("> Do you want to move (enter the direction), talk, fight or take the object in the room? ")
  command = command.lower()
# Check wether a direction was typed
  if command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
  elif command == "talk":
# Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
        inhabitant.talk()
        time.sleep(1)
    else:
      print("There is no one here to talk with") 
      time.sleep(1)    
# Fight with the character
  elif command == "fight":
# You can check whether an object is an instance of a particular
# class with isinstance() - useful! This code means
# if the character is an Enemy"
    if inhabitant is not None and isinstance(inhabitant, Enemy):
# Fight with the inhabitant, if there is one
      print("> What will you fight with? ")
      fight_with = input()
      fight_with = fight_with.lower()
      if fight_with in inventory:
        if inhabitant.fight(fight_with) == True:
# What happens if you win?
          print("Hooray, you won the fight!")
          current_room.set_character(None)
          time.sleep(1) 
          if Enemy.enemies_to_defeat == 0:
                      print("Congratulations, you defeated all the enemies!")
                      dead = True
                      time.sleep(1) 
        else:
# What happens if you lose?
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
          time.sleep(1) 
      else:
        print("You don't have that in your inventory...")
        time.sleep(1) 
    else:
      print("There is no one here to fight with...")
      time.sleep(1)
# Command to take an object and put it into the inventory
  elif command == "take":
    if item is not None:
      print(f"You put the {item.get_name()} in your inventory.")
      inventory.append(item.get_name())
      current_room.set_item(None)
      time.sleep(1) 
    else:
      print("There's nothing to take here...")
      time.sleep(1)
  else:
    print("Invalid command")
    time.sleep(1)
#  elif command == "hug":
# Display credits after game ends
RPGInfo.credits()