#!/usr/bin/env python3
import random

class Playa:
  def __init__(self, name="", p_health=0):
    self.name = name
    self.health = p_health

  @property
  def health(self):
    return self.__health

  @property
  def name(self):
    return self.__name

  @health.setter
  def health(self, newhealth):
    self.__health = newhealth
    return self.__health

  @name.setter
  def name(self, newname):
    self.__name = newname
    return self.__name

  def __str__(self):
    return "Player name: " + self.name + " and Health: " + str(self.health)

def main():
  p_name1 = input("Player 1: ")
  p_name2 = input("Player 2: ")

  player1 = Playa(p_name1, random.randint(50, 100))
  player2 = Playa(p_name2, random.randint(50, 100))
  print()
  print("In the Benninging: ")
  print(player1)
  print(player2)
  print()

  """print(f"The current player, {player1.name} has a health of {player2.health}")
  print(f"The second player, {player2.name} has a health of {player2.health}")
  """
  life_1 = 1
  life_2 = 1
  while life_1 and life_2 > 0:
    player1.health -= random.randint(2,10)
    life_1 = check_life(player1.health)
    player2.health -= random.randint(2, 10)
    life_2 = check_life(player2.health)
    if life_1 == 0 or life_2 == 0:
      break
    if life_1 == 0 and life_2 == 0:
      print ("TIED")
    print(f"Player 1: {player1.health} and player 2: {player2.health}")

  print()
  print("In the Ed: ")
  print(player1)
  print(player2)
  print()
  
  if player1.health >= 0 and player2.health <= 0:
    print(f"DRUMROLLS PLEASE, {player1.name.upper()} WON!!")
  if player2.health >= 0 and player1.health <= 0:
    print(f"DRUMROLLS PLEASE, {player2.name.upper()} WON!!")
    
def check_life(value):
  if value <= 0:
    print("Stop, HE'S ALREADY DEAD")
    return 0
  else:
    return 1

main()