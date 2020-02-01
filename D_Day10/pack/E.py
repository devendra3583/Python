#Q. How will you call superclass's constructor from sublass?
#And:
from A import *
class E(A): #E inherits A
	def __init__(self,a,b):
		print 'class E constructor'
		A.__init__(self,a,b) #A's constructor is explicitly called
					#Note- self will also be passed else u get error 
					#TypeError: unbound method __init__() must be called with A instance as first argument (got int instance instead)

	def dis(self):
		print self.x #note it will be self.x here because only self.x and self.y were initialized by A's consructor
				#Note-if u write self.a u get error
				#AttributeError: E instance has no attribute 'a'


if __name__ == "__main__":
	obj = E(50,5) #since E's constructor is present hence will be called which in turn is explicitly calling A's constructor
	obj.dis()
