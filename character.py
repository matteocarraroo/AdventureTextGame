class Character():
# Create a character
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self.conversation = None
# Describe this character
  def describe(self):
    print( self.name + " is here!" )
    print( self.description )
# Set what this character will say when talked to
  def set_conversation(self, conversation):
    self.conversation = conversation
# Talk to this character
  def talk(self):
    if self.conversation is not None:
      print("[" + self.name + " says]: " + self.conversation)
    else:
      print(self.name + " doesn't want to talk to you")
# Fight with this character
  def fight(self, combat_item):
    print(self.name + " doesn't want to fight with you")
    return True
# Enemy class
class Enemy(Character):
# Check the number of enemies to defeat
  enemies_to_defeat = 0
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness= None
# When an enemy is created, enemies to defeat is updated
    self.enemies_to_defeat = self.enemies_to_defeat + 1
# Set and get weakness
  def set_weakness(self, item_weakness):
    self.weakness = item_weakness
  def get_weakness(self):
    return self.weakness
# Fight method
  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You fend " + self.name + " off with the " + combat_item + "!")
      return True
    else:
      print(self.name + " crushes you, puny adventurer.")
      return False
# Friend inherited class
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.mood = None
# Mood getters and setters
    def set_mood(self, mood):
        self.mood = mood     
    def get_mood(self):
        return self.mood
#Hug method (currently unused)
    def hug(self):
        print(self.name + " hugs you back!")
      