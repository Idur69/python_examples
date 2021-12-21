## display prinumber with in instervales 


#lower = 900
#upper = 1000

lower = 9
upper = 20

for num in range(lower, upper+1):
	# all prime numbers are grater than one
	if num > 1:
		for i in range(2, num):
			if (num % i == 0):
				break
		else:
			print(num)