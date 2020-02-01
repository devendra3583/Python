######################## FILE HANDLING IN PYTHON ###################

#create a file and write into it
f=open('xyz.txt','w') #write mode
f.write('hi hello')
f.close()


#overwrite a file
f=open('xyz.txt','w')
a=raw_input('enter:')
f.write(a) #overwrites
f.close()


#read from a file
f=open('xyz.txt','r') #read mode
d=f.read() #read entire as string
f.close()
print d

"""
Q. Display line by line
Inside file xyz1.txt write

my name is abc
my name is def
my name is ghi
my name id john
my name is abc
my name is abc
"""

f=open('xyz1.txt','r')
d=f.readlines() #read multiple lines
f.close()
print d[0] #display 1st line
print d[1] #display 2nd line

print d
print type(d)
print 'Read all lines line-by-line'

for i in d:#d is a list containing each line as its element as a string
	print i


#Q. Display only that line from xyz1.txt which contains the word 'john'
#M-I
f=open('xyz1.txt','r')
d=f.readlines()
f.close()
for k,i in enumerate(d):
	if i.find('john') > -1:
		print '{}. {}'.format(k+1,i)
#Note-> in can be used with list | tuple | string | dict (on key here) 
#a=[1,2,3,4,5] 
#if 5 in a:

#h='hello'
#if 'l' in h:
#if 'hel' in h:

#M-II
for v,i in enumerate(d,start=1):
	print "%d. %s"%(v,i)



#If .txt file contains , separated
f=open('xyz2.txt','r')
d=f.readlines()
f.close()
for i in d:
	print i

"""
xyz,43,delhi
abc,31,delhi
"""



#Using csv files in python
#If u want to store in a csv file, data must be in list
print 'Reading from csv'
import csv
path = 'xyz2.csv'
csv_file=open(path,'rb')
d=csv_file.readlines()
csv_file.close()
for i in d:
	print i


print 'writing data to csv'
path = 'xyz3.csv'
csv_file=open(path,'wb')
writer = csv.writer(csv_file)
d = [['Dev',31,'Computer Science'],['Himanshu',30,'Computer Science'],['Faheem',28,'Computer Science']]
for i in d:
	writer.writerow(i)
csv_file.close()


###########Read from a csv file using iterator
print 'read from csv using iterator'
#import csv
exampleFile = open('abcd.csv')
exampleReader = csv.reader(exampleFile)
#print exampleReader.next()
ex = list(exampleReader)
print ex
for row in ex:
	print row


###########Read from csv and display only those rows which have people from Delhi
print 'read from csv and display if from Delhi'
#import csv
exampleFile = open('abcd.csv')
exampleReader = csv.reader(exampleFile)
ex = list(exampleReader)
#print ex
for row in ex:
	if 'Delhi' in row:
		print row



################# os module
"""
import os
>>>os.getcsw() #get current working directory 
'c:\\Python27' in windows
#>>> import os
#>>> os.getcwd()
'/home/devendra/Desktop/os_module'

#>>> os.listdir('.') #lists all files/folders in cwd in a list. '.' is cwd in python. Displays no information about subfolders
['test.txt']

#>>> os.chdir('../') #to change directory to just the previous one
#>>> os.getcwd()
'/home/devendra/Desktop'


#>>> a=os.listdir('.')
#>>> a
displays all files/folders in cwd inside a list


#>>> os.getcwd()
'/home/devendra/Desktop/os_module'
#>>> os.listdir('.')
['xyz', 'test.txt']
##>>> os.chdir('xyz')
#>>> os.listdir('.')
['t3.txt', 't2', 't1']
#>>> os.getcwd()
'/home/devendra/Desktop/os_module/xyz'


Q. Display all files/folders present in cwd
Ans:
#>>> os.listdir('.')
['t3.txt', 't2', 't1']
#>>> c = os.listdir('.')
#>>> c
['t3.txt', 't2', 't1']
#>>> for i in c:
...     i
... 
't3.txt'
't2'
't1'


Q. Display all directories present in cwd
Ans:
#>>> c = os.listdir('.')
#>>> c
['t3.txt', 't2', 't1']
#>>> for i in c:
...     if os.path.isdir(i):
...             print i
... 
t2
t1
 


Q. Similarly, if is a file
Ans:
#>>> for i in c:
...     if os.path.isfile(i):
...             print i
... 
t3.txt

Q. Check if a directory file exists and print ok if it does
Ans:
#>>> os.mkdir('hello')
#>>> if os.path.exists('hello'):
...     print 'ok'
... 
ok
#>>> os.listdir('.')
['t3.txt', 't2', 't1', 'hello']


Q. How can you remove a directory
Ans:
M-I
#>>> os.listdir('.')
['t3.txt', 't2', 't1', 'hello']
#>>> os.rmdir('hello')
#>>> os.listdir('.')
['t3.txt', 't2', 't1']

Since dir was empty so it got removed by os module. If it is not empty, use shutil module
M-II To remove non-empty dir
#>>> os.listdir('.')
['t3.txt', 't2', 't1']
#>>> os.mkdir('hello')
#>>> os.chdir('hello')
#>>> os.listdir('.')
[]
#>>> os.mkdir('t1')
#>>> os.mknod('t2.txt') #create a file using os module
#>>> os.listdir('.')
['t2.txt', 't1']
>>>os.chdir('../')
#>>> os.listdir('.')
['t3.txt', 't2', 't1', 'hello']
#>>> import shutil
#>>> os.rmdir('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 39] Directory not empty: 'hello'
#>>> shutil.rmtree('hello')
#>>> os.listdir('.')
['t3.txt', 't2', 't1']


Q. How to remove a file
Ans:
#>>> os.listdir('.')
['t3.txt', 't2', 't1']
#>>> os.remove('t3.txt')
#>>> os.listdir('.')
['t2', 't1']


#Use shutil.copyfile() to copy file
           .copytree() to copy dir
           .move() to move file/dir
           


copy(src, dst)
        Copy data and mode bits ("cp src dst").
copyfile(src, dst)
        Copy data from src to dst
copytree(src, dst, symlinks=False, ignore=None)
        Recursively copy a directory tree using copy2().
        
        The destination directory must not already exist.
        If exception(s) occur, an Error is raised with a list of reasons.
move(src, dst)
        Recursively move a file or directory to another location. This is
        similar to the Unix "mv" command.
        
        If the destination is a directory or a symlink to a directory, the source
        is moved inside the directory. The destination path must not already
        exist.
        
        If the destination already exists but is not a directory, it may be
        overwritten depending on os.rename() semantics.
        
        If the destination is on our current filesystem, then rename() is used.
        Otherwise, src is copied to the destination and then removed.
        A lot more could be done here...  A look at a mv.c shows a lot of
        the issues this implementation glosses over.
Q. WAP to take a path to a directory as imput  and display all files and folders present in that directory including all its sub-folder's files and folder
"""
