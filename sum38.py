import time
# generators
# generators are iterators

# iterator nd iterable
# l=[1,2,3] #iterable
# map(lambda a:a**2,l)#iterator
# for n in map(lambda a:a**2,l):
#     print(n)

# generators are iterators------->sequence
# one time one number generated---<memory usage and performance increases>--->
# if sequence used once--<generator>
# if sequence used n no. of times---<list>

# first generator creation
# 1)generator function
# 2)or Generator comprehension

# def nums(n):
#     for i in range(1,n+1):
#         print(i,end="")
# nums(10)

# for generator
# def nums(n):
#     for i in range(1,n+1):
#         yield i
# print(nums(10))
# for n in nums(10):
#     print(n,end="")
# num=nums(10)
# for n in num:
#     print(n,end=" ")
# for n in num:
#     print(n,end=" ")
# l=list(nums(10))
# for n in l:
#     print(n,end=" ")
# for n in l:
#     print(n,end=" ")



# # ex1
# def gen_even(n):
#     for i in range(2,n+1,2):
#         yield i
# for i in gen_even(8):
#     print(i,end=" ")
# for i in gen_even(9):
#     print(i,end=" ")



# # generator comprehension
# sq=(i**2 for i in range(0,9))
# print(sq)
# print(next(sq))
# print(next(sq))
# for n in sq:
#     print(n,end=" ")
# for n in sq:
#     print(n,end="")

# t1=time.time()
# l=[i**2 for i in range(100000000)]
# t2=time.time()
# print(t2-t1)
# t1=time.time()
# g=(i**2 for i in range(100000000))
# t2=time.time()
# print(t2-t1)
