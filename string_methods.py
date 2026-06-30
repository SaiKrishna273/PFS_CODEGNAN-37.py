Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string length
#len( no of characters in a given string)
a = "Python"
len(a)
6
b = "python course"
len(b)
13
c=""
len(c)
0
d = " "
len(d)
1
#count()
#it is a method which can print repeated the words in char
a = "twinkle twinkle little star "
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count(" ")
4
4
4
#find a string
a = "code"
a[1]
'o'
a.find("d")
2
a.find("o")
1
b = "saiii"
b.find("i")
2
b[2:]
'iii'

 

#escpae sequence

#\n - new line
#\t - tabspace
a = "name:saii\nplace:bhimavaram\tmail id:saikrishnagudla556@gmail.com\nphone no:9154313556\tcollege:IIITS"
print(a)
name:saii
place:bhimavaram	mail id:saikrishnagudla556@gmail.com
phone no:9154313556	college:IIITS
#\->backslash used in coding
#/->forward slash used in url

#________________________________________________________
#replace()
a = "wait until you succed"
a.replace("wait","work")
'work until you succed'
a
'wait until you succed'
b = "wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'

#upper()
a = "saii"
a.upper()
'SAII'
#lower()
a.lower()
'saii'
c.upper()
''
a.upper()
'SAII'
a.upper(0)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.upper(0)
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c[0].upper()
IndexError: string index out of range
a[0].upper()
'S'
a.capitalize()
'Saii'
# if we want starting capital with printing whole word we will use capitalize()
#title
a = "i am learning python course"
a.title()
'I Am Learning Python Course'
a = "jaava"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.is digit()
SyntaxError: invalid syntax
b = "python course"
b.isalpha()
False
c = "pythoncourse"
c.isalpha()
True
c.isdigit()
False
d = 1223
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
#because it is only for string methods
d ="123"
d.isdigit()
True
d.isalnum()
True
d = "saii@gmail.com"
d.isalnum()
False
d="saiikrishna"
d.isalnum()
True
#-------------------------------------------------------------------------------------
d.isnotalnum()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    d.isnotalnum()
AttributeError: 'str' object has no attribute 'isnotalnum'. Did you mean: 'isalnum'?
d.is not alnum()
SyntaxError: invalid syntax
#starts with and enswith()
a = "hello world"
a.startswith("h")
True
a.endswith("n")
False
a.endswith("d")
True
#strip
a = "            sai         "
a.lstrip()
'sai         '
a.rstrip()
'            sai'
a.strip()
'sai'
#split()
a = "python java c c++"
a.split()
['python', 'java', 'c', 'c++']
s = " i am in vijayawada"
s.split()
['i', 'am', 'in', 'vijayawada']
c = "codegnan"
c.split()
['codegnan']
#join()
a = "vja hyd vzg"
a.join()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
a.join(a)
'vvja hyd vzgjvja hyd vzgavja hyd vzg vja hyd vzghvja hyd vzgyvja hyd vzgdvja hyd vzg vja hyd vzgvvja hyd vzgzvja hyd vzgg'
"".join(a)
'vja hyd vzg'
b = "vja","hyd","vzg"
" ".join(b)
'vja hyd vzg'
#comcatenation
#comcatenation
#concatenation
a = "hello"
b = "world"
proitn(a+b)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    proitn(a+b)
NameError: name 'proitn' is not defined
print(a+b)
helloworld
#for concatenation
fname= "saii"
lname = "g"
print(fname.title()+" "+lname.title())
Saii G
print(fname+" "+lname(title.()))
SyntaxError: invalid syntax
print((fname+" "+lname).title())
Saii G
#for concatination we can use different types of string methods
#formatting
a = 4
b = 8
print(a+b)
12
print("the sum is:",a+b)
the sum is: 12
x = "vja"
print("city is",x)
city is vja
#format
a = "sai"
b = "krishna"
print("hii {} {}".format(a,b))
hii sai krishna
print("ela {}unnav{}".format(a,b))
ela saiunnavkrishna
print("elaunnav {}{}".format(a,b))
elaunnav saikrishna

#in format we use multiple methods
##fstring
a = "sai"
b = "krishna"
print(f"hello {a}{b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a}{b}")
...       
hello saikrishna
>>> a = 2
...       
>>> b = 3
...       
>>> print(f"the product is: {a}*{b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"the product is:{a*})
...       
SyntaxError: f-string: expecting '=', or '!', or ':', or '}'
>>> a = 2
...       
>>> b = 10
...       
>>> c = a*b
...       
>>> print(f"the product is: {c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"the product is: {c}")
...       
the product is: 20
>>> the product is: 20
...       
SyntaxError: invalid syntax
>>> print(f"the product is: {a}{*}{b})
...       
SyntaxError: f-string: expecting a valid expression after '{'
>>> #
... print(f"the product is : {a*b})
...       
SyntaxError: unterminated f-string literal (detected at line 2)
>>> print(f"the product is:{a*b}")
...       
the product is:20
