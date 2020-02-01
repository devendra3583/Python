from A import *
#import A #will not work as then u have to specifically give className.functionName()
class B(A):
	def power(self,n):
		return n ** n

if __name__ == "__main__":
	obj = B(12,2) #since B does not have a constructor hence A's constructor (if it exists) would be called. However, if B had a constructor then B's constructor would be called
	print obj.power(4)
