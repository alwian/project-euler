from math import sqrt

largest = 0
limit = 600851475143

x = 3 # Current factor to test
while limit > 1: # Loop until there are no more factors other than 1
	if limit % x == 0: # Check if x is a factor
		limit /= x # Reduce the limit to reduce the number of factors to be checked
		prime = True
		for y in range(2, int(sqrt(x)) + 1): # Test if x is prime
                        if x % y == 0:
                        	prime = False
                        	break
		if prime and x > largest: # Keep track of largest prime found
			largest = x
	x += 2 # Increment by 2 as from 3 onwards primes are always odd
print(largest)
