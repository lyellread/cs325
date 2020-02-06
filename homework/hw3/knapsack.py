#!/usr/bin/python3

# Naive and Dynamic Programming 0-1 Knapsack Problem
# Lyell Read / 2/5/2020


import sys, os, time, random

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


def knapsack_dp(w, v, n, c, o):

	#if we already have an entry for this n, c pair, return it
	if o[n][c] != None:
		return o[n][c]

	#if capacity is 0 or n is 0 (we are at first
	#	element), we are at base case.
	if c == 0 or n == 0:
		return 0

	#if the weight of the current item is more than we can
	#	carry, we must go to the next item
	if w[n] > c:
		return knapsack_dp(w, v, (n - 1), c, o)

	#now we are sure we have an item that we *can* take. Do we
	#	take it?
	#what will we get if we leave it?
	leave = knapsack_dp(w, v, (n - 1), c, o)

	#what will we get if we take it?
	take = knapsack_dp(w, v, (n - 1), (c - w[n]), o) + v[n]

	#the max value will be returned
	o[n][c] = max(leave, take)
	return max(leave, take)

def run (n, c, dp):

	w = [0 for x in range(0, n)]
	while sum(w) < c:
		w[random.randint(0, len(w)-1)] += 1

	v = [random.randint(0, 50) for x in range (0, n)]

	w.insert(0, None)
	v.insert(0, None)

	o = [[None for x in range(0,c+1)] for y in range(0,n+1)]

	dp_start_time = time.time()
	dp_result = knapsack_dp(w, v, n, c, o)
	dp_end_time = time.time()

	print("Completed: n=", n, 
			" c=", c, 
			" DP Time: ", (dp_end_time - dp_start_time), 
			" DP Result: ", dp_result, 
			".")

	dp.append(dp_end_time - dp_start_time)

def printarray (a):
    for e in a:
        print(e, end="\n")
    print()


if __name__ == "__main__":

	lengths = [x for x in [50, 100, 150, 200, 250, 300, 350, 400, 600, 800]]
	
	
	for r in range (0, 5):
		dp = []
		print("==== RUN ", r, " ====")
		for x in lengths:
			run(x,100, dp)

		printarray(dp)
	
