#Multiple inheritance with same method name
class A():
	def h(self):
		print 'class A'
	def hi(self):
		print 'hi from class A'

class B():
	def hi(self):
		print 'hi from class B'

class C(A,B): #Multiple inheritance is supported in Python #C inherits A,B from left to right
	def hello(self):
		print 'class C'

obj = C()
obj.hello()
obj.hi()
obj.h()
              
