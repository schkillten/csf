import visual as v
import random

colors = [v.color.red, v.color.blue, v.color.yellow, v.color.cyan, v.color.orange, v.color.white, v.color.green, v.color.magenta]

length = random.randrange(len(colors)-1)

floor = v.box(pos=(0,0,0), length = 4, height= 0.5, width = 4, color = v.color.white)
### Ball1 specs
ball = v.sphere(pos=(0,4,0), radius = 1, color = v.color.blue)
ball.velocity = v.vector(0,-1,0)
### Ball2 specs
ball2 = v.sphere(pos=(0,-4,0), radius = 1, color = v.color.blue)
ball2.velocity = v.vector(0,-1,0)
dt = 0.01
print ball.y



def make_color(lst):

	rand_color = random.randrange(len(lst))
	return lst[rand_color]

while 1:

	v.rate (100)
	ball.pos = ball.pos + ball.velocity*dt
	ball2.pos = ball2.pos + ball2.velocity*dt
	if ball.y < ball.radius:



		ball.color = make_color(colors)
		print "Ball1 color: ", ball.color
		floor.color = make_color(colors)
		print "Floor color: ", floor.color
		ball.velocity.y = abs(ball.velocity.y)

		ball2.velocity.y = abs(ball2.velocity.y)
	
	else:
		ball.color = make_color(colors)
		ball.velocity.y = ball.velocity.y - 9.8*dt

		ball2.velocity.y = ball.velocity.y - 9.8*dt

	
