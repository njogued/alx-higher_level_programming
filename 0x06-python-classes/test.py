#!/usr/bin/env python3

class Playa:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  @property
  def health(self):
    print(f"{self.name}'s current health is {self.health}")
    return self.health

  @health.setter
  def health(self, newhealth):
    self.health = newhealth

  def __str__(self):
    return "Player: " + self.name + "\n" + "Health: " + str(self.health)

def main():
  p_name1 = input("Player 1: ")
  p_name2 = input("Player 2: ")

  player1 = Playa(str(p_name1), "100")
  player2 = Playa(str(p_name2), "100")

  print(f"The current player, {player1.name} has a health of {player2.health}")
  print(f"The second player, {player2.name} has a health of {player2.health}")
  print("Try this")
  print(player1)
  print(player2)

main()