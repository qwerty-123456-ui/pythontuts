# f=open('file1.txt')
# # string
# print(f"cursor position -{f.tell()}")
# print(f.read())
#
# print("Before seek method")
# f.seek(0)
# print("After seek")
# print(f"cursor position -{f.tell()}")
#
# f.read()
# print(f"cursor position -{f.tell()}")
# f.seek(0)
# print(f"cursor position -{f.tell()}")
#
# # print(f.readline(),end="")
# # print(f.readline())
# lines=f.readlines()
# print(lines)
# for line in lines[:1]:
#     print(line,end="")
# for line in f:
#     print(line)
# print(f.closed)
# f.close()
# print(f.closed)


# # with Block
# # context manager
# with open('file.txt','r') as f:
#     data=f.read()
#     print(data)
#
# print(f.closed)
# with open('file1.txt','w') as f:
#     f.write('hello\n')
# with open('file1.txt','a') as f:
#     f.write('hello\n')
# # can't create file just read and write -- r+
# with open('file2.txt','r+') as f:
#     f.seek(len(f.read()))
#     f.write('hi')
#
# with open('file1.txt','r') as rf:
#     with open('file3.txt','w') as wf:
#         wf.write(rf.read())


# ex 1
# with open('sa.txt','r') as rf:
#     with open('sal.txt','w') as wf:
#         for line in rf.readlines():
#             n,s=line.split(',')
#             wf.write(f'{n}\'s salary is {s}')

# # ex2
# with open('index.html','r') as rf:
#     with open('com.txt','w') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 pos=line.find("<a href=")
#                 first=line.find("\"",pos)
#                 sec=line.find("\"",first+1)
#                 url=line[first+1:sec]
#                 wf.write(url+"\n")
# with open('index.html','r') as rf:
#     with open('co.txt','w') as wf:
#         page=rf.read()
#         link_exist=True
#         while link_exist:
#             pos=page.find('<a href=')
#             if pos==-1:
#                 link_exist=False
#             else:
#                 # pos=line.find("<a href=")
#                 first=page.find("\"",pos)
#                 sec=page.find("\"",first+1)
#                 url=page[first+1:sec]
#                 wf.write(url+"\n")
#                 page=page[sec:]
# with open('ls.txt','r',encoding='utf-8') as f:
#     print(f.encoding)
#     data=f.read(5)
#     while len(data)>0:
#         print(data)
#         data=f.read(5)
#     print(data)
