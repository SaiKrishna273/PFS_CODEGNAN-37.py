Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=4;b=10
>>> print(a+b)
14
>>> #more than 3 varibles
>>> a,b,c=2,3,4
>>> print(a,b,c)
2 3 4
>>> a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
>>> #unpack
>>> a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
