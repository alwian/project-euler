digits = 3
max = int("9" * digits)
largest = 0

for x in range(0, max + 1): # Loop up to the max n digit number
	for y in range(x, max + 1): # Start looping at x to prevent duplicate checks
		product = x * y
		if str(product) == str(product)[::-1] and product > largest: # Check for palindrome and store if largest
			largest = product
print(largest)
