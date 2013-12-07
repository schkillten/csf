import visual as v

scene2 = v.display(title="Example of Tetrahedrons", x=0, y = 0, width = 600,height = 200,center=(5,0,0),backround = (0,1,1))

for obj in scene2.objects:
	if isinstance(obj,box):
		obj.color = color.red

print "test"

p = v.points(pos=[(-1,0,0), (1,0,0)], size = 50, color = v.color.red)
