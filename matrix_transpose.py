

X = [[12,5],
	 [4,7],
	 [6,9]]

result = [[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
	# iterate through columns
	for j in range(len(X[0])):

		result[j][i] = X[i][j]
print(result)