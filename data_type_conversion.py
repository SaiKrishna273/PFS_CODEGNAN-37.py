Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #data type conversion
>>> #int
>>> int(6)
6
>>> int(6.1)
6
>>> int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
>>> int(3+3j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> #float
>>> float(5)
5.0
>>> float()
0.0
>>> float(6.6)
6.6
>>> float("sai")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("sai")
ValueError: could not convert string to float: 'sai'
>>> float(4+5j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
float(False)
0.0

#string
string(5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string(5)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(5.5)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    string(5.5)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string("sai")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    string("sai")
NameError: name 'string' is not defined. Did you forget to import 'string'?
str(10)
'10'
str(6.6)
'6.6'
str("sai")
'sai'
str(4+4j)
'(4+4j)'
str(True)
'True'
str(False)
'False'

#comple
#complex

complex(2)
(2+0j)
complex(6.6)
(6.6+0j)
complex("sai")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex("sai")
ValueError: complex() arg is a malformed string
complex(4+4j)
(4+4j)
complex(True)
(1+0j)
complex(False)
0j


#boolen
bool(2)
True
bool(4.5)
True
bool("sai")
True
bool(-1)
True
bool(0)
False
bool(4+6j)
True
bool(True)
True
bool(False)
False
