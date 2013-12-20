import sys

# Takes binary string and converts to decimal
def binaryToDecimal(binary):

  powers_of_two = []
  total = 0
  binary = binary[::-1]

  for i in range(len(binary)):
    powers_of_two += [2**i]

  for i in range(len(binary)):

    if binary[i] == "1":
      total += powers_of_two[i]

  return total

#Takes a decimal number as a string or int and converts to binary,
# 8 bit word size only (0-255)
def decimalToBinary(decimal):

  decimal = int(decimal)
  binary = ""

  while decimal > 0:
    mod  = decimal % 2
    decimal = decimal / 2

    if mod == 1:
      binary += "1"
    else:
      binary += "0"

  size = len(binary)
  if size != 8:
    sub = 8 - size
    binary += "".join("0" * sub)

  #return binary
  #FIXME Somewhere in cellular_automata.py using this functon gives issues when its reversed at the end
  # But now the binary number is backards if we don't reverse it
  return binary[::-1]

def resetScreen():
  sys.stdout.write('\033[2J')
  sys.stdout.write('\033[H')
  sys.stdout.flush()

def printError():
  resetScreen()
  print "Invalid rule, please enter a number between 0-255."

def getValidRuleFromUser():
  resetScreen()
  valid_rule = False
  rule_input = ""

  while not valid_rule:
    print "Enter the cellular rule\n$",
    rule_input = raw_input()

    if not rule_input.isdigit():
      printError()
    else:
      rule = int(rule_input)

      if rule >= 0 and rule < 256:
        valid_rule = True
      else:
        printError()

  return rule_input



