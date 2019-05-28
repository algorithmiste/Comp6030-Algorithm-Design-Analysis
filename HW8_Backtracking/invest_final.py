

def greedy_invest(T, costs, profits):
	pc_ratio = []
	for i in range(len(costs)):
		pc_ratio.append((profits[i] / costs[i], profits[i], costs[i]))
	pc_ratio.sort(reverse=True)
	print(pc_ratio)
	best_profit = 0
	current_budget = T
	for i in range(len(pc_ratio)):
		if current_budget <= 0:
			break
		# have enough money to invest in this item
		if current_budget >= pc_ratio[i][2]:
			current_budget -= pc_ratio[i][2]   	# take this item
			best_profit += pc_ratio[i][1]		# record the profit
			print('Take item with cost {} and profit {}.  Current budget: {}'.format(pc_ratio[i][2], pc_ratio[i][1], current_budget))
	return best_profit


#-------------------------------------------------------------------
# output: max investment given items 0, 1, ..., i
#-------------------------------------------------------------------
def dp_invest(T, costs, profits, i):
	if i<0:
		return 0

	# analyzing possibilities:
	# there're only two possibilities about item i
	# 1. invest in item i
	invest = 0
	if T >= costs[i]:
		invest = dp_invest(T-costs[i], costs, profits, i-1) + profits[i]

	# 2. do not invest in item i.
	not_invest = dp_invest(T, costs, profits, i-1)

	return max(invest, not_invest)

#-------------------------------------------------------------------
Costs =   	[24, 10, 10, 	7]
Profits = 	[24, 15, 15, 	11]
Budget = 24
#-------------------------------------------------------------------
# print(greedy_invest(Budget, Costs, Profits))
# print(dp_invest(Budget, Costs, Profits, len(Costs)-1))

'''
dp_invest(24, [24, 10, 10, 7], [24, 15, 15, 11], 3)

1. Invest invest in the 4th item, the max profit will be:
dp_invest(24-7, [24, 10, 10, 7], [24, 15, 15, 11], 2) + 11

2. If we do not invest in the 4th item, the max profit will be:
dp_invest(24, [24, 10, 10, 7], [24, 15, 15, 11], 2)


Sets and permutations.
Say we have 3 items: 0, 1, 2
How many sets: {}, {0}, {1}, {2}, {0,1}, {0,2}, {1,2}, {0,1,2}
How many permutations: [0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]

For n items, there are 2^n sets and n! permutations.

Investment is a "set" problem.  Why? Optimal profit comes from a set of items.
In the example above, optimal solution is {1,2}, which gives the optimal profit
of 30.

Find a group of 10 FaceBook users that mutually know each other.  This is a set problem.

Given an interconnected network of roads, find a minimum number of intersections to place cameras to watch all roads.  This is a set problem.

Given 50 COMP courses, find a sequence of these courses that satisfy their prerequisites.  This is a permutation problem.

TSP is permutation problem.

N-queen.  Best to formulate this as a permutation problem.

'''

# Problem: generating all sets of n items.
#1. Representation: represent a set as a list of n boolean values.
N = 4
# Presume that s[0], s[1], s[2], ..., s[i] have been "configured" or "assigned" values to.


# Input: s, a list (representing a set of n items), i, a number ("level")
# Output: None
# Precondition: s[0], s[1], ..., s[i] have been "set" or "assigned values".
#				This means items 0, 1, .., i have been either selected or not selected
# Postcondition: print out all sets having items 0, ..., i with the assigned values.
def sets(s, i):
	if i==len(s)-1:
		if valid(s):		# check for validity
			print(s)
	else:
		# we generate all possibilities for the next level
		s[i+1] = True
		sets(s, i+1)   # use same strategy

		# now, go back and reset the choice
		s[i+1] = False
		sets(s, i+1)   # use same strategy


def valid(s):
	return True

#-------------------------------------------------------------------
# sets([True, False, True, None, None], 2)

#-------------------------------------------------------------------
Costs =   	[24, 10, 10, 	7]
Profits = 	[24, 15, 15, 	11]
Budget = 24
# This is a set problem.

#---------------------------------------------------------
# Postcondition: print out all investable portfolios
def invest_bt(portfolio, i, costs, profits, budget):
	if i==len(portfolio)-1:
		if investable(portfolio, costs, profits, budget):
			print(portfolio, show_portfolio(portfolio, costs, profits))
	else:
		portfolio[i+1] = True
		invest_bt(portfolio, i+1, costs, profits, budget)
		portfolio[i+1] = False
		invest_bt(portfolio, i+1, costs, profits, budget)

#---------------------------------------------------------
# Postcondition: find a most profitable portfolio
best_profit, best_porfolio = 0, None
def most_profitable(portfolio, i, costs, profits, budget):
	global best_profit, best_porfolio
	if promising(portfolio, i, costs, profits, budget):
		if i==len(portfolio)-1:
			c ,p = show_portfolio(portfolio, costs, profits)
			if p > best_profit:
				best_profit, best_porfolio = p, portfolio.copy()
				print(portfolio, c, p)
		else:
			portfolio[i+1] = True
			most_profitable(portfolio, i+1, costs, profits, budget)
			portfolio[i+1] = False
			most_profitable(portfolio, i+1, costs, profits, budget)
#---------------------------------------------------------
def promising(portfolio, i, costs, profits, budget):
	c, p = show_portfolio(portfolio[0:i+1],costs, profits)
	return c <= budget
#---------------------------------------------------------
def show_portfolio(p, costs, profits):
	cost_p = sum([costs[i] for i in range(len(p)) if p[i]==True])
	profit_p = sum([profits[i] for i in range(len(p)) if p[i]==True])
	return cost_p, profit_p
#---------------------------------------------------------
def investable(portfolio, costs, profits, budget):
	c, p = show_portfolio(portfolio, costs, profits)
	return c <= budget
#---------------------------------------------------------
most_profitable([None]*len(Costs), -1, Costs, Profits, Budget)
print(Costs)
print(Profits)
print(show_portfolio(best_porfolio, Costs, Profits))



