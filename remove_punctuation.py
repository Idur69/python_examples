
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# take input from user

#my_str = input("Enter a string ")

my_str = "Hello!!!, he said ---and went."

rm_punct = ""
for char in my_str:
	if char not in punctuations:
		rm_punct = rm_punct + char

# display the unpunctuated string

print(rm_punct)
