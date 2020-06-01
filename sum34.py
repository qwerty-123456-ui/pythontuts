# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:19:55 2020

@author: Isha Gupta
"""


# #make flexible function
# # *operator
# # *args--input->tuple--->args=tuple
# def total(a,b):
#     return a+b
# def all_total(*args):
#     print(args)
#     print(type(args))
#     total=0
#     for n in args:
#         total+=n
#     return total
# print(total(3,4))
# print(all_total(3,4,10,8,7))


# # *args with normal parameter
# def mul(a,*args):
#     m=1*a
#     for i in args:
#         m*=i
#     return m
# print(mul(9,8,1))
# print(mul([9,8,1]))
# print(mul(*[9,8,1])) #*list unpacking
# print(mul((9,8,1)))
# print(mul(*(9,8,1))) #*tuple unpacking


# # ex 1
# def power_list(n,*args):
#     # if args==None:
#     if not (args):
#     # if not len(args):
#         return "u didn't pass any argument"
#     else:
#         l=[i**n for i in args]
#         return l
# print(power_list(3,*[1,2,3]))


# # **kwargs-->keyword arguments
# # **-->double star operator
# # dict <--input
# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# fun(n='isha',l='gupta')
# d={'n':'isha','age':20}
# fun(**d)


#
# # all parameters--->normal,default,args,kwargs
# def fun(n='unknown',a=20):
#     print(n)
#     print(a)
# fun('isha')
# # correct order--->normal,*args,default,**kwargs----------->padk-->parameter,args,default parameter,kwargs
# def func(n,*args,ln="unknown",**kwargs):
#     print(n)
#     print(args)
#     print(ln)
#     print(kwargs)
# func("isha",1,2,3,a=0,b=1)
#
# def func2(n,ln="unknown"):
#     print(n)
#     print(ln)
# func2("isha")




# # ex1
# def str_fir_cap_rev(l,**kwargs):
#     # print(kwargs.values())
#     if kwargs.get('reverse_str')==True:
#         # print(kwargs)
#         return [i[::-1].title() for i in l]
#     else:
#         return [i.title() for i in l]
# l=["isha","keras"]
# print(str_fir_cap_rev(l))
# print(str_fir_cap_rev(l,reverse_str=True))
