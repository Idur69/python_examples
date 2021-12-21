# access indes with value 
#Using enumerate(), we can print both the index and the values.
my_lst = [12,34,45,67,7]

for index, values in enumerate(my_lst):
	print(index, values)


# start index with non zero values
for index, values in enumerate(my_lst, start=1):
	print(index, values)