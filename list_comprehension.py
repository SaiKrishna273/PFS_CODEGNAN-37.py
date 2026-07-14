#list comprehension
a =["codegnan","python","course"]
#["COURSE","PYTHON","COURSE"]
#print(a.upper())

'''b = str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

'''b =[]
for i in a:
    b.append(i.uuper())
print(b)'''


#syntax
#a=[expression for variable in collection/range]

'''a = [i.upper() for i in a]
print(a)'''
# tasks-   title
'''a = ["vja","hyd","vzg"]

a = [i.title() for i in a]
print(a)'''

#task-2
'''a = [1,2,3,4,5,6,8,12,13]
a = [i**2 for i in a]
print(a)
a = [1,2,3,4,5,6,8,12,13]
a = [pow(i,2) for i in a]
print(a)'''



#task -3
'''a = [i for i in range(16)]
print(a)'''

#if - usage in list comprehension
'''a = [i for i in range(16) if i %2 ==0]
print(a)'''

'''a = [i for i in range(16) if i%2!=0]
print(a)'''


#task  -4
#printing even numbers squares in range of 21
'''a = [i**2 for i in range(21) if i %2 ==0]
print(a)'''

#task - 5

'''a =["apple","banana","grapes","mango","kiwi","dragon","berry"]
b = [a for a in a if "a" in a ]
print(b)'''


'''a =["apple","banana","grapes","mango","kiwi","dragon","berry"]
b = [a for a in a if "a" not in a ]
print(b)'''

#no elif usage in list comprehesion

'''a = [i**2 if i % 2 == 0  else i*5 for i in range(31)]
print(a)'''

#task -6
a = [1,2,3,4,5]
b = [5,4,3,2,1]
#[6,6,6,6,6]
'''v = [a[i]+b[i] for i in range(len(a))]
print(v)'''

'''v = [a[i]+b[i] for i in range(5)]
print(v)'''





