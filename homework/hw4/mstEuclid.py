#!/usr/bin/python3

# Euclidian MST 
# Lyell Read / 2/5/2020


import sys, os, math, itertools

def distancebetween (a, b):

	return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))

def printarray (a):
    for e in a:
        print(e, end="\n")
    print()


def run(filename):

	with open(filename, "r") as f:
		lines = f.read().splitlines()[1:-1]
	f.close()

	coords = [[int(y) for y in x.split(" ")] for x in lines]

	edges = [list (x) for x in list(itertools.combinations(coords, 2))]

	printarray(edges)


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
	
