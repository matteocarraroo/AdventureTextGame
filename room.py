class Room():
  number_of_rooms = 0
# Creating constructor
  def __init__(self):
    self.name = None
    self.description = None
    self.linked_rooms = {}
    self.character = None
    self.item = None
    Room.number_of_rooms = Room.number_of_rooms + 1
# Name setter and getter
  def set_name(self, room_name):
    self.name = room_name
  def get_name(self):
    return self.name
# Description setter and getter
  def set_description(self, room_description):
    self.description = room_description
  def get_description(self):
    return self.description
# Methods to link rooms and new describe method
  def link_room(self, room_to_link, direction):
    self.linked_rooms[direction] = room_to_link
  def get_details(self):
    print(self.name)
    print("----------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print("The " + room.get_name() + " is " + direction + ".")
# Get current character
  def get_character(self):
    return self.character
  def set_character(self, new_character):
    self.character = new_character
# Method to allow the player to move
  def move(self, direction):
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("There's nothing there...")
      return self
# Get and set item
  def set_item(self, itemname):
    self.item = itemname
  def get_item(self):
    return self.item
