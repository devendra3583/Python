Day 7 Contd ..

Modules & Packages
Q. How to import a module?
Ans: Using import keyword. For eg-if you are on \Desktop, then the file you are importing must be also on your pwd i.e. Desktop

There are following 2 methods to import a module:
M-I

hii.py
-------------
a=10
def add(x,y):
    print x,y

p.py
-------------
import hii #here hii is known as module. i.e. Any python file is known as module. So, here module is "hii"   ---(1)
print hii.a
hii.add(4,5)

output
10
4 5

Note-> as soon as you import hii i.e. import hii.py i.e. import hii module and execute p.py(in which you have imported hii module(or hii.py file, imported as hii)) as python p.py, there will be a hii.pyc (which is the compiled file of module hii will be generated)

Using import keyword, we can import a python module.
moduleName.varName
moduleName.FnName
Note-Both files should be present in same directory

M-II
Using from keyword
from,import have to used together

i.
from hii import * #this will work as M-I and you don't need to explicitly say moduleName.varName or moduleName.FnName when using import keyword
print a
add(4,5)

10
4 5
Note-When using from, need not mention module name when assessing module variable or function

ii.
from hii import a,add #u can import specific variables and fns of the module separated by ,
print a
add(4,5)

10
4 5

iii.
from hii import a
print a

10

There are 3 ways to use from & import
i. to import all use *
ii. to import >1 use separated by ,
iii. to import 1 exactly import that. 

However, using (1) you cannot import a single variable/function, you have to import everything i.e. everything will be imported. Also, if you are only importing then no output will come

hii.py
---------
def add(x,y):
    print x+y

add(4,5)

9

Note-
if you do python hii.py then you will see 9 as output on terminal/console. It is to be noted that, here, hii.pyc is first created which is then executed and ouput 9 is generated from it and then deleted

>>> from hii import *
9
>>> 
$ls
hii.py  hii.pyc
$rm hii.pyc


>>> import hii
9
>>> 
$ls
hii.py  hii.pyc


Understanding about python

          Py
(every python file has some module name & that depends on 2 things: whether we import, or we run that file directly). If we import the file then the module name will be hii i.e. __name__ will hold the filename i.e. hii here. However, if we self run that file/module (i.e. python file.py) then __name__ will hold __main__
             |
            \/
          module name (i.e. __name__)

          /    \
import     self run
   |               |
   \/             \/
 filename    __main__




hii.py
------------
a=10
def add(x,y):
    print x+y

print __name__

$python hii.py
__main__


p.py
------------
from hii import *

$python p.py
hii


Q1. How can u do that inside hii.py function add() is called only when the file hii.py is self run but not called if it is imported?
Note-> This is done so that: i. u can use file (i.e. self-run it) and use the file as a module (i.e. import it inside another file so that you can use its fns)
Ans:
hii.py
-----------
a=10
def add(x,y):
        print x+y

if __name__ == "__main__":
        add(5,6)


p.py
----------
from hii import *


$python p.py  
$   //hii.pyc is created but there is no output            

$python hii.py
11


Package
To create a package with name pack do the following:

create a folder in pwd as pack
$pwd
\package
$mkdir pack && cd pack
$vi __init__.py

__init__.py                         Note->U can also keep an empty __init__.py file but it( __init__.py ) should be present inside /prac/ for prac to become a package
----------------------------
print 'hello'
import numpy

$vi hii.py

hii.py
-----------------------------
def add(x,y):
        print x+y

if __name__ == "__main__":
        add(3,4)


$cd /package
$vi p.py

p.py
--------------
from pack.hii import *
add(3,4)


$python p.py
hello
7



eg-2

p1.py
-----------
from pack import *
ar = numpy.array([1,2,3,4,5])
print ar

\package\$python p1,py
hello
[1 2 3 4 5]

eg-3
p2.py
-----------
from pack.hii import *
ar = numpy.array([1,2,3,4,5])
print ar


\package$python p2.py
hello
Traceback (most recent call last):
  File "p2.py", line 2, in <module>
    ar = numpy.array([1,2,3,4,5])
NameError: name 'numpy' is not defined


Note->Until you explicitly import everything from package i.e. 
from pack import * 
the __init__.py 's import statement will not be called although print of __init__.py will be executed everytime (even when importing particular module(file means module when referenced from inside another file) of package only)

In the above eg, p1.py and p2.py both output hello as it is a print statement. However, p1.py (which contains from pack import *) imports numpy but p2.py does not import numpy


Q. How to install python package?
Ans: $pip install package-name
All packages are installed in Python2.7\lib\site-packages>


Q. How does python run in background?

                | --------------- Python interpreter handles these steps ----------------------------------------- |
Your Source Code   -----(python compiler)->   bytecode   ----------> PVM (Python Virtual Machine)   ---------> O/p(output)
    eg-hello.py                         hello.pyc                    PVM has 2 functions: i. execute pyc, ii. delete pyc


PVM has 2 functions: i. executes the compiled (or executable) version of the python file , ii. deletes .pyc after execution of .pyc 
Python Compiles compiles the py file to .pyc


Name of the Python interpreter is python. It is the python interpreter that first creates the bytecode (contained in hello.pyc) from hello.py and then executes hello.pyc and then deletes it once execution is complete

Suppose there is a file.py which contains import hello
when u do $python file.py then hello.pyc is created (but if hello.py would have been indivdually executed then although hello.pyc would be created intermediately but would be deleted) and you can see it

In the same directory:
pattern_1_line.py
-------
a=4
print '\n'.join([(' '*(a-i))+('*'*i) for i in range(1,a+1)])
print '\n'.join([(' '*(a-i))+('*'*i) for i in range(a,0,-1)])
print '\n'.join([(str(i)+' ')*i for i in range(1,6)])
print '\n'.join([(str(i)+' ')*i for i in range(1,6)])

p.py
-----------
import pattern_1_line

$python p.py
#u will see the print stmt output from pattern_1_line.py and you can also see the compiled file containing the bytecode i.e. pattern_1_line.pyc that is created. Now you can do 
$python pattern_1_line.pyc #to execute the bytecode manually


lso do i.e You can create a package within a package using the same process /pack(contains __init__.py)/subpack/__init__.py
package.subpackage.module

from package import *
from package.subpackage import *
from package.subpackage.filename import *


Command Line Arguements
Those commands which u give from command line

$python p.py 4 5 #In linux, argv[0] is p.py
c:\>p.py 4 5 #In windows, argv[0] is p.py

command_line_args1.py
------------
import sys
a=int(sys.argv[1]) #takes input as string so typecast to int
b=int(sys.argv[2])
print 'Sum={}'.format(a+b)
print 'name of file: {}'.format(sys.argv[0])

$python command_line_args1.py  5  10
Sum=15
name of file: command_line_args1.py

a=sys.argv[1]
print type(a)
<str>


Command line Tools
#print the lines containing thw word 'ravi 'along with its line no
$python lookup.py -w ravi -f find.txt

