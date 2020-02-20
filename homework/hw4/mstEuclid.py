#!/usr/bin/python3

# Euclidian MST (Done Sketchily. Thank NDSS for that)
# Lyell Read / 2/5/2020


import sys, os, math, itertools

def distancebetween (a, b):

	return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))


def printarray (a):
    for e in a:
        print(e, end="\n")
    print()

def printedge(a):
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

	ret = 0
	path_exists = 0

	if [a, b, 1] in taken_edges or [b, a, 1] in taken_edges or [a, b, 0] in taken_edges or [b, a, 0] in taken_edges:

		return 1

	for x in taken_edges:

		if x[0] == a and x[2] == 0:

			#print("----")

			bak_x = x

			# taken_edges.remove([x[1], x[0]])
			# taken_edges.remove(x)

			###
			for y in taken_edges:

				if y[0] == x[0] and y[1] == x[1]:

					y[2] = 1

				if y[1] == x[0] and y[0] == x[1]:

					y[2] = 1


			ret += check_points(bak_x[1], b, taken_edges)

			path_exists += 1

	if path_exists == 0:

		return 0

	else:

		return ret


def check_edge(current_edge, taken_edges):

	#check if either end of current_edge connects to the other end

	taken_edges_bidirectional = []

	for x in taken_edges:
		taken_edges_bidirectional.append([x[0], x[1], 0])
		taken_edges_bidirectional.append([x[1], x[0], 0])

	#print("++++++++++")

	return check_points(current_edge[0], current_edge[1], taken_edges_bidirectional)


def mst(c, e):

	taken_edges = []
	edge_index = 0

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

		#dbg
		else:

			continue
			#print("== DISCARDING Edge:", current_edge, "in context", taken_edges)

	return taken_edges	


def run(filename):

	with open(filename, "r") as f:
		readlines = f.read().splitlines()
	f.close()

	count = readlines[0]

	lines = readlines[1:int(count) + 1]

	#print (lines)

	L_coords = [[int(y) for y in x.split(" ")] for x in lines]

	L_edges = [list(x) for x in list(itertools.combinations(L_coords, 2))]

	for x in L_edges:
		d = distancebetween(x[0], x[1])
		x.append(d)

	L_edges = sorted(L_edges, key = lambda x: x[2])

	#print("===", L_edges)

	i = 0
	coords = {}
	for x in L_coords:
		coords[str(i)] = str(x)
		i += 1

	i = 0
	edges = L_edges

	ret = mst(coords, edges)

	s = 0

	for x in ret:
		s += x[2]

	print("Edges Taken:")
	[printedge(x) for x in ret]
	print ("\nTotal Weight Taken:", s)

	a = []

	for x in ret:
		if x[0] not in a:
			a.append(x[0])

		if x[1] not in a:
			a.append(x[1])

	print("\nVertex Check:")
	print(" - Uniqie Verticies Visited:", len(a))
	print(" - Total Verticies Provided:", len(L_coords))
	



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
	
