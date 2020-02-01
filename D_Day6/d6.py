#####Practise on lambda and map
a=map(lambda x:x%2 == 0, range(2,8))
print a#[True, False, True, False, True, False]

a=filter(lambda x:True if x%2 == 0 else False, range(2,8))
print a#[2, 4, 6]

a=filter(lambda x:'even' if x%2 == 0 else 'odd', range(2,8))
print a#[2, 3, 4, 5, 6, 7]
 
a=map(lambda x:'even' if x%2 == 0 else 'odd', range(2,8))
print a#['even', 'odd', 'even', 'odd', 'even', 'odd']

#Note->filter() works only on True False

a=map(lambda x,y:x if x>y else y, range(3,10),range(2,9)) #giving multiple arguments as input
print a#[3, 4, 5, 6, 7, 8, 9]

#Alternatively, if I use function in place of lambda in above:
def check(x,y):
	if x>y:
		return x
	else:
		return y

a=map(check,range(3,10),range(2,9))
print a#[3, 4, 5, 6, 7, 8, 9]


#Multiple arguments in map, using a fn
def check1(x):
	if x[0]>x[1]:
		return x[0]
	else:
		return x[1]

"""a=map(check1,(1,2))
print a #Traceback (most recent call last):
  File "d6.py", line 37, in <module>
    a=map(check1,(1,2))
  File "d6.py", line 32, in check1
    if x[0]>x[1]:
TypeError: 'int' object has no attribute '__getitem__'
"""

def check2(x,y):
	if x>y:
		return x
	else:
		return y

a=map(check1,([3,4,5],[7,8,9]))
print 'output = {}'.format(a)#output = [4, 8]

"""
a=map(check2,([3,4,5],[7,8,9]))
print 'output = {}'.format(a)

Traceback (most recent call last):
  File "d6.py", line 55, in <module>
    a=map(check2,([3,4,5],[7,8,9]))
TypeError: check2() takes exactly 2 arguments (1 given)
"""

###########reduce()

#reduce()
print 'reduce()'
a=reduce(lambda x,y:x if x>y else y, [3,4,5,6,7])#used to find max value in a list
print a#7
#reduce gives output of 1 operation as input to the next one and so on..

a=reduce(lambda x,y:x if x>y else y, [3,4,15,6,7])#used to find max value in a list
print a#15



#############WAP to o/p string as a dict in reverse order

d = {i:k for i,k in enumerate('hello')}
print d


for k,v in d.items():
        print k,v
print ''
for j in range(len(d)-1,-1,-1):
        print j,d[j]


###1. WAP to reverse d={'a':1,1:'app', 'c':23}
print ''
d={'a':1,1:'app', 'c':23}
print d
for k,v in d.items():
        print k,v
print ''
for k,v in d.items()[-1::-1]:#note the v that is directly displayed rather than d[k]
        print k,v
print ''
for k,v in reversed(sorted(d.items())):
	print k,v

"""
for k,v in reversed(sorted(d)):
	print k,v

Traceback (most recent call last):
  File "d6.py", line 104, in <module>
    for k,v in reversed(sorted(d)):
ValueError: need more than 1 value to unpack

"""




#Note-> sorted() and reversed() work only on sequences i.e. it works on list,tuple, string where all 3 are sequences, but dict is not a sequnce
#For ordered dictionary, use OrderedDict class of collections file of python






###############################33
#map() always returns a list
def power(x):
	return x ** 2

a=map(power, (3,4,5,6))
print a#[9, 16, 25, 36]

a=map(power, [3,4,5,6])
print a#[9, 16, 25, 36]



#filter() returns list, tuple, string whichever type is the input sequence
def power1(x):
	if x%2 == 0:
		return x ** 2

a=filter(power1,(3,4,5,6))
print a#(4, 6)


#2. WAP to print no. and its power of 2
def power2(x):
	return (x,x**2)
a=map(power2,(3,4,5,6))
print a#[(3, 9), (4, 16), (5, 25), (6, 36)]


#Write 2 using map & lambda
a=map(lambda x:(x,x**2), (3,4,5,6))
print a


#####Passing fn to a function
#1. 
def hello():
	print 'hi'

def add(a):
	a()#the fn a is called from here

add(hello)#no bracket when passing a function #since u r passing function name u r not calling it



#2. 
def hello(s):
	print s

def add(a):
	a('hi')#hello will be called on hi


add(hello)#hello will be called on hi

#3.
def hello():
	print 'hi'

def add(a):
	def h():
		print 'nested'
	return a,h #u r passing a hello and a nested function

c=add(hello)
print c[1]#<function h at 0x7fca104f1d70>
print c[0]#function hello at 0x7f897548ade8>



###########Practise
#Q1. WAP to o/p no. and its square in a tuple with each tuple coming inside a list
#for i/p -> (3,4,5,6) o/p should be [(3,9),(4,16),(5,25),(6,36)]

def power(x):
        return (x,x**2)

a=map(power,(3,4,5,6))
print a#[(3, 9), (4, 16), (5, 25), (6, 36)]


#Q2. Convert o/p of Q1. to a dict
#M-I
print 'M-I'
d={}
for i in a:
        d[i[0]]=i[1]
print d#is correct but there exists a better way

#Alternatively, the correct way
print 'Obtain a dictionary from a list: M-II'
print 'As a dict {}'.format(dict(a))#u typecast it to dict. Note the tuple change to key,value pairs

#Alternative way to obtain a dictionary 
print 'M-III'
print dict({i:k for i,k in map(power,(3,4,5,6))})
print 'M-IV'
print {i:k for i,k in map(power,(3,4,5,6))} #.......................(1)

#Q3. Convert dict to list
#Alternatively. The correct way
print list({i:k for i,k in map(power,(3,4,5,6))})#[3, 4, 5, 6] #only keys will appear #Hint: u typecast

#Q4. Print reversed list
e = list({i:k for i,k in map(power,(3,4,5,6))})
print 'e={}'.format(e)
print list(reversed([1,2,3,4,5]))

#Q5. Do (1) using lambda and map
a = dict(map(lambda x:(x,x**2), (3,4,5,6)))#tuples inside a list. Convert that to dict i.e. dict([(3, 9), (4, 16), (5, 25), (6, 36)]) -> {3: 9, 4: 16, 5: 25, 6: 36}
print a


#Q6. Try to reverse dict when keys are no.s
#reverse dict
d={2:2**2, 3:3**2, 4:4**2}
print d

for i in reversed(d.keys()):
        print i,':',d[i]

#whenever keys are no. then it always sorts the dictionary




####################
def sum(a,b):
        return a+b

def add(fn):
        return fn(2,3) + 5 #calling another function from inside a function

print add(sum) #10

####################
def sum(a,b):
        return a+b

def add(fn,a,b):
        return fn(a,b) + 5

print add(sum,2,3)#10 #passing function along with arguments it should be called on


