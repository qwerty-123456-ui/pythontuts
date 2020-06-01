# # dictionary
# # unordered collection of data in key:value pair
# u={'n':'i','a':24}
# print(u)
# print(type(u))
# # second method
# u=dict(n='i',a=20)
# print(u)
# print(type(u))
# print(u['n'])
# # no index
# ui={'n':'i',
#     'a':20,
#     'fm':['in','incep'],
#     's':['pe','ka']
# }
# print(ui)
# # empty dictionary
# ui2={}
# ui2['n']='i'
# print(ui2)


# # looping and in key
# ui={'n':'i',
#     'a':20,
#     'fm':['in','incep'],
#     's':['pe','ka']
# }
# if 'n' in ui:
#     print('present')
# if 20 in ui.values():
#     print('present')
# if ['in','incep'] in ui.values():
#     print('present')
# for  i in ui:
#     print(i)
# for  i in ui.values():
#     print(i)
# print(ui.values())
# print(type(ui.values()))
# for  i in ui.keys():
#     print(i)
# print(ui.keys())
# print(type(ui.keys()))
# for i in ui:
#     print(ui[i])
# # items method
# uis=ui.items()
# print(uis)
# print(type(uis))
# for key,value in ui.items():
#     print(f"key is {key} and value is {value}")


# # add and delete
# ui={'n':'i',
#     'a':20,
#     'fm':['in','incep'],
#     's':['pe','ka']}
# ui['fs']=['l','lo']
# print(ui)
# # pop
# # print(ui.pop('fs'))
# print(type(ui.pop('fs')))
# # popitem()
# print(ui.popitem())
# print(type(ui.popitem()))


# # update()
# ui={'n':'i',
#     'a':20,
#     'fm':['in','incep'],
#     's':['pe','ka']
# }
# mi={'s':'h'}
# ui.update(mi)
# print(ui)


# fromkeys
# d={}
# d={'n':'u','a':'u'}
# d=dict.fromkeys(['n','a','h'],'u')
# print(d)
# d=dict.fromkeys(('n','a','h'),'u')
# print(d)
# d=dict.fromkeys("abc",'u')
# print(d)
# d=dict.fromkeys(range(1,11),'u')
# print(d)
# d=dict.fromkeys("abc",['u','u'])
# print(d)

# # get
# d={'n':'u','a':'u'}
# print(d['n'])
# print(d.get('n'))
# print(d.get('ns'))
# if d.get('n'):
#     print('present')

# # clear
# d={'n':'u','a':'u'}
# d.clear()
# print(d)

# # copy---->creates diff. dict same values
# d={'n':'u','a':'u'}
# d1=d.copy()
# print(d1)
# print(d1 is d)
# d1=d
# print(d1 is d)


# # get()
# d={'n':'h','a':20,'a':21}
# # later value taken
# print(d.get('ns','not found'))
# print(d.get('a'))


# # ex 1
# def cube(n):
#     d={}
#     for x in range(1,n+1):
#         d.update({x:x**3})
#     return d
# print(cube(7))

# # ex 2 word counter dictionary
# def counter(s):
#     d={}
#     for c in s:
#         d[c]=s.count(c)
#     return d
# print(counter("harshit"))

# # ex 3
# fm=[]
# fs=[]
# n,a=(input("Enter name,age,favourite movies,favourite songs (, separated):").split(","))
# fm=input("Enter favourite movies (, separated):").split(",")
# fs=input("Enter favourite songs (, separated):").split(",")
# print(fm,fs)
# # isha,20
# # Enter favourite movies (, separated):interstellar,the kissing booth
# # Enter favourite songs (, separated):perfect,kasam
# # ['interstellar', 'the kissing booth'] ['perfect', 'kasam']
#
# d={'name':n,'age':a,'fav movies':fm,"fav songs":fs}
# for i in d:
#     print(f"{i}:{d[i]}")
