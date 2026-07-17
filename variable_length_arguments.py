#Variable -length arguments
#---> varaibl lengths are automatically stored in tuple and we use star arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"sai","age":21,"place":"BVRM"}
check(*d)'''


#task
'''def check1(*a):
    d=1 #creating a varible
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"sai")'''

#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''


#difference both * and ** usage

'''def final(*a,**b):
    d=1
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d +=1
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,2.3,4.5,2.6)
final(*data)
details={"year":[2024,2025,2026],
         "month":["nov","dec","jan"]}
final(**details)
final(*data,**details)'''

#Mini project

'''raiway ticket
it has to  give inputs like
tickect -1000


gender - male,female

male divided into two >60 flat 30,<60 no discount
female  divided into two >60 flat 500 ,<60 flat 700'''

def railway_ticket(gender, age):
    ticket_price = 1000

    if gender.lower() == "male":
        if age > 60:
            discount = 30
            final_price = ticket_price - (ticket_price * discount / 100)
        else:
            final_price = ticket_price

    elif gender.lower() == "female":
        if age > 60:
            final_price = ticket_price - 500
        else:
            final_price = ticket_price - 700

    else:
        print("Invalid Gender")
        return

    print("Final Ticket Price:", final_price)


while True:
    gender = input("Enter Gender : ")
    age = int(input("Enter Age: "))

    railway_ticket(gender, age)

    
    
        
    


