#!/usr/bin/python3

# Merge Sort 3 Program
# Lyell Read / 1/23/2020


import sys, os, random, time


def merge3(a, b, c, o):
	#iterate until we have all empty lists
	while len(a) > 0 or len(b) > 0 or len(c) > 0:
		#if any two lists are empty, pop from the one non empty
		if len(a) == 0 and len(b) == 0:
			#only c remains, pop to o
			o.append(c[0])
			c.remove(c[0])

		#if any two lists are empty, pop from the one non empty
		elif len(a) == 0 and len(c) == 0:
			#only b remains, pop to o
			o.append(b[0])
			b.remove(b[0])

		#if any two lists are empty, pop from the one non empty
		elif len(b) == 0 and len(c) == 0:
			#only a remains, pop to o
			o.append(a[0])
			a.remove(a[0])

		else:
			#at least two lists are full:
			#if empty list is a, then compare c and b and pop the lower of the two
			if len(a) == 0:
				if b[0] > c[0]:
					o.append(c[0])
					c.remove(c[0])
				else:
					o.append(b[0])
					b.remove(b[0])

			#if emoty list is b, compare a and c and pop lower
			elif len(b) == 0:
				if c[0] > a[0]:
					o.append(a[0])
					a.remove(a[0])
				else:
					o.append(c[0])
					c.remove(c[0])

			#if empty list is c, pop from min of a, b
			elif len(c) == 0:
				if a[0] > b[0]:
					o.append(b[0])
					b.remove(b[0])
				else:
					o.append(a[0])
					a.remove(a[0])

			else:
				#now we have all three lists full by PoE
				#assemble the first elements into an array
				t = [a[0], b[0], c[0]]

				#find the min of that array
				p = min(t)

				#if the min is the first element of a, choose to pop from a
				if p == a[0]:
					o.append(a[0])
					a.remove(a[0])

				#elif its the first element of b, pop from b
				elif p == b[0]:
					o.append(b[0])
					b.remove(b[0])

				#now we know it must be from c, so pop from c
				else:
					o.append(c[0])
					c.remove(c[0])
	
	#return our completed list
	return o

def mergesort3(x):
	if len(x) > 1:
		#generate midpoints of the initial list
		#left one will be first third
		ls = len(x)//3
		#right one will be second third (or half of what
		# is left after third is removed)
		rs = ls + (len(x)-ls)//2

		#split the list up into a(1), b(2) and c(3) thirds
		a = x[:ls]
		b = x[ls:rs]
		c = x[rs:]

		#recursively call mergesort on those three
		a = mergesort3(a)
		b = mergesort3(b)
		c = mergesort3(c)

		#merge a b and c to form x.
		o = []
		x = merge3(a, b, c, o)

	return x


def listgen(n):
	#new blank list
	return [random.randint(0, 10000) for x in range (0, n)]


if __name__ == "__main__":

	#define list of lengths
	#lengths = [500, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000]
	lengths = [100000]
	print('\n'.join([str(x) for x in lengths]))

	for n in lengths:
		l = listgen(n)

		#get starting time
		starttime = time.time()

		#perform a mergesort
		x = mergesort3(l)

		#get end time
		endtime = time.time()

		#print message to user
		print(endtime - starttime)

	exit()

