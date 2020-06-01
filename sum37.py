from functools import wraps
import time
# # first class function/closures
# # decorators
# def sq(a):
#     return a**2
# s=sq(7)
# print(s)
# s=sq
# print(s(7))
# print(s.__name__)
# print(sq.__name__)
# print(s)
# print(sq)

# l=[1,2,3,4]
# def sq(a):
#     return a**2
# print(map(sq,l))
# print(list(map(sq,l)))
#
# def my_map(func,l):
#     new_list=[]
#     for item in l:
#         new_list.append(func(item))
#     return new_list
# print(my_map(sq,l))
# print(my_map(lambda a:a**3,l))
#
# def my_map2(func,l):
#     new_list=[func(item) for item in l]
# print(my_map(sq,l))
# print(my_map(lambda a:a**3,l))


# # fn returning fn
# def outerf():
#     def innerf():
#         print("hello")
#     return innerf
# var=outerf()
# print(var)
# var()
# def outerf():
#     def innerf():
#         print("hello")
#     return innerf()
# var=outerf()


# def outerf2(msg):
#     def innerf2():
#         print(f"message is {msg}")
#     return innerf2
# var=outerf2("i m isha ")
# var()


# function returning function (closure)
# def to_power(p):
#     def cal_power(n):
#         return n**p
#     return cal_power
# cube=to_power(3)
# cube(5)
# to_power(4)(2)
# "hi"
# print(to_power(3)(5))


# decorators---enhance the functionality of other functions

# def decorator_fn(anyf):
#     def wrapper_fn():
#         print('this is awesome function')
#         anyf()
#     return wrapper_fn
#
# def f1():
#     print("this is function 1")
# def f2():
#     print("this is function 2")
#
# var1=decorator_fn(f1)()
# var2=decorator_fn(f2)()

# f1=decorator_fn(f1)
# f1()

# @decorator_fn
# def f3():
#     print("this is function 3")
# f3()
# # shorthand not working with hydrogen


# # @ for decorator
# def decorator_fn(anyf):
#     @wraps(anyf)
#     def wrapper_fn(*args,**kwargs):
#         '''this is wrapper function'''
#         print('this is awesome function')
#         return anyf(*args,**kwargs)
#     return wrapper_fn
#
# @decorator_fn
# def f(a):
#     print(f'this is function {a}')
# f(7)
#
# @decorator_fn
# def add(a,b):
#     '''this is add function'''
#     return a+b
# print(add(2,3))
# print(add.__doc__)
# print(add.__name__)

# def print_fn_data(anyf):
#     # @wraps(anyf)
#     def wrapper_fn(*args,**kwargs):
#         print('you r calling',anyf.__name__,'function')
#         print(anyf.__doc__)
#         return anyf(*args,**kwargs)
#     return wrapper_fn
#
# @print_fn_data
# def add(a,b):
#     '''this fn takes two args and return their sum'''
#     return a+b
# print(add(5,8))


# # ex1
# # time.time()
# def cal_time(anyf):
#     @wraps(anyf)
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         v=anyf(*args,**kwargs)
#         t2=time.time()
#         print(f"function took {t2-t1} time")
#         return v
#     return wrapper
# @cal_time
# def f(n):
#     return [i**2 for i in range(1,n+100)]
# print(f(10000))



# def only_int(f):
#     @wraps(f)
#     def wrapper(*args,**kwargs):
#         if all([type(i)==int for i in args]):
#             return f(*args,**kwargs)
#         else:
#             print("all arguments should be int")
#     return wrapper
#
# @only_int
# def add_all(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
#
# add_all(9,9,8,0,[9,0])

# 
# # decorator with arguments
# def only_type(dtype):
#     def deco(f):
#         @wraps(f)
#         def wrapper(*args,**kwargs):
#             if all([type(i)==dtype for i in args]):
#                 return f(*args,**kwargs)
#             else:
#                 print("all arguments should be int")
#         return wrapper
#     return deco
#
# @only_type(str)
# def str_join(*args):
#     string=''
#     for i in args:
#         string+=i
#     return string
#
# print(str_join('isha','gupta',9))
