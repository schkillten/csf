import visual as v
import random


rs = [v.color.red, v.color.blue, v.color.cyan, v.color.orange, v.color.magenta, v.color.white, v.color.yellow]



def make_color(colors):

	return colors[random.randrange(len(colors))]



i = 1
y = 1
z = 1
rad = 0.5



"""

for i in range(25):
	v.rate(25)

	line = v.sphere(pos=(i-1, i-1,0), radius = 1, color = make_color(rs))
	line2 = v.sphere(pos=((i-1) * -1, (i-1) * -1, 0), radius =1, color = make_color(rs))
	line3 = v.sphere(pos=((i -1) * -1, i-1, 0), radius = 1, color = make_color(rs))
	line4 = v.sphere(pos=((i-1), (i-1) * -1, 0), radius = 1, color = make_color(rs))
	line5 = v.sphere(pos=((i-1),0,0), radius = 1)	
	line6 = v.sphere(pos=(0,i-1,0),radius = 1)
	line7 = v.sphere(pos=((i-1) * -1, 0,0), radius = 1)
	line8 = v.sphere(pos=(0, (i-1) * -1, 0), radius = 1)


"""


while True:

	v.rate(20)

	first_half = v.sphere(pos=((i * 0.5),(i * 0.2),z), radius = rad, color = make_color(rs))
	print first_half.y
	second_half = v.sphere(pos=(first_half.x * -1, first_half.y * -1, 0), radius = rad, color = make_color(rs))
	i +=1
	if first_half.y > 15:
		first_half.pos = fist_half.pos + first_half.y * -1	
