#!/usr/bin/python3

# Insertion Sort Program
# Lyell Read / 1/13/2020


import sys, os


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


def printarray (a):
	for e in a:
		print(e, end=" ")
	print()

if __name__ == "__main__":

	#check arg len
	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	#check file existance
	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	#open file, read and close
	with open(sys.argv[1], "r") as f:
		lines = [ [int(y) for y in x.replace('\n', '').split(" ")][1:] for x in f.readlines()]
		f.close()

	#run insertsort and generate a set of results
	result = [insertsort(x) for x in lines]

	#print result
	# for x in result:
	# 	printarray(x)

	#save results
	with open("insert.txt", "w") as f:
		for x in result:
			f.write(' '.join([str(z) for z in x]) + "\n")

	exit()

