'''x = 32
def add():
    x = 1
    y = 3
    global z
    z = x+y
    print(x)
    print("sum is:",z)
add()
print(x,z)'''
#Positional argument
'''def cal(a,b,c):
    d= a+b+c
    print(d)
cal(5,6,7)
cal(5,6)
cal()'''

#keyword argument
'''
def cal(a,b,c):
    d= a+b+c
    print(d)
cal(a=5,b=6,c=7)
cal(b=3,a=1,c=9)
cal(x=1,y=2,z=3)'''
#default argument
'''
def cal(a=0,b=0,c=0):
    d = a+b+c
    print(d)
cal()
cal(5)
cal(5,6)
cal(5,6,7)
cal(4,b=3)'''
#variable length argument
'''
def cal(*x):
    s = sum(x)
    print(s)
cal(5,6,7)
cal(5,6)'''
'''
def prints(*x):
    print(x)
prints(5,5,3,2,1)
prints(2,1)
prints(5,5,3,2,1,4,1)
prints(1)
prints()
'''

'''def details(name,age,sal,*address):
    print(name)
    print(age)
    print(sal)
    print(address)
details("Ram",36,45000,"Delhi","Chennai","Pune")'''
#Arbitrary keyword arguments
def person(**details):
    print(details)
person(name = "Ram",age=45,sal=45000)



























