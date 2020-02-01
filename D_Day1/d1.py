print 'Hello World!'


print ('Hello World!')



# t = 6, y =9 Throws error in python

a,b=3,5
print a+b


t=6
y=9
print t+y



print 'sum of %d & %d = %d'%(a,b,a+b)

print 'sum of {1} & {0} = {2}'.format(a,b,a+b)

h='hello {}'
print h.format('hi')

t=7
type(t) #tells type of t in python shell

a=raw_input('Enter name:')  #takes input as string
print a

a=raw_input('Enter Integer:')
#print a+6 Gives error as a is '5' and 6 is integer
print int(a)+6

help(int) #on python shell to know about int from documentation

a=5.6
a=int(a)
print a+10

#a=input('Enter name:') Gives error as it expects number
a=input('Enter no: ')  #takes input as no
print a


a=float(input('Enter integer:'))
print a

