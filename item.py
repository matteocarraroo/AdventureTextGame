class Item():
  #Creating constructor
  def __init__(self):
    self.name= None
    self.description= None
  #Name getter

  def set_name(self, item_name):
    self.name = item_name
  def get_name(self):
    return self.name
  #Description setter and getter  
  def set_description(self, item_description):
    self.description= item_description
  
  def get_description(self):
    return self.description
#Describe item
  def describe(self):
    print(f"There is a {self.name} in this room -  {self.description}")
    