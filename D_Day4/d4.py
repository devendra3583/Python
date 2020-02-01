##########Practise
#1. WAP to output following pattern
"""
1
2 2
3 3 3
4 4 4 4
..
..
taking a no. as input and printing accordingly"""


#M-I
n = input("Enter no: ")
#print a

for i in range(1,n+1):#[1,2,3,4,....n]
        for j in range(1,i+1):#[1,2,3,...,t-1]
                print i,
        print '\n'



#M-II
for k in range(1,n+1):#[1,2,3,4,.....,n]
	for j in range(k):#[0,1,2,3,4,...,k-1] #u can also do (1,k+1) here
		print k,#to appear in same line with 1 space
	print ''#for newline i.e. next will come in new line


#2. WAP to output
"""
1
1 2
1 2 3
1 2 3 4
"""
print '\n'
#M-I
for k in range(1,n+1):
	for j in range(1,k+1):
		print j,
	print ''

#Note-> There are 3 ways to write range -> 1. (stop) 2. (start,stop) excluding stop 3. (start,stop,step) excluding stop


#3. WAP to output

"""
    1
   21
  321
 4321
"""

print '\n'

#M-0 Tried
print 'M-0' 
for k in range(1,n+1):
        for i in range(n-k,0,-1):
                print ' ',
        for j in range(k,0,-1):
                print j,
        print ''



#M-I 
for k in range(1,n+1):
	for j in range(k,0,-1):
		for l in range(j-1):
			print ' ',
		print j,
	print ''

#formatting is improper

#M-II The correct way
for k in range(1,n+1):
	for i in range(n-k):
		print ' ',
	h=k
	for j in range(k):
		print h,
		h=h-1#or h-=1
	print ''#no space

#4. WAP to output
"""
1
2 3
4 5 6
7 8 9 10
"""

#M-0 Tried
print 'M-0'
a=1
for k in range(1,n+1):
        for j in range(k,0,-1):
                print a,
                a += 1
        print ''


#M-I
a=1 #1*
for k in range(1,n+1):
	#2*
	for j in range(k):
		print a,
		a=a+1
	print ''

#Alternatively, let's try and see output puting line 1* at 2*
for k in range(1,n+1):
        a=1
        for j in range(k):
                print a,
                a=a+1
        print ''
#The output is the same as Exercise # 2


#####################################Functions in python
"""
def Add():
    #block
Add() #function calling


function in python vs function in C
1. No return type defined in python
whereas in C, we have void main()
or int main()
2. Add(int a) #wrong
Add(a) #correct
Parameter datatype is not defined in python. 'a' takes in whatever is sent to it.
https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter
"""
def Add(a):
	print a

Add('hello')


print Add(5) # output will be
             #5
             #None

b=Add(5)#5 will be displayed at terminal
print type(b)#<type 'NoneType'>


#Q. By default, python fn returns what value?
#Ans: None. 
#None is not a keyword. None is datatype of type 'NoneType'
#NoneType is a class but No value will be displayed<type 'NoneType'>



def Add(a):
	return a
print Add(6)


#M-II to display 6 as done above
b=Add(6)
print b


#5. WAP to print all prime no.s b/w 2 no.s (5,11) and display in a list
#Soln:
def primeIsInP(a,b):
        #print all prime no.s between a and b including both
        l = []
        for i in xrange(a,b+1):
                if isPrime(i):
                        l.append(i)
        print l

def isPrime(a):
        count = 0
        for i in xrange(1,a+1):
                if(a%i) == 0:
                        count += 1
        if count == 2:
                return True
        else:
                return False

primeIsInP(input('Enter no a: '), input('Enter no b: '))

#Note-> xrange() works for both small & large values
#for eg-when obtaining prime no.s for large values, use xrange()

import sys
a=range(1,100)
b=xrange(1,1000)
print 'size of range(1,100) in bytes: %d'%(sys.getsizeof(a))
print 'size of xrange(1,1000) in bytes: %d'%(sys.getsizeof(b))
#U should use xrange() as it is efficient
#sys.getsizeof() returns size in bytes


#6. WAP to take string as input & count all letters, how many they are repeated in the following ways:
"""
eg-for a string 'hello'
dictionary:
{'h': 1, 'e': 1, 'l': 2, 'o': 1} 
within list as a tuple:
[('h',1), ('e',1), ('l',2), ('o',1)]
"""
#for dictionary
#assuming all letters are in lower case
#countInDict(raw_input('Enter string: '))
#print a


# for dictionary
#M-I
def countInDict(a):
	print 'M-1'
	d={}
#	alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in a:
        	d[i] = 0
	for i in a:
        	d[i] += 1
	print d
#M-II
def countInDict1(a):
	print 'The correct way'
	a=a.lower()
	d={}
	for i in a:
		if i.isalpha():
			c=a.count(i)
			d[i]=c #will be overwritten for 2nd 3rd .. entry
	print d


#for list
def countInList(a):
	print 'M-I'
	#first I create dictionary and use it for list, iterating it on dictionary's keys
	#Create Dictionary first
	d={}
	for i in a:
	        d[i] = 0
	for i in a:
        	d[i] += 1

	#Now create empty list and append accordingly
	l=[]
	for i in d.keys():#iterate in dict's keys
        	l.append((i,d[i]))
	print l
"""
        d=[]
        for i in a:
                d.append((i,0))
        for k,i in enumerate(a):
                d[i]
"""

def countInList1(a):
	a=a.lower()
	print 'The correct way'
	d=[]
	for i in a:
		if i.isalpha():
			c=a.count(i)
			if (i,c) in d:
				continue
			else:
				d.append((i,c))
	print d


inp = raw_input('Enter string(works for lower | upper | any case letters): ')
countInDict(inp)
countInDict1(inp)
countInList(inp)
countInList1(inp)
