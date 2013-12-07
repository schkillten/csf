import visual as v
import random
import sys

colors = [v.color.red, v.color.blue, v.color.yellow, v.color.cyan, v.color.orange, v.color.white, v.color.green, v.color.magenta]





def make_color(lst):

	return lst[random.randrange(len(lst))]

	


floor = v.box(pos=(0,0,0), length = 10, width = 0.5, height  = 0.5, color = make_color(colors))

#Ball 1 starts on the right side
ball1 = v.sphere(pos=(floor.length/float(2), 6, 0), radius = 0.5, color = make_color(colors))

# Ball 2 starts on the left side
ball2 = v.sphere(pos=(floor.length/float(2) *-1, 6, 0), radius = 0.5, color = make_color(colors))




ball1.velocity = v.vector(-0.2, -1, 0)
ball2.velocity = v.vector(0.2, -1, 0)

dt = 0.01

### Uncomment 
count = 0

while 1:

	# Controls number of iterations per second in the loop to control speed
	v.rate(300)
	ball1.pos = ball1.pos + ball1.velocity*dt
	ball2.pos = ball2.pos + ball2.velocity*dt
	print "Ball1: ",ball1.pos
	print "Ball2: ", ball2.pos

	
	##### Uncomment if you want colors to change every 25 iterations through while loop
	count += 1
	#if count > 25:
		#ball1.color = make_color(colors)

		#ball2.color = make_color(colors)

		#floor.color = make_color(colors)
		#count = 0

	if ball2.pos.x > floor.length/float(2):
		print "test"
		ball2.velocity.x = ball2.velocity.x * -1

	

	if ball1.pos.x < floor.length/float(2) * -1:
		print "Test2"	
		ball1.velocity.x = ball1.velocity.x * -1

	elif ball1.pos.x > floor.length/float(2) and ball2.pos.x < floor.length/float(2) * -1:
		sys.exit(0)


	if ball1.y < ball1.radius:


		# causes colors to change of all objects on coloision with the floor
		ball1.color = make_color(colors)
		ball2.color = make_color(colors)
		floor.color = make_color(colors)

		ball1.velocity.y = abs(ball1.velocity.y) 
		ball2.velocity.y = abs(ball2.velocity.y)

	else:

		ball1.velocity.y = ball1.velocity.y - 9.8*dt
		ball2.velocity.y = ball2.velocity.y - 9.8*dt
