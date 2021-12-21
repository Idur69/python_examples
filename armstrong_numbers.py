## Armstong numbers of three
# abcd... = an + bn + cn + dn + ...
#In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. 
#For example:

#153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

num = int(input("Enter a number "))

sum = 0

# sum of  the cube of each digit

temp = num
while (temp >0):

	digit = temp % 10

	print("Digists :",digit)
	sum += digit **3
	print("sume is " , sum)
	temp //=10

	print("temp is : ", temp)


if num == sum :
	print(num , "is armstrong number")
else:
	print(num, "is not a armstrong number")


