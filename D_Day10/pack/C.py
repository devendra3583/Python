from A import *
class C(A):
	def check(self):
		if self.x % 2 == 0:
			print '%d is even'%self.x
		else:
			print '%d is odd'%(self.y)

if __name__ == "__main__":
	obj = C(12,2) #since C does not have a constructor, A's constructor will be called. self.x & self.y are now initialized to 12 & 2 respectively
	obj.check()
