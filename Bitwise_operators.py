Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#BITWISE OPERATORS
a&b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a&b
NameError: name 'a' is not defined
a=2
b=4
a&b
0
a=7
b=5
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
#or operation
a =3
b=5
a|b
7
a =4
b=5
a|b
5
#not operation
a=5
-(a+1)
-6
~a
-6
a=9
~a
-10
b=-9
~b
8
c=-12
~c
11

#xor operations
a=3
b=5
>>> a^b
6
>>> a=7
>>> b=9
>>> a^b
14
>>> 
>>> #left shift right shift
>>> a=12
>>> b=10
>>> a^b
6
>>> #left shift
>>> 
>>> a=3
>>> a<<2
12
>>> b=4
>>> a<<3
24
>>> b<<3
32
>>> a=5
>>> a>>1
2
>>>   a=2
...   
SyntaxError: unexpected indent
>>> b=2
>>> a<<2
20
>>> b<<2
8
>>> #right shift
>>> a=4
>>> b=5
>>> a>>2
1
>>> b>>2
1
