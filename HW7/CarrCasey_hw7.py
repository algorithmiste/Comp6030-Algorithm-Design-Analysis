''' Casey Carr
	04/05/2018
	Assignment 7 '''

''' Question 1: Given a list L consisting of n unordered objects, an item is a majority element if its frequency is greater than n/2. 
				For example, in the list [C, C, T, T, C, T, C, C], C is the majority item, because the frequency of C is 5, which is greater than 4.
				Another example, the list [C, C, T, C, C, S, T, T] has no majority item. These objects are not ordered. 
				You can only compare them using equality as follows: L[i] == L[j].

				Write an iterative program, which counts the frequency of each object, to determine the majority element of a list of objects. 
				Your program should return an object or None, in case there is no majority element. '''

def iterative_majority_finding(L):
	table = {}
	for objects in L:
		if objects in table:
			table[objects] += 1
		else:
			table[objects] = 1

	majority_frequency = len(L)/2
	for key in table:
		if table[key] > majority_frequency:
			return key


# list1 = ["C", "C", "T", "T", "C", "T", "C", "C"]
# list2 = ["C", "C", "T", "C", "C", "S", "T", "T"]
# print(iterative_majority_finding(list1))
# print(iterative_majority_finding(list2))


''' Question 2: Specify the running time function of your program.

	T(n) = 1 + 3n + 1 + 2n = 2 + 5n = a + bn, where a and b are constants

'''


''' Question 3: Write a Python program to find the majority element of a list of unordered objects, based on the following strategy and observations:
				• Divide the list in two halves (say, Left and Right) and find the majority element in each half.
				• If the original list, L, has a majority element, it must be the majority element of either the list Left or the list Right.
				• Take care of the base case. '''

def allObjectsEquivalent(L): # API: input - array of size n, output - True/False
	toReturn = True
	first = L[0]
	for index in range(1,len(L)):
		if first != L[index]:
			toReturn = False
	return toReturn

def frequency(L, x): # API: input - array of size n, output - number of elements equivalent to x
	count = 0
	for i in L:
		if i == x:
			count +=1
	return count

def dc_majority_finding(L): 

	if L == []:
		return None
	if len(L) == 1:
		return L[0]


	left = L[0:len(L)//2]
	right = L[len(L)//2:]


	majority_left = dc_majority_finding(left)
	majority_right = dc_majority_finding(right)
	
	if majority_left == majority_right:
		return majority_left
	elif majority_left != majority_right:
		countL = frequency(L, majority_left)
		countR = frequency(L, majority_right)
		if countL > len(L)//2:
			return majority_left
		elif countR > len(L)//2:
			return majority_right
		else:
			return None
	else:
		return None


	# if majority_left in right:
	# 	return majority_left
	# if majority_right in left:
	# 	return majority_right

	# if majority_left == majority_right:
	# 	return majority_left
	# if majority_left is not None and majority_right is not None:
	# 	if majority_left != majority_right:
	# 		if majority_left in right and majority_right not in left:
	# 			if allObjectsEquivalent(left):
	# 				return majority_left
	# 			else:
	# 				return None
	# 		if majority_right in left and majority_left not in right:
	# 			if allObjectsEquivalent(right):
	# 				return majority_right
	# 			else:
	# 				return None

	# if majority_left is not None and majority_right is None:
	# 	if majority_left in right:
	# 		return majority_left
	# if majority_right is not None and majority_left is None:
	# 	if majority_right in right:
	# 		return majority_right

listA = ["C","T"]
listA = ["C", "C", "T", "T", "C", "T", "C", "C"] 
listB = ["C", "C", "T", "C", "T", "S", "T", "T"] 
listC = ["C", "C", "T", "C", "C", "S", "T", "T"] 
listD = ["C", "C", "C", "C", "C", "T", "T", "T"]

print(dc_majority_finding(listA))
print(dc_majority_finding(listB))
print(dc_majority_finding(listC))
print(dc_majority_finding(listD))



''' Question 4: Specify the running time function of this program in Problem 3 and describe its running time using Theta. 
	T(n) = c + b*n + 2log(n/2) = n + 2log(n/2), therefore T(n) is in Theta(nlog(n))


''' 


''' Question 5: In this “investment” problem, you are given $T, which is the total amount you can invest on n different products. 
				Product x (x is a number between 0 and n-1) has a cost, c[x] and a profit p[x]. The goal is to maximize the profit 
				without spending more than $T.
				
				(See example on handout)
				If T = 24, the best investment is to spend $20 (out of $24) to buy products B and C and make $36 in profit.
				
				The API of your program looks like this:
				
				def invest(T, Costs, Profits):
				# return a number, which is the best profit you can make.

				You will have to do two things:
				• Explain your strategy cleanly and neatly in English.
				• Write a Python program to implement your strategy. '''

''' Strategy: My strategy is to find the maximum profit of all possible combinations (i.e. the power set) that do not exceed T. Along the way, 
			  I match each index to its cost within a list. Then, employ a power set function to find all of the combinations. Then, find the 
			  maximum profit among all combinations.

'''
def powerSet(A):
	if len(A) == 0:
		return [[]]
	return powerSet(A[1:]) + [[A[0]] + x for x in powerSet(A[1:])];

def invest(T, Costs, Profits): 
	if Costs == [] and Profits == []:
		return 0
	L = [] 
	for i in range(0, len(Costs)):
		L.append((Costs[i], i))

	L2 = powerSet(L) 
	L3 = [] 
	for set1 in L2:
		sum_cost = 0
		for tuple1 in set1:
			sum_cost = sum_cost + tuple1[0]
		if sum_cost <= T:
			L3.append(set1)

	max_profit = 0
	L4 = []
	for set2 in L3:
		profits = 0
		for tuple2 in set2:
			profits = profits + Profits[tuple2[1]]

		if profits > max_profit:
			max_profit = profits
			L4.append(set2)

	return max_profit


Costs = [24, 10, 10, 7]
Profits = [24, 18, 18, 10]
T = 24
print("Maximum profit =", invest(T, Costs, Profits))


