# f=['o','a','ap','ba','ki','a','ba']
# print(f.count('a'))
# # f.sort()
# print(f)
# print(sorted(f))
# print(f)
# # f.clear()
# # print(f)
# f_copy=f.copy()
# print(f_copy)

# list comparison
# f1=[1,1,1,1]
# f2=[1,1,1,1]
# f3=[2,2,2,2]
# print(f1 is f2)
# print(f1 == f2)
# print(f1 is f3)
# print(f1 == f3)


# # split(str to list) and join
# u='isha gupta'.split(',')
# print(u)
# u,a='isha,20'.split(',')
# print(u,a)
# u=['isha','20']
# print(','.join(u))

# list vs array
# list --store any data/flexible
# array -- homogeneous data type
# python array module--fix data type
# js array==python list
# numpy array==binding c


# #strings--immutable
# #list--immutable
# s='isha'
# t=s.title()
# print(s,t)
#
# l=['w1','w2','w3']
# l.pop()
# print(l)
# l.append('w3')
# print(l)

# #for loops
# f=['a','b','c']
# for fr in f:
#     print(fr)
# i=0
# print(f)
# while (i<len(f)):
#     print(f[i])
#     i+=1


#list inside list---2d list
# m=[[1,2,3],[4,5,6],[7,8,9]]
# # print(m[2])
# # for i in m:
# #     for j in i:
# #         print(j)
# print(type(m))

# list using range
l=list(range(1,11))+[1,8,9,9,1]
# print(l)
# print(l.pop())
# print(l)
# index method
# print(l.index(1,11,14))

# pass list to a function
# def neg_list(l):
#     l1=[]
#     for x in l:
#         l1.append(-x)
#     return l1
#
# print(neg_list(list(range(-9,10))))


# # exercise 1
# def sq(l):
#     l1=[]
#     for x in l:
#         l1.append(x*x)
#     return l1
#
# print(sq([1,2,3,4]))


# # exercise 2 reverse list
# def rev(l):
#     l1=[]
#     for x in range(len(l)):
#         l1.append(l.pop())
#     return l1
# print(rev(['w1','w2','w3']))


# #ex 3
# def strrev(l):
#     l1=[]
#     for x in l:
#             l1.append(x[::-1])
#     return l1
# print(strrev(['abc','bac','cab']))

#
# # ex 4 evoddlist
# def evoddlist(l):
#     e=[]
#     o=[]
#     for x in l:
#         if x%2==0:
#             e.append(x)
#         else:
#             o.append(x)
#         # print(e,o)
#     return [e,o]
# print(evoddlist([1,2,3,4,5,6,7,8,9,10]))


# # ex 5
# def lcommom(l1,l2):
#     l3=[]
#     for x in l1:
#         if x in l2:
#         # for y in l2:
#         #     if x==y:
#             l3.append(x)
#     return l3
# print(lcommom([1,2,3,4,5],[1,2,3]))

#
# # min and max fns.
# n=[6,60,2]
# print(max(n))
# print(min(n))
# def greatest_diff(n):
#     return max(n)-min(n)
# print(greatest_diff(n))


# ex 6
def no_of_list(l):
    c=0
    for x in l:
        # print(type(x))
        if type(x)==list:
            c+=1
    return c
print('no of lists inside list is ',no_of_list([[1,1],1,2,[1,2,3],[6,7]]))
