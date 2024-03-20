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