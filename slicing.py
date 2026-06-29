Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a ="codegnan"
>>> a[0]+a[1]+a[2]+a[3]
'code'
>>> #slicing
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[:8]
'codegnan'
>>> a[4:8]
'gnan'
>>> b= "work intil you succed"
>>> b[:5]
'work '
>>> b[:10]
'work intil'
>>> b[4:10]
' intil'
>>> a[10:14]
''
>>> a[10:15]
''
>>> a[11:15]
''
>>> b[10:15]
' you '
>>> b[:4]
'work'
>>> b[15:20]
'succe'
>>> c = "codegnan it solution"
>>> c[9:11]
'it'
>>> b[0:8]
'work int'
c[0:8]
'codegnan'
c[12:20]
'solution'
d = "saikrishna"
d[:10]
'saikrishna'
#negative slicing
a1="saikrishna"
a1[-7:-1]
'krishn'
a[-7:0]
''
a1[-7:0]
''
a1[-8:-1]
'ikrishn'
a1[-7:-1]
'krishn'
#negative indexing
sai = "Vijayawada is a royal city"
sai[-11:-4]
' royal '
sai[-10:-5]
'royal'
sai[-22:-17]
'yawad'
sai[-4:-1]
'cit'
sai[-4:]
'city'
saii="VIZAY IS CITY OF DESTINY"
sai[-15:-11]
'is a'
saii[-15:-11]
'CITY'
saii[-24:-19]
'VIZAY'
saii[-7:]
'DESTINY'
