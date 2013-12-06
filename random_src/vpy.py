import visual as v


floor1 = v.box(pos=(0,0,0), length = 4, height= 0.55, width = 4, color = v.color.blue)
floor2 = v.box(pos=(0,4,0), length = 4, height= 0.55, width = 4, color = v.color.green)
wall1 = v.box(pos=(-2.8,2.7,0), length = 1, height = 6, width = 0.2, color = v.color.yellow)
wall2 = v.box(pos=(2.8, 2.7,0), length = 1, height = 6, width = 0.2, color = v.color.yellow)



cyl = v.sphere(pos=(0,4,0), radius = 1, color = v.color.red)
cyl.velocity = v.vector(0,-1,0)
dt = 0.03


while 2:

	v.rate (100)
	cyl.pos = cyl.pos + cyl.velocity*dt

	if cyl.y < cyl.radius:
		cyl.velocity.y = abs(cyl.velocity.y)

	else:
		cyl.velocity.y = cyl.velocity.y - 9.8*dt
		
	
