# n1,n2,n3=input("Enter 3 numbers").split(",")
# print(f"Average of 3 numbers {n1} , {n2} ,{n3} is {(int(n1)+int(n2)+int(n3))/3} ")

#this was a question
#String indexing
lang="python"
# p=0,-6
# y=1,-5
# t=2,-4
# h=3,-3
# o=4,-2
# n=5,-1
print(lang[5])
#print(lang[start argument : stop argument -1:step])
print(lang[:])
print(lang[2:4])
print(lang[2:])
print(lang[:6])
print("Harshit"[::])
print("Harshit"[1::1])
print("Harshit"[:2:2])
print("Harshit"[::3])
print("Harshit"[1:2:])
print("Harshit"[::-1])#trick
print("Harshit"[-1::-1])
print("Harshit"[:3:-1])
print("Harshit"[1:-3:])
print("Harshit"[1::-3])
print("Harshit"[-7::3])
name=input("Enter name ")
print(f"REVERSE NAME IS {name[::-1]}")