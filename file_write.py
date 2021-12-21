
try :
	file_name = "cit_data.txt"
	with open(file_name, 'w') as f:
		f.write("Well com to cit \n")
		f.write("This is next line \n")
	with open(file_name, 'a+') as f:

		f.write("Working as software engineer")
finally:
	f.close()