n = 100
for x in range(n, 1, -1): # Calculate factorial manually
	n *= x

sum = 0
for digit in str(n): # Sum up digits in resulting number
	sum += int(digit)

print(sum)
