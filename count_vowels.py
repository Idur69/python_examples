# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make dictionay with key and values
count = {}.fromkeys(vowels,0)
print("count first :", count)
for chr in ip_str:
	if chr in vowels:
		#print("chr : ", chr)
		count[chr] += 1

print(count)
