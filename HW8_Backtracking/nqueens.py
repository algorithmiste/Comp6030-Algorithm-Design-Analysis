
#1. know how to generate all permutations:

# Input: s, a list (representing a permutations of n items), i, a number ("level")
# Output: None
# Precondition: s[0], s[1], ..., s[i] have been "assigned values".
# Postcondition: print out all permutations having items 0, ..., i with the assigned values.
def perm(s, i):
	if i==len(s)-1:
		print(s)
	else:
		# (a) assign all possible values to index/level i+1
		# (b) then "use the same strategy" to generate all perm's ...
		for possibility in range(0, len(s)):
			if possibility not in s[0:i+1]:
				s[i+1] = possibility
				perm(s, i+1)
#----------------------------------------
# Input: s, a list (representing a permutations of n items), i, a number ("level")
# Output: None
# Precondition: s[0], s[1], ..., s[i] have been "assigned values".
# Postcondition: print all n-queen positions having items 0, ..., i with the assigned values.
def queens(s, i):
	if promising(s, i):
		if i==len(s)-1:
			print(s)
		else:
			# (a) assign all possible values to index/level i+1
			# (b) then "use the same strategy" to generate all perm's ...
			for possibility in range(0, len(s)):
				if possibility not in s[0:i+1]:
					s[i+1] = possibility
					queens(s, i+1)
#----------------------------------------
def promising(s,i):
	col_of_queen_i = s[i]
	for j in range(0, i):
		# where's the Q on row j?
		col_of_queen_j = s[j]
		# does it attack the Q on row i (at column s[i])?
		if i-j == abs(col_of_queen_i - col_of_queen_j):
			return False
	return True
#----------------------------------------
queens([None]*3, -1)


