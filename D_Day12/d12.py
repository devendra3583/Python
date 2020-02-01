# create static method
class A():
	@staticmethod
	def add():
		print 'Inside static method'
		print 'hello'

A.add()

########## Regex
#Q. why do we use regex?
#Ans: used for pattern matching

import re
s="hello my name is john name"
m=re.search(r'name',s) # r stands for 'raw string' #search for name in string s #search returns 1st name
print m
if m:
	print m.group() #to display name
else:
	print 'not found'



#To return all name
m1 = re.findall(r'name',s)
print m1

f1 = s.find('name')
print f1 #['name','name']


m = re.search(r'\w',s)
print m.group() #h

t="9hello"
print re.search(r'\w',t).group() #9 #\w reads a single letter(from starting) whether it be a-z or A-Z or 0-9 but does not read any special character. In case of special character, will read next character

t="#hello"
print re.search(r'\w',t).group() #h


t="!hello"
print re.search(r'\w',t).group() #h

t="Dffffffff^$%$%trhTRHTJTYJTYJTY^%Y%^&%I&^&"
print re.search(r'\w',t).group() #D







m=re.search(r'\w+',s) #stops at white space or special character #does not read white space and special character i.e. scans from left (excluding starting spaces or special characters) pattern like 0-9 a-z A-Z and stops till it reaches a space or special character. Returns this string(u may call this a word)
print m.group()


t = "hello123j my my"
print re.search(r'\w+',t).group() #hello123j

t = "@#@$#%$%$$^^$  %$%$ %$^$ ##$ hello123j my my"
print re.search(r'\w+',t).group() #hello123j

m=re.search('\d',s) #None #\d finds a digit scanning from left till it finds a letter (a-z or A-Z) or special character or space #\d returns a digit, however \d+ will represent entire number
print m
if m:
	print m.group()
else:
	print 'not found'



t="122344 regtr httr h hthyth"
print re.search('\d',t).group() #1
print re.search('\d+',t).group() #122344

t=356666666666666
#print re.search('\d',t).group() #TypeError: expected string or buffer
#Thus, must supply a string to search into

t='434564567765'
print re.search('\d',t).group() #4

print re.search('\d+',t).group() #434564567765

t='#$%$#^%$^$%^$% RGHRTHRE%%$$%$%$%Bgtr thyrt56^ 4565464'
print re.search('\d+',t).group() #56

# \d+ terminates at 1st space or special character
 


# '.' is used to match any single character # r'.' would means single character as a raw string
print re.search(r'.',s).group() #h

t='@hello'
print re.search(r'.',t).group() #@

t=' hello'
print re.search(r'.',t).group() # 1 empty space

#r'.+' will match entire string ('.' is generally used to match even special characters and spaces)
print re.search(r'.+',s).group() #would match every single character (this time multiple since + is there i.e. >=2) from starting to last, #here entire string is matched


#Q. WAP to match email?
#Ans:
t='my name is abc@gmail.com Hello'
print re.search(r'\w+@\w+\.\w+',t).group() #abc@gmail.com
#if email is not found, .search() would return None and if not None then u can use .group() to see that value #.search() returns 1st match in the string

"""
\w+ means word should come (before it, it can have any # of special characters, letter/words/spaces)
@ means @ should be there after \w+
\w+ is to match gmail
\. is to explicitly match . after \w+ i.e. match . after gmail  . Note-If u used only . then that would be to match any character including space but here u wanted explicitly . character
Finally, \w+ is to match com
"""
#note-> Above will not match abc@gmail#com

#Q. WAP to match email of type abc-cde@gmail.com
#Ans:
t="my name is abc-cde@gmail.com my my"
print re.search(r'\w+-\w+@\w+\.\w+',t).group()
print re.search(r'\w+\-\w+@\w+\.\w+',t).group() #is also correct but would be more relevant if '-' would have had special meaning just like .


#Q. abc-@gmail.com
t="my name is abc-@gmail.com my my"
print re.search(r'\w+\-\@\w+\.w+',t) #None


# [] is used for or i.e. [] is used like or with ideentifiers (identifier mean a-z A-Z 0-9)
#Note-> within [] u do not put + u just put outside it once. Thats it
# \w is 1 time i.e. single
# \w+ is >1 of same type

print re.search(r'[\w-]+@[\w.]+',t).group() #will match all types of email abc-@gmail.com and abc-cde@gmail.com and abc@gmail.com all

#[\w-]+ matches letters a-z A-Z 0-9 and - appearing any no of times
#@ match specific @ symbol
#[\w.]+ matches letters & no.s a-z A-Z 0-9 and . appearing any no of times


#Q. WAP to match Ph. no of the form 011-24040401 
#Ans:
t='my no is 011-2404040401 my my'
#print re.search(r'[\d-\d]+',t).group()#gives as takes - to be a range::  error sre_constants.error: bad character range
print re.search(r'[\d\-\d]+',t).group() #contains redundant \d
print re.search(r'[\d\-]+',t).group() #is the best soln 


# \w is for 1 character (a|A|9)
# \w+ is for >= 2 chars
# [\w]+ would match (wefewfer | reGERGERGTRggreg | GEREGT | rere4534h | 66457)

# hello
# \w would be h
# \w+ would be hello

#abc123@gmail.com
# \w+ would match abc123 but since @ would not be matched, it would return None

# abc123-abc@gmail.com
# [\w-]+ would match abc123-abc part

# \d matches single digit
# \d+ matched digits but will break when sees space or special character or letter here

# \w includes digit


