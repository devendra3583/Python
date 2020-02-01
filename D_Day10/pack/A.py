class A():
	c = 10
	@staticmethod
        def Div(x,y): #Note - static method does not need self. Also this x,y is different from self.x and self.y
                return x/y
	def __init__(self,x,y):
		print 'class A constructor'
		self.x = x
		self.y = y
	def dis(self):
		print self.x + self.y
	def Mul(self):
		print self.x * self.y
	@staticmethod
	def Div(x,y): #Note - static method does not need self. Also this x,y is different from self.x and self.y
		return x/y

if __name__ == "__main__":
	obj = A(12,2)
	obj.dis()
	obj.Mul()
	A.Div(12,2)
	
