from visual import *
import random

# Note to self, remember to be careful naming variables
# since vissual module methods are named cylinder, box, 
# sphere etc...


colors = [color.red, color.yellow, color.blue, color.cyan, color.orange, color.green, color.magenta, color.black, color.white]



length = random.randrange(len(colors)-1)
print length


wall = box(pos = (0, 5, 0), length = 1, width = 1, height = 1, color = colors[length])
bounds = sphere(pos = (0,0,0), radius = 1)

random.shuffle(colors)

ball = sphere(pos=(0, 6, 0), radius = 1, color = colors[length])
