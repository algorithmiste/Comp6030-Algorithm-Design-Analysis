import relationship
'''
The pair (b1, g1) is not stable if there's (b2, g2) such that
b1 likes g2 more than g1, and g2 likes b1 more than b2.

(Steve, Rose) is unstable because we have another pair (Jose,Alexis)
and Steve likes Alexis more than Rose and Alexis likes Steve more
than Jose.

'''

# output: True or False.  False if there's an unstable pair.
def is_stable(pair, pairs):
	# for (b,g) in pairs:
	for (b2, g2) in pairs:
		if pair[0].prefers(g2,pair[1]) and g2.prefers(pair[0],b2):
			#print('{} likes {} more than {} and {} likes {} more than {}'.format(b.name,g2.name,g.name,g2.name,b.name,b2.name))
			return False
	return True

def find_unstable_pair(pair, pairs): 
	for (b2,g2) in pairs:
		if pair[0].prefers(g2,pair[1]) and g2.prefers(pair[0],b2):
			return (b2, g2)   
	return None

# return the number of unstable pairs
def instability(pairs):
	count = 0
	for (b,g) in pairs:
		for (b2, g2) in pairs:
			if b.prefers(g2,g) and g2.prefers(b,b2):
				print('{} likes {} more than {}; {} likes {} more than {}'.format(b.name,g2.name,g.name,g2.name,b.name,b2.name))
				count += 1
	return count


# names1 = ['John', 'Steve', 'Jason', 'Jose', 'Tommy']
# names2 = ['Mary', 'Stacey', 'Alexis', 'Kim', 'Rose']

# boys, girls, pairs = relationship.random_arrangement(names1, names2)

# relationship.print_arrangement(pairs)
# # print(instability(pairs))



