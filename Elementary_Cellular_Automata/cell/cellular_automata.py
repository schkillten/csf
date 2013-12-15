from utilities import decimalToBinary, binaryToDecimal
import random

class CellularAutomata(object):
  LIST_SIZE = 150

  def __init__(self, rule):
    self.rule = decimalToBinary(rule)
    self.generation_list = [[]]

    # FIXME Simple first gen init. Make a function to generate a random 1 gen
    #self.generation_list.append(['0'] * self.LIST_SIZE)
    #self.generation_list[0][self.LIST_SIZE/2] = "1"

    for i in range(self.LIST_SIZE):
      rand = random.randint(0,1)
      self.generation_list[0].append(str(rand))

  def generateNext(self):
    prv_index = len(self.generation_list) - 1
    next_generation = []

    for i in range(len(self.generation_list[prv_index])):
      neighbors = self.__getNeighbors(i, prv_index)
      rule_index = binaryToDecimal(neighbors)
      new_cell = self.rule[rule_index]
      next_generation.append(new_cell)

    self.generation_list.append(next_generation)

  def __getNeighbors(self, current_cell, last_generation):
    neighbors = ""
    current_generation = self.generation_list[last_generation]

    if current_cell -1 >= 0:
      neighbors += (current_generation[current_cell - 1])
    else:
      neighbors += "0"

    neighbors += (current_generation[current_cell])

    if current_cell + 1 < len(current_generation):
      neighbors += (current_generation[current_cell + 1])
    else:
      neighbors += "0"
    return neighbors

  def getAllGenerations(self):
    return self.generation_list
