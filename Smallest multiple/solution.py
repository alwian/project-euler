i = 20 # Start i at 20 as it's the min to be divisible by 20
while True:
	divisible = True # Assume divisble until proven otherwise
	for x in range(1, 21): # Check if divisble by all numbers 1 to 20
		if i % x != 0:
			divisible = False
			break
	if divisible:
		break
	i += 2 # Increment by 2 as to be divisble by even numbers, i must be even
print(i)
