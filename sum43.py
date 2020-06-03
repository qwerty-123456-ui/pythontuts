# built in errors
# exceptions
# syntax,indentation,name,type,index,value,attribute,key error

# def add(a,b):
#     if (type(a) is int and type(b) is int):
#         return a+b
#     raise TypeError('oops')

# print(add('10',70))


class Animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        raise NotImplementedError('you have to define method in subclass')

class Dog(Animal):
    def __init__(self, name,bread):
        super().__init__(name)
        self.bread=bread
    
    # def sound(self):
        # return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name,bread):
        super().__init__(name)
        self.bread=bread

    # def sound(self):
        # return 'meow meow'

doggy=Dog('chup','raho')
print(doggy.sound())