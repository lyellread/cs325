#!/usr/bin/python3

# Euclidian MST (Done Sketchily. Thank NDSS for that)
# Lyell Read / 2/5/2020


import sys, os, math, itertools

def distancebetween (a, b):
	
	#return the nearest integer distance between two points
	return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))


def printarray (a):
	
	#print array
    for e in a:
        print(e, end="\n")
    print()

def printedge(a):
	
	#print an edge prettily
	print(" - (" + 
			str(a[0][0]) + 
			", " + 
			str(a[0][1]) + 
			") --> (" + 
			str(a[1][0]) + 
			", " + 
			str(a[1][1]) + 
			")  \tWeight:" + 
			str(a[2]))

def check_points (a, b, taken_edges):
	
	#Check that points a, b are or are not connected somehow

	#zero the return value
	ret = 0

	#zero the path exists
	path_exists = 0

	#if there exists a taken edge that connects a and b, return 1 (T)
	if [a, b, 1] in taken_edges or [b, a, 1] in taken_edges or [a, b, 0] in taken_edges or [b, a, 0] in taken_edges:
		return 1

	#Otherwise, for each of the edges that are being considered
	for x in taken_edges:
	
		#if that edge starts with point a (and goes to x[1], and has not been 'visited' (x[2] = 0))
		if x[0] == a and x[2] == 0:
	
			#make a backup of x
			bak_x = x

			#for each of the other edges, examine if it is the same as x, of so set the visited bit
			for y in taken_edges:

				if y[0] == x[0] and y[1] == x[1]:

					y[2] = 1

				if y[1] == x[0] and y[0] == x[1]:

					y[2] = 1

			#check that new start point (end of x) for connection to b
			ret += check_points(bak_x[1], b, taken_edges)

			#assert that we found at least one edge leading out of a
			path_exists += 1

	#we found no edges leading out of a, so a cannot connect to b
	if path_exists == 0:

		return 0

	#return ret.
	else:

		return ret


def check_edge(current_edge, taken_edges):

	#check if either end of current_edge connects to the other end


	#generate a list of unidirectional edges (a->b and b->a for a,b)
	taken_edges_bidirectional = []

	for x in taken_edges:
		taken_edges_bidirectional.append([x[0], x[1], 0])
		taken_edges_bidirectional.append([x[1], x[0], 0])

	#call check points on specific points
	return check_points(current_edge[0], current_edge[1], taken_edges_bidirectional)


def mst(c, e):

	#initialization
	taken_edges = []
	edge_index = 0

	#while we have not found #vert-1 edges, 
	while len(taken_edges) < len(c)-1:

		#1. choose smallest next edge
		current_edge = e[edge_index]
		edge_index += 1

		#print("== Chose Edge:", current_edge)

		#2. check edge for cycle
		if check_edge(current_edge, taken_edges) != 1:

			#check found no cycle; add edge

			#print("== Keeping Edge:", current_edge)
			taken_edges.append(current_edge)

		# dbg
		# else:

		# 	continue
			#print("== DISCARDING Edge:", current_edge, "in context", taken_edges)

	return taken_edges	


def run(filename):

	#open and read from file
	with open(filename, "r") as f:
		readlines = f.read().splitlines()
	f.close()

	#get count - first line
	count = readlines[0]

	#now we know the lines
	lines = readlines[1:int(count) + 1]

	#generate coordinate list
	coords = [[int(y) for y in x.split(" ")] for x in lines]

	#generate edge list
	edges = [list(x) for x in list(itertools.combinations(coords, 2))]

	#for each edge, calculate the distance between the points, and add that to the element
	for x in edges:
		d = distancebetween(x[0], x[1])
		x.append(d)

	#Sort edges by increasing weight
	edges = sorted(edges, key = lambda x: x[2])

	#Run MST!!!
	ret = mst(coords, edges)

	#generate sum of weights used
	s = 0
	for x in ret:
		s += x[2]

	# IO!
	print("Edges Taken:")
	[printedge(x) for x in ret]
	print ("\nTotal Weight Taken:", s)

	#generate set of coords used
	a = []
	for x in ret:
		if x[0] not in a:
			a.append(x[0])
		if x[1] not in a:
			a.append(x[1])

	#moar IO
	print("\nVertex Check:")
	print(" - Uniqie Verticies Visited:", len(a))
	print(" - Total Verticies Provided:", len(coords))
	



if __name__ == "__main__":

	#arg len
	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	#file exists check
	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	#start the program!
	run(sys.argv[1])
	
