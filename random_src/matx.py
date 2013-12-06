import networkx as nx
import matplotlib.pyplot as plot
import random as rm


"""
comp = nx.Graph()
romp = nx.Graph()



all_nodes = "abcdefghijklmnopqrstuvwxyzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
all_names = ["Kyle", "JIM", "Timmy"]

test = rm.randrange(250)

romp.add_edge(all_names[0], all_names[1])
romp.add_edge(all_names[0], all_names[2])
romp.add_edge(all_names[1], all_names[2])

for c in range(test):
	romp.add_edge("Kyle", all_nodes[c])

	test = rm.randrange(250)

	for c in range(test):
		romp.add_edge("Timmy", all_nodes[c])

		for c in range(test):
			romp.add_edge("JIM", all_nodes[c])


print romp.nodes()
print romp.edges()

for n in all_nodes[:10]:
	
	comp.add_node(n)




for i in all_nodes[10:20]:
	comp.add_edge("Kyle", i)	

for c in range(len(all_nodes)):

	comp.add_edge("jim", all_nodes[c])

for l in range(len(all_nodes[::-1])):

	comp.add_edge("bob", all_nodes[l])

for i in range(len(all_nodes)):

	romp.add_edge("bob", all_nodes[i])

nx.draw(romp)
nx.draw(comp)
plot.show()
"""

ng = nx.Graph()


alph_low = "abcdefghijklmnopqrstuvwxyz"
alph_up = alph_low.upper()


for i in range(len(alph_low)):

	ng.add_edge(alph_low[i], alph_up[i])




print ng.number_of_nodes()
print ng.number_of_edges()

nx.draw_circular(ng)
plot.show()

