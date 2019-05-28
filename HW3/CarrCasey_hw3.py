''' Casey Carr
	02/20/2018
	Assignment 3 '''

# Question 1: Use the definition of O to prove that 5n3 + 10n2 + 1 is in O(n4)

	# T(n) = 5n^3 + 10n^2 + 1 <= 5n^4 + 10n^4 + 1n^4 = 16n^4
	# Therefore, T(n) <= 16n^4 for all n > 1, with c = 16. So T(n) is in O(n^4)

# Question 2: Use the definition of Ω to prove that 5n3 + 10n2 + 1 is in Ω(n3)
	# T(n) = 5n^3 + 10n^2 + 1 >= 1n^3
	# Therefore, T(n) >= 1n^3 for all n > 1, with c = 1. So T(n) is in Ω(n^3)

# Question 3: Use the geometric sum to find the answer for 1 + 6 + 6^2 + 6^3 + … + 6^31.
	# Geometric sum: [r^(k+1)-1] / r - 1
	# Thus, 1 + 6 + 6^2 + 6^3 + … + 6^31 = [6^(32) - 1] / (6 - 1) = [6^(32) - 1] / 5

# Question 4: Use repeated substitution to find the running time of T(n) = 4n + T(n-1). Assume T(1) = 1.
	# T(n) = 4n + T(n-1)
	#      = 4n + (4n + T(n-2))       					since T(n-1) = 4n + T(n-2)
	#      = 4n + 4n + (4n + T(n-3))  					since T(n-2) = 4n + T(n-3)
	# 	   = 4n + 4n + 4n + (4n + T(n-4))				since T(n-3) = 4n + T(n-4)
	# ...
	# 	   = 4n + 4n + 4n + 4n + ... + 4n + T(1) 	 	since T(2) = 4n + T(1)
	# 	   = 4n + 4n + 4n + 4n + ... + 4n + 1			since T(1) = 1

	# Thus, T(n) = 4n*(n-1) + 1

# Question 5: Use repeated substitution to find the running time of T(n) = 4n + T(n/2). Assume T(1) = 1. 
# 			  If you can do problem 3 and know how to use substitution, you should be able to do this problem.
	# T(n) = 4n + T(n/2)
	#	   = 4n + (4n + T(n/4)) 						since T(n/2) = 4n + T(n/2) 				
	#	   = 4n + 4n + (4n + T(n/8))					since T(n/4) = 4n + T(n/8)
	#	   = 4n + 4n + 4n + (4n + T(n/16))				since T(n/8) = 4n + T(n/16)
	#...
	#	   = 4n + 4n + 4n + 4n + ... + (4n + T(1))		since T(n/(2^n-1)) = 4n + T(1)
	#      = 4n + 4n + 4n + 4n + ... + 4n + 1			since T(1) = 1
	# Thus, T(n) = 4n*log2(n) that is, since we add 4n, k times => k = log2(n)

''' Question 6: Write a recursive Python function that takes as input two sorted lists of numbers and
	returns a sorted union of the two input lists. For example, union([1,5,10,20], [2,4,10]) returns [1,2,4,5,10,10,20].

The function should look like this:
# Input: A and B are both sorted lists
# Output: C is sorted and is a union of A and B.

The following observations can be helpful:
• Problem size is len(A) + len(B)
• Compare the first elements of A and B.
• Suppose A[0] < B[0]. Then, you can remove A[0] and know that it is the first element of the union.
• How do you the same problem with problem size len(A) + len(B) - 1? Answer: use the same strategy.
• Do not trace function calls. Instead abstract the same strategy as a recursive call.
• Of course, you will need to take care of “smallest” cases, where you can’t remove the first element of A or B.

'''
def union(A, B):

	C = []

	if (A is None) ^ (B is None):
		if A is not None:
			return A
		return B

	if ((A is None and B is None) or (len(A) == 0 and len(B) == 0)): 
		return C

	if (len(A) == 0 and len(B) != 0):
		elementToAppend = B.pop(0)
		C = [elementToAppend] + union(A,B)

	elif (len(B) == 0 and len(A) != 0):
		elementToAppend = A.pop(0)
		C = [elementToAppend] + union(A,B) 

	elif (A[0] < B[0]):
		elementToAppend = A.pop(0)
		C = [elementToAppend] + union(A,B) 

	elif (B[0] < A[0]):
		elementToAppend = B.pop(0)
		C = [elementToAppend] + union(A,B) 

	else: 										#if (A[0] == B[0]):
		elementToAppend = A.pop(0); B.pop(0)
		C = [elementToAppend] + union(A,B)  

	return C

A = [1]; B = [2]

print(union([1,5,10,20], [2,4,10]))
print(union([2,4,10],[1,5,10,20]))

print(union(A,None))
print(union(None,B))
print(union(None, None))
