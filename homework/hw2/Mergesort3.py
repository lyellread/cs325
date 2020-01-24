#!/usr/bin/python3

# Merge Sort Program
# Lyell Read / 1/13/2020


import sys, os


def merge(a, b, c, o):
	while len(a) > 0 or len(b) > 0 or len(c) > 0:
		if len(a) == 0 and len(b) == 0:
			#only c remains, pop to o
			o.append(c[0])
			c.remove(c[0])

		elif len(a) == 0 and len(c) == 0:
			#only b remains, pop to o
			o.append(b[0])
			b.remove(b[0])

		elif len(b) == 0 and len(c) == 0:
			#only a remains, pop to o
			o.append(a[0])
			a.remove(a[0])

		else:
			#at least two lists are full:

			if len(a) == 0:
				if b[0] > c[0]:
					o.append(c[0])
					c.remove(c[0])
				else:
					o.append(b[0])
					b.remove(b[0])

			elif len(b) == 0:
				if c[0] > a[0]:
					o.append(a[0])
					a.remove(a[0])
				else:
					o.append(c[0])
					c.remove(c[0])

			elif len(c) == 0:
				if a[0] > b[0]:
					o.append(b[0])
					b.remove(b[0])
				else:
					o.append(a[0])
					a.remove(a[0])

			else:

				t = [a[0], b[0], c[0]]
				p = min(t)

				if p == a[0]:
					o.append(a[0])
					a.remove(a[0])

				elif p == b[0]:
					o.append(b[0])
					b.remove(b[0])

				else:
					o.append(c[0])
					c.remove(c[0])
	return o

def mergesort(x):
	if len(x) > 1:
		#generate midpoints
		ls = len(x)//3
		rs = ls + (len(x)-ls)//2

		a = x[:ls]
		b = x[ls:rs]
		c = x[rs:]

		a = mergesort(a)
		b = mergesort(b)
		c = mergesort(c)

		#merge left and right
		o = []
		x = merge(a, b, c, o)

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

