
import tree


''' Question 1: We discussed in class a decrease and conquer strategy to find the minimum number in a list. 
	The Python function was like this:
	def my_min(L):
	if L==[]:
		print("undefined behavior.")
		return
	if len(L) == 1:
		return L[0]

	first = L.pop(0)
	smallest_of_the_tail = my_min(L)
	if first < smallest_of_the_tail:
		return first
	else:
		return smallest_of_the_tail
	
Trace by listing in order all recursive function calls resulted from the following function call my_min([10,5,20,7,10]). 

So, trace my_min([10,5,20,7,10]):

my_min([10,5,20,7,10]) sets first = 10 and smallest_of_the_tail = my_min([5,20,7,10])

my_min([5,20,7,10]) sets first = 5 and smallest_of_the_tail = my_min([20,7,10])

my_min([20,7,10]) sets first = 20 and smallest_of_the_tail = my_min([7,10])

my_min([7,10]) sets first = 7 and smallest_of_the_tail = my_min([10])

my_min([10]) returns 10

Now, smallest_of_the_tail = 10 and first = 7 returns 7

Now, smallest_of_the_tail = 7 and first = 20 returns 7

Now, smallest_of_the_tail = 7 and first = 5 returns 5

Now, smallest_of_the_tail = 5  and first = 10 returns 5

Thus, final return value = 5
'''

'''Question 2: Employ the decrease and conquer strategy to write a recursive Python function to compute the sum of a list.  
   Here’s the API:

   # Input: a list of numbers
   # Output: a number, which is the sum of all numbers in the list '''

def my_sum( a_list ):
	if a_list == []:
		return 0
	else:
		first = a_list.pop(0)
		return my_sum(a_list) + first

print(my_sum([1,2,3,4,5,6,7,9,8,10])) 
print("\n")

''' Question 3: Employ the decrease and conquer strategy to write a recursive Python function to reverse a list. 
	Here’s the API:
	# Input: a list of things
	# Output: another list, which is the reverse of the input list [1,2,3,4,5] '''

def my_reverse( a_list ):
	if a_list == []:
		return "Can't reverse an empty list!"
	elif len(a_list) == 1:
		return a_list
	else:
		currentElement = a_list.pop(0)
		return my_reverse(a_list) + [currentElement] 

print(my_reverse([1,2, 3, 5, 25, 197])) 

'''Question 4: Employ the decrease and conquer strategy to write a recursive Python function to compute the depth of a binary tree.  
   The depth of a binary tree is the longest distance from the root to any leaf.  Here’s the API:

	# Input: root node of a binary tree
	# Output: a number, which is the depth of the tree rooted by the input node

	number of levels in a tree B is equal to
	(a) the greater of the number of levels in the left subtree of B and the number of levels in the right subtree of B, plus
	(b) the presence of the root B = 1 '''


def my_depth( a_root_node ):
	root, left, right = 0, 0, 0

	if a_root_node is not None:
		root = 1
	else:
		return 0

	if a_root_node.left is not None:
		left = my_depth(a_root_node.left) + root

	if a_root_node.right is not None:
		right = my_depth(a_root_node.right) + root

	if left > right:
		return left
	else:
		return right 


B = tree.random_tree(1, colors=['r', 'g', 'b'], seed = 1)
print("\n")
print(B.node_ids())

# tree.draw(B)
print(my_depth(B))
print("\n")
