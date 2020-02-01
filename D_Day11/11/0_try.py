#Q. WAP to ask for number and repeat till the user enter a no
#Ans:
def call():
	try:
		a=input('enter no:')
		print a
	except:
		print 'not a no'
		call()
call()


