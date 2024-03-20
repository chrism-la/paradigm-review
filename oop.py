#Object Oriented Programming prompt 
'''
First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
Define a repair() method that will update the condition of the podracer to "repaired".
Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed"
'''

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"


class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed,condition,price)

  def boost(self):
    self.max_speed *= 2


class SebulbasPod(Podracer):
  def __init__(self,max_speed,condition,price):
    super().__init__(max_speed,condition,price)

  def flame_jet(self, other_podracer):
    other_podracer.condition = "trashed"



regular_podracer = Podracer(max_speed=250,condition="perfect",price=9999)

anakins_podracer = AnakinsPod(max_speed=300,condition="perfect",price=999999)
anakins_podracer.boost()

sebulbas_podracer = SebulbasPod(max_speed=150,condition="trashed",price=9)
sebulbas_podracer.flame_jet(regular_podracer)

regular_podracer.repair()

print(regular_podracer.max_speed, regular_podracer.condition, regular_podracer.price)
print(anakins_podracer.max_speed,anakins_podracer.condition,anakins_podracer.price)
print(sebulbas_podracer.max_speed,sebulbas_podracer.condition,sebulbas_podracer.price)