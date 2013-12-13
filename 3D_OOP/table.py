import visual as v



leg1 = v.box(pos=(-10, 0, -1), height = 10, length = 2, color = v.color.blue)
leg2 = v.box(pos=(-5, 0, -1), height = 10, length = 2, color = v.color.blue)

leg3 = v.box(pos=(-10, 0, 9), height = 10, length = 2, color = v.color.blue)
leg4 = v.box(pos=(-5, 0, 9), height = 10, length = 2, color = v.color.blue)

top = v.box(pos=((leg1.pos.x + leg2.pos.x)/float(2),5, 5),  length = 7, width = 10, color = v.color.red)


