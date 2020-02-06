#!/usr/bin/python3

# Naive and Dynamic Programming 0-1 Knapsack Problem
# Lyell Read / 2/5/2020


import sys, os

def knapsack_naive(w, v, n, c):

	#if capacity is 0 or n is 0 (we are at first
	#	element), we are at base case.
	if c == 0 or n == 0:
		return 0

	#if the weight of the current item is more than we can
	#	carry, we must go to the next item.
	if w[n] > c:
		return knapsack_naive(w, v, (n - 1), c)


	#now we are sure we have an item that we *can* take. Do we
	#	take it?
	#what will we get if we leave it?
	leave = knapsack_naive(w, v, (n - 1), c)

	#what will we get if we take it?
	take = knapsack_naive(w, v, (n - 1), (c - w[n])) + v[n]

	#the max value will be returned
	return max(leave, take)






if __name__ == "__main__":

	n = 8
	o = [-sys.maxsize - 1 for x in range (0,n)]
	o.insert(0, None)
	p = [None, 1, 5, 8, 9, 10, 17, 17, 19]
	c = 2

	print(optimal(n, p, o, c))

