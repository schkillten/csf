import factory as fact
import visual as v
import random



colors = [v.color.red, v.color.blue, v.color.cyan, v.color.orange, v.color.magenta, v.color.white, v.color.yellow]


floor = fact.make_floor(0,0,0,4,1,0.5)

#ball1 = fact.make_sphere(0, 0, 0, 1)

#ball2 = fact.make_rand_ball(20, 1)
#print ball2.pos

#print ball1.pos, ball1.radius

#ball3 = fact.make_rand_ball(3, 1)	

def make_rand_color(lst):
	return lst[random.randrange(len(lst))]


xx = -50
yy = 50



constant = fact.make_sphere(-50, 50, 0, 5)

	





count = 0
while 1:
	count += 1
	
	fact.control_rate(20)
	ball = fact.make_rand_ball(15, 100)
	ball.color = v.color.red
	ball2 = fact.make_rand_ball(15, -100)

	ball2.color = make_rand_color(colors)
	ball.color = make_rand_color(colors)
	#ball3 = fact.make_rand_ball(15, 

	print ball2.pos
	print ball.pos, ball.radius



