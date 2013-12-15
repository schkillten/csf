import sys
from time import sleep
from utilities import decimalToBinary, binaryToDecimal, \
                      getValidRuleFromUser, resetScreen

from cellular_automata import CellularAutomata

def main():
  rule = getValidRuleFromUser()
  print "Rule %s : %s entered." % (rule, decimalToBinary(rule))

  automata = CellularAutomata(rule)

  for i in range(200):
    automata.generateNext()
    sleep(0.1)
    resetScreen()
    output = automata.getAllGenerations()

    size = len(output)
    start = 0
    if size - 45 >= 0:
      start = size - 45

    for i in range(start, len(output)):
      for j in range(len(output[i])):
        if output[i][j] == '1':
          sys.stdout.write(u'\u2588')
        else:
          sys.stdout.write(' ')
      print ''

main()
