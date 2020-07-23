with open("nums.txt", "r") as file: # Go through each number in file, adding to sum
	sum = 0
	for num in file:
		sum += int(num)
print(str(sum)[:10]) # Show first 10 digits
