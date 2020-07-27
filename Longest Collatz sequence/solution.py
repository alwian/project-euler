longest_length = 0
longest_start = 0

for x in range(1, 1000000):
	previous_term = x # Keep track of the longest chain and the value it started with
	length = 1

	while previous_term != 1:
		if previous_term % 2 == 0: # Create new term based on Collatz conjecture rules
			previous_term /= 2
		else:
			previous_term = (previous_term * 3) + 1

		length += 1
		if length > longest_length: # Update longest values accordingly
                        longest_length = length
                        longest_start = x
print(longest_start)
