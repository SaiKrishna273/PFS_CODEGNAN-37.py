Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a = (4,5.6,"code",5+9j,True,False)
>>> print(a)
(4, 5.6, 'code', (5+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count(5+9j)
1
>>> a.index(True)
4
>>> len(a)
6
>>> a.index(saiiii)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.index(saiiii)
NameError: name 'saiiii' is not defined
>>> a.index("saiiii")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.index("saiiii")
ValueError: tuple.index(x): x not in tuple
>>> a='saiii'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.index()
TypeError: index expected at least 1 argument, got 0
>>> a = ("saii")
>>> a.index(saiii)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.index(saiii)
NameError: name 'saiii' is not defined
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.index()
TypeError: index expected at least 1 argument, got 0
>>> 
