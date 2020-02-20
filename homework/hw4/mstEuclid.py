#!/usr/bin/python3

# Euclidian MST 
# Lyell Read / 2/5/2020


import sys, os, math

def distancebetween (a, b):

	return int(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))

def printarray (a):
    for e in a:
        print(e, end="\n")
    print()


if __name__ == "__main__":

	
	
