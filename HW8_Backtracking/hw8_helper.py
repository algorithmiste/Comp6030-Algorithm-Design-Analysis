import graph

g1 = graph.random_graph(10,0.15,directed=False,seed=2018)
g2 = graph.random_graph(10,0.20,directed=False,seed=2018)
g3 = graph.random_graph(10,0.22,directed=False,seed=2018)

# Note for homework 8
# g1 is the graph shown in the image rg_10_15_2018.png
# g2 is the graph shown in the image rg_10_20_2018.png
# g3 is the graph shown in the image rg_10_22_2018.png

# check if (3,9) is an edge in g1.  It is!
e = (3,9)
if e in g1:
	print("Yes, the edge", e, "is in g1.")
else:
	print("No, the edge", e, "is not in g1." )

# check if (3,0) is an edge in g1.  It is not.
e = (3,0)
if e in g1:
	print("Yes, the edge", e, "is in g1.")
else:
	print("No, the edge", e, "is not in g1." )

# traverse the neighbors of a given node. May be needed for last problem.
for v in g1.Neighbors[8]:
	print(v, "is a neighbor of 8")

#print(g1.Neighbors[0])
#print(g1.Vertices)
sum_n = 0
for node in g1.Vertices:
	if (g1.Neighbors[node] != set()): # meaning that there exists a road attached to the station (node,vertex) in question
		print('Camera {} can view the following stations: {}'.format(node, g1.Neighbors[node]))


def numVertices(g):
	total = 0
	for node in g.Vertices:
		total += 1
	return total
#print(numVertices(g1))

cameraAtVertex_i = [None]*numVertices(g1)
print(cameraAtVertex_i)
#def initializeCameras(g)

