#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020


import sys, os


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


def printarray (a):
	for e in a:
		print(e, end=" ")
	print()

if __name__ == "__main__":

	#arg len
	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	#file exists check
	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	#open, read, close file
	with open(sys.argv[1], "r") as f:
		lines = [ [int(y) for y in x.replace('\n', '').split(" ")][1:] for x in f.readlines()]
		f.close()

	#generate results list
	result = [mergesort(x) for x in lines]

	#print result
	# for x in result:
	# 	printarray(x)

	#save results
	with open("merge.txt", "w") as f:
		for x in result:
			f.write(' '.join([str(z) for z in x]) + "\n")

	exit()

