def greater(a,b):
    if a>b:
        return a
    else:
        return b

def new_greatest(a,b,c):
    # big=greater(a,b)
    return greater(greater(a,b),c)
a,b,c=input("Enter 3 no , separated: ").split(",")
print(f"{new_greatest(int(a),int(b),int(c))} is the biggest")