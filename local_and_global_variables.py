#global and local variables

#----->Definition: A variable inside and outside the function is called global and local variables
#*A varible is defined above the function and is accessible to the to the entire space is called global varible
#*A variable is inside the function is called local variable
#--> First case of global variable
'''a =4
def check1():
    print("inside value is",a)
check1()
print("outside value is ",a)'''

#second case of golbal variables
'''a =2
def check2():
    a =5
    a =a**2
    print("inside value is ",a)
check2()
print("outside value is",a)'''


#third case of both global and local variables
'''a = 6
def check3():
    a =8
    print("inside value is ",a)
    a =10
    print("updated value is ",a+5)
    b = 13 #local variable
    b = b+a
    print("value of b is ",b)
check3()
print("a value is",a)
print("b value is",b)'''#--->it will give error because it doesn't assign in global variable


#Usage of gobal keyword -->when user wants to access the global variable inside the function
#directly and carry forward the updated value even outside the function then we need to use global keyword
#Usage of global keyword
'''a =4
def final():
    global a,b
    print("inside value is",a)
    a =15
    print("updated value is",a)
    #global
    b = 20
    b =b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#--->Attendence Tracker
def attendence_tracker():
    n = int(input())
    c_p = 0
    c_a = 0
    for i in range(1,n+1):
        attendence = input("enter the absentese ")
        if attendence == "p":
            c_p+=1
        elif attendence =="a":
            c_a+=1
        else:
            print("invalid")
print("f present is{count}")
print(f"absent is {temp}")
attendence_tracker()

'''students = int(input("enter the no of students"))
c_p = 0
c_a = 0
for i in range(1,students+1):
    attendance = input("enter the attendence:")
    if attendance =="p":
        c_p+=1
    elif attendance =="a":
        c_a+=1
    else:
        print("invalid")
print(f"the present students is{c_p}")
print(f"the absent students is{c_a}")'''



        
