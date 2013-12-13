import visual as v

ball = v.sphere(pos=(0,4, 0), radius = 1, color=v.color.red)
ball.velocity = v.vector(0,-1,0)

floor = v.box(pos=(0,0,0), length=4, width = 4, height = 0.5, color=v.color.orange)

dt = 0.01

while True:


	v.rate(20)
	ball.pos = ball.pos + ball.velocity*dt
	print ball.velocity.y
	if ball.y < ball.radius:
		ball.velocity.y = abs(ball.velocity.y)	

	else:

		ball.velocity.y = ball.velocity.y - 9.8*dt
