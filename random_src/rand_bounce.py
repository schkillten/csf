import visual as v
import random
import sys


#######

# Need to have Vpython installed 


#######


# Function to make a random color out of the specified colors
def makeRandomColors(lst):
	return lst[random.randrange(len(lst))]


x = 0.5
y = 0
z = 0
	

colors = [v.color.red, v.color.blue, v.color.yellow, v.color.cyan, v.color.orange, v.color.white, v.color.green, v.color.magenta]

floor = v.box(pos=(0,0,0), length = 15, height = 0.5, width = 5, color = makeRandomColors(colors)) 

print floor.length

sph = v.sphere(pos = (1, 6, 0), radius = 1, color = makeRandomColors(colors))
sph.velocity = v.vector(x, y, z)
dt = 0.01

count = 0

while 1:
	
		
	v.rate(400)
	# Checks if the sphere y axis is < the sph radius
	count += 1
	
	sph.pos = sph.pos + sph.velocity*dt	
	print sph.pos.x	

	
	# Somewhat of a timer/counter, every 25 iterations throught eh while loop
	# the colors are changed on the sphere and floor piece, then the counter is reset
	if count == 25:
		sph.color = makeRandomColors(colors)
		floor.color = makeRandomColors(colors)

		count = 0




	if sph.y < sph.radius:	
		sph.velocity.y = abs(sph.velocity.y)


	else:
		sph.velocity.y = sph.velocity.y - 9.8*dt



	if sph.pos.x > floor.length/float(2):
		sph.velocity.x = -0.5


	elif sph.pos.x < floor.length/float(-2):
		sys.exit(0)


	else:
		print "test cond"
