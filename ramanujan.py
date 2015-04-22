import math

def factorial(n):
		''' Computes the factorial of n '''
		if n == 0:
				return 1
		else:
				recurse = factorial(n - 1)
				result = n * recurse
				return result
