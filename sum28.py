#list-->int,float,str,list...
n=[1,'a',None,2.3]
print(n)
print(n[1:-1])
n[1:]=["word",'w']
print(n)
#add items
f=['g','d']
f.append('a')
print(f)
f=[]
f.append('a')
f.append('g')
print(f)
#insert,concatenate(join),extend
f.insert(1,'q')
print(f)
f.insert(20,'u')
print(f)
f1=['d','as','g']
f2=f+f1
print(f2)
f1.extend(f)
print(f1)
f1.append(f)
print(f1)
#delete data from list: pop
print(f1.pop())
print(f1)
print(f1.pop(1))
print(f1)
#delete
del f1[1]
print(f1)
#remove
f1.remove('g')
print(f1)
