## Print pyramid patterns

rows = 5

for i in range(5):
	for j in range(i+1):
		print("*", end="")

	print("\n")
print("--"*2*rows)
for i in range(rows, 0, -1):
	#print("i", i)
	for j in range(0, i):
		#print("j", j)
		print("*", end="")
	print("\n")

for i in range(5):
	for j in range(i+1):
		print(j+1, end="")

	print("\n")
print("="*2*rows)
