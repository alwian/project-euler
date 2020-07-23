for a in range(0, 1001): # Loop up to max sum
	for b in range(a + 1, 1001 - a): # Start at a + 1 as b > a, go to 1001 - a as max sum is 1000
		for c in range(b + 1, 1001 - (a + b)): # Start at b + 1 as c > a, got to 1001 - (a+b) as max is 1000
			if a + b + c == 1000 and a*a + b*b == c*c: # Check if right combination found
				print(a*b*c)

