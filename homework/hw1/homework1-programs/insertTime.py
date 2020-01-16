#!/usr/bin/python3

# Insertion Sort Program for Time Trials
# Lyell Read / 1/13/2020


import sys, os, random, time


def insertsort(x):
	for i in range(1, len(x)):
		#if i-1 > i, relocate i
		if x[i-1] > x[i]:
			#starting index to find slot
			j = 0
			
			#iterate through until we find slot, stored in j
			while x[i] > x[j]:
				j += 1

			#copy out the element we're moving
			t = x[i]

			#iterate through all elements between j and i
			while i > j:
				#move element at i-1 to i
				x[i] = x[i-1]
				i -= 1

			#set that index to be the element we are moving
			x[j] = t

	return x


def listgen(n):
	#new blank list
	return [random.randint(0, 10000) for x in range (0, n)]


def printarray (a):
	for e in a:
		print(e, end=" ")
	print()

if __name__ == "__main__":

	#define list of lengths
	lengths = [500, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000]
	#lengths = [1000]

	print('\n'.join([str(x) for x in lengths]))

	for n in lengths:
		l = listgen(n)

		#get starting time
		starttime = time.time()

		#perform a mergesort
		x = insertsort(l)

		#get end time
		endtime = time.time()

		#print message to user
		print(endtime - starttime)

	exit()

