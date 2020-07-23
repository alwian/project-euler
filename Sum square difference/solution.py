sum_of_squares = 0
squared_sum = 0

for x in range(1, 101): # Loop through first 100 natural numbers
	sum_of_squares += x * x # Add square to sum of squares
	squared_sum += x # Add x to sum to be squared
squared_sum = squared_sum * squared_sum # Square the sum

print(abs(sum_of_squares - squared_sum)) # Find difference
