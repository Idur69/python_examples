

class CalculatorIdur:
	# class variables
	answer = 0
	sub = 0
	#a = 0
	#b = 0
	def __init__(self, x, y):
		#instance variables
		self.a = x
		self.b = y
	def display(self):
		print("first : ", self.a)
		print("second : ", self.b)
		print("Addition of two numbers : ", str(self.answer))
		print("Subtraction : ", self.sub)
	def addition(self):
		# local variables
		self.answer = self.a + self.b
		#print ("Add : ", self.answer)
		#return self.answer
	def subtraction(self,c, d):
		#self.c = c
		#self.d = d
		self.sub = c - d
		

#cal = Calculator(200, 500)

#cal.addition()

#cal.display()
