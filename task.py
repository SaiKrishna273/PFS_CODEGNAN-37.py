Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = [9,1,5,2,8,6,3,7,0]
a.append(0)
a
[9, 1, 5, 2, 8, 6, 3, 7, 0, 0]
b = set(a)
b
{0, 1, 2, 3, 5, 6, 7, 8, 9}
b = set(a())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b = set(a())
TypeError: 'list' object is not callable
b = list(a(b))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b = list(a(b))
TypeError: 'list' object is not callable
b = a(b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b = a(b)
TypeError: 'list' object is not callable
b = a(list(b))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b = a(list(b))
TypeError: 'list' object is not callable
my_set = {5, 2, 8, 1}

my_list = list(my_set)
print(my_list)
SyntaxError: multiple statements found while compiling a single statement
a = [9,1,5,2,8,6,3,7,0]
mlist = list(a)
print(mlist)
[9, 1, 5, 2, 8, 6, 3, 7, 0]
lst = [9, 1, 5, 2, 8, 6, 3, 7, 0]

s = set(lst)
print(list(s))
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax
>>> 
>>> a = [9,1,5,2,8,6,3,7,0]
>>> b = [::2]
SyntaxError: invalid syntax
>>> a[::2]
[9, 5, 8, 3, 0]
>>> a[1::2]
[1, 2, 6, 7]
>>> p = a[::2]+a[1::2]
>>> p
[9, 5, 8, 3, 0, 1, 2, 6, 7]
>>> p.reverse()
>>> p
[7, 6, 2, 1, 0, 3, 8, 5, 9]
>>> [7, 6, 2, 1, 0, 3, 8, 5, 9]
[7, 6, 2, 1, 0, 3, 8, 5, 9]
>>> 
>>> a = [9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> c = a1+a2
>>> c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
