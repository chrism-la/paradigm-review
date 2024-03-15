#Functional Programming Prompt
'''Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.'''



def asc_order(arr):
  result = []
#Flattening using List comprehension
  for subarr in arr:
    for element in subarr:
      result.append(element)
      result.sort()
  return result 


arr1 = [[1,2,4,7],[5,6,3]]
arr2 = [["hello","my"],["friend"]]
print(asc_order(arr1))
print(asc_order(arr2))
    

















#Object Oriented Prompt
'''
 Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
Define a repair() method that will update the condition of the podracer to "repaired".
Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''
