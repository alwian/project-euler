import math

sum = 0

for a in range(0, 10000):
	d_a = 0
	for x in range(1, a): # Get sum of a's factors
		if a % x == 0:
			d_a += x
	b = d_a
	if b <= a: # Skip duplicate pairs
		continue

	d_b = 0
	for x in range(1, b): # Get sum of b's factors
		if b % x == 0:
			d_b += x

	if d_a == b and d_b == a: # Check if a and b are amicable
		sum += a
		sum += b
print(sum)

