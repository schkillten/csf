import networkx as nx
import matplotlib.pyplot as plt

practice_graph = nx.Graph()

practice_graph.add_nodes_from("ABCDEF")

D = "EBCF"
A = "BC"
C = "BF"

for a in A:
	practice_graph.add_edge("A", a)

	for c in C:
		practice_graph.add_edge("C", c)

		for d in D:
			practice_graph.add_edge("D", d)
"""
nx.draw(practice_graph)
plt.show()
"""

rj = nx.Graph()

rj.add_nodes_from([("Nurse"), ("Juliet"), ("Capulet"), ("Tybalt"), ("Romeo"), ("Benvolio"), ("Montague"), ("Friar Laurence"), ("Escalus"), ("Mercutio"), ("Paris")])

J = ["Tybalt", "Capulet", "Romeo", "Friar Laurence", "Nurse"]
R = ["Friar Laurence", "Benvolio", "Montague", "Mercutio"]
C = ["Tybalt", "Paris", "Escalus"]
E = ["Paris", "Mercutio", "Montague"]


#got lazy when adding edges
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Montague", "Benvolio")

for j in J:
	rj.add_edge("Juliet", j )

	for r in R:
		rj.add_edge("Romeo", r)
		
		for c in C:
			rj.add_edge("Capulet", c);

			for e in E:
				rj.add_edge("Escalus", e)



nx.draw(rj)
plt.show()
"""
practice_graph.add_nodes_from("ABCDEF")
practice_graph.add_edge("E", "D")
practice_graph.add_edge("D", "B")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("F", "C")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "B")
practice_graph.add_edge("C", "A")
practice_graph.add_edge("A", "B")

#practice_graph.add_edge

#practice_graph.add_edges_from([("a","b"), ("c","d")])
#practice_graph.add_edges_from([("abcdef", "f"), ("abcdef", "e")])

test = "abcdef"

for i in test:
	practice_graph.add_edge("abcdef", i)
#practice_graph.add_edges_from
"""
