#Multilevel inheritance
class A():
	def hi(self):
		print 'hi from A'

class B(A):
	def hi(self):
		print 'hi from B'

class C(B):
	def hello(self):
		print 'hello'

obj = C()
obj.hi() #first it will see in C, if found then display. Else it will see in B, if found then display. Else it will go to A and display of found

