from room import Room

kitchen = Room("kitchen")
kitchen.set_description("Blebleble")

dining_hall = Room("dining_hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall")

ballroom = Room("ballroom")
ballroom.set_description("cccccccccccc")

kitchen.describe()
dining_hall.describe()
ballroom.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")

current_room = kitchen

from item import Item

waldek = Item("Waldi")
waldek.set_description("Krzyzowski")
waldek.describe()

from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dave.describe()
dave.talk()

current_room = kitchen

dead = False

while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  command = input("> ")
  
  if command in ["north", "south", "east", "west"]:
    # Move in the given direction
    current_room = current_room.move(command)
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
  elif command == "fight":
    # You can check whether an object is an instance of a particular
    # class with isinstance() - useful! This code means
    # "If the character is a Friend"
    if inhabitant == None or isinstance(inhabitant, Friend):
      print("There is no one here to fight with")
    else:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      if inhabitant.fight(fight_with) == True:
        # What happens if you win?
        print("Hooray, you won the fight!")
        current_room.set_character(None)
      else:
        # What happens if you lose?
        print("Oh dear, you lost the fight.")
        print("That's the end of the game")
        dead = True
  elif command == "hug":
    if inhabitant == None:
      print("There is no one here to hug :(")
    else:
      if isinstance(inhabitant, Enemy):
        print("I wouldn't do that if I were you...")
      else:
        inhabitant.hug()
