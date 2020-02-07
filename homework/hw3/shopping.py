#!/usr/bin/python3

# Dynamic Programming Solution to Modified 0-1 Knapsack Problem
# Lyell Read / 2/6/2020


import sys, os, time, random


def knapsack_dp(w, v, n, c, o, t):

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
		return knapsack_dp(w, v, (n - 1), c, o, t)


	#now we are sure we have an item that we *can* take. Do we
	#	take it?
	#what will we get if we leave it?
	leave = knapsack_dp(w, v, (n - 1), c, o, t)

	#what will we get if we take it?
	take = knapsack_dp(w, v, (n - 1), (c - w[n]), o, t) + v[n]

	#the max value will be returned
	o[n][c] = max(leave, take)

	return max(leave, take)


def printarray (a):
    for e in a:
        print(e, end="\n")
    print()


def run (filename):

	# T (1 ≤ T ≤ 100) is given on the first line of the input file.
	#  Each test case begins with a line containing a single integer number N that indicates the number
	# of items (1 ≤ N ≤ 100) in that test case
	#  Followed by N lines, each containing two integers: P and W. The first integer (1 ≤ P ≤ 5000)
	# corresponds to the price of object and the second integer (1 ≤ W ≤ 100) corresponds to the
	# weight of object.
	#  The next line contains one integer (1 ≤ F ≤ 30) which is the number of people in that family.
	#  The next F lines contains the maximum weight (1 ≤ M ≤ 200) that can be carried by the i
	# th person in the family (1 ≤ i ≤ F). 

	#read arguments from file
	with open(filename, "r") as f:
		#parse the arguments 
		args = [x.split(" ") if " " in x else x for x in f.read().splitlines()]
		#printarray(args)
	f.close()

	#convert the argument list to all ints
	for x in range (0, len(args)):
		if type(args[x]) == list:
			for y in range(0, len(args[x])):
				args[x][y] = int(args[x][y])
		else:
			args[x] = int(args[x])

	#for each test case, repeat the following argument checking
	test_cases = args[0]
	idx = 1
	for x in range (0, test_cases):

		#blank out arrays
		v = []
		w = []
		f = []

		#get numnber of items
		items = args[idx]
		idx += 1

		#for each item, copy its values into the respective lists
		for y in range(0, items):

			v.append(args[idx][0])
			w.append(args[idx][1])
			idx += 1

		#get then number of family members
		family_members = args[idx]
		idx += 1

		#for each family member, add their carrying capacity to the f array
		for y in range(0, family_members):

			f.append(args[idx])
			idx += 1

		# print ("\nArgument Parsing Complete: Test Cases:", test_cases,
		# 	" Values:", v,
		# 	" Weights:", w, 
		# 	" Family Member Weights:", f)

		#Make a run with the current data before it is blanked

		#for each family member, get the amount they can carry using 0-1 knapsack
		member_profits = []
		member_items = []
		w.insert(0, None)
		v.insert(0, None)
		
		for m in range(0,family_members):

			t = []

			#Create our optimal nested list, None filled
			o = [[None for x in range(0,f[m]+1)] for y in range(0, items+1)]

			member_profits.append(knapsack_dp(w, v, items, f[m], o, t))

			print("===> T: ", t)

		print("Test Case: " + str(1))
		print("Total Price: " + str(sum(member_profits)))
		print("Member Items")

		for m in range(0,family_members):

			print(str(m+1) + " : " + "<values go here>")






	

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
	
	
