# Quiz 3 / CS325 Winter 2020

## Question 1
Every problem in P can be reduced to 3-SAT,
> True

## Question 2
The traveling salesman problem can never be solved exactly.
> False

## Question 3
NP-complete is a subset of NP-Hard.
> True

## Question 4
If you discover a polynomial time algorithm for the SET-PARTITION problem this will imply that P=NP.
> True

## Question 5
If P does not equal NP, there is a polynomial-time algorithm for 3SAT.
> False

## Question 6
Let X be an NP-complete problem and Y and Z be two other problems not known to be in NP. Y is polynomial time reducible to X and X is polynomial-time reducible to Z. Which of the following statements is true?
> [T] Z is in NP-complete
> [F] Z is in NP-Hard
> [F] Y is in NP-complete
> [F] Y is in NP-Hard

## Question 7
Select all of the following statements about the bin packing problem that are true. 
> The bin packing probiem can be solved in polynomial time using dynamic programming.
> The set-partition problem can reduce to the decision version of the bin packing problem.
> There exists a 1-approximation polynomial time algorithm for the bin packing problem,
> The decision version of the bin pecking problem is in P.
> First-Fit is a 2-approximation algorithm for the bin packing problem.

## Question 8
Which of the following algorithms can be used to create a polynomial-time 2-approximation algorithm for the traveling salesman problem?
> [F] Knap-Sack
> [F] Merge Sort
> [F] Shortest Path
> [T] MST
> [F] None of the above

## Question 9
You are using a polynomial time 2-approximation algorithm to find a tour t for the traveling salesman problem. Which of the following statements is true.
> [F] The tour t is never optimal.
> [T] The cost of tour t is at most twice the cost of the optimal tour.
> [F] The cost of tour t is always 2 times the cost of the optimal tour.
> [F] The ratio of the cost of the optimal tour divided by the cost of tour t is 2.
> [F] All of the above

## Question 10
A vertex cover C of a graph G= (V, E) is a subset of vertices such that each edge of the graph is incident to at least one vertex in C. The problem of finding a minimum vertex cover is NP-Hard.
a) Describe an approximation algorithm to find the minimum vertex cover of a graph G=(V,E).
b) What is the running time of the algorithm?
c) What is the approximation ratio for the approximation algorithm?

> Algorithm:
```
1. Generate empty list to store resultant values, R
2. Assume E is the set of all edges in G (provided)
3. While E has items:
	1. Pop e from E
	2. Push e_start_ and e_end_ (edge endpoints) to R
	3. Pop all edges from E that start or end at e_start_or e_end_
4. Return R
```

> Running Time:
> 	O(V+E)
> Approximation Ratio:
> 	<=2-approximation

## Question 11
Consider the following decision problem:
LONG-PATH: Given an undirected graph G = (V, E) , two vertices u and win V and a parameter k, is there a simple path in G from u to w with length at most k?
Prove that LONG-PATH is NP-complete.
Your Answer:

> Disproof by Counterexample:
> LONG PATH as presented is not NP-Complete: Simply applying Djikstra's Algorithm (Polynomial Time, with Worst Case O(|E|+|V|log|V|) can determine the shortest path between u and w, and a simple comparison between the path weight and k will perform the same result as LONG-PATH (if shortest path is longer than k, then the decision is there is no path; if the path length is less than k, there is a path). Therefore, this is not NP-Complete, as it can be completed in polynomial time, while NP-Complete problems cannot.

## Question 12 (Extra Credit)
Use induction to prove the correctness of MERGE-SORT
```
MERGE-SORT(A,p,r)
if p < r
	q = (p + r) / 2
	MERGE-SORT(A,p,q)
	MERGE-SORT(A,q+1,r)
	MERGE(A,p,q,r)
```

Assume that you have a function MERGE that has been proven to correctly merge two sorted subarrays A[p]...A[q] and
A[q+1]...A[r].

> Proof By Induction:
> 1. Base Case: Array of length 1: By default this is sorted. Base Case is true.
> 2. Induction: MERGE-SORT will properly sort an array where len{array) < n, specifically where len(array) == n/2.
> 3. Suppose we choose array s.t. len(array) == n: This call will result in MERGE-SORT calling two instances of itself, each with len(array) == n/2. We have already claimed that this will succeed in sorting those arrays, based on our IH. Based on the assumption that MERGE() will process these arrays properly, MERGESORT on an array where ten(array) == n will be correct.

## Question 13 (Extra Credit)

You just started a consulting business where you collect a fee for completing various types of projects (the fee is
different for each project). You can select in advance the projects you will work on during some finite time period. You
work on only one project at a time and once you start a project it must be completed to receive your fee. There is a set
of n projects p;, p2,.. p, each with a duration dy, do, ..d, (in days) and an associated fee f;, fo, ... f, (in dollars). That is
project pi takes di days and you collect fi dollars after it is completed.

Each of the n projects must be completed in the next D days or you lose its contract. Unfortunately you do not have
enough time to complete ail the projects. Your goal is to select a subset S of the the projects to complete that will
maximize the total fees you earn in D days.

(a) What type of algorithm would you use to solve this problem? Divide and Conquer, Greedy or Dynamic Programming.
Why?

(b) Describe the algorithm verbally and give pseudo-code.

(c} What is the running time of your algorithm?