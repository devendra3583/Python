f=open('xyz.txt','r')
d=f.readlines()
f.close()

for i in d:
	print i


c=1
for i in d:
	if 'john' in i:
	        print '%d,%s'%(c, i)
	c +=1
