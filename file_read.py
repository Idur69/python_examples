
file_name = "cit_data.txt"
f = open(file_name, 'r', encoding='utf-8')
print("Read 4 letters :\n", f.read(4))   # read the first 4 data
print("\n Read : \n", f.read())
print("file position : ", f.tell() ) # get current file position
f.close
#print("bring to initial position : ".f.seek(0))  # bring the cursor to initial postion

with open(file_name, 'r') as f:
	data = f.read()
	print("data : \n", data)
	#print("bring to initial position : ".f.seek(0))
	#print("Read line :\n",f.readline())
	#print("Read lines :\n",f.readlines())

f.close()
	