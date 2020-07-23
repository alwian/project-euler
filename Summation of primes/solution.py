from math import sqrt

sum = 2 # Start sum at 2 as only even prime
for x in range(3, 2000000, 2): # Check all odd numbers below 2000000
	prime = True # Assume prime until proven otherwise
	for y in range(3, int(sqrt(x)) + 1): # Check for primality up to sqrt of number to be tested
		if x % y == 0:
			prime = False
			break
	if prime:
		sum += x
print(sum)
