'''Casey Carr
   04/24/2018
   HW 8 '''

'''Imagine a graph representing a network of stations (nodes) connecting by roads (edges). 
   If a camera is placed at a node, it can “watch” all roads connected to it. 
   For example, in the network rg_10_15_2018, a camera placed at station 8 can watch the roads that connect station 8 to 
   stations 3, 4, and 0. In this network, cameras placed at stations 3, 4, 0 and 1 can watch all roads. 
   Therefore, {3, 4, 0, 1} is a camera placement on this network that covers all roads. '''

import graph

g1 = graph.random_graph(10,0.15,directed=False,seed=2018)
g2 = graph.random_graph(10,0.20,directed=False,seed=2018)
g3 = graph.random_graph(10,0.22,directed=False,seed=2018)

def numVertices(g):
	total = 0
	for node in g.Vertices:
		total += 1
	return total

'''Q1. Write a Python program, using the backtracking technique we learned, to generate all possible camera 
       placements on a network. Test your program on the 3 networks given. '''
''' Input: g, a graph network (representing n nodes with a set of i cameras, each located at any one of the n nodes), 
							   i (a number, or "level") '''
# Output: None
# Precondition: V[0], V[1], ..., V[i] - the graph's vertices - have been "assigned values - camera loci - up to i".
# Postcondition: print out all sets (graphs) of camera loci, having cameras 0, ..., i placed in the graph.

# verified that 1024 possible combinations for each
def allCameraLoci(g, cameraAtVertex, i):

	def valid(cameraAtVertex):
		return True	

	if i == len(cameraAtVertex)-1:
		if valid(cameraAtVertex):		# check for validity
			print(cameraAtVertex)
			
	else:
		# we generate all possibilities for the next level
		cameraAtVertex[i+1] = True
		allCameraLoci(g, cameraAtVertex, i+1)   # use same strategy

		# now, go back and reset the choice
		cameraAtVertex[i+1] = False
		allCameraLoci(g, cameraAtVertex, i+1)   # use same strategy
	

# print(allCameraLoci(g1,[None]*numVertices(g1), -1))
# print(allCameraLoci(g2,[None]*numVertices(g2), -1))
# print(allCameraLoci(g3,[None]*numVertices(g3), -1))


'''Q2. We are limited with resources and have budget for only 6 cameras. Write a Python program, using the backtracking 
       technique we learned, to generate all possible camera placements on a network that uses only 6 or fewer cameras. 
       Test your program on the 3 networks given. '''

def isValid(cameraAtVertex, numCameras):
	count = 0
	for vertex in cameraAtVertex:
		if vertex == True:
			count += 1
	if count > numCameras:
		return False
	return True


def allCameraLoci_budget(g, cameraAtVertex, i, numCameras):
	
	if i == len(cameraAtVertex)-1:
		if isValid(cameraAtVertex, numCameras):		# check for validity
			print(cameraAtVertex)		
	else:
		# we generate all possibilities for the next level
		cameraAtVertex[i+1] = True
		allCameraLoci_budget(g, cameraAtVertex, i+1, numCameras)   # use same strategy

		# now, go back and reset the choice
		cameraAtVertex[i+1] = False
		allCameraLoci_budget(g, cameraAtVertex, i+1, numCameras)   # use same strategy
	
# print(allCameraLoci_budget(g1,[None]*numVertices(g1), -1, 6))
# print(allCameraLoci_budget(g2,[None]*numVertices(g2), -1, 6))
# print(allCameraLoci_budget(g3,[None]*numVertices(g3), -1, 6))



'''Q3. Write a Python program, using the backtracking technique we learned, to find the minimum number of cameras that 
	   can be placed to watch all roads of a given network. Print out the placement that gives the minimum number of cameras. 
	   Test your program on the 3 networks given. '''
def getNumCameras(cameraAtVertex):
	cameras = 0
	for i in range(len(cameraAtVertex)):
		if cameraAtVertex[i] == True:
			cameras += 1
	return cameras

def stationsWatched(g, cameraAtVertex):
	stationsWatched = set()
	for vertex in range(len(cameraAtVertex)): #indicates the index of a given station
		if cameraAtVertex[vertex] == True:
			if (g.Neighbors[vertex] != set()): # meaning that there exists a road attached to the station (node,vertex) in question
				for neighbor in g.Neighbors[vertex]:
					stationsWatched.add(neighbor)
	return stationsWatched

def numStationsWithRoads(g):
	total = 0
	for vertex in g.Vertices:
		if (g.Neighbors[vertex] != set()): 
			total += 1
	return total

def stationsWithRoads(g):
	stationsSet = set()
	for vertex in g.Vertices:
		if (g.Neighbors[vertex] != set()): 
			stationsSet.add(vertex)
	return stationsSet

def isNetwork(g, cameraAtVertex):
	if stationsWatched(g, cameraAtVertex).issubset(stationsWithRoads(g)) and stationsWithRoads(g).issubset(stationsWatched(g, cameraAtVertex)): 
		return True
	return False

numCameras = None
currentMinSet = None
def minNumCameras(g, cameraAtVertex, i):   
	global currentMinSet
	global numCameras

	if i == len(cameraAtVertex)-1:
		if isNetwork(g, cameraAtVertex) and (numCameras is None or (getNumCameras(cameraAtVertex) < numCameras)):		# check for validity
			numCameras = getNumCameras(cameraAtVertex)
			currentMinSet = cameraAtVertex
			print('The minimum number of cameras needed: {}'.format(numCameras))	
			print('The optimized placement is: {}'.format(currentMinSet))	
	else:
		# we generate all possibilities for the next level
		cameraAtVertex[i+1] = True
		minNumCameras(g, cameraAtVertex, i+1)   # use same strategy

		# now, go back and reset the choice
		cameraAtVertex[i+1] = False
		minNumCameras(g, cameraAtVertex, i+1)   # use same strategy

#Note: Since numCameras and currentMinSet are declared as GLOBAL, only execute one of the following at a time.
#print(minNumCameras(g1, [None]*numVertices(g1), -1))
#print(minNumCameras(g2, [None]*numVertices(g2), -1))
#print(minNumCameras(g3, [None]*numVertices(g3), -1))

'''Q4. Again we have a budget of k cameras. For example, k=6. We want the camera to cover as many roads as possible. 
	   It is possible we won’t be able to cover all roads. Write a Python program, using the backtracking technique we
       learned, to find the camera placements that cover as many roads as possible. '''

currentMaxSet = None
def maxCoverage(g, cameraAtVertex, i, numCameras):   
	global currentMaxSet

	if i == len(cameraAtVertex)-1:
		if isValid(cameraAtVertex, numCameras):		# check for validity
			if currentMaxSet == None or len(stationsWatched(g, cameraAtVertex)) > len(currentMaxSet):
				currentMaxSet = stationsWatched(g, cameraAtVertex)
				print('The maximum coverage placement for {} cameras is: {}'.format(numCameras, cameraAtVertex))	
	else:
		# we generate all possibilities for the next level
		cameraAtVertex[i+1] = True
		maxCoverage(g, cameraAtVertex, i+1, numCameras)   # use same strategy

		# now, go back and reset the choice
		cameraAtVertex[i+1] = False
		maxCoverage(g, cameraAtVertex, i+1, numCameras)   # use same strategy

# print(maxCoverage(g1, [None]*numVertices(g1), -1, 6))
# print(maxCoverage(g2, [None]*numVertices(g2), -1, 6))
# print(maxCoverage(g3, [None]*numVertices(g3), -1, 6))