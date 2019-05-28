''' Casey Carr
	03/22/2018
	Assignment 5 '''

''' Question 1: Use the arithmetic sum to find the answer for 2 + 3 + 4 + … + 2018 
				Lemma: 1 + 2 + 3 + 4 + … + 2018 = (2018)(2018 + 1) / 2 = 2037171
				Since 2 + 3 + 4 + … + 2018 = 1 + 2 + 3 + 4 + … + 2018 - 1, using the Lemma:
				2 + 3 + 4 + … + 2018 = 2037171 - 1 = 2037170

'''

''' Question 2: Use the geometric sum to find the answer for 1 + 6 + 6^2 + 6^3 + … + 6^31
				Thus, 1 + 6 + 6^2 + 6^3 + … + 6^31 = [6^(31+1) - 1] / (6 - 1) = (6^32 - 1) / 5

'''

''' Question 3: Use the geometric sum to find the answer for 1/3 + (1/3)^2 + (1/3)^3 + … + (1/3)^20
				Lemma: 1 + 1/3 + (1/3)^2 + (1/3)^3 + … + (1/3)^20 = [(1/3)^21 - 1] / [(1/3) - 1] = [(1/3)^21 - 1] / [-2/3] = (-3/2) * [(1/3)^21 - 1]
					   Hence, 1 + 1/3 + (1/3)^2 + (1/3)^3 + … + (1/3)^20 = 1.5
				So, using the Lemma, 1/3 + (1/3)^2 + (1/3)^3 + … + (1/3)^20 = 1.5 - 1 = 0.5
'''

''' Question 4: Find the running time equation, T(n), of this python function. You don’t have to solve the equation.
				def foo(L): 			# L is a list
					if L == []:
						return 1
					s = 0
					for x in L:
						for y in L:
							s = s + x*y
					A = L[0, len(L)//2]
					B = L[len(L)//2, len(L)]
					return foo(A) + s + foo(B)
				
				T(n) = 2 + 1 + n*(1*n) + (n/2) + (n/2) + 1 + T(n/2) + T(n/2) = 4 + n^2 + n + 2*T(n/2)
				And, in general terms, T(n) = c + n^2 + n + d*T(n/2), where c,d are constants

'''

''' Question 5: Use repeated substitution to find the running time of T(n) = 4n + T(n-1). Assume T(1) = 1.
				T(n) = 4n + T(n-1)
					 = 4n + 4(n-1) + T(n-2), since T(n-1) = 4(n-1) + T(n-2)
					 = 4n + 4(n-1) + 4(n-2) + T(n-3), since T(n-2) = 4(n-2) + T(n-3)
					 = 4n + 4(n-1) + 4(n-2) + 4(n-3) + T(n-4), since T(n-3) = 4(n-3) + T(n-4)
					 ... <after many steps>

					 = 4n + 4(n-1) + 4(n-2) + 4(n-3) + 4(n-4) + ... + 4
					 = 4*[n + (n-1) + (n-2) + (n-3) + (n-4) + ... 1] = 4 * [n(n+1) / 2] = 2 * n*(n+1)
		Thus, 	T(n) = 2*n^2 + 2*n
				So, T(n) is in Theta(n^2)
'''

''' Question 6: Use repeated substitution to find the running time of T(n) = 4n + T(n/3). Assume T(1) = 1
				T(n) = 4n + T(n/3)								---> T(n/3) = 4(n/3) + T(n/3^2)
					 = 4n + 4(n/3) + T(n/9) 					---> T(n/9) = 4(n/9) + T(n/3^3)
					 = 4n + 4(n/3) + 4(n/9) + T(n/27)			---> T(n/27) = 4(n/27) + T(n/3^4)
					 = 4n + 4(n/3) + 4(n/9) + 4(n/27) + T(n/81)
					 ... <after k steps>
					 = 4n(1 + 1/3 + (1/3)^2 + (1/3)^3 + (1/3)^4 +...+ (1/3)^(k-1) + T(n/3^k))

			Thus, this is a Geometric Series which stops when n / 3^k = 1  <==>  n = 3^k  <==>  k = log3(n)

			Therefore, T(n) = 4n*G(1/3,log3(n)-1) is in Theta(n)

'''

''' Question 7: Use repeated substitution to find the running time of T(n) = n^2 + 4T(n/2). Assume T(1) = 1
				T(n) = n^2 + 4T(n/2)																		---> T(n/2) = (n/2)^2 + 4T(n/4)
					 = n^2 + 4((n/2)^2 + 4T(n/4)) = n^2 + n^2 + (4^2)T(n/4)									---> T(n/4) = (n/4)^2 + 4T(n/8)
					 = n^2 + n^2 + (4^2)*((n/4)^2 + 4T(n/8)) = n^2 + n^2 + n^2 + (4^3)T(n/8) 				---> T(n/8) = (n/8)^2 + 4T(n/16)
					 = n^2 + n^2 + n^2 + (4^3)*((n/8)^2 + 4T(n/16)) = n^2 + n^2 + n^2 + n^2 + (4^4)T(n/16)
					 ... <after k steps>
					 = n^2 + n^2 + n^2 + n^2 + ... + n^2 + (4^k)*T(n/2^k)

			So, this sequence terminates when n / 2^k = 1  <==>  n = 2^k  <==>  k = log2(n)	

			That is, there are k = log2(n) iterations of n^2

			Thus, T(n) = (n^2)*log2(n) is in Theta((n^2)*log2(n))



'''