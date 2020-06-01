''''total=0
num1=input("Enter a number")
for i in range(0,len(num1)):
    total+=int(num1[i])
print("total is "+str(total))'''
name=input("enter ur name")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+=name[i]
