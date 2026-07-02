Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{} it is a pair format elements
a = {"name":'SAI',"city":"bhimavaram"}
print(a)
{'name': 'SAI', 'city': 'bhimavaram'}
type(a)
<class 'dict'>
b = {5,6,7,8,9"name"}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b = {5,6,7,8,9,"name"}
print(b)
{5, 6, 7, 8, 9, 'name'}

#dictionary methods
a = {"name":'SAI',"city":"bhimavaram","mailid":"saikrishnagudla556@gmail.com"}
a.items()
dict_items([('name', 'SAI'), ('city', 'bhimavaram'), ('mailid', 'saikrishnagudla556@gmail.com')])
a.keys()
dict_keys(['name', 'city', 'mailid'])
a.values()
dict_values(['SAI', 'bhimavaram', 'saikrishnagudla556@gmail.com'])

#in update we more than one in dictionary
a = {"course":"python","institute":"codegnan"}
a.update({"name":"sai"})
a
{'course': 'python', 'institute': 'codegnan', 'name': 'sai'}
a.update({"year":2026})
a
{'course': 'python', 'institute': 'codegnan', 'name': 'sai', 'year': 2026}
#IN UPDATE WE CAN ADD MORE THAN ONE IN DICTIONARY


##SET_DEFAULT
a = {"YEAR":2026,"MONTH":"JULY"}
a.setdefault("date",2)
2
a
{'YEAR': 2026, 'MONTH': 'JULY', 'date': 2}
## IT CAN ADD ONLY ADD ONE

a
{'YEAR': 2026, 'MONTH': 'JULY', 'date': 2}
##pop()
a = {"time":12,"hour":1,"min":3}
a.pop("time")
12
a
{'hour': 1, 'min': 3}
a.popitem()
('min', 3)
a
{'hour': 1}
a.pop()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
#we  have to argument to pop
#for popitem it will pop both keys and values


## get
 a = {"college":"IIITS","branch":"ECE"}
 
SyntaxError: unexpected indent
a = {"college":"IIITS","branch":"ECE"}
a
{'college': 'IIITS', 'branch': 'ECE'}
a.get("college")
'IIITS'
a.get("branch")
'ECE'

a = {"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
a
{}
b={}
b.update({"name":"sai"})
b
{'name': 'sai'}
8
8

#len()
a = {"name":"pooja","course":"python","year":2026}
a
{'name': 'pooja', 'course': 'python', 'year': 2026}
a.count("name")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a ={"name":"sai","city":"bhimavarm","name":"sai"}
a
{'name': 'sai', 'city': 'bhimavarm'}
a = {"name":"sai","city":"BVRM","name":"saiii"}
>>> a
{'name': 'saiii', 'city': 'BVRM'}
>>> a = {"name1":"saii","city":"BVRM","name2":"krishna"}
>>> a
{'name1': 'saii', 'city': 'BVRM', 'name2': 'krishna'}
>>> ## assigning more valuse to keys

>>> a = {"idnos":[10,20,30],"names":["harsha","trinadh","sai"],"marks":[60,70,80]}
>>> a
{'idnos': [10, 20, 30], 'names': ['harsha', 'trinadh', 'sai'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['harsha', 'trinadh', 'sai'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['harsha', 'trinadh', 'sai']), ('marks', [60, 70, 80])])
>>> a.get("names")
['harsha', 'trinadh', 'sai']
>>> a.upate("name")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.upate("name")
AttributeError: 'dict' object has no attribute 'upate'. Did you mean: 'update'?
>>> a.update(names)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.update(names)
NameError: name 'names' is not defined
>>> a.update("names")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.update("names")
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
>>> 
>>> 
>>> 
>>> #from keys
