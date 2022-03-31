class RPGInfo():
  author = "Anonymous"
# Constructor
  def __init__(self, game_title):
    self.title = game_title
# Welcome message
  def welcome(self):
    print(f"Welcome to {self.title}!")
# Static method
  @staticmethod
  def info():
    print("Made using the OOP RPG Creator")
# Class method
  @classmethod
  def credits(cls):
    print("Thank you for playing!")
    print(f"Created by {cls.author}")