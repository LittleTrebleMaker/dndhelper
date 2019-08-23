print("""



############################################ 
          Welcome to the DnD-inator 
      Please select your Character, Mortal.
############################################



""")

import random

class Character:
  def __init__(self, name, wis):
    self.name = name
    self.wis = wis
    #self.items = []

Dilys = Character("Dilys", 3)

print("My Character is " + Dilys.name)

def roll_save(attr, adv):
  adv = adv
  attr = str(attr)
  roll = random.randint(0,20)
  advroll=random.randint(0,20)
  bonus = Dilys.wis
  total = roll+bonus
  advtotal=advroll+bonus
  text = "Your {0} save is {1} with a natural bonus of {2} for a total of {3}."
  advtext = "Your {0} save is {1} with a natural bonus of {2} for a total of {3}."
  if adv == "N":
    print(text.format(attr,roll,bonus,total))
  elif adv == "Y":
    if roll > advroll:
      print(text.format(attr,roll,bonus,total))
    elif advroll > roll:
      print(advtext.format(attr,advroll,bonus,advtotal))
  


class Item: 
    def __init__(self,name,desc,mod,attr):
      self.name = name
      self.desc = desc
      self.mod = mod
      self.attr = attr

BatCloak = Item("Cloak of the Bat", "Fly speed 40ft, must be in darkness, advantage to stealth, and can turn into a bat once per night", 0, "dex")
