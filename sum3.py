#string methods
name ="hARSHIT vAsHSISTH"
#1.len() function
print(len(name))
#2.lower() method
print(name.lower())
#3.upper() method
print(name.upper())
#4.title() method
print(name.title())
print(name)
#5.count() method
print(name.count("H"))
print(name.count("h"))

#Exercise 3
name,sc=input("Enter ur name and a single  character ").split(",")
print(f"Name is {name} and no of counts is {name.lower().count(sc.lower())}")