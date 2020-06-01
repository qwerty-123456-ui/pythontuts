# # lambda expression(anonymous function)
# def add(a,b):
#     return a+b

# add2=lambda a,b : a+b #no need to assign
# print(add2(2,3))
# # used with built in functions--map,reduce,filter
# mul=lambda m,n :m*n
# print(mul(3,4))

# def is_even(n):
#     return n%2==0
# print(is_even(8))
# is_even2=lambda a:a%2==0
# print(is_even2(8))

# def last_char(s):
#     return s[-1]
# last_char2=lambda a:a[-1]
# print(last_char("isha"))
# print(last_char2("isha"))

# # lambda with if-else
# def f(s):
#     if len(s)>5:
#         return True
#     return False
# f2=lambda s: True if len(s)>5 else False
# print(f2("isha"))

def f(s):
    return len(s)>5
f2=lambda s:len(s)>5
print(f2("isha"))
