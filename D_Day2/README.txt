Day 2

Use WING as IDE for python in linux

There are the following datatypes in python:
Number
String
List
Tuple
Dictionary

>>>a=5.6
>>>a
5.6
>>>type(a)
<type 'float'>


Number
-Integer
A number can be integer
a=5
32 bit m/c
See range in documentation

64 bit m/c
-float
a=5.6

10.3676
To display 2 decimal places, use:
%.2f  //python
10.36

type(a)
float

-long
In python, double is the same as long i.e. an int. There is no double explicitly
For decimal, in python, there is only float
-complex
a=complex(4,5)

type(a)
4+5i



String
                            -3-2-1
h='hello hi, I am john'
     0123456789..
Python's string is like an array but not an/cannot be called as an array


You can perform 2 operations on a string:
1. index
Where we want to get a particular value at that index
>>>print h[0]
h
>>>print h
Entire string displayed here
>>>h[2]
l
h[-1]
n

2. Slice
Used to slice sub-part
>>>print h[1:5]
                Startpoint:endpoint. But not including end-point
h is an object
ello


h[5:6]
_


h[2:]
Displays entire

h[:4]
From beginning
hell

+1 it does by default unless u provide

h[1:9:2]
2 ka increment
1 3 5 7 
cl_i
9 won't come since upto 8 only

h[-5:-1]
-5 -4 -3 -2 
-1 won't come


h[-1:-5]
It won't display anything 
//It checks entire sequence first, which it will not find -1 then 0 then 1, it won't find so no display

h[-1:-5:-1]
-1 -2 -3 -4

Built in methods on string
upper()
lower()
find()
replace()
split()
count()
index ()
There are more but above are the main ones.

h.upper()
//Converts entire string h to uppercase
Returns string in uppercase but h does not change
U can assign to another
h.lower()

h.lower()

h.find('am')
Returns beginning index of am
12

'a1m'
-1

If 2 am's returns 1st

h.replace('am','was')
Replaces all occurences of am with was


h.split()
Skip for now

h.count('h')
3

h.index('i')
7

h.index('am')
12

In list, find() is not there only index() is there
This was string
--
h.
Press tab in windows to know all string built-in methods

>>>help(h.find)
Documentation opens up

>>>help(str)
help is a function, str is 'string class'
Shows all methods of str class









List is a collection of same or might be different datatypes separated by a ',' and inside in a square bracket []
U can give int|float|string|long
a=[]
a=[1,2,3,4,5]
a=[1,2,3, 'hello', 4.5]

Tuple is a collection of different or might be same datatype separated by a ',' and inside a parenthesis ()
b=()
b=(1,2,3,4) or b=1,2,3,4 
() is optional

type(b)
tuple

Difference between list and tuple
Modification/deletion/updation not possible in tuple

Dictionary
{} Using key value pairs. Key must be unique else overwritten
d={'name':'abc',1:'app','marks':[2,3,4]}

--
>>>a=5.6
>>>a
5.6
>>>type(a)
<type 'float'>


To check if ubuntu is 32 bit or 64 bit 
https://askubuntu.com/questions/41332/how-do-i-check-if-i-have-a-32-bit-or-a-64-bit-os
devendra@devendra-Inspiron-N5010:~$ uname -a
Linux devendra-Inspiron-N5010 4.10.0-37-generic #41~16.04.1-Ubuntu SMP Fri Oct 6 22:42:59 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

Max Int value for 64 bit:
>>> import sys
>>> sys.maxint
9223372036854775807

Min Int value 
-sys.maxint -1


>>> a=9223372036854775807
>>> type(a)   
<type 'int'>
>>> a=9223372036854775808
>>> type(a)
<type 'long'>


Complex no.s
>>> a=complex(4,5)   
>>> a
(4+5j)


>>>help(h.find)
>>>help(str) #shows all methods of str class



