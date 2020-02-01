while True:
	try:
		a=input('enter no:')
		print a
	except:
		print 'not a no'
		continue
	else:
		print 'hello'
		break
	finally:
		print 'HelloWorld!!'
