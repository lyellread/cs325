#!/usr/bin/python3

# Dynamic Programming Rod Problem with Cost To Cut
# Memoize, Bottom Up
# Lyell Read / 2/5/2020


import sys, os

def optimal(n, p, o, c):

	#print("Called optimal with n = ", n, "| p = ", p, "| o = ", o, "|")

	#handle base case
	if n == 1:
		o[1] = p[1]
		#print("Base Case Reached -- Returned o[1] == ", o[1])
		return o[1]

	#we are at n > 1; do we have an entry in 
	#	the optimal array for n?
	if o[n] == (-sys.maxsize - 1):
		
		#we do! set O (the current max optimal) to int min	
		O = p[n]
		
		#iterate over all possible cuts at this point
		for k in range (1, n):

			#Result is the total of the price of the cut
			#	piece and the optimal of the rest
			#	charge for a cut (c) here as this split requires a cut
			R = (p[k] + optimal(n-k, p, o, c) - c)

			#Update if we have found a new max
			if R > O:
				O = R
		#Update our optimal array with the new max
		o[n] = O

		#print("Search for new o found, resulted in O == ", O)
		#Return the optimal for our length
		return O

	else:

		#print("Found a stored O value == ", o[n])

		#we do indeed have something in the optimal array; return that
		return o[n]

if __name__ == "__main__":

	n = 8
	o = [-sys.maxsize - 1 for x in range (0,n)]
	o.insert(0, None)
	p = [None, 1, 5, 8, 9, 10, 17, 17, 19]
	c = 2

	print(optimal(n, p, o, c))

