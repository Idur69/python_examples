# regexpression 
# https://www.programiz.com/python-programming/regex
# Note :
# Metacharacters:

#--> [] . ^ $ * + ? {} () \ |
#^ - Caret 
#The caret symbol ^ is used to check if a string starts with a certain character.
#	epression = '^a...s$'

#$ - Dollar

# The dollar symbol $ is used to check if a string ends with a certain character.

# * - Star

#The star symbol * matches zero or more occurrences of the pattern left to it.

# ex: ma*n
# 1. maaan --> Matched
# 2 . maikn--> Not matched

#\d - Matches any decimal digit. Equivalent to [0-9]
# ex : \d 
# 1.  12abc3 --> 3 matches (at 12abc3)
# 2.  lkjldsjfsd --> No match

# \D - Matches any non-decimal digit. Equivalent to [^0-9]
# \D
#  1. 1ab34"50 -- > 3 matches (at 1ab34"50)
# 2. 1235 --> No match



import re


# ----------- match -------------
pattern = '^a...s$]'

#pattern = '[afjlljsldfssd]'
my_string = 'aliags'

result = re.match(pattern, my_string)

if result:
	print("Matched successfully")
else:
	print("Not matched!")

# output :

#alias   matched
#alibas not matched
#--------- findall() ----------
string1 = 'hello 12 hi 89. Howdy 34'
#pattern1 = '\d+'    #  ['12', '89', '34']

pattern1 = '\D+'  ## ['hello ', ' hi ', '. Howdy ']


result1 = re.findall(pattern1, string1)
print("result 1 :", result1)

#---------- split() ----------

string2 = 'Twelve:12 Eighty nine:89.'
pattern2 = '\d+'   # ['Twelve:', ' Eighty nine:', '.']
#pattern2 = '\D+'   #['', '12', '89', '']

result2 = re.split(pattern2, string2)
print("result 2 : ", result2)

# ------------- search ------------

string3 = "Python is fun"
pattern3 = "\APython1"

result3 = re.search(pattern3, string3)
if result3:
	print("Pattern match in a string")
else:
	print("Pattern not match")


