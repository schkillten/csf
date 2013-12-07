import random as r
from visual import *

sph = sphere(pos=(0,0,0), radius = 1, color = color.red)
bx = box(pos=(0,5,0), width = 3, height = 3, length = 3, color = color.blue)



def makeColor(test):

	return test[r.randrange(len(test)-1)]



for i in range(5):
	print "Pre",sph.color
	sph.color = sph.color[0] + 0.5
	print "After", sph.color
