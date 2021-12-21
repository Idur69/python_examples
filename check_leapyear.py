# Python program to check if year is a leap year or not

year = int(input("Enter year  :\n"))


if (year % 4 == 0):
	if (year % 100 == 0):
		if (year % 100 == 0):
			print("{0} is leap year".format(year))
		else:
			print("{0} is not leap year".format(year))
	else:

		print("{0} is leap year".format(year))
else:
	print("{0} is not leap year".format(year))
