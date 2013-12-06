import visual as v
import random

colors = [v.color.red, v.color.blue, v.color.yellow, v.color.cyan, v.color.orange, v.color.black, v.color.white, v.color.green, v.color.magenta]

length = random.randrange(len(colors)-1)

floor = v.box(pos=(0,0,0), length = 4, height= 0.5, width = 4, color = v.color.red)

ball = v.sphere(pos=(0,4,0), radius = 1, color = v.color.blue)
ball.velocity = v.vector(0,-1,0)
dt = 0.01
print ball.y




while 1:

	v.rate (100)
	ball.pos = ball.pos + ball.velocity*dt
	if ball.y < ball.radius:
		#print "hey"
		#print ball.color
					
		#ball.color = v.color.red

		rand_color = random.randrange(len(colors))		
		print colors[rand_color]	
		ball.color = colors[rand_color]
		#print ball.color
	
		ball.velocity.y = abs(ball.velocity.y)

	else:
		ball.velocity.y = ball.velocity.y - 9.8*dt
