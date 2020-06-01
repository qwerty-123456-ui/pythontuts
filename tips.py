from getpass import getpass
# tips and tricks

# 1
i=2 if True else False
print(i)

# 2
n1=1_00_000_000
n2=90_000
print(n1+n2)
print(f"{(n1+n2):,}")

# 3
with open('t1.txt','w') as f:
    f.write('hello')
with open('t1.txt','r') as f:
    print(f.read())

# 4
n=[1,2,3]
for i,nu in enumerate(n):
    print(i,nu)
for i,nu in enumerate(n,start=1):
    print(i,nu)


# 5
n=['n1','n2','n3']
h=['h1','h2','h3']
for na,he in zip(n,h):
    print(f"{na} is actually {he}")



# 6
a,_=(9,8)
print(a)
print(_) # to show not to be used
a,b,*c,d=(1,2,3,4,5,6,7)
print(a)
print(b)
print(*c)
print(d)
for c1 in c:
    print(c1)
print(type(c))


# 7
class Person():
    """docstring for ."""
    pass

p=Person()
k='first'
v='isha'
# p.first=k
# p.last=v
# print(p.first)
# # print(p.last)
# setattr(p,k,v)
# print(getattr(p,k))

s={'first':'isha','last':'gupta'}
for k,v in s.items():
    setattr(p,k,v)

for n in s.keys():
    print(getattr(p,n))


# 8
u=input("Username : ")
n=getpass("Password : ")
print("logging in....")


# 9
