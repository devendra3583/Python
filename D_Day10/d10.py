"""-class is a collection of methods, variables |*
 by creating object u can use *

-self means current object. Here, self is representing current object
"""

class A(): #() is optional
	c=10
	def dis(self):
		print self

obj = A()
obj1 = A()
obj.dis()
obj1.dis()


#Passing parameter into method
class A:
	def dis(self,x):#1st parameter will always be self
		print x

obj = A()
obj.dis(12)




class A():
	def dis(self,x,y):
		print x+y

obj = A()
obj.dis(12,2)



#Q. How to use the same variable in same class but in some other method
#Ans:
print '------------------'
class A():
	c = 10 #c is a class variable(of python) or static variable(of Java)
	def assign(self,x,y):
		self.x = x
		self.y = y
	def dis(self):
		print self.x
		print self.y
	def add(self):
		print self.x + self.y
	def mul(self):
		print self.x * self.y #here we are using self.x and self.y as the same variable of the same class but in some other method, here in mul()
obj = A()
obj.assign(12,2)
obj.dis()
obj.add()
obj.mul()

#to access c from outside the class use A.c

#Difference between class variable and instance variable(i.e. variable w.r.t object)?
print '--------------'
obj = A()
obj.assign(12,2)
obj.add()
obj.mul()
obj.c = 89
print A.c #10  #class variable/static variable. is fixed. is same for all object
print obj.c #89 #is different for different objects

#To access c as a instance variable, define it as self.c
print '--------------'
class B():
	c=10
	def assign(self,x,y):
		self.c = 0
		self.x = x
		self.y = y
	def dis(self):
		print self.x + self.y + self.c

b  = B()
b.assign(10,5)
b.dis()
	

#Q. How to call a method from inside another method of the same class?
#Ans:
"""
class C:
	def dis(self,x,y):
		self.c = 0
		self.x = x
		self.y = y
		print x + y + self.c
		self.mul()

	def mul(self):
		self.dis()

obj = C()
obj.dis()  # this will go into an infinite loop calling each other

"""


################concept of Constructor in python
#Use __init__(self,x,y) to write a constructor for a class
print '-------------------'
class A():
	c=10 #.............(1)
	def __init__(self,x,y):
		print 'class A constructor'
		self.x = x
		self.y = y
	def dis(self):
		print self.x + self.y
	def Mul(self):	
		print self.x * self.y

obj = A(12,2) #self.x and self.x are initialized w.r.t. obj
obj.dis()
print obj.c #is 10 since c is 10 on (1). However if u define self.c inside __init()__ or in any other method then that value will be reflected here

#see 10/

print '---------------------'
class C():
	c=5
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.c = 0
	def dis(self):
		print self.c
c = C(1,2)
print c.c #0
c.dis()
print A.c #5






######## Inheritance
# A superclass
# B subclass
class B(A): #inherit A
	def power(self,n):
		return n ** n

obj = B(3,4) #since B() does not hold a constructor, hence A's constructor would be called
obj.Mul() #12
obj.dis() #7
print obj.power(4) #256

#See pack/


#to make a method static
Use @staticmethod
