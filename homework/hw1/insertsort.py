#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020


import sys, os


def insertsort(x):
	for i in range(1, len(x)):

		#if i-1 <= i; do nothing
		#if x[i-1] <= x[i]:
		#	pass

		#if i-1 > i, relocate i
		if x[i-1] > x[i]:
			#starting index to find slot
			j = 0
			
			#iterate through until we find slot, stored in j
			while x[i] > x[j]:
				j += 1

			#copy out the element we're moving
			t = x[i]

			#make k be a copy of j
			#k = j

			#iterate through all elements between j and i
			while i > j:
				#move element at i-1 to i
				x[i] = x[i-1]
				i -= 1

			x[j] = t

	return x

def printarray (a):
	for e in a:
		print(e, end=" ")
	print()

if __name__ == "__main__":

	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	with open(sys.argv[1], "r") as f:
		lines = [ [int(y) for y in x.replace('\n', '').split(" ")] for x in f.readlines()]
		f.close()


	result = [insertsort(x) for x in lines]

	#print result
	for x in result:
		printarray(x)

	exit()

