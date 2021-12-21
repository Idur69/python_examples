## find factorial of number given by user

#input take from user
num  = int(input("Enter factorial number : "))

factorial = 1
if num < 0:
	print("Sorry factorial number doesnot exist of negative number")

elif num == 0:
	print("The factorial number 0! is 1")
else:
	for i in range(1, num+1):
		factorial = factorial * i
	print("factorial of ",num,"! is ", factorial)
