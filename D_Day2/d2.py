""">>>a=5.6
>>>a
5.6
>>>type(a)
<type 'float'>


To check if ubuntu is 32 bit or 64 bit
https://askubuntu.com/questions/41332/how-do-i-check-if-i-have-a-32-bit-or-a-64-bit-os
devendra@devendra-Inspiron-N5010:~$ uname -a
Linux devendra-Inspiron-N5010 4.10.0-37-generic #41~16.04.1-Ubuntu SMP Fri Oct 6 22:42:59 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

Max Int value for 64 bit:
>>>import sys
>>>sys.maxint
9223372036854775807

Min Int value
-sys.maxint -1


>>>a=9223372036854775807
>>>type(a)
<type 'int'>
>>>a=9223372036854775808
>>>type(a)
<type 'long'>


Complex no.s
>>>a=complex(4,5)
>>>a
(4+5j)
"""


print 'Day 2'
a=10
type(a)

a=10.5
type(a)


a=complex(4,5)
print a

##########String
#1. Index 
h='hello hi, i am john'
print h[0] #h
print h[2] #l
print h[-1] #n

#2. splice

print h[1:5] #ello


print h[5:6] #single space

print h[2:] #from 'l' to last

print h[:5] #from beginnig to 4th index i.e. hello

#+1 by default

print h[1:9:2] #now +2 by default

print h[-5:-1] #-5 -4 -3 -2 

print 'h[-1:-5]'
print h[-1:-5] #nothing
 
print h[-1:-5:-1] #nhoj

#How to reverse string in python?
print h[-1::-1] #since endpoint is not mentioned, hence it will go till last(here 0th index(if taking from left))


#string object does not support item assignment
#h[-1]='y' #u can't   #using = u can't

#Built-in methods on string
#1. upper()
print h.upper()#string in upper case but h does not change

#2. lower()
print h.lower()

#3. find()
print h.find('am') #returns beginning index of 'am'
print h.find('a1m')#not found, so returns -1
#if 2 am's returns index of 1st

#4. replace()
print h.replace('am','was')

#5. split()
#skip for now

#6. count()
print h.count('h') #returns no. of h's in the string

#7. index()
print h.index('i') #returns index of given
print h.index('am')
print h.index('h') #0


#############lIST
a=[]#empty list
#type(a) #<type 'list'>
a=[1,2,3,4,5]#a is the list of integers
a=[1,2,3,'hello',4.5] #a is also a list, has integer,string and float

print a[0] + a[1]
print a[3].upper()#a[3] does not change unless u assign it to some variable

#>>> a.append(10) #appends at end
#>>> a
#[1, 2, 3, 'hello', 4.5, 10] 


a.append(10)
print a

b=[]
b.append(10)#appended at 0th index as empty list
print b

a.insert(1,100)#(index no. at which to insert, value to insert) #1st index element would shift to right
print a

a.insert(1,[3,5,6])#inserting a list of ints on 1st index
print a






a=[]
a.append(12)
print a
a.append([1,2,3,4,'hello'])
print a
a.insert(1,[4,5])
print a #a=[12,[4,5],[1,2,3,4,'hello']]


print a[-1]


a[1].insert(-1,100) #inside [4,5] the 5 will shift to right and 100 will come at -1th index
print a


a.remove(12) #removes the element(here int) 12
print a


del a[0][-1] #from [4,100,5] removes 5
print a



############Tuple
b=()
print b

b=1,2,3,4
print b
#OR
b=(1,2,3,4)
print b #() bracket is optional in tuple

#type(b) #<type 'tuple'>

#Difference between list vs tuple
#Ans: modification/deletion/updation not possible in tuple



"""
>>>c='ergerger'
>>>c[-1]='t' #not allowed on string
TypeError: 'str' object does not support item assignment

>>>b=[4,5]
>>>b
[4,5]
>>>b[-1]='hello' #allowed on list
>>>b
[4,'hello']

>>>c=(1,2)
>>>c
(1,2)
>>>c[0]
1
>>>c[1]
2
>>>c[-1]
2
>>>c[-1]=5 #not allowed on tuple
TypeError: 'tuple' object does not support item assignment

index and slicing both allowed on string,list,tuple but neither is allowed on dictionary
a[0] #indexing
a[0:] #slicing

"""


##########Dictionary
#Are key value pairs inside {} separated by ,
d={}
print d
#type(d) #<type 'dict'>

d={'name': 'abc', 1: 'app', 'marks': [2,3,4], 'subject': {'H':34}}
print d

#'name' is key and 'abc' is value
#1 is a key whose value is 'app'

print d['name']
print d[1]
print d['subject']
#print d[0] #<error> as 0 key not present
#key must be unique. If not, overwritten


#built-in methods in dictionary
#clear() #makes empty
d.clear()
print d

d = {'a':12}
print d.get('a') #12


d = list(d) #typecasting dictionary to list, takes key
print d #['a']

###Practise
a=[('a',12),('b',23)] #is a list containing 2 tuples 
m=a
m.append(('c',23))
print m
print a #m and a both change in list


a=(1,2)
b=a
#tuple does not have anything like append, so above not possible in tuple

a={'t':'hello',1:'world'}
b=a
b['e'] = '!!'
print a
print b #both change in dictionary too


"""import numpy
>>>a=numpy.array([3,4])
>>>a
array([3,4])
#Size of array
>>>a.shape
(2,) #It is not 2,1 it is 2,_
>>>a.reshape(2,1)
>>>a.shape
(2,1)
>>>a.ndim
2
"""








