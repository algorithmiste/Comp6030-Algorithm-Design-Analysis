'''Casey Carr
   03/29/18
   Assignment 6'''

'''Question 1: Use the Master’s theorem to find the complexity (in terms of Theta) of this function T(n) = n^2 + 4T(n/2)
			   2 = log2(4), therefore T(n) is in Theta(n^2log(n))

'''

'''Question 2: Use the Master’s theorem to find the complexity (in terms of Theta) of this function T(n) = n^2 + 6T(n/2)
			   2 < log2(6), therefore T(n) is in Theta(n^log2(6))

'''

'''Question 3: Use the Master’s theorem to find the complexity (in terms of Theta) of this function T(n) = n^2 + 3T(n/2)
			   2 > log2(3), therefore T(n) is in Theta(n^2)

'''

'''Question 4: Find the running time equation of this Python function
			   def foo(L): # L is a list with n numbers
					if L==[]:
						return 5
					s = 0
					for x in L:
						s = s + x
					A = L[0: len(L)//2] # in general, slicing takes n steps (since copying the slice to new array), in this case n/2 steps 
					return foo(A) + s

				T(n) = 3 + n + n/2 + 1 + T(n/2) = c + n + n/2 + T(n/2) = c + (3/2)n + T(n/2)

'''

'''Question 5: Use the Master’s theorem to find the complexity in terms of Theta of the running time equation in problem 4
			   1 > log2(1) = 0, therefore T(n) is in Theta(n)

'''

'''Question 6: Find the running time equation of this Python function
			   def foo(L): # L is a list with n numbers
					if L==[]:
						return 5
					s = 0
					for x in L:
						s = s + x
					A = L[0: len(L)//4]
					B = L[len(L)//4 : len(L)//2]
					C = L[len(L)//2 : 3*len(L)//4]
					return foo(A) + foo(B) + foo(C) + s

				T(n) = 3 + n + n/4 + n/4 + n/4 + 3*T(n/4) = c + (7/4)n + 3*T(n/4) 

'''

'''Question 7: Use the Master’s theorem to find the complexity in terms of Theta of the running time equation in problem 6
			   1 > log4(3), therefore T(n) is in Theta(n)

'''

'''Question 8: Use a global table (dictionary) to cache the following function '''
Table = {}
def foo(n):
	global Table
	if n in Table:
		return Table[n]

	if n==0:
		Table[n] = 0
		# return 0
		return Table[n]
	if n==1:
		Table[n] = 1
		# return 1
		return Table[n]
	if n==2:
		Table[n] = 2
		# return 2
		return Table[n]
	if n%3 == 0:
		Table[n] = foo(n-1) + foo(n-2) + foo(n-3)
		# return foo(n-1) + foo(n-2) + foo(n-3)
		return Table[n]
	if n%3 == 1:
		Table[n] = foo(n-1)
		# return foo(n-1)
		return Table[n]
	Table[n] = foo(n-1) + foo(n-3)
	# return foo(n-1) + foo(n-3)
	return Table[n]				

