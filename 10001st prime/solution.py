from math import sqrt

found = 2
x = 3
while found != 10001: # Keep searching until 10001st prime found
	x += 1
	prime = True # Assume prime until proven otherwise
	for y in range(2, int(sqrt(x)) + 1): # Check if prime
		if x % y == 0:
			prime = False
	if prime: # If prime increase found count
		found += 1
print(x)
