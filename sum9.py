# watch coco
name,age=input("Enter ur name and age separate by comma ").split(",")
age=int(age)
# if(name[0].lower()=='a' and age>10):
if (name[0]=="a" or name[0]=="A") and age>10 :
    print("U can watch movie !")
else:
    print("U can not watch movie !")