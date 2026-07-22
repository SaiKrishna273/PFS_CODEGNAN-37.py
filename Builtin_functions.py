#built-in functions
#print(dir())

#print(dir("__builtins__"))
'''['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''
#fromkeys()
'''a = "codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))
b = dict.fromkeys(a)
print(b)

c = dict.fromkeys(a,"sai")
print(c)

c["d"] = "python"
print(c)'''

#eval()----> It can ascept all the datatypes on input()
'''while True:
    a=int(input("Enter the a value:"))
    b=int(input("enter the b value:"))
    print(a+b)
while True:
   a=float(input("Enter the a value:"))
   b=float(input("enter the b value:"))
    print(a+b)
while True:
   a=input("Enter the a value:")
   b=input("enter the b value:")
    print(a+b)'''
'''while True:
   a=eval(input("Enter the a value:"))
   b=eval(input("enter the b value:"))
   print(a+b)'''

#zip() -> we can combine multiple collections into one collection
'''a=[10,20,30,40,50,60]
names=["khushal","manoj","harsha","sumanth","gopi"]
print(a+names)

b = zip(a,names)
print(b)

c = list(zip(a,names))
print(c)

c =tuple(zip(a,names))
print(c)

c =dict(zip(a,names))
print(c)

output
[10, 20, 30, 40, 50, 60, 'khushal', 'manoj', 'harsha', 'sumanth', 'gopi']
<zip object at 0x000001F1AE18BF40>
[(10, 'khushal'), (20, 'manoj'), (30, 'harsha'), (40, 'sumanth'), (50, 'gopi')]
((10, 'khushal'), (20, 'manoj'), (30, 'harsha'), (40, 'sumanth'), (50, 'gopi'))
{10: 'khushal', 20: 'manoj', 30: 'harsha', 40: 'sumanth', 50: 'gopi'}'''

#enumerate()-> we can give counter to the collection

'''names=["sai","nikitha","krishna","prabhas","jessi"]
for i in range(len(names)):
    print(i)

b = list(enumerate(names))
print(b)
b = list(enumerate(names,10))
print(b)
b = dict(enumerate(names,100))
print(b)

output

0
1
2
3
4
[(0, 'sai'), (1, 'nikitha'), (2, 'krishna'), (3, 'prabhas'), (4, 'jessi')]
[(10, 'sai'), (11, 'nikitha'), (12, 'krishna'), (13, 'prabhas'), (14, 'jessi')]
{100: 'sai', 101: 'nikitha', 102: 'krishna', 103: 'prabhas', 104: 'jessi'}'''

#ASCII ->American standard coded information interchange
#chr()
#ord()
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z"))
print(ord("y"))'''

#to print() all  alphabets
'''for i in range(97,123):
    print(chr(i),end=" ")
output
a b c d e f g h i j k l m n o p q r s t u v w x y z '''
    
'''for i in range(65,91):
    print(chr(i),end=" ")
output
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '''

'''for i in range(97,123):
    print(chr(i),end=" ")
for i in range(65,91):
    print(chr(i),end=" ")'''

'''name = input()
for char in name:
    print(char,"-",ord(char),end=",")
output
saikrishna
s - 115,a - 97,i - 105,k - 107,r - 114,i - 105,s - 115,h - 104,n - 110,a - 97,'''

#BMI weight calcuator
'''W = eval(input())
H = eval(input())
Cal = W/H**2
if Cal <=18.5:
    print("under weight")
elif 18.5<=Cal<=24.5:
    print("Healthy weight")
elif 24.5 <= Cal<=29.5:
    print("overweight")
elif cal>30:
    print("obesity")
else:
    print("Invalid")'''

'''x = input().split()
for i in range(len(x)):
    print(x[i][::-1],end=" ")'''
'''a = input().split()
for i in a:
    print("".join(reverse(i),end="")'''

'''N = input()
v = "aeiouAEIOU"
count,count1=0,0
for i in N:
    if i in v:
        count+=1
    else:
        count1+=1
print(count)
print(count1)'''

'''n=int(input())
for i in range(65,69):
    for j in range(n):
        print(chr(i),end=" ")
    print()'''
  
'''n=int(input())   
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-1-j),end=" ")
    print()'''
    
'''n=int(input())
for i in range(n):
    for j in range(n-1):
        print(chr(65+n-1),end=" ")'''

'''n = int(input())

for i in range(n):
    for j in range(i+1):
        print(chr(65 + j), end=" ")
    print()'''
'''output
4
A 
A B 
A B C 
A B C D '''

'''output
A B C D
A B C
A B
A'''

'''n = int(input())
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()'''

'''n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(68-i),end=" ")
    print()'''

'''output
D
D C
D C B
D C B A'''
'''output
A
B B
C C C
D D D D'''

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()


