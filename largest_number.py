
# largest number among three


num1 = 10
num2 = 14
num3 = 13

if (num1 >= num2) and (num1 >=num3):
	largest = num1
	print("Largest number 1 is ", largest)
elif (num2 >= num1) and (num2 >=num3):
	largest = num2

	print("Largest number 2 is ", largest)
else:
	largest = num3

	print("Largest number 3 is ", num3)

