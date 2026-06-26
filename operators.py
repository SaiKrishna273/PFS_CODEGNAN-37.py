Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OPERATORS
#arthematic
a = 20
b=10
print(a+b)
30
print(a-b)
10
print(a*b)
200
print(a//b)
2
print(a/b)
2.0
print(a**b)
10240000000000
print(a%b)
0
#assignment
a=3
b=5
b+=a
b
8
a=10
b
8
a=10
b=20
b+=a
b
30
b-=10
b
20
b*=2
b
40
b//=10
b
4
b/=10
b
0.4
b**=3
b
0.06400000000000002
b%=8
b
0.06400000000000002
b%=7
b
0.06400000000000002


#COMPARISION OPERATORS
a=4
b=10
a<=b
True
a>=b
False
b<a
False
b>a
True
b>=a
True
a==b
False
b!=a
True
b==a
False
b=a
b
4


#LOGICAL

#LOGICAL OPERATOR
a =3
b=4
a<b and b>a
True
a<=b and b>=a
True
a!=b or a==b
True
a<= or a>=b
SyntaxError: invalid syntax
a<=b or a>=b
True
not True
False
 not False
 
SyntaxError: unexpected indent
>>> not False
True
>>> not a>b
True
>>> not b>=a
False
>>> 
>>> #IDENTIFY OPEARATORS
>>> 
>>> a = 10
>>> b = 20
>>> type(a) is int
True
>>> type(b) is not int
False
>>> type(a*b) is 200
False
>>> a*b is 200
True
>>> a%b is 0
False
>>> type(a) is float
False
>>> type(b) is str
False
>>> type(a//b) is int
True
>>> 
>>> #MEMBERSHIP OPERATORS
>>> 
>>> a =10,2,3,4,5,6,7,8,9,1
>>> 10 in a
True
>>> 20 not in a
True
>>> 20 in a
False
>>> 2 in  a
True
