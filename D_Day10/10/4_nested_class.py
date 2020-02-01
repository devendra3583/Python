#Q. How to create object of a nested class
class A():
	def pow_a(self,n):
		return 2 ** n

	class B():
		def pow_b(self,m):
			return 3 ** m


a = A()
print a.pow_a(5)
#M-1
obj = a.B()
print obj.pow_b(5)

#M-2
a=A().B()
print a.pow_b(6)


#See M-III to do this

