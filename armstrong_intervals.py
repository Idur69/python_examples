# armstrong intervals

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


lower = 100
upper = 500

for num in range(lower, upper + 1):

	# order of number
	order = len(str(num))

	# initialize sum
	sum = 0

	temp  = num
	while temp > 0:
		digit = temp % 10
		sum += digit ** order
		temp //=10

	if num ==sum:
		print(num)