#Annonymous ---> annonymous functions are nameless functions and we use a keyword  called as lambda to create annonymous function. 

#write a function to calculate 2*x+5
'''def mul():
    x = int(input())
    a = 2*x+5
    print(a)
mul()


def mul(x):
    a = 2*x +5
    print(a)
mul(5)'''


#Syntax
#a=lambda arg:expr
'''a =int(input())
b = lambda x:2*x+5
print(b(a))'''
#multiply
'''a= int(input())
b = int(input())
c = lambda a,b:a*b
print(c(a,b))'''

'''a = lambda x,y:x*y
print(a(5,5))'''

#Task
'''a =input()
b =lambda a:a.upper()
print(b(a))'''

'''a = lambda a:a.upper()
print(a("codegnan"))'''


#task

'''a ="python course"
b = lambda a:a.title()
print(b(a))'''
'''a = input()
b = lambda a:a.title()
print(b(a))'''


#task
'''fn = input()
ln = input()
fname = lambda fn,ln:(fn+" "+ln).title()
print(fname(fn,ln))'''

'''a,b =[x for x in input("enter the name").split(",")]
c = lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#Filter()
'''a=[10,30,50,100,127,39,45,67,200]
for i in a:
    if i % 2==0:
        print(i,"even values")
    elif i %2 !=0:
        print(i,"odd values")'''

#Filter()
'''a=[10,30,50,100,127,39,45,67,200]
b = list(filter(lambda i:i%2==0,a))
print(b)'''

a =[[],set(),{},"",None,5,9.0,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)






