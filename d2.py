print("The intEger number is: {}".format(123))
print("The intEger number is: {:d}".format(123))
print("The intEger number is: {:5d}".format(123))
print("The intEger number is: {:08d}".format(123))
print("The float number is: {:8.3f}".format(123.4567))
print("The float number is: {:08.3f}".format(123.4567))
print("The float number is: {:08.3f}".format(123.45))
print("The float number is: {:08.3f}".format(786786123.45))
print("int value with sign:{}".format(123))
print("int value with sign:{}".format(-123))
print("float value with sign:{:+f}".format(123.456))
print("float value with sign:{}".format(-123.456))
print("{:>3d}".format(12)) 
import datetime
#datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))
n=[1,2,3,4,5]
n.insert(100,777)
n.insert(-100,999)
print(n.index(999))  
s="honey"
l=[]
for x in s:
    l+=x
print(l)
l.sort()
print(l)
l1=[chr(48)]
for x in l1:
    print(ord(x))
x,a,b=[50,20,30]
y=[50,50,60,100,200]
#print(x>y)
t=10,
print(type(t))
print(x)
print(a)
print(b)
s='senorita'
l=list(s)
print(l)
t=()
print(type(t))
t=10,20,30,40
print(type(t))
t=10
print(type(t))
t=10,
print(type(t))
t=(10)
print(type(t))
t=(10,)
print(type(t))
t=(10,20,30,40)
print(type(t))
a,b,c=9,8,7
print(type(a))
s={90,67,80}
s=set(sorted((89,547,44)))
print(s)