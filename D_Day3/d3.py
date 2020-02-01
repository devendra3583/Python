"""if condition:
	#block
else:
	#block
 
or


if (________):
	#block
elif (______):
	#block
..
..
..
else:  #is optional
	#block

"""

a=3
if a>0: #or (a>0) i.e. bracket is optional in python. Also, python uses = for assignment and == for comparison. There is no === n python
	print 'a is greater than zero'
elif a==0:
	print 'a is zero'
elif a<0:
	print 'a is less than zero'


#########
a=2
i=1
while i<11:
	print '%d x %d = %d'%(a,i,a*i)
	i=i+1 #or i+=1


a=range(5) #will be a list of int from 0 to 4. #5 is stop
print a

""">>>help(range)
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
"""
a=range(1,7) #1 is start, 7 is stop 
print a

a=range(7,1) #[]
print a

a=range(7,0,-1) #range(start,stop,step) excluding stop
print a

a=range(1,10,2)
print a

######for loop in python
for i in range(5):#for,i are keywords 
	print i #i starts from 0 upto 4 in a list


for i in range(5):
	print i,#in same line


"""in python3.x
	print(i,end='')
"""

###range() works on string,tuple,dict,list
print ''#new line
#for with string
for i in 'hello':
	print i,

#for i in 7 error

print ''
#for with tuple
for i in (3,4,5,6):
	print i,

print ''



#typecast tuple to list
for i in list((3,4,5,6)):
	print i,

print ''


for i in range(10,0,-1):
	print i,

print ''




a={'name': 'abc', 'marks': [1,2,3,4], 'age': 12}
print a

for i in a:#takes keys
	print i, 
print ''




#if u want in 1 line evey key:value pair
for i in a:
	print i,':',a[i]


#.keys() returns list of keys of a dictionary (can be in any order)
for i in a.keys():
	print i,
print ''



#.values() returns list of values of a dictionary 
for i in a.values():
	print i,
print ''



#.items() returns tuples (key,value) inside a list
for i in a.items():#i is a tuple
	print i


#if u want key & value separately
for i,j in a.items():	
	print i,j

###range()
for i in range(7): #7 is stop
	print i,
print ''
for i in range(1,7): #1 is start 7 is stop
	print i,
print ''

#d.keys() d.values() d.items() are all methods on dictionary


############################33333
#while
i=8
while True:
	if i == 0:
		break#breaks from while
	print i
	i -= 1


	

#continue and break
for i in range(1,7):
	if i ==4:
		continue
	print i



for i in range(1,7):
	if i == 4:
		break
	print i


"""
Ask instance() not working
for i in a:
	if i=='marks':
		if instance(a[i],list):#instance() returns True if the object that u have passed belongs to the class that u have passed
			break
	print i

"""


for i in 'hello':
	if i == 'e':
		if i in ['a','e','i','o','u']:#i is a vowel
			break
	print i
#here, break breaks from for loop

vowel=['a','e','i','o','u']
"""
#################
#Ask??
for i in 'hello':
	while True:
		r = raw_input('enter str: ') #enter char
		if i == r:
			if r in vowel:
				break
			else:
				continue
	print i
#in above, continue continues while loop
#if the letter entered matches the letter in hello and is a vowel then break

"""

###############
"""
Ask????
while True:
	r=raw_input('str: ') #input string
	for i in r:
		if i in vowel:
			print 'vowel found'
			break
	print r
#in above, break breaks from for loop
#inside a string if a vowel is found then break

"""

print 'duplicate prgram start:'
a=[]
while True:
	s=input('enter no: ')
	if s in a:
		print 'duplicate'
		break
	a.append(s)
print a
#if a number is entered again then the appended list of no.s entered till now is displayed. In all other cases, the no. is appended


####################################
#1. WAP to print sum of digits that is send input
#M-I
print 'sum of digits program start:'
a=input('enter: a Natural no: ')
b=str(a)
c=0
for i in b:
        c = c+ int(i)
print 'sum of digits of %d = %d'%(a,c)

#M-II
d=[]
for i in raw_input('enter no: '):
	d.append(int(i))
print sum(d)

#M-III In 1 line
print sum([int(i) for i in raw_input('Enter no whose digits you want to sum: ')]) #known as list comprehension


#obtain indices of string letter
for i in enumerate('hello'):
	print i

for i,v in enumerate('hello'): #i is index v is value #enumerate() can take int/list/string as input and give its index,value at that index 1-by-1
	print i,v


################ Methods to create dictionary
d={i:v for i,v in enumerate('hello')}
print d

#Q. What is the difference between enumerate() and d.items() //returns a tuples in a list when obtained on a dict
for i,v in d.items():
	print i,v #  1*



#Remember .items() , .keys() , .values() output comes in a list form


#2. WAP to reverse display of 1*
#M-I
d={i:v for i,v in enumerate('hello')}
print d
for i,v in d.items():
        print i,v

for i in range(len(d)-1,-1,-1):
        print i,d[i]

#M-II more efficient way
f=d.items()[-1::-1] #take reverse string i.e. -1 (o) -2 (l) -3 (l) -4 (e) -5 (h)
for i,v in f:
	print i,v
		

#3. WAP to reverse case of a string i.e. those letters which are in uppercase should be changed to lowercase and which are in lower should change to upper
a=raw_input('Enter string to reverse its case: ')
v = []
for i in a:
        if i.isupper():
                v.append(i.lower())
        else:
                v.append(i.upper())
print v

print ''.join(v)

