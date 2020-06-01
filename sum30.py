# # tuple--data str. but immutable--no append,no insert,no pop,no remove--once data created data can't be changed
# e=('one','two','three')
# d=('mon','tues')
# # tuples r faster than list
# # methods
# # count
# # index
# # len
# # slicing
# print(e[:2])


# # looping
# n=(1,2,3,4.0)
# for i in n:
#     print(i)


# # tuple with one element
# n=(10,)
# print(type(n))


# # tuple without paranthesis
# g='e','f','d'
# print(type(g))


# # tuple unpacking
# g='a','b','c'
# g1,g2,g3=g
# print(g1,g2,g3)


# # list inside tuple
# f=(1,2,[3,4,5])
# f[2].pop()
# f[2].append(8)
# print(f)


# # fns. min(),max(),sum
# n=[1,2,3]
# print(min(n))
# print(max(n))
# print(sum(n))

# # returning 2 values from a function
# def func(i1,i2):
#     add=i1+i2
#     mul=i1*i2
#     return add,mul
# a,m=(func(2,3))
# print(a,m)


# n=tuple(range(1,11))
# print(n)
# n1=list(n)
# print(n)
# n2=str(n)
# print(n2)
# print(type(n2))
# n3=str(n1)
# print(n3)
# print(type(n3))
