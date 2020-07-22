sum = 0
for x in range(0, 1000): # Loop up to limit
	if x % 3 == 0 or x % 5 == 0: # If multiple of 3 or 5 add to sum
		sum += x
print(sum)
