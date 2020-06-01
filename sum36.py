# # enumerate function
# # for loop---to track index/position of item in iterable
# # without enumerate
# n=['abc','abcdef','isha']
# pos=0
# for i in n:
#     print(f"{pos}--->{i}")
#     pos+=1
# # with enumerate
# for pos,i in enumerate(n):
#     print(f"{pos}--->{i}")


# # ex1
# def strs(l,s):
#     for pos,i in enumerate(l):
#         if i==s:
#             return pos
#     return -1
# r=strs(['abc','abcdef','isha'],'hisha')
# if r !=-1:
#     print("string at position",r+1)
# else:
#     print("string not found")

#
#
# # map function
# n=[1,2,3,4]
# # def sq(a):
# #     return a**2
# # s=list(map(sq,n))
# # print(s)
# # t=tuple(map(sq,n))
# # print(t)
# ss=list(map(lambda a:a**2,n))
# print(ss)



# n=['abc','abcdef','isha']
# # print(list(map(lambda a:len(a),n)))
# print(list(map(len,n)))
# length=map(len,n)
# for i in length:
#     print(i)
# for i in length:
#     print(i)
# length=list(map(len,n))
# for i in length:
#     print(i)
# for i in length:
#     print(i)

#
#
# # filter function
# # def is_even(a):
# #     return a%2==0
# n=[3,4,5,1,2,6,7,8,9]
# # evens=[]
# # print(filter(is_even,n))
# # print(tuple(filter(is_even,n)))
# print(tuple(filter(lambda a:a%2==0,n)))
# evens=tuple(filter(lambda a:a%2==0,n))
# print(evens)
# for i in evens:
#     print(i)
# # map and filter function can be iterated once but tuple and list can iterated n number of times


# iterator vs iterable
# tuple,list,string --->iterables
# map,filter ---->iterator
"""for loop working
step 1: calls iter function
step 2:iter(n)--->now it acts like iterator
step 3:next(iter(n))
"""
# n=[1,2,3,4]
# n_iter=iter(n)
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))
# print(next(n_iter))

# n=[1,2,3,4]
# s=map(lambda a:a**2,n)
# print(s)

# for i in n:
#     print(i)
# for i in s:
#     print(i)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s)) no error coz map is iterator
# print(next(n)) error coz list is not iterator




# zip function---------->iterator----------------->to iterable using list(),tuple()
# u=['u1','u2','u3']
# n=['n1','n2','n3']
# l=['l1','l2','l3']
# print(zip(u,n,l))
# print(list(zip(u,n,l)))
# print(dict(list(zip(u,n,l)))) error
# u=['u1','u2']
# n=['n1','n2','n3']
# print(zip(u,n))
# print(list(zip(u,n)))
# a=list(zip(u,n))
# print(dict(a))


# # zip(*xxxx)
# l=[(1,2),(3,4),(5,6)]
# l1,l2=zip(*l)
# print(l1,l2)
# print(list(l1),list(l2))

# l1=[1,3,6]
# l2=[8,4,2]
# nl=[]
# for pair in zip(l1,l2):
#     nl.append(max(pair))
# print(nl)


# # ex1
# # def average(*args):
# #     l3=[]
# #     for pair in zip(*args):
# #         # l3.append((pair[0]+pair[1])/2)
# #         l3.append(sum(pair)/len(pair))
# #     return l3
# # print(average([1,2,3],[4,5,6],[7,8,9]))
# avg=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(avg([1,2,3],[4,5,6],[7,8,9]))



# # any,all function
# n1=[2,4,6,8,10]
# n2=[1,3,5]
# # e1=list(map(lambda a:a%2==0,n1))
# # print(e1)
# # print(all(e1))
# # print(all([True, False, True, True, True]))
# print(all([num%2==0 for num in n1]))
# print(all([num%2==0 for num in n2]))
# print(any([num%2==0 for num in n1]))
# print(any([num%2==0 for num in n2]))


# def my_sum(*args):
#     e=all([(type(arg)==int or type(arg)==float) for arg in args])
#     total=0
#     print(e)
#     if e:
#         for num in args:
#             total+=num
#     return total
# print(my_sum(1,2,3,4,8.9))#,'harshit',['harshit']


# advance max and min function
# def func(i):
#     return len(i)
# s=['abc','isha','ab']
# # print(max(s,key=func))
# # print(min(s,key=func))
# print(max(s,key=lambda a:len(a)))
# print(min(s,key=lambda a:len(a)))

# s1=[
# {'n1':'nisha','score':70,'age':19},
# {'n1':'risha','score':80,'age':29},
# {'n1':'isha','score':90,'age':20}]
# print(max(s1,key=lambda item:item.get('score')))
# print(max(s1,key=lambda item:item.get('score'))['n1'])
# print(max(s1,key=lambda item:item.get('age'))['n1'])


# s2={
#      'harsh':{'score':70,'age':20},
#      'harshit':{'score':90,'age':21},
#      'harshi':{'score':60,'age':22}
# }
# print(max(s2,key=lambda i:s2.get(i)['score']))


# # sort()  only for list not for tuple
# # sorted() for tuple  and set-->returns sorted list
# f1=['b','r','c']
# f2=('b','r','c')
# f1.sort()
# print(f1)
# print(sorted(f2))
# print(f2)
# f3={'b','r','c'}
# print(sorted(f3))
# print(f3)


# g=[
#     {'n':'a','price':1000},
#     {'n':'ab','price':900},
#     {'n':'abc','price':300},
#     {'n':'abcd','price':500}
# ]
# print(sorted(g,key=lambda a:a.get('price'),reverse=True))



# doc strings
def add(a,b):
    '''fn takes 2 args and return sum'''
    return a+b
print(add.__doc__)
# len,sum,min,max,sorted
print(len.__doc__)
print(sum.__doc__)
print(help(sum))
