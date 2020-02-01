class A():
	def h(self):
		print 'class A'

class B():
	def hi(self):
		print 'class B'

class C(A,B): #Multiple inheritance is supported in Python #C inherits A,B from left to right
	def hello(self):
		print 'class C'

obj = C()
obj.hello()
obj.hi()
obj.h()
              
