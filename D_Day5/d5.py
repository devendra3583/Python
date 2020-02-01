"""
1. WAP to display following pattern?

*
* *
* * *
* * * *

M-I
"""
for i in range(1,5):
	for k in range(i):
		print '*',
	print ''

#M-II: In 1 line
print ['* ' * i for i in range(1,5)] #The string '* ' is repeated i no. of times. It is appended to a list, as we have given [] here

#Q. What does ''.join(any_list) do?
#Ans: It joins elements of any_list with '' string


print '\n'.join(['* ' *i for i in range(1,5)])


#2. WAP to output
"""

* * * *
* * *
* *
*

"""
print ''
a = ['* ' *i for i in range(5,0,-1)]
print '\n'.join(a)

"""pls note that 
a=5 #here a is a int object
b=''#here b is a string object
but 
5.anyStringMethod() #here 5 is a string class
''.join() #here '' is string class
"""

#3. What will be the output of the following:
a=5
print '\n'.join([(' ' * (a-i)) + ('*' * i) for i in range(1,a+1)])

"""Ans:

___*
__**
_***
****

"""

#4. WAP to output following in 1 line
"""
1
2 2
3 3 3
4 4 4 4
"""
#M-I writing for loop
a=5
for i in range(1,a+1):
        for j in range(i):
                print i,
        print ''

#M-II In 1 line
print '\n'.join([(str(i) + ' ' ) *i for i in range(1,a+1)]) #typecasting i to string

# 5. How to reverse a dict
#M-I:
print ''
d={'a':1, 1: 'app', 'c':23}
for k,v in d.items()[-1::-1]: #d.items() returns list of D's (key, value) pairs i.e. list containing tuples of (key,value) pairs
	print k,v
#M-II Using reversed() keyword
print ''
p=reversed(d.items())
print type(p)
print p
print list(p)

for k,v in reversed(d.items()):#for loop supports listreverseiterator object. However when printing any reversed(any_list) you will need to typecase the listreverseiterator object to list else it will show <listreverseiterator object at 0x7f5850ad9390>
	print k,v

#6. Sort dictionary on basis of key
#sort in ascending order
d1={'b':12, 'a': 'app', 'd': 1, 'c': 45}
print d1
print 'Sorted'
for k in sorted(d1.keys()): #d1,keys() returns keys of d1 inside a list
	print k,d1[k]

#reversed sorted
print 'Reversed Sorted'
for k in reversed(sorted(d1.keys())):
	print k,d1[k]

#Power of an int
def power_of_int(a):
	return a ** 2 #u can return any statement and expression
print power_of_int(3)

#lambda keyword
#returns value of the expression (that u write after the :) by default
b = lambda x: x**2 #lambda does it in 1 line
	#any input:any stmt or expression which is also the return value
	#in input u can also write x,y 
print b(3)

#if i do b = lambda x: x,x**2 #error
#            lambda x:(x,x**2) #works as return type is an expression/stmt i.e. here being a tuple 

#how to give multiple inputs to lambda
print 'multiple i/p to lambda'
b=lambda x,y:(x,y)
print b(10,3)

b=lambda x: (x,x**2)
print b(10)

b=lambda x,y:(x,x**2,y,y**2)
print b(3,4)

#7. WAP to print exactly those no.s that are even from a list
#Soln: M-I by function
print 'M-I'
def even(x):
	if x%2 == 0:
		return x
#always give 1 space after defining defining a function and calling it. Makes it more readable

print even(10) #10
print even(11) #None


#M-II Using lambda
print 'M-II'
b=lambda x:even(x)
print b(10)#10
print b(11)#None

#M-III
print 'M-III'
b=lambda x:x%2 == 0
print b(10)

#Soln to above Q. by function
def even_from_list(x):#x is a list
	d=[]
	for i in x:
		if i%2==0:
			d.append(i)
	return d
c=even_from_list([4,5,6,7,8])
print c

#Soln to above Q. by filter()
def is_even(x):
	return x%2 == 0 #Note-> Function written for a filter always takes a single i/p and returns True or False (It is due to this True | False that that particular no/item will be appended to the result)
print 'Using filter'
b=filter(is_even,range(3,11)) #since the i/p sequence is a list, here b will be a list
        #function,any sequence(can be list,tuple,string but never a dictionary because dict is not a sequence whereas list/tuple/string all are sequence)
print b

#Note- filter takes first argument as a function(Note-this function returns True of False) and 2nd arguement is a sequence i.e. can be list,tuple or string
b=filter(is_even,(3,4,5,6,7,8,9,10)) #here i/p sequence is a tuple so b will be a tuple
print b


#Another eg of filter
def check(a):
	if a.islower():
		return a #a evaluates to True but for H it will return None that's why it was giving correct answer
f=filter(check,'Hello')
print f

def check1(a):
	if a.islower():
		return True #correct way
f=filter(check1,'Hello')
print f

#7. WAP to ouput even no.s using lambda and filter
print 'print even using lambda and filter'
b=filter(lambda x: x%2==0, range(3,11))#since input sequence is a list hence b will be a list
print b#all even no.s in a list

print 'eg-2'
b=filter(lambda x: x%2 == 0,(3,4,5,6)) #since u have passed a tuple, b willl be a tuple
print b


def check3(a):
	return False
b=filter(check3,range(1,5))
print b #[]

#map

def power1(a):
	return a**2

b=map(power1,range(1,5))
print b

b=map(power1,(1,2,3,4))
print b


#8. WAP to return if no. is odd else return no. inside a list
def odd(x):
	if x % 2 == 0:
		return x
	else:
		return 'odd'

b=map(odd,range(1,5))
print b

b=map(odd,(1,2,3,4))
print b


b=map(lambda a: a if a.islower() == True else None, 'Hello')
print b #[None, 'e', 'l', 'l', 'o']


b=map(lambda a: True if a.islower() == True else False, 'Hello')
print b #[False, True, True, True, True]
