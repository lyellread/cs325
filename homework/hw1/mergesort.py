#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020
# Citations: 
# - 

import os, sys


def merge(l, r, o):

	if len(l) == 0 and len(r) == 0:
		return o

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

	#recurse
	return merge(l, r, o)





def mergesort(x):

	if not len(x) == 1:
		#run on the left side
		mergesort()
		





if __name__ == "__main__":

	if len(sys.argv) < 2:
		print ("Insufficient Arguments Provided. Quitting.")
		exit()

	if not os.path.exists(sys.argv[1]):
		print ("File Provided Does Not Exist. Quitting.")
		exit()

	with open(sys.argv[1], "r") as f:
		lines = [x.split(" ") for x in f.readlines()]
		f.close()

	result = [mergesort(x) for x in lines]

	#print result
	exit()

