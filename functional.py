#Functional Programming Prompt
'''Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.'''



def asc_order(arr):
#1st iteration
  '''
  result = []
  for subarr in arr:
    for element in subarr:
      result.append(element)
      result.sort()
  return result
  ''' 
#Flattening using List comprehension
  '''
  result = [element for subarr in arr for element in subarr]
  result.sort()
  return result
  '''
#Returning new sorted list as opposed to modifying the original
  result = [element for subarr in arr for element in subarr]
  sorted_list = sorted(result)
  return sorted_list

arr1 = [[1,2,4,7],[5,6,3]]
arr2 = [["hello","my"],["friend"]]
print(asc_order(arr1))
print(asc_order(arr2))
    


'''
How does this solution ensure data immutability?
  It ensures data immutability by returning a new list rather than modifying the original.

Is this solution a pure function? Why or why not?
  Yes this is a pure function because given the same input the function will always return the same output.

Is this solution a higher order function? Why or why not?
  No it is not a higher order function because it does not take any other functions as arguments or returns a function as its result.

Would it have been easier to solve this problem using a different programming style?
  Functional programming is better for this problem because it leads to a concise and readable solution.

Why in particular is functional programming a helpful paradigm when solving this problem?
  Functional programming provides better tools such as list comprehensions.

'''















#Object Oriented Prompt
'''
 Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
Define a repair() method that will update the condition of the podracer to "repaired".
Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
'''
