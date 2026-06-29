Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Striding
a = "DATA SCIENCE"
a[::]
'DATA SCIENCE'
a[::1]
'DATA SCIENCE'
a[::2]
'DT CEC'
a[::3]
'DACN'
b = "cloud computing"
b[::5]
'c u'
b[::4]
'cdmi'
b[::8]
'cm'
>>> a[2:]
'TA SCIENCE'
>>> b[:2]
'cl'
>>> c[2:]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c[2:]
NameError: name 'c' is not defined
>>> b[2:]
'oud computing'
>>> b[:9]
'cloud com'
>>> b[3:11]
'ud compu'
>>> b[::2]
'codcmuig'
>>> b[::6]
'cci'
>>>  #for position
>>> c="MACHINE LEARNING"
>>> C[3:14:2]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    C[3:14:2]
NameError: name 'C' is not defined. Did you mean: 'c'?
>>> c[3:14:2]
'HN ERI'
>>> c[5:15:4]
'NEI'
>>> c[2:12:3]
'CNLR'
>>> c[0:10:1]
'MACHINE LE'
>>> 
>>> #negative striding
>>> sai="python course"
>>> sai[-5:-11:-3]
'on'
