
num = 407

# To take input from the user
#num = int(input("Enter a number: "))



def primefunc(num):
	# prime numbers are greater than 1
	if num > 1:
		for i in range(2, num):
			if (num % i == 0):
				print("not prime number")
				break
		else:
			print("prime ")
	else:
		print("not prime")
	

primefunc(num)
