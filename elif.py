#for elif using comparison operators
# <, >, <=, >=, ==, !=)
'''a = 20
b = 20
if a > b:
    print("a is greater")
elif a == b:
    print("Both are equal")
#less than
a = 10
b = 30
if a > b:
    print("Greater")
elif a < b:
    print("Smaller")

#double equality
a = 50
if a > 50:
    print("Greater than 50")
elif a == 50:
    print("Equal to 50")

#not equal to
a = 25
b = 30
if a >= b:
    print("Greater")
elif a != b:
    print("Not Equal")

#using Logical Operators and, or, not
#for and
a = 10
b = 20
if a > b and b > a:
    print("Condition 1")
elif a < b and b > a:
    print("Condition 2")'''

#not
'''a = 15
b = 20
if not a < b:
    print("Condition 1")
elif not a > b:
    print("Condition 2")
#or
a = 5
b = 10
if a > b or b < a:
    print("Condition 1")
elif a < b or b > a:
    print("Condition 2")
#elif using Identity Operators is, is not
#is 
a = 10
if type(a) is float:
    print("Float")
elif type(a) is int:
    print("Integer")
#is not
a = "Python"
if type(a) is not str:
    print("Not String")
elif type(a) is str:
    print("String")
#multiple elif
a = int(input())
if a > 90:
    print("Grade A")
elif a > 75:
    print("Grade B")
elif a > 50:
    print("Grade C")
elif a > 35:
    print("Grade D")
else:
    print("Fail")'''

#if-elif-else
'''a = 4
b = 6
if a<b:
    print("less")
elif b>a:
    print("greater")'''
'''a ==4
b =6
if a ==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("ok")'''
'''a = 4
b =6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''
'''a = 10
b = 5
if a>b and b<a:
    print("true")
elif a!=b or b!=a:
    print("yes")
elif  not b!=10:
    print("true")
else:
    print("sai")'''
'''a = 10
b = 5
if a<b and b<a:
    print("true")
elif a=b or b!=a:
    print("yes")
elif  not b!=10:
    print("true")
else:
    print("sai")'''
'''a = 10
b = 5
if a>=b and b<a:
    print("true")
elif a==b or b==a:
    print("yes") 
elif  not b!=10:
    print("true")
else:
    print("sai")'''
'''a = 10
b = 5
if a<=b and b<=a:
    print("true")
elif a==b or b==a:
    print("yes")
elif  not b==5:
    print("rue")
else:
    print("sai")'''
'''a = 10
b = 5
if a<b and b<a:
    print("true")
elif a==b or b==a:
    print("yes")
elif  not b<a:
    print("True")
else:
    print("sai")'''

#identify
'''a =5
if type(a) is int:
    print("int")
elif type(a) is not int:
    print("not int")'''

'''a =6.5
if type(a) is int:
    print("int")
elif type(a) is not int:
    print("not int")'''
#membership
'''a = 10
b = [10,20,30]
if a in b:
    print("Yes")
else:
    print("No")'''
'''a = 20
b = 60
c =50
d = [10,20,30,40,50]
if a not in d:
    print("yes1")
elif b in d:
    print("yes2")
elif c in d:
    print("yes3")
else:
    print("no")'''

#multiple if conditions
'''a = 20
b = 40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")

a = 20
b = 40
if a==b:
     print("less")
elif a<b:
    print("less than")
else:
    print("correct")'''

#logical operators
'''a = 10
b = 20
if a<b and b>a:
    print("true")
if a>b or b>a:
    print("true")
if  not a ==b:
    print("true")'''

#identity operators
'''a = 10
b = 20
c = 10
if a is c:
    print("s")
if a is not b:
          print("s1")'''
#membership operators
'''a = ["sai","k","krishna"]
b = "sai"
c ="k"
d = "s"
if b in a:
    print("yes")
if d not in a :
    print("yes")
else:
    print("correct")'''
# nested if conditions
'''a = 4
b =9
if a<b:
    print("less")
    if b>a:
        print("greater")'''
'''a = 4
b = 9
if a>b:
    print("less")
    if b>a:
        print("greater")'''
'''a = 40
b =50
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''
'''a = 10
b = 20
if a!=b:
    print("true")
    if a<b:
        print("true")
    else:
            print("s")'''
'''a = 10
b =20
if a==b:
    print("true")
    if a>b:
        print("true")
    else:
            print("s")
else:
    print("correct")'''
'''
a =[1,2,3,4,5,6]
b,c = 3,4
d = 10
if b in a:
    print("yes1")
    if c in a:
        print("yes2")
    if d not in a:
        print("yes")
else:
    print("no")'''
'''a = int(input())
b = int(input())
if a!=b:
    print("true")
    if a >b:
        print("greater than")
    if b>a:
        print("yes")
    else:
        print("false")
else:
    print("program")'''




