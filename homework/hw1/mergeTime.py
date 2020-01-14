#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020


import sys, os, random, time


def merge(l, r, o):
	while len(l) > 0 or len(r) > 0:

		if len(r) == 0:
			#pop top l
			o.append(l[0])
			l.remove(l[0])

		elif len(l) == 0:
			#pop top r
			o.append(r[0])
			r.remove(r[0])

		else:
			if l[0] >= r[0]:
				#pop top r
				o.append(r[0])
				r.remove(r[0])

			else:
				#pop top l
				o.append(l[0])
				l.remove(l[0])

	return o

def mergesort(x):
	if len(x) > 1:
		#generate midpoint and split list
		m = int(len(x)/2)
		l = x[:m]		
		r = x[m:]

		#recursively mergesort left
		l = mergesort(l)

		#recursively mergesort right
		r = mergesort(r)

		#merge left and right
		o = []
		x = merge(l, r, o)

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
	#lengths = [5000, 6000, 8000, 10000, 20000, 25000, 30000, 40000, 50000, 60000]
	lengths = [250, 500, 1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
	#lengths = [1000]

	print('\n'.join([str(x) for x in lengths]))

	for n in lengths:
		l = listgen(n)

		#get starting time
		starttime = time.time()

		#perform a mergesort
		x = mergesort(l)

		#get end time
		endtime = time.time()

		#print message to user
		print(n, ":", endtime - starttime)

	exit()

