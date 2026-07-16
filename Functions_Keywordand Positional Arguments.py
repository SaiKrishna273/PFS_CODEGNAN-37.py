#arguments --------
#first argement is keyword and positional arguments
'''def Details(id,name,mailid):
    id =10
    name="sai"
    mailid="saikishnagudla556@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="sai@gmail.com")
Details(id=20,name="manoj",mailid="m@gmail.com")
Details(id=30,name="harsha",mailid="h@gmail.com")
Details(40,"trinadh","t@gmail.com")
Details("sai@gmail.com",50,"sai")
Details(mailid="m@gmail.com",id=60,name="gopi")'''

#Program 1: The values passed to the function are ignored because they are overwritten inside the function before printing.
#Program 2: The function prints exactly the values it receives.
#Positional arguments are matched based on their position.
#Keyword arguments are matched by parameter name, so their order does not matter.
#Python does not enforce that id must be a number or mailid must be an email; it simply stores and prints the values you pass.


#----->default arguments

'''def Grocery(items,price):
    print("item is %s" %items)
    print("price id %.2f" %price)
Grocery("sugar",100)


def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()

def Grocery(item,price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    print("item is &s",%item)
    print("price is %.2f",%price)
Grocery(100)'''


#Task----
#cake_name,price,qty
'''def Grocery(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
Grocery("redvelvet",1200,1)'''


'''def Bakery(cake_name,price = 1200,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
Bakery()'''

'''def Bakery(cake_name,price = 1200,qty=1):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
Bakery("redvelvet")'''

'''def Bakery(cake_name ="redvelvet",price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %.2f" %qty)
Bakery(1200,1)'''

#* arguments(* is used to unpack the elements)

'''a =[2,3,4,5,6,7]
print(a)
print(*a)

a = (2,3,4,5,6,7)
print(a)
print(*a)

a ={2,3,4,5,6,7}
print(a)
print(*a)

b = {"name": "sai","city":"bhimavaram"}
print(b)
print(*b)
#for dictionaries it wil print only keys

c ="python"
print(c)
print(*c)

a,b,c = 2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c) #error

a,b,c = 2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c =2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)

a,b,c ="codegnan"
print(a)
print(b)
print(c) #error

a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c = "codegnan"
print(a)
print(b)
print(*c)'''





