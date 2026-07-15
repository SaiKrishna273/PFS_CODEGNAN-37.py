#functions

#A fuction is a block organisdd,reusuable code and  that is used to perform a single or multiple task
#Python gives inbuilt function like print. you can make your own function also these are called user defined functions
#pyhton block begin with the keyword "def" followed by the function name and parenthesis (())
'''a = 10
b = 20
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product is ",a*b)

a =100
b =200
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product is ",a*b)

a= 1000
b = 2000
print("the sum is ",a+b)
print("the diff is ", a-b)
print("the product is ",a*b)'''

'''def calculate(a,b):
    print("the sum is ",a+b)
    print("the diff is ", a-b)
    print("the product is ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the integer div is ",a//b)
    print("the power is ", a**b)
    print("the modulo is ",a%b)
calculate(10,20)
calculate(100,200)
calculate(1,3)'''

#recursive function
'''def add(a,b):
    print(a+b)
add(4,5)

while True:
    def cal():
        a = int(input("a value"))
        b = int(input("b value"))
        print(a+b)
    cal()'''

'''def cal():
    a = int(input("a value"))
    b = int(input("b value"))
    print(a+b)
    cal()
cal()'''

'''def fullname():
    fname = input("first name")
    lname = input("last name")
    print((fname +" "+lname).title())
fullname()'''


#Difference between print and return

# print - print just shows the human user input in a console
#return - return will terminate the function and gives back a value from the function


'''def mul(a,b):
    print(a*b)
mul(3,5)

def mul(a,b):
    return a*b
print(mul(2/3))'''

#print v/s return

'''def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)
add(10,20)'''

'''def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    return c
    return d
    return e
print(add(10,20))'''

''' def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    return c,d,e
print(add(6,8))'''

'''#splitbill()
def splitbill():
    a = int(input("enter the bill a"))
    b = int(input("enter the persons"))
    print(a//b)
splitbill()

#f sting
def split():
    a = int(input("enter the ammount"))
    b = int(input("enter the count"))
    c = a//b
    print(f"split amount is {c}")
splitbill()

#.format
def split():
    a = int(input("enter the ammount"))
    b = int(input("enter the count"))
    c =b//a
    print("amount is {}".format(c))
splitbill()'''


#add, sub, multi
'''def taking():
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    option = int(input(('''click the option:
                                           1.add
                                           2.sub
                                           3.product:''')))
    if option == 1:
        print(a+b)
    elif option == 2:
        print(a-b)
    elif option ==3:
        print(a*b)
taking()'''


