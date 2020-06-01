n =input("Enter ur name ")
i=0
j=0
temp=""
while i<len(n):
    c=n.count(n[i])
    if n[i] not in temp:
        temp +=n[i]
        print(f"{n[i]} : {c}")
    i +=1
    # good question