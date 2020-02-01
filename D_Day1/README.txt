---===---
Python Basics
Python is a Programming Language as well as a scripting language like perl,ruby (what is scripting language? Ans: which can be used as a script, is a precompiled code)

To download Anaconda: "download anaconda"  on google

Install Python 2.7.14 on Windows
1. Download python-2.7.14.msi (17MB) from python.org
2. Run it
After installation, start -> it shows IDLE(Python GUI) -> click to Open it -> Python shell opens up
Has no ; 
{
} brackets

How to print Hello World?
WAY-1: In a shell  //useful when you want to see output of a variable
M-I
>>>python 'hello world'
hello world
print is a keyword, 'hello world' is string

Commands/Shorcuts for linux(ubuntu):
Press Ctrl+D to exit out of python shell in ubuntu(linux)
$python -V #to know version of python u r running
Alt+Shift+G -> to go to last line when editing in vi editor


M-II
print ('hello world') //as a function

In 2.7.x M-I,II both are available but in 3.x only M-II is available

WAY-2: To write in a file & then execute
Python Shell -> File -> New -> A new file opens up -> write print 'hello world'
-> Save -> write h -> automatically saves as h.py

h.py -> Run -> Run module -> you will see output in 'interactive shell'

WAY-3: open cmd 
cd:>cd Desktop
cd:\Desktop>r.py
hello world
 u can also do c:\Desktop>python r.py //after adding PATH to ENVIRONMENT VARIABLE
Here python is the 'interpreter name'

M-I 
a=5
b=6
M-II
a,b=5,6 //is correct


c = 'hello' //c becomes string
d = 10 //d becomes int
d = 10.5 //d becomes float

Note -> Everything in python is an object

Here, c is an object of string class
d is an object of float class

-We don't need to define datatype in python. So, we say python is a dynamic language i.e. datatype is known at runtime. Other languages are statis languages eg-C,C++,Java static datatype defined


%d -> integrer
%s -> string
%f -> float

M-I to print sum of 5 & 6 = 11
print 'sum of %d & %d = %d'%(a,b,a+b)


M-II 
print 'sum of  {} & {} = {}'.format(a,b,a+b)
                                                   0,1,2

here we use {} hence not fixed as integer (like %d earlier). what u give integer/string/float will go

{0} {1} {2}

{1} {0} {2}
b    a    a+b

format() method for string class
object.member
 here 'vvrbrt' is a string and format is a method of class string


h = 'hello {}'
print h.fomrat('hi')
hello hi

Q2. How to get i/p from user?
raw_input() //takes as string
input() //takes as

a = raw_input('Enter name:')
print a
Enter name: John
John

type(a)


print a+6
error
since a = '5' string and 6 is integer


print int(a) + 6 //type-casting //M-I
to check if int is a class or function
>>>help(int)
//displays details from documentation

a = int(a) //M-II 
print a+6


a = input('Enter name')
Enter name: John //error
5 or 5.6 is ok as input() take integer/float

Typecast:
a = float(input('Enter name:'))
Enter name: 5
Output: 5.0


Datatypes in python:
1. Number
4 types:
-integer
-float
-long(double is same as long in python)
-complex
-
2. String (single quotes '  '   and double  "    ")
3. List   []
4. Tuple   ()
5. Dictionary  {key: value}

if else

--
Python is a programming and scripting programming language. It is
-high level
-interpreted(do not compile code like C manually)
Uses oops

No ; or {} 
Python is a dynamic language (i.e datatypes is known at runtime. Other languages are static languages like C/C++/Java i.e. datatype is explicitly defined in these)
--
