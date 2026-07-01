Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> a = {5,8.9,"sai",5+9j,True,False}
>>> print(a)
{False, True, (5+9j), 5, 8.9, 'sai'}
>>> type(a)
<class 'set'>
>>> 
>>> #sets method
>>> #subset
>>> a = {3,4,5,6,7,8}
>>> b = {5,6,7,8}
>>> b.issubset(a)
True
>>> b.issubset(b)
True
>>> a.issubset(b)
False
>>> 
>>> #superset
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> b.issuperset(b)
True
>>> b.issuperset(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.issuperset(c)
NameError: name 'c' is not defined
>>> c = {3,4}
>>> b.issuperset(c)
False
>>> d={6,7}
>>> c.issuperset(d)
False
>>> a.issuperset(d)
True
>>> 
#union merging
a = {2,3,4,5,6,7,8,10}
b = {2,3,4,59,6,7}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 10, 59}
c = {6,7,8,9,10,1}
a.union(c)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {"sai","sai","krishna"}
c = {"sai"}
c.union(b)
{'sai', 'krishna'}
#intersection common elements

a = {3,4,5,6,7,8,9}
b = {6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}

#update
#it can print the latest updated value
a = {10,20,30,40,50,60,70,80,90}
b = {40,50,60,70,80,90}
a
{70, 40, 10, 80, 50, 20, 90, 60, 30}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 90, 60, 30}
b
{80, 50, 70, 40, 90, 60}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 90, 60, 30}


#difference
a = {4,5,6,7,8,9,10,11}
b = {3,4,5,6,7,11,12,13}
a.difference(b)
{8, 9, 10}
b.difference(a)
{3, 12, 13}
 #symmetric difference

a = {3,4,5,6,7,8,9}
b = {1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
# intersection update

a = {1,3,5,6,7,8,9,11,13}
b = {2,3,4,5,6,7,1,13}
a.intersection_update(b)
a
{1, 3, 5, 6, 7, 13}
b
{1, 2, 3, 4, 5, 6, 7, 13}
b.intersection_update(a)
b
{1, 3, 5, 6, 7, 13}


#difference_update
a = {2,3,4,5,6,7}
b = {9,8,7,5,6,4,2}
a.difference_update(a)
a
set()
a.difference_update(b)
a
set()
a.difference_update(b)
a
set()
c = {2,3,4,5,6,7}
d = {9,8,7,5,6,4,2}
c.difference_update(d)
c
{3}
 #symmetric_difference_update

a = {11,12,13,14,15,16,17}
b = {13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 17, 11, 12, 13, 14, 15}
a = (12,1)
a.
SyntaxError: invalid syntax

a = {4,5,6,8,9,10}
a.pop()
4
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
a
{6, 8, 9, 10}
b = {3,4,5,6,7,9}
a.discard(7)
a
{6, 8, 9, 10}
a.copy()
{8, 9, 10, 6}
a.clear()
a
set()
b = set()
b.add(2)
b
{2}

a = {3,4,5,6,7}
len(a)
a

