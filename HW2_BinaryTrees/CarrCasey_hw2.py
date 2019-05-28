# HW2 Assignment:

''' Question 1: Every node in a binary tree can have 0, 1 or 2 children.  A leaf node has no children. 
	Write a Python function to decide whether all nodes, except leaves, in a tree have exactly two children.

# Input:  a node which is the root of the tree
# Output: True if all nodes in the tree have either 0 or 2 children.
#		False if some node has only one child.
# (leaves) or exactly two children (internal nodes).
def  is_full_house( root_node ):
	# your code…
'''
import tree

def addBoolean(b1,b2):
	if (b1 == True and b2 == True):
		return True
	else:
		return False

# def is_full_house2(root_node):
# 	if root_node is None:
# 		return False

# 	if ((root_node.left is None) ^ (root_node.right is None)):
# 		return False

# 	elif (root_node.left is None and root_node.right is None):
# 		return True

# 	else:
# 		left = addBoolean(is_full_house2(root_node.left), True)
# 		right = addBoolean(is_full_house2(root_node.right), True)
# 		return (left and right)

# QUESTION: Could you tell me as part of the feedback, in your opinion, which algorithm looks more technically correct and understandable??
#			is_full_house or is_full_house2  ???
# 			They both always return the same result, but I wrote them slightly differently. Thanks!
def is_full_house(root_node):
	if root_node is None:
		return False

	result = True  # must initialize result
	if ((root_node.left is None) ^ (root_node.right is None)):
		result = False
		return result

	elif (root_node.left is None and root_node.right is None):
		return result

	else:
		left = is_full_house(root_node.left) and result
		right = is_full_house(root_node.right) and result
		return (left and right)
	
T = tree.random_tree(3)
# tree.draw(T)
print(is_full_house(T))
# print(is_full_house2(T))

''' Question 2: Given the following function

# Input: a list of numbers, L.
# Output: a number
def do_something( L ):			# iterations
	s = 0							1	
	for x in L:						n
		s = s + x					1   n(2+n(2+n)) + 3
		print(s)					1
		for y in L:					n
			s = s + y 				1
			print(s, x, y)			1
			for z in L:				n
				s = s + z			1
	s = s*5							1
	return s 						1

Let T(n) be the running time function of do_something.  What is n? 

	n is the input size of the function, which depends on the length of the list of numbers i.e. len(L)
'''

''' Question 3: Continuing with problem 2.  Write down T(n) as accurately as you can, with specific numbers.

	T(n) ≈ n(2+n(2+n)) + 3 = 2n + 2n2 + n3 + 3 
'''

''' Question 4: Continuing with problem 3.  Describe T(n) using big-O notation.
	T(n) ≈ n(2+n(2+n)) + 3 = 2n + 2n2 + n3 + 3  <= c*g(n) = n^3 + 2n^3 + 2n3 + 3n3 = 8*n^3, with c = 8, for all n > 1
	Thus, f(n) is in O(n^3)
'''

''' Question 5: Given the following function

# Input: a list of numbers L
# Output: a number
def foo(L):
	s = 0
	for x in L:   		n(1+4log2(n)) + 2
		j = len(L)
		while j > 1:
			j = j / 2
			s = s + x
			print(s)
	return s

Let T(n) be the running time function of foo.  Write down T(n) as accurately as you can, with specific numbers.
	T(n) ≈ n(1+4log2(n)) + 2 
'''

''' Question 6: Describe T(n) using big-O notation.
	T(n) ≈ n(1+4log2(n)) + 2 = n + 4nlog2(n) + 2 <= c*g(n) = nlog(n) + 4nlog(n) + 2nlog(n) = 7*n*log(n), with c = 6, for all n large enough (> 1)
	Thus, f(n) is in O(n*log(n))
'''

''' Question 7: Describe 20n + 5n^2 using big-O notation.
	f(n) is in O(n^2)
'''

''' Question 8: Describe 10n^3 + 20n^2 using big-O notation.
	f(n) is in O(n^3)

'''