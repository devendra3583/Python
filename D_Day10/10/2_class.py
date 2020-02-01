class A:
	c=10
	def __init__(self,x,y):
		self.x = x
		self.y=y
	def dis(self,x,y):
		print x+y+self.c

a = A(5,8)
a.dis(1,2)

