with open("p022_names.txt", "r") as file: # Read and preprocess the names list
	names = file.read()
names = names.replace("\"","").split(",")
names.sort()

sum = 0
for i in range(0, len(names)): # Sum up scores for each name
	for char in names[i]:
		sum += (ord(char) - 64) * (i + 1)
print(sum)
