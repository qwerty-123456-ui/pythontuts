name=" She is beautiful and is amazing"
print(name.replace("is","was",1))
print(name.replace("is","was",2))
print(name.find("is"))
print(name.find("is",6))
# center method
name=input("Enter ur name ")
print(name.center(len(name)+8,"*"))
print(name.center(len(name)+7,"*"))
# strings are immutable
name="String"
name.replace('t','T')
print(name)
# we have assign to new variable or just use print above
name1=name.replace('t','T')
print(name1)
# assignment operators
name="isha"
name +=" gupta"
print(name )