Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#INDEXING
#POSITIVE INDEXING
a ="i am in class"
a[8] + a[9] + a[10] +a[11] +a[12]
'class'
a[5]+a[6]
'in'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a[2]+a[3]
'am'

#In positive indexing the index start with "0"
#TASK
a = "I AM LEARNING PYTHON"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[5]+a[6]+[7]+a[8]+a[9]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[5]+a[6]+[7]+a[8]+a[9]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
TypeError: can only concatenate str (not "list") to str
a[5]+a[6]+[7]+a[8]+a[9]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a[5]+a[6]+[7]+a[8]+a[9]
TypeError: can only concatenate str (not "list") to str
a[5] + a[6] + a[7] + a[8] + a[9]
'LEARN'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[5]+a[6]+a
[7]+a[8]+a[9]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
SyntaxError: multiple statements found while compiling a single statement
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[5]+a[6]+a[7]+a[8]+a[9]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[5]+a[6]+a[7]+a[8]+a[9]+a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
IndexError: string index out of range
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'PYTHON'
a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
IndexError: string index out of range

b= "TIME IS VERY PRECIOUS"
b[1] + b[2] +b[3]+ b[4]
'IME '
b[8]+b[9]+b[10]+b[11]
'VERY'
b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'PRECIOUS'
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'PRECIOUS'
>>> b[8]+b[9]+b[10]+b[11]
'VERY'
>>> b[0]+b[1] + b[2] +b[3]+ b[4]
'TIME '
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
IndexError: string index out of range
>>> a[21]+a[22]+a[23]+a[24]+a[25]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[21]+a[22]+a[23]+a[24]+a[25]
IndexError: string index out of range
>>> a[22]+a[23]+a[24]+a[25]+a[26]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a[22]+a[23]+a[24]+a[25]+a[26]
IndexError: string index out of range
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
' PYTHO'
>>> #FOR NEGATIVE INDEXING
>>> a = "simple is better than complex"
>>> b = "I Love Python"
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]
'xelpmoc'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-28]+a[-27]+a[-26]+a[-25]+a[-24]+a[23]
'impleo'
>>> a([-12 to -9])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a([-12,-9])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a([-12,-9])
TypeError: 'str' object is not callable
