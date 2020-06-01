# a,b=input("Enter 2 no , separated: ").split(",")
# def comp(a,b):
#     return a>b
# print(f"{a} bigger than {b} {comp(int(a),int(b))}")
a,b,c=input("Enter 3 no , separated: ").split(",")
def comp(a,b,c):
    if (a>b and a>c):
        return a
    if b>c:
        return b 
    return c
print(f"{comp(int(a),int(b),int(c))} is the biggest")