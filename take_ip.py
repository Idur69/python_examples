
str = input("Enter string \n")

match= "[12*(4-5)xya]"
message = '     Learn Python  '
print("strip : ", message.strip('Lea'))

msg = "idur"
print("split : ", msg.split("---"))

string = 'android is awesome'
print(string.strip('an'))

if str[0] != match[0]:
	print("] bracket not match : ", str[0], match[0])
elif str[-1] != match[-1]:
	print("] bracket not match : ", str[-1], match[-1])

else:
	print("Given string Matched : ", str)



