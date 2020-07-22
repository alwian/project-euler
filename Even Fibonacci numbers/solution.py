sum  = 0
num1 = 1 # The penultimate value in a list of Fibonacci numbers
num2 = 1 # The final value in a list Fibonacci numbers

while num2 <= 4000000: # Loop while final value is <= limit
	temp = num2 # Save the current final value
	num2 = num1 + num2 # Generate the new final value
	num1 = temp # Place the previous final value into the penultimate position
	if num2 % 2 == 0: # If current final value is multiple of 2, add to sum
		sum += num2
print(sum)
