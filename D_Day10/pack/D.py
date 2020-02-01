#if init is present in subclass then superclass constructor will not be called
from A import *
class D(A): #D inherits A
	def __init__(self,a,b):
		print 'class D constructor'
		self.a = a
		self.b = b
	def dis(self):
		print self.a

if __name__ == "__main__":
	obj = D(50,5) #since D's constructor is present hence will be called and will not goto A's constructor
	obj.dis()
