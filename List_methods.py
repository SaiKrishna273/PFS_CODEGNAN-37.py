Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [2,6.6,"python",6+9j,True,False]
print(a)
[2, 6.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b = 5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>

#list is a collection of data
#list methods
a = ["python","c++","c","java"]
print(a)
['python', 'c++', 'c', 'java']
a.append("DSA")
print(a)
['python', 'c++', 'c', 'java', 'DSA']
#append can add element in the list

#it can append or add only one element
a.append(["ml","ai"])
print(a)
['python', 'c++', 'c', 'java', 'DSA', ['ml', 'ai']]
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)

#it cant be add more one element
#extend
a = ["ml","ai","dsa"]
a.extend(["c","c++","pyhton"])
print(a)
['ml', 'ai', 'dsa', 'c', 'c++', 'pyhton']

#insert
a=["vja","hyd"]
a.insert(1,"vzg")
print(a)
['vja', 'vzg', 'hyd']
#in insert we can insert at aparticular position

#index
a =["yellow","red","green","blue"]
a.index("blue")
3
b =a.copy()
print(b)
['yellow', 'red', 'green', 'blue']
b.count("blue")
1
sai= ["i","i","i"]
sai.count(i)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    sai.count(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
sai.count("i")
3
saii = ["ssaiiii"]
saii.count('i')
0

# sorting it can print in ascending order or alphabetic order

a = ["grapes","apples","mango","banana"]
a.sort()
a
['apples', 'banana', 'grapes', 'mango']
b= [2,3,4,1,2,3,4,5,6,10]
a.sort()
a
['apples', 'banana', 'grapes', 'mango']
b.sort()
b
[1, 2, 2, 3, 3, 4, 4, 5, 6, 10]

#reverse
#it can print from last
a = ["c",'c++',"python"]
a.pop()
'python'
a.pop(1)
'c++'
a
['c']
a.pop()
'c'
a
[]
>>> #remove
>>> 
>>> a = ["c++","c","java"]
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> a.remove("c")
>>> a
['c++', 'java']
>>> a.remove("java")
>>> a
['c++']
>>> a.remove("c++")
>>> a
[]
>>> a = ["sai","saiii","krishna","saikrishna"]
>>> len(a)
4
>>> c = "saiii"
>>> len(c)
5
>>> a.clear()
>>> a
[]
>>> a.append("hi")
>>> a
['hi']
