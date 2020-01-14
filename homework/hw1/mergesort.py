#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020
# Citations: 
# - 

import os, sys


def mergesort(x):

	if len(x) == 1:


	else:
		





if __name__ == "__main__":

	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	with open(sys.argv[1], "r") as f:
		lines = [x.split(" ") for x in f.readlines()]
		f.close()

	result = [mergesort(x) for x in lines]

	#print result
	exit()

