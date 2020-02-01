class A:
	c=10
	def __init__(self,x,y):
		self.x = x
		self.y=y
		self.c = 50#this always accesses of its own object. To access that c of class variable u need A.c
	def dis(self):
		print self.c

a = A(5,8)
a.dis()
print a.c
print A.c
