# bubble sort


#a = input("Enter a list ")

def bubble_sort(a):
	b = len(a) 
	#b=len(a)-1nbsp; 
	#print(b)
	for x in range(b):
		for y in range(b-x):
			
			a[y] = a[y]+1
			

			print(a[y])

a = [34,5,74,33,9]
bubble_sort(a)