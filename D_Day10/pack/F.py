from A import *
class F(A):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def check(self):
		if self.x % 2 == 0:
			print '%d is even'%self.x
		else:
			print '%d is odd'%(self.x)

if __name__ == "__main__":
	obj = F(11,1) #F's constructor will  be called
	obj.check()
