class A:
	c=10
	def __init__(self,x,y):
		self.x = x
		self.y=y
	def dis(self):
		self.c=self.c+10

a = A(5,8)
print a.c
a.dis()
print a.c
a.c=15
print a.c
print A.c
