# # class and object
# class Person:
#     """docstring fo Person."""
#
#     def __init__(self, fn,ln,age):
#         #instance variables
#         self.age = age
#         self.fn=fn
#         self.ln=ln
# p1=Person('isha','gupta',20)
# print(p1)
# print(p1.age)
# print(p1.fn)
# print(p1.ln)


# # ex1
# class Laptop:
#     def __init__(self,b,m,p):
#         self.b=b
#         self.m=m
#         self.p=p
# l1=Laptop("mac","latest",90000000)
# print(l1.b)
# print(l1.m)
# print(l1.p)


# # instance methods
#  class Person:
#     """docstring fo Person."""
#
#     def __init__(self, fn,ln,age):
#         #instance variables
#         self.age = age
#         self.fn=fn
#         self.ln=ln
#     # instance method
#     def full(self):
#         print(f"{self.fn} {self.ln}")
#     def is_above_18(self):
#         return self.age>18
# p1=Person('isha','gupta',20)
# print(p1)
# print(p1.age)
# print(p1.fn)
# print(p1.ln)
# p1.full()
# Person.full(p1)
# Person.is_above_18(p1)
#
# # eg
# l=[1,2]
# list.clear(l)
# # or l.clear()
# print(l)
# list.append(l,10)
# print(l)


# # ex2
# class Laptop:
#     def __init__(self,b,m,p):
#         self.b=b
#         self.m=m
#         self.p=p
#     def applydisc(self,i):
#         return self.p-(i*self.p/100)
# l1=Laptop("apple","macbook pro",90000000)
# print(l1.b)
# print(l1.m)
# print(f"{l1.p:,}")
# print(f"{l1.applydisc(40):,}")
#
# # class variable
# class Laptop:
#     d=40
#     def __init__(self,b,m,p):
#         self.b=b
#         self.m=m
#         self.p=p
#         self.n=b+" "+m
#     def applydisc(self):
#         # return self.p-(Laptop.d*self.p/100)
#         return self.p-(self.d*self.p/100)
# l1=Laptop("apple","macbook pro",90000000)
# print(l1.b)
# print(l1.m)
# print(f"{l1.p:,}")
# print(f"{l1.applydisc():,}")
# Laptop.d=10
# print(l1.b)
# print(l1.m)
# print(f"{l1.p:,}")
# print(f"{l1.applydisc():,}")
# print(l1.__dict__)
# l1.d=50
# print(f"{l1.applydisc():,}")


# # ex3
# class methods
# class P:
#     c = 0
#
#     def __init__(self):
#         P.c += 1
#
#     @classmethod
#     def count(cls):
#         return f"{cls.c} of {cls.__name__} class"
# p1 = P()
# p2 = P()
# p3 = P()
# print(P.c)
# # print(p2.c)



# classmethod as constructor
#  class Person:
#     """docstring fo Person."""
#
#     def __init__(self, fn,ln,age):
#         #instance variables
#         self.age = age
#         self.fn=fn
#         self.ln=ln
#     @classmethod
#     def from_str(cls,string):
#         f,l,a=string.split(',')
#         return cls(f,l,a)
#
#     # instance method
#     def full(self):
#         print(f"{self.fn} {self.ln}")
#     def is_above_18(self):
#         return self.age>18
# p1=Person('isha','gupta',20)
# p2=Person.from_str('isha,gupta,20')
# print(p2)
# print(p2.fn)


# # static method
# class Person:
#     """docstring fo Person."""

#     def __init__(self, fn,ln,age):
#         #instance variables
#         self.age = age
#         self.fn=fn
#         self.ln=ln
#     @classmethod
#     def from_str(cls,string):
#         f,l,a=string.split(',')
#         return cls(f,l,a)

#     # instance method
#     def full(self):
#         print(f"{self.fn} {self.ln}")
#     def is_above_18(self):
#         return self.age>18
#     @staticmethod
#     def hello():
#         print("hello")
# Person.hello()


# encapsulation,abstraction,name mangling
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        # if price>0:
        #     self._price=price
        #     self.__price=price
        # else:
        #     self._price=0'
        # self.complete_specifications=f"{self.brand} {self.model_name} and price {self._price}"

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}....")

    def full_name(self):
        return f"{self.brand}  {self.model_name}"

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price {self._price}"

    #getter(),setter() decorator
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
# _name #convention of private name
# __name__#dunder/magic methods

# l=[3,4,1,2]
# l.sort()
# print(l)

# # name mangling
p1=Phone("n","0",-90)
# print(p1._price)
# print(p1.brand)
# print(p1.model_name)
# print(p1._price)
# print(p1.price)
# # print(p1.complete_specification())
# print(p1.complete_specification)
# # p1._price=-100
# # print(p1._price)
# # print(p1.__dict__)
# # # print(p1.__price)
# # print(p1._Phone__price)
# # p1._Phone__price=-100
# # print(p1._Phone__price)
# # p1._price=-500
# print(p1._price)
# p1.price=90
# print(p1.price)

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_mem,rear_camera):
        # two
        # Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_mem=internal_mem
        self.rear_camera=rear_camera
        # if price>0:
        #     self._price=price
        #     self.__price=price
        # else:
        #     self._price=0'
        # self.complete_specifications=f"{self.brand} {self.model_name} and price {self._price}"
    #
    # def make_a_call(self,phone_number):
    #     print(f"calling {phone_number}....")
    #
    # def full_name(self):
    #     return f"{self.brand}  {self.model_name}"

phone=Phone('nokia','1111',1111)
sp=Smartphone('apple','iphone 11',20000,'2','32','20')
print(phone.full_name())
print(sp.full_name())
