import visual as v
import random




colors = [v.color.red, v.color.blue, v.color.cyan, v.color.orange, v.color.magenta, v.color.white, v.color.yellow]


def make_color(col):
	pass

def control_rate(speed):
	return v.rate(speed)

def make_floor(x,y,z,leng, wid, hei):

	return v.box( pos = (x,y,z), length = leng, width = wid, height = hei)

def make_sphere(x, y, z, rad):
	return v.sphere( pos = (x, y, z), radius = rad)

#makes a random ball of random size and position
def make_rand_ball(size, position):

	if position < 0:

		x = random.randrange(abs(position)) * -1
		y = random.randrange(abs(position)) * -1
		z = random.randrange(abs(position)) * -1

	else:
		x = random.randrange(position)
		y = random.randrange(position)
		z = random.randrange(position)

	

	sz = random.randrange(size)
	
	return v.sphere( pos = (x,y,z), radius = sz)
	

def make_rand_color(colors):
	pass

