# # list comprehension
# s=[i**2 for i in range(1,11)]
# print(s)
#
# n=[-i for i in range(1,11)]
# print(n)
#
# na=['Isha','Kat','Aaron']
# nf=[i[0] for i in na]
# print(nf)

#
# # ex1
# def revs(l):
#     l1=[i[::-1] for i in l]
#     return l1
# print(revs(['abc','xyz','pqr']))

#
# # with if statement
# l=[i for i in range(1,11) if i%2==0]
# print(l)


# l=input("Enter a list :(, separated)").split()
# print(l)
# for i in l:
#     print(type(i))
#     if (type(i)==str or type(list(i)==list)):
#         l.remove(i)
# l1=[i for i in l if type(int(i))==int]
# print(l1)


# # if-else
# n=list(range(1,11))
# n2=[i*2 if i%2==0 else -i for i in n]
# print(n2)


# # nested list comprehension
# e=[[1,2,3],[1,2,3],[1,2,3]]
# ne=[[ i for i in range(1,4)] for j in range(3)]
# print(ne)

#
#
# # dict comprehension
# sq={f"square of {num} is":num**2 for num in range(1,11)}
# print(sq)
# for k,v in sq.items():
#     print(f"{k}:{v}")


# s="Harshit"
# w={char:s.count(char) for char in s}
# print(w)


# # if-else
# d={1:'odd',2:'even'}
# o_e={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(o_e)


# 
# # set comprehension
# s={k**2 for k in range(1,11)}
# print(s)
#
# n=['har','IDEA ']
# f={na[0] for na in n}
# print(f)
