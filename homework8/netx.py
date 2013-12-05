import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1,2), (1,3)])
G.add_node(1)
G.add_edge(1,15)
G.add_node("KYLE")
G.add_nodes_from("abcdef")
G.add_edges_from([("abc", "def")])
G.number_of_nodes()
G.number_of_edges()
G.nodes()
G.edges()
G.neighbors(1)
#G.remove_nodes_from("spam")

#G.remove_edge(1,3)



H=nx.DiGraph(G)
H.edges()

edgelist = [(0,1), (1,2), (2,3) ]
H=nx.Graph(edgelist)

G[1]
G[1][2]
G.add_edge(1,3)
G[1][3]['color'] = 'blue'



FG=nx.Graph()
FG.add_weighted_edges_from([(1,2,0.125), (1,3,0.75), (2,4,1.2), (3,4,0.375)])

for n,nbrs in FG.adjacency_iter():
	for nbr,eattr in nbrs.items():
		data = eattr['weight']
		if data < 0.5: print('(%d, %d, %.3f)' % (n,nbr,data))

nx.draw(FG)

#nx.draw(H)
#nx.draw(G)
plt.show()

