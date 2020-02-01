class A:
	class B:
		def hello(self):
			print 'hello'
	obj = B()
	def h(self):#this self is of A's object self i.e. a
		self.obj.hello()

a = A()
a.h()
