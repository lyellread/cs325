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

def run (n, c, dp, naive):

	#make a list of weights with all being 0
	w = [0 for x in range(0, n)]

	#while the sum is not equal to the carrying capacity, add to a random weight
	while sum(w) < c:
		w[random.randint(0, len(w)-1)] += 1

	#generate a bunch of random values to correspond with those weights
	v = [random.randint(0, 50) for x in range (0, n)]

	#add a 'None' at the start of those lists so indicies line up
	w.insert(0, None)
	v.insert(0, None)

	#Create our optimal nested list, None filled
	o = [[None for x in range(0,c+1)] for y in range(0,n+1)]

	#perform the timing runs of each naive and dp
	naive_start_time = time.time()
	naive_result = knapsack_naive(w, v, n, c)
	naive_end_time = dp_start_time = time.time()
	dp_result = knapsack_dp(w, v, n, c, o)
	dp_end_time = time.time()

	#print the complete message
	print("Completed: n=", n, 
			" c=", c, 
			" Naive Time: ", (naive_end_time - naive_start_time), 
			" DP Time: ", (dp_end_time - dp_start_time), 
			" Naive Result: ", naive_result, 
			" DP Result: ", dp_result, 
			".")

	#append the result lists so they include the times
	dp.append(dp_end_time - dp_start_time)
	naive.append(naive_end_time - naive_start_time)

def printarray (a):
    for e in a:
        print(e, end="\n")
    print()


if __name__ == "__main__":

	lengths = [x for x in range (5, 26)]
	
	
	for r in range (0, 5):
		dp = []
		naive = []
		print("==== RUN ", r, " ====")
		for x in lengths:
			run(x,100, dp, naive)

		#printarray(dp)
		#printarray(naive)	
	
