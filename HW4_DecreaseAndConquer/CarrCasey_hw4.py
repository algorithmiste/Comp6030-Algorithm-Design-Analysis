''' Casey Carr
	03/01/2018
	Assignment 4 '''

# Question 1: Use the geometric sum to find the answer for 1 + 6 + 6^2 + 6^3 + … + 6^31.
	# Geometric sum: [r^(k+1)-1] / r - 1
	# Thus, 1 + 6 + 6^2 + 6^3 + … + 6^31 = [6^(32) - 1] / (6 - 1) = [6^(32) - 1] / 5

# Question 2: Use repeated substitution to find the running time of T(n) = 4n + T(n-1). Assume T(1) = 1.
	# T(n) = 4n + T(n-1)
	#      = 4n + (4n + T(n-2))       					since T(n-1) = 4n + T(n-2)
	#      = 4n + 4n + (4n + T(n-3))  					since T(n-2) = 4n + T(n-3)
	# 	   = 4n + 4n + 4n + (4n + T(n-4))				since T(n-3) = 4n + T(n-4)
	# ...
	# 	   = 4n + 4n + 4n + 4n + ... + 4n + T(1) 	 	since T(2) = 4n + T(1)
	# 	   = 4n + 4n + 4n + 4n + ... + 4n + 1			since T(1) = 1

	# Thus, T(n) = 4n*(n-1) + 1

# Question 3: Use repeated substitution to find the running time of T(n) = 4n + T(n/2). Assume T(1) = 1. 
# 			  If you can do problem 3 and know how to use substitution, you should be able to do this problem.
	# T(n) = 4n + T(n/2)
	#	   = 4n + (4n + T(n/4)) 						since T(n/2) = 4n + T(n/2) 				
	#	   = 4n + 4n + (4n + T(n/8))					since T(n/4) = 4n + T(n/8)
	#	   = 4n + 4n + 4n + (4n + T(n/16))				since T(n/8) = 4n + T(n/16)
	#...
	#	   = 4n + 4n + 4n + 4n + ... + (4n + T(1))		since T(n/(2^n-1)) = 4n + T(1)
	#      = 4n + 4n + 4n + 4n + ... + 4n + 1			since T(1) = 1
	# Thus, T(n) = 4n*log2(n) that is, since we add 4n, k times => k = log2(n)

''' Question 4: Given a random pairing of boys and girls, we know that it can have many unstable pairs. In this problem, you will design an algorithm
				that improves upon a random pairing by removing unstable pairs, one by one. There is no warranty that you can actually decrease the
				number of unstable pairs, because when you “stabilize” an unstable pair, you might introduce another unstable pair. However, 
				intuitively, removing unstable pairs, one at a time, should improve upon a random pairing of boys and girls.'''

''' We discussed and implemented in class a function that detects unstable pairs. You can modify this function to return None if 
	the pair is stable or in case it is unstable a pair that makes it unstable. For example, if (‘John’, ‘Rose’) is stable, then 
	your function, find_unstable_pair((‘John’, ‘Rose’)) returns None. If, however, (‘John’, ‘Rose’) is unstable, 
	then find_unstable_pair((‘John’,‘Rose’)) returns the pair, say (‘Joe’, ‘Mary’), that makes it unstable. A minor
	modification of is_stable (which we implemented in class) should work. 

	This is a decrease-and-conquer strategy at work. We attempt to remove unstable pairs one by one.
	In this algorithm, you go through the list of pairs only once, trying to fix unstable pairs. 
	It is possible that after you finish going through the list, there are still unstable pairs. For now, this is expected.'''
import relationship
import relationship_test

def improve_stability( pairs ):
# Strategy: iterate through each pair and “fix” it if it is unstable.
# This function should call another function, find_unstable_pair, see below.
# If the current pair is unstable, you fix it by swapping boys and girls in the
# two pairs. You should remove these two pairs from the list and add two
# new pairs to the list.
# Python lists have methods append (for adding) and remove (for deletion).
		
	for (pair) in pairs:
		
		unstablePair = relationship_test.find_unstable_pair(pair, pairs)
		if unstablePair is not None:
			newPair = pair
			pairs.remove(pair)
			newUnstablePair = unstablePair
			pairs.remove(unstablePair)
			
			newPair[0].mate = unstablePair[1]
			unstablePair[1].mate = newPair[0]
			newPair[1].mate = unstablePair[0]
			unstablePair[0].mate = newPair[1]
			
			pairs.append((newPair[0], unstablePair[1]))
			pairs.append((unstablePair[0], newPair[1]))	
	return pairs

''' Question 5: Compare your algorithm to the random arrangement. The relationship module, as you should know, has a random_arrangement
				function that returns a list of random pairs. You can count the number of unstable pairs in the random pairing, to the number 
				of unstable pairs returned from your algorithm.

				Write a function called compare_to_random that iterates 100 times, and prints out the average number of unstable pairs of the 
				random pairing and of your improved pairing. '''
def compare_to_random():
	names1 = ['John', 'Steve', 'Jason', 'Jose', 'Tommy']
	names2 = ['Mary', 'Stacey', 'Alexis', 'Kim', 'Rose']

	totalUnstableRandom = 0
	totalUnstableImproved = 0
	N = 100
	for i in range(0,N):
		totalUnstableRandom += relationship_test.instability(relationship.random_arrangement(names1, names2)[2])
		totalUnstableImproved += relationship_test.instability(improve_stability(relationship.random_arrangement(names1, names2)[2]))

	averageUnstableRandom = totalUnstableRandom / N
	averageUnstableImproved = totalUnstableImproved / N 
	return averageUnstableRandom, averageUnstableImproved
 
averages = compare_to_random()
names1 = ['John', 'Steve', 'Jason', 'Jose', 'Tommy']
names2 = ['Mary', 'Stacey', 'Alexis', 'Kim', 'Rose']
boys, girls, pairs = relationship.random_arrangement(names1, names2)

print()
print('Average number of unstable pairs of the RANDOM pairing: {}'.format(round(averages[0],1)))
print('Average number of unstable pairs of the IMPROVED pairing: {}'.format(round(averages[1],1)))